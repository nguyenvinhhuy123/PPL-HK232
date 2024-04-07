from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

#!Import to use intelisense
from main.zcode.utils.AST import *
from main.zcode.utils.Visitor import *
from main.zcode.utils.Utils import Utils
def param_logger(func):
    def wrapper(obj,ast,param):
        print("At " + func.__name__)
        print("Param: ", [str(x) for x in param])
        print("AST: ", str(ast))
        return func(obj,ast,param)
    return wrapper

class Symbol:
    name: Id
    kind: Kind
    scope: int
    
    def __init__(self,
                name,
                kind,
                scope):
        self.name = name
        self.kind = kind
        self.scope = scope
        
    def __str__(self):
        pass

class UnResolveType(Type):
    def __str__(self):
        return "UnResolve"

class VariableSymbol(Symbol):
    '''Type of variable'''
    value_type: Type
    def __init__(self, name, kind, scope, value_type):
        super().__init__(name, kind, scope)
        self.value_type = value_type
    
    def __str__(self):
        res =  ("VarSymbol:" +  str(self.name) + ", " +
                str(self.kind) + ", " +
                str(self.scope) + ", " +
                str(self.value_type) + ", " )
        return res
    
class FunctionSymbol(Symbol):
    param: List[VariableSymbol]
    ''' Param of a function'''
    define: bool
    ''' define is if a symbol have a definition,
    ie if function is forward declared -> define = false
    ie if var does not have a var init value yet -> define = false
    '''
    #!None might change to VoidType? 
    return_type = Type
    '''Return type of symbol,
    None if symbol is funcDecl and have no return stmt 
    if varDecl is scala typed then return type = type declared
    if varDecl is dynamic (var and dynamic kw) then return type = type of Expression
    if if varDecl is dynamic kw and have no expr then return type None'''
    def __init__(self, name, kind, scope,
                param = [], define=False, return_type = UnResolveType()):
        super().__init__(name, kind, scope)
        self.param = param
        self.define = define
        self.return_type = return_type
        
    def __str__(self):
        res =  ("FuncSymbol:" +  str(self.name) + ", " +
                str(self.kind) + ", " +
                str(self.scope) + ", " +
                "Param: " + str([str(x) for x in self.param]) + ", " +
                str(self.define) + ", " +
                str(self.return_type) + ", " )
        return res

class StaticChecker(BaseVisitor, Utils):
    
    def __init__(self,ast):
        self.ast = ast
        
        #*Loop pointers, value + 1 when visit a loop ctx, 
        #*value - 1 when done visiting a loop ctx
        self.in_loop_pointer = 0;
        
        #*Scope pointers, value + 1 when go to inner scope
        #*Value - 1 when get out of inner scope
        self.scope_pointer = 0;
        
        self.global_env = [
            #* I/O API Symbol
            FunctionSymbol(
                name= Id("readString"),
                kind = Function(),
                scope = 0,
                define=True,
                return_type = StringType()
            ),
            FunctionSymbol(
                name= Id("readBool"),
                kind = Function(),
                scope = 0,
                define=True,
                return_type = BoolType()
            ),
            FunctionSymbol(
                name= Id("readNumber"),
                kind = Function(),
                scope = 0,
                define=True,
                return_type = NumberType()
            ),
            FunctionSymbol(
                name= Id("writeString"),
                kind = Function(),
                scope = 0,
                param= [VariableSymbol(
                    name=Id("anArg"),
                    kind = Parameter(),
                    scope = 1,
                    value_type = StringType()  
                )],
                define=True,
                return_type = VoidType()
            ),
            FunctionSymbol(
                name= Id("writeBool"),
                kind = Function(),
                scope = 0,
                param= [VariableSymbol(
                    name=Id("anArg"),
                    kind = Parameter(),
                    scope = 1,
                    value_type = BoolType()  
                )],
                define=True,
                return_type = VoidType()
            ),
            FunctionSymbol(
                name= Id("writeNumber"),
                kind = Function(),
                scope = 0,
                param= [VariableSymbol(
                    name=Id("anArg"),
                    kind = Parameter(),
                    scope = 1,
                    value_type = NumberType()  
                )],
                define=True,
                return_type = VoidType()
            ),
        ]
    
    def check(self):
        return self.visit(ast=self.ast,param=self.global_env)
    
    #**********************************#
    #*          UTILS METHOD          *#
    #**********************************#
    def move_scope_in(self):
        self.scope_pointer += 1
    
    def move_scope_out(self):
        self.scope_pointer -= 1
        
    def move_loop_in(self):
        self.in_loop_pointer += 1
    
    def move_loop_out(self):
        self.in_loop_pointer -= 1
        
    def entry_check(self, env):
        '''Check if environment have entry point
        env: Environment to check'''
        main_check = self.lookup(name=Id("main"),lst=env,func=lambda x: x.name)
        if (not main_check 
            or not isinstance(main_check,FunctionSymbol)
            or (main_check.param != []) 
            or not main_check.define
            ):
            raise NoEntryPoint()
        
    def var_redeclared_check(self,target,env):
        """Check if a variable is declared in the current environment

        Args:
            target (VariableSymbol): variable to check
            env (List[Symbol]): Environment to check

        Raises:
            Redeclared: if found a symbol witth similar name and scope
        """
        target_id = target.name
        found = self.lookup(target_id, reversed(env), lambda x: x.name)
        #!Use reverse to reverser the env list, 
        #!thus the element with match name is the lastest ele
        #*This is a way to "hidden" outer scope elements (!! idk man, wtf)
        if found:
            if (target.scope == found.scope):
                raise Redeclared(kind=Variable(),name=target_id.name)
    
    def func_redeclared_check(self,target,env):
        """Check if a function is declared in the current environment

        Args:
            target (FunctionSymbol): function to check
            env (List[Symbol]): Environment to check

        Raises:
            Redeclared: if a function symbol with similar name is found 
            with matching parameters and already have a body
        """
        target_id = target.name
        look_res = self.lookup(target_id, reversed(env), lambda x: x.name)
        if look_res:
            if (isinstance(look_res,FunctionSymbol)
                and self.compare_parameter_list(look_res.param,target.param)
                and ((look_res.define == False) and (target.define == True))
            ):  #* These condittion verified if a symbol is a forwards declaration
                #*So we should update the body of the function too match the later declaration
                look_res.define = True
            else: 
                raise Redeclared(kind=Function(),name=target_id.name)
    
    def symbol_undeclared_check(self, target_id, env):
        """ Check if a symbol is declared in the current environment

        Args:
            target_id (Id): target_id to check
            env (List[Symbol]): Environment to check

        Raises:
            Undeclared: no Symbol with target_id = target_id is declared
            
        Returns: 
            symbol(Symbol): inner most scope symbol with target_id = target_id
        """
        symbol = self.lookup(target_id, reversed(env), lambda x: x.name)
        if not symbol:
            raise Undeclared(kind=Identifier(),name=target_id.name)
        return symbol
    
    def func_undeclared_check(self, target_id, env):
        """Check if func symbol is declared in the current environment

        Args:
            target_id (Id): func symbol to check
            env (List[Symbol]): Environment to check

        Raises:
            Undeclared: if no symbol found
            Undeclared: found symbol is not a function
        """
        symbol = self.symbol_undeclared_check(target_id, env)
        if not isinstance(symbol,FunctionSymbol):
            #*found symbol is not a function
            raise Undeclared(kind=Function(),name=target_id.name)
        
    def func_definition_check(self, env):
        """Check if all functions are defined

        Args:
            env (List[Symbol]): Environment to check

        Raises:
            NoDefinition: exist a function symbol without definition
        """
        for func in env:
            if not isinstance(func,FunctionSymbol):
                continue
            if not func.define:
                target_id = func.name
                raise NoDefinition(name=target_id.name)
    
    def compare_type(self, type_1, type_2):#
        """Compare 2 type object

        Args:
            type_1 (Type): first type object
            type_2 (Type): second type object

        Returns:
            bool: True if equal, False otherwise
        """
        #*Both are scala types
        if ((isinstance(type_1, NumberType) and isinstance(type_2, NumberType))
        or (isinstance(type_1, BoolType) and isinstance(type_2, BoolType))
        or (isinstance(type_1, StringType) and isinstance(type_2, StringType))):
            return True
        if (isinstance(type_1, ArrayType) and isinstance(type_2, ArrayType)):
            #*both are arrays
            #*compare array elements type
            if (not self.compare_type(type_1.eleType, type_2.eleType)):
                return False
            #*compare array elements size
            if (type_1.size != type_2.size):
                return False
            return True
        return False
    
    def compare_parameter_list(self, param_list_1, param_list_2):
        """Compare 2 parameter lists

        Args:
            param_list_1 (list[VariableSymbol]): list of parameter symbols
            param_list_2 (list[VariableSymbol]): list of parameter symbols

        Returns:
            bool : True if parameter lists are equal, False otherwise
        """
        if (len(param_list_1)!= len(param_list_2)):
            return False
        for i in range(len(param_list_1)):
            if (param_list_1[i].name != param_list_2[i].name):
                return False
            if (not self.compare_type(param_list_1[i].value_type, param_list_2[i].value_type)):
                return False
        return True
    
    def get_var_type_by_id(self, target_id, current_inferred_type, param):
        """Get the type of the Id object with variable kind

        Args:
            target_id (Id): target Id to find the type of
            current_inferred_type (Type): type inferred from the outer expr
            If current_inferred_type value is None 
            -> mean outer expr/stmt can not inferred a type to this Id
            param (List[Symbol]): environment to find Symbol of Id

        Returns:
            Type: Type of the found symbol match with Id
            None: if return type is mismatched with outer inferred type (for outer to call Type mismatch)
            UnresolveType: if Id type is unresolved and outer type is None (cant be inferred)
            a valid type if symbol return type match with inferred type or symbol type can be inferred
        """
            
        symbol = self.symbol_undeclared_check(target_id, param)
        if (isinstance(symbol.value_type, UnResolveType)):
            if (current_inferred_type == None):
                return UnResolveType()
            symbol.value_type = current_inferred_type
        if (symbol.value_type != current_inferred_type):
            return None
        return symbol.value_type
        
    def get_function_type_by_id(self, target_id, current_inferred_type, param):
        """Get the type of the Id object with variable kind

        Args:
            target_id (Id): target Id to find the type of
            current_inferred_type (Type): type inferred from the outer expr
            If current_inferred_type value is None 
            -> mean outer expr/stmt can not inferred a type to this Id
            param (List[Symbol]): environment to find Symbol of Id

        Returns:
            (Type, param_list)
            param_list: list of function parameters
            Type : Type of the found symbol match with Id
            None: if return type is mismatched with outer inferred type (for outer to call Type mismatch)
            UnresolveType: if Id type is unresolved and outer type is None (cant be inferred)
            a valid type if symbol return type match with inferred type or symbol type can be inferred
        """
        symbol = self.func_undeclared_check(target_id, param)
        param_list = symbol.param
        if (isinstance(symbol.return_type, UnResolveType)):
            if (current_inferred_type == None):
                return (UnResolveType(), param_list)
            symbol.return_type = current_inferred_type
        if (symbol.return_type != current_inferred_type):
            return (None, param_list)
        return (symbol.return_type, param_list)
    
    def inferred_to_call_expression(self, call_expression_ast, current_inferred_type, param):
        (target_id, args_list) = self.visit(call_expression_ast, param)
        (symbol_type, param_list) = self.get_function_type_by_id(
            target_id=target_id,
            current_inferred_type=current_inferred_type,
            param=param
        )
        #*Check symbol_type
        if (symbol_type is None):
            raise TypeMismatchInExpression(call_expression_ast)
        if (isinstance(symbol_type, VoidType)):
            raise TypeMismatchInExpression(call_expression_ast)
        
        #*Compare and inferred args list to parameter list
        if (len(args_list) != len(param_list)):
            raise TypeMismatchInExpression(call_expression_ast)
        for i in range(len(args_list)):
            if (isinstance(args_list[i], Id)):
                args_type = self.get_var_type_by_id(
                target_id=args_list[i],
                current_inferred_type=param_list[i].value_type,
                param=param,
                )
            elif (isinstance(args_list[i], CallExpr)):
                args_type = self.inferred_to_call_expression(
                target_id=args_list[i],
                current_inferred_type=param_list[i].value_type,
                param=param,
                )
            else :
                args_type = self.visit(args_list[i], param)
            if (args_type is None):
                raise TypeMismatchInExpression(call_expression_ast)
            if (isinstance(args_type, UnResolveType)):
                return args_type
        #Return symbol type if every param and args is checked
        return symbol_type
                
    def get_op_type(self, op):
        #TODO: Implement get_binary_op_type return operator, operand type
        if (op in ["+", "-", "*", "/", "%"]):
            operand_type = NumberType()
            return_type = NumberType()
        if (op in ["and", "or", "not"]):
            operand_type = BoolType()
            return_type = BoolType()
        if (op in ["..."]):
            operand_type = StringType()
            return_type = StringType()
        if (op in ["=", "!=", ">", "<", ">=", "<="]):
            operand_type = NumberType()
            return_type = BoolType()
        if (op in ["=="]):
            operand_type = StringType()
            return_type = BoolType()
        return (operand_type, return_type)
    #**********************************#
    #*          VISIT METHOD          *#
    #**********************************#
    #! Every method control it own scope to pass to children via param ref
    #! Children return a symbolic reference of it self, 
    #! or a type for parent to handle
    
    #! If expression is type Id -> use get_id_type_instead
     
    #!Scope env list should be in order [outermost scope, .. innermost scope]
    def visitExpr(self, current_inferred_type, ast, param):
        if (isinstance(ast, Id)):
            return self.get_var_type_by_id(
                target_id=ast.left,
                current_inferred_type=current_inferred_type,
                param=param,
            )
        elif (isinstance(ast, CallExpr)):
            return self.inferred_to_call_expression(
            target_id=ast.left,
            current_inferred_type=current_inferred_type,
            param=param,
            )
        else :
            return self.visit(ast, param)
    @param_logger
    def visitProgram(self, ast, param):
        """
        # decl: List[Decl]
        """
        parent_env = param
        decl_list = []
        list(map(lambda symbol : decl_list.append(self.visit(symbol, parent_env + decl_list)), ast.decl))
        print([str(x) for x in decl_list])
        self.entry_check(decl_list)
        self.func_definition_check(decl_list)
    @param_logger
    def visitVarDecl(self, ast, param):
        """
        # name: Id
        # varType: Type = None  # None if there is no type
        # modifier: str = None  # None if there is no modifier
        # varInit: Expr = None  # None if there is no initial
        """
        #*param should be a list of current environment variables
        #* look up similar symbol and check var type
        #? should we check for lookups result kind here?
        #? ex: var a lookup res is function a
        result_type = ast.varType
        parent_env = param
        if (ast.varInit):
            exprType = self.visitExpr(None, ast.varInit, parent_env)
            if (exprType == UnResolveType()):
                raise TypeCannotBeInferred(ast)
            if (not self.compare_type(exprType, ast.varType) and 
                ast.varType != None):
                raise TypeMismatchInStatement(ast)
            result_type = exprType
            
        
        symbol = VariableSymbol(
            name = ast.name,
            kind=Variable(),
            scope=self.scope_pointer,
            value_type=result_type if result_type else UnResolveType()
        )
        
        self.var_redeclared_check(symbol, parent_env)

        return symbol
    @param_logger
    def visitFuncDecl(self, ast, param):
        """
        # name: Id
        # param: List[VarDecl]  # empty list if there is no parameter
        # body: Stmt = None  # None if this is just a declaration-part
        """
        parent_env = param
        func_param_list = []
        return_symbol = FunctionSymbol(
            name=ast.name,
            kind=Function(),
            scope=self.scope_pointer,
            param=func_param_list,
            define=True if ast.body else False,
            return_type=UnResolveType()
        )
        self.move_scope_in()
        list(map(lambda symbol: 
                func_param_list.append(self.visit(symbol, parent_env + [return_symbol]+ func_param_list))
            , ast.param))
        
        for symbol in func_param_list:
            symbol.kind = Parameter()
        
        self.move_scope_out()

        #TODO: check again return type algorithm
        return_symbol.return_type = self.visit(ast.body,
                                            parent_env + 
                                            [return_symbol] + 
                                            func_param_list) if ast.body else UnResolveType()
        
        self.func_redeclared_check(return_symbol, param)
        return return_symbol

    def visitNumberType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
        """
        # size: List[float]
        # eleType: Type
        """
        pass

    @param_logger
    def visitBinaryOp(self, ast, param):
        """
        # op: str
        # left: Expr
        # right: Expr
        """
        
        (operand_type, return_type) = self.get_op_type(op=ast.op)
        left_type = self.visitExpr(operand_type, ast.left, param)

        right_type = self.visitExpr(operand_type, ast.right, param)
        
        if (
            isinstance(left_type,UnResolvedType) or 
            isinstance(right_type,UnResolvedType)
        ):
            return UnResolveType()
        
        if (left_type == None or right_type == None):
            raise TypeMismatchInExpression(ast)
        if (not self.compare_type(left_type, right_type)
            or not self.compare_type(left_type, operand_type)):
            raise TypeMismatchInExpression(ast)
        return return_type
    @param_logger
    def visitUnaryOp(self, ast, param):
        """
        # op: str
        # operand: Expr
        """
        (operand_type, return_type) = self.get_op_type(op=ast.op)
        (operand_type, return_type) = self.get_op_type(op=ast.op)
        op_type = self.visitExpr(ast.operand, param)
        if (
            isinstance(op_type,UnResolvedType)
        ):
            return UnResolveType()
        
        if (op_type == None):
            raise TypeMismatchInExpression(ast)
        if (not self.compare_type(op_type, operand_type)):
            raise TypeMismatchInExpression(ast)
        return return_type

    @param_logger
    def visitCallExpr(self, ast, param):
        """
        # name: Id
        # args: List[Expr]
        """
        Id = ast.name
        args_list = [ele for ele in ast.args]
        return (Id, args_list)
    
    def visitId(self, ast, param):
        """
        # name: str
        """
        '''Return Id'''
        return self.symbol_undeclared_check(ast,param)

    def visitArrayCell(self, ast, param):
        """
        # arr: Expr
        # idx: List[Expr]
        """
        idx_type_list = []
        for ele in ast.idx:
            idx_num = self.visitExpr(NumberType(), ele, param)
            if (idx_num is None): 
                raise TypeMismatchInExpression(ast)
            if (isinstance(idx_num, UnResolveType)): 
                return idx_num
            idx_type_list.append(idx_num)
        arr = self.visitExpr(None, ast, param)
        if (not isinstance(arr, ArrayType)):
            raise TypeMismatchInExpression(ast)
        return arr

    @param_logger
    def visitBlock(self, ast, param):
        """
        # stmt: List[Stmt]  # empty list if there is no statement in block
        """
        '''Return type of return stmt if any else return VoidType'''
        self.move_scope_in()
        scope = param
        decl_list = []
        stmt_list = []
        list(
            map(lambda symbol : 
                decl_list.append(self.visit(symbol, decl_list + scope))
                if isinstance(symbol, Decl) 
                else stmt_list.append(self.visit(symbol, decl_list + scope))
                , ast.stmt
            )
        )
        return_type = VoidType()
        self.move_scope_out()
        #TODO: Return Type of body
        return return_type

    def visitIf(self, ast, param):
        """
        # expr: Expr
        # thenStmt: Stmt
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        # elseStmt: Stmt = None  # None if there is no else branch
        """
        pass

    def visitFor(self, ast, param):
        """
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        """
        pass

    def visitContinue(self, ast, param):
        if self.in_loop_pointer == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.in_loop_pointer == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        """
        expr: Expr
        """
        '''Return a type object'''
        if (ast.expr):
            res = self.visit(ast.expr, param)
        return VoidType()

    def visitAssign(self, ast, param):
        """
        # lhs: Expr
        # exp: Expr
        """
        pass

    def visitCallStmt(self, ast, param):
        """
        # name: Id
        # args: List[Expr]  # empty list if there is no argument
        """
        pass

    def visitNumberLiteral(self, ast, param):
        '''Return Number Type'''
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        '''Return Bool Type'''
        return BoolType()

    def visitStringLiteral(self, ast, param):
        '''Return String Type'''
        return StringType()

    def visitArrayLiteral(self, ast, param):
        """
        # value: List[Expr]
        """
        '''Return Array Type'''
        #TODO: Handle type inference
        initial_type =self.visitExpr(None, array_ele_type_list ,param)
        array_ele_type_list = [self.visitExpr(initial_type, ele,param) for ele in ast.value[1:]]
        if (isinstance(initial_type, ArrayType)):
            initial_size = array_ele_type_list[0].size
            if not all(isinstance(x, initial_type) and initial_size == x.size for x in array_ele_type_list):
                raise TypeMismatchInExpression(ast)
            arr_size = [float(len(array_ele_type_list))]+ initial_size
            return ArrayType(size= arr_size, eleType=array_ele_type_list[0])
        if (not all(isinstance(x, initial_type) for x in array_ele_type_list)):
            raise TypeMismatchInExpression(ast)
        arr_size = [float(len(array_ele_type_list))]
        return ArrayType(size=arr_size, eleType=array_ele_type_list[0])
