from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *
from functools import reduce

#!Import to use intelisense
# from main.zcode.utils.AST import *
# from main.zcode.utils.Visitor import *
# from main.zcode.utils.Utils import Utils
def param_logger(show_args):
    def logger(func):
        def wrapper(obj,ast,param):
            if (show_args):
                print("At " + func.__name__)
                if (isinstance(param, list)):
                    print("Param: ", [str(x) for x in param])
                else:
                    print("Param: ", [str(x) for x in param[0]], "Return Symbol: ", param[1])
                print("AST: ", str(ast))
            else:
                print("At " + func.__name__)
            return func(obj,ast,param)
        return wrapper
    return logger

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
            Redeclared: if found a symbol with similar name and scope
        """
        target_id = target.name
        found = self.lookup(target_id, reversed(env), lambda x: x.name)
        #!Use reverse to reverser the env list, 
        #!thus the element with match name is the lastest ele
        #*This is a way to "hidden" outer scope elements (!! idk man, wtf)
        if found:
            if (target.scope == found.scope):
                raise Redeclared(kind=Variable(),name=target_id.name)
    
    def param_redeclared_check(self,target,env):
        """Check if a variable is declared in the current environment

        Args:
            target (VariableSymbol): variable to check
            env (List[Symbol]): Environment to check

        Raises:
            Redeclared: if found a symbol with similar name and scope
        """
        target_id = target.name
        found = self.lookup(target_id, reversed(env), lambda x: x.name)
        #!Use reverse to reverser the env list, 
        #!thus the element with match name is the lastest ele
        #*This is a way to "hidden" outer scope elements (!! idk man, wtf)
        if found:
            if (target.scope == found.scope):
                raise Redeclared(kind=Parameter(),name=target_id.name)
    
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
        Returns: 
            symbol(Symbol): inner most scope func symbol with target_id = target_id
        """
        symbol = self.symbol_undeclared_check(target_id, env)
        if not isinstance(symbol,FunctionSymbol):
            #*found symbol is not a function
            raise Undeclared(kind=Function(),name=target_id.name)
        return symbol
        
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
        if ((type_1 is None)or (type_2 is None)):
            return False
        if ((isinstance(type_1, NumberType) and isinstance(type_2, NumberType))
        or (isinstance(type_1, BoolType) and isinstance(type_2, BoolType))
        or (isinstance(type_1, StringType) and isinstance(type_2, StringType))
        or (isinstance(type_1, VoidType) and isinstance(type_2, VoidType))):
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
            if (current_inferred_type is None):
                return UnResolveType()
            symbol.value_type = current_inferred_type
        if (not self.compare_type(symbol.value_type, current_inferred_type)):
            if (current_inferred_type is None): return symbol.value_type
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
            if (current_inferred_type is None):
                return (UnResolveType(), param_list)
            symbol.return_type = current_inferred_type
        if (symbol.return_type != current_inferred_type):
            return (None, param_list)
        return (symbol.return_type, param_list)
    
    def inferred_to_call_expression(self, call_expression_ast, current_inferred_type, param):
        """Type inferrence and checking of call expression

        Args:
            call_expression_ast (call_expr_tree): target Id to find the type of
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
        if (isinstance(symbol_type, UnResolveType)):
            return UnResolveType()
        #*Compare and inferred args list to parameter list
        if (len(args_list) != len(param_list)):
            raise TypeMismatchInExpression(call_expression_ast)
        for i in range(len(args_list)):
            args_type = self.visitExpr(param_list[i].value_type, args_list[i], param)
            if (args_type is None):
                raise TypeMismatchInExpression(call_expression_ast)
            if (isinstance(args_type, UnResolveType)):
                return UnResolveType()
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
    
    #! Every expr should call visitExpr wrapper method
    #! Every non vardecl stmt should call visitStmt wrapper method
    
    #!Scope env list should be in order [outermost scope, .. innermost scope]
    def visitExpr(self, current_inferred_type, ast, param):
        print("at visitExpr")
        if (isinstance(ast, Id)):
            return self.get_var_type_by_id(
                target_id=ast,
                current_inferred_type=current_inferred_type,
                param=param,
            )
        elif (isinstance(ast, CallExpr)):
            return self.inferred_to_call_expression(
            call_expression_ast=ast,
            current_inferred_type=current_inferred_type,
            param=param,
            )
        
        else :
            if (isinstance(ast, ArrayLiteral)):
                return_type = self.visit(ast, (param, current_inferred_type))
            else:
                return_type = self.visit(ast, param)
            if (return_type is None):
                return None
            if (isinstance(return_type,UnResolveType)):
                return UnResolveType()
            if (current_inferred_type is None):
                return return_type
            if (not self.compare_type(return_type, current_inferred_type)):
                return None
            else:
                return return_type
    def visitStmt(self, outer_return_symbol, ast, param):
        print("at visitStmt")
        if (isinstance(ast, VarDecl)):
            return self.visit(ast, param)
        return self.visit(ast, (param, outer_return_symbol))
    def visitParam(self, ast, param):
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
        symbol = VariableSymbol(
            name = ast.name,
            kind=Parameter(),
            scope=self.scope_pointer,
            value_type=result_type if result_type else UnResolveType()
        )
        
        if (ast.varInit):
            exprType = self.visitExpr(result_type, ast.varInit, parent_env + [symbol])
            if (exprType is None):
                raise TypeMismatchInStatement(ast)
            if (isinstance(exprType,UnResolveType)):
                raise TypeCannotBeInferred(ast)
            result_type = exprType
        
        symbol.value_type = result_type if result_type else UnResolveType()
        self.param_redeclared_check(symbol, parent_env)
        
        return symbol
    # #@param_logger(show_args=False)
    def visitProgram(self, ast, param):
        """
        # decl: List[Decl]
        """
        parent_env = param
        decl_list = []
        list(map(lambda symbol : decl_list.append(self.visit(symbol, parent_env + decl_list)), ast.decl))
        
        self.func_definition_check(decl_list)
        
        self.entry_check(decl_list)
    # @param_logger(show_args=True)
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
        symbol = VariableSymbol(
            name = ast.name,
            kind=Variable(),
            scope=self.scope_pointer,
            value_type=result_type if result_type else UnResolveType()
        )
        
        if (ast.varInit):
            exprType = self.visitExpr(result_type, ast.varInit, parent_env + [symbol])
            if (exprType is None):
                raise TypeMismatchInStatement(ast)
            if (isinstance(exprType,UnResolveType)):
                raise TypeCannotBeInferred(ast)
            result_type = exprType
        
        symbol.value_type = result_type if result_type else UnResolveType()
        self.var_redeclared_check(symbol, parent_env)

        return symbol
    #@param_logger(show_args=True)
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
                func_param_list.append(self.visitParam(symbol, [return_symbol]+ func_param_list))
            , ast.param))

        #TODO: check again return type algorithm
        if (ast.body):
            self.visitStmt(return_symbol, ast.body, parent_env + [return_symbol]+ func_param_list)
            if (isinstance(return_symbol.return_type,UnResolveType)):
                return_symbol.return_type = VoidType()
        self.move_scope_out()
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
    # #@param_logger(show_args=False)
    def visitBinaryOp(self, ast, param):
        """
        # op: str
        # left: Expr
        # right: Expr
        """
        
        (operand_type, return_type) = self.get_op_type(op=ast.op)
        left_type = self.visitExpr(operand_type, ast.left, param)

        right_type = self.visitExpr(operand_type, ast.right, param)
        print(left_type, right_type, operand_type)
        if (
            isinstance(left_type,UnResolveType) or 
            isinstance(right_type,UnResolveType)
        ):
            return UnResolveType()
        
        if (left_type is None or right_type is None):
            raise TypeMismatchInExpression(ast)
        if (not self.compare_type(left_type, right_type)
            or not self.compare_type(left_type, operand_type)):
            raise TypeMismatchInExpression(ast)
        return return_type
    # #@param_logger(show_args=False)
    def visitUnaryOp(self, ast, param):
        """
        # op: str
        # operand: Expr
        """
        (op_type, return_type) = self.get_op_type(op=ast.op)
        operand_type = self.visitExpr(
            current_inferred_type=op_type,
            ast=ast.operand, 
            param=param)
        if (
            isinstance(operand_type,UnResolveType)
        ):
            return UnResolveType()
        
        if (operand_type is None):
            raise TypeMismatchInExpression(ast)
        if (not self.compare_type(operand_type, op_type)):
            raise TypeMismatchInExpression(ast)
        return return_type
    #@param_logger(show_args=True)
    def visitCallExpr(self, ast, param):
        """
        # name: Id
        # args: List[Expr]
        """
        Id = ast.name
        args_list = [ele for ele in ast.args]
        return (Id, args_list)
    #@param_logger(show_args=False)
    def visitId(self, ast, param):
        """
        # name: str
        """
        '''Return Id'''
        return self.symbol_undeclared_check(ast,param)
    #@param_logger(show_args=False)
    def visitArrayCell(self, ast, param):
        """
        # arr: Expr
        # idx: List[Expr]
        """
        parent_env = param
        idx_type_list = []
        for ele in ast.idx:
            idx_num = self.visitExpr(NumberType(), ele, parent_env)
            if (idx_num is None): 
                raise TypeMismatchInExpression(ast)
            if (isinstance(idx_num, UnResolveType)): 
                return idx_num
            idx_type_list.append(idx_num)
        arr = self.visitExpr(None, ast.arr, parent_env)
        if (arr is None):
            raise TypeMismatchInExpression(ast)
        if (not isinstance(arr,ArrayType) or len(idx_type_list) > len(arr.size)):
            raise TypeMismatchInExpression(ast)
        if (isinstance(arr,UnResolveType)):
            return UnResolveType()
        if (len(idx_type_list) == len(arr.size)):
            return arr.eleType
        return_array_type = ArrayType(size=arr.size[len(idx_type_list):],
                                    eleType=arr.eleType,)
        return return_array_type
    #@param_logger(show_args=True)
    def visitBlock(self, ast, param):
        """
        # stmt: List[Stmt]  # empty list if there is no statement in block
        """
        self.move_scope_in()
        (parent_env, outer_symbol) = param
        decl_list = []
        list(
            map(lambda children_ast : 
                decl_list.append(self.visitStmt(outer_symbol,children_ast, (parent_env + decl_list )))
                if isinstance(children_ast, VarDecl) 
                else self.visitStmt(outer_symbol,children_ast, (parent_env + decl_list ))
                , ast.stmt
            )
        )
        self.move_scope_out()
        return None
    #@param_logger(show_args=True)
    def visitIf(self, ast, param):
        """
        # expr: Expr
        # thenStmt: Stmt
        # elifStmt: List[Tuple[Expr, Stmt]] # empty list if there is no elif statement
        # elseStmt: Stmt = None  # None if there is no else branch
        """
        (parent_env, outer_symbol) = param
        decl_list = []
        condition_type = self.visitExpr(BoolType(), ast.expr, parent_env + decl_list)
        if (condition_type is None):
            raise TypeMismatchInStatement(ast)
        if (isinstance(condition_type,UnResolveType)):
            raise TypeCannotBeInferred(ast)
        then_type = self.visitStmt(outer_symbol, ast.thenStmt, parent_env + decl_list)
        if (isinstance(then_type, VarDecl)):
            decl_list.append(then_type)
        #*Handle all elif statements
        for ele in ast.elifStmt:
            elif_condition_type = self.visitExpr(BoolType(), ele[0], parent_env + decl_list)
            if (elif_condition_type is None):
                raise TypeMismatchInStatement(ast)
            if (isinstance(elif_condition_type,UnResolveType)):
                raise TypeCannotBeInferred(ast)
            if (not self.compare_type(elif_condition_type, BoolType())):
                raise TypeMismatchInStatement(ast)
            elif_type = self.visitStmt(outer_symbol, ele[1], parent_env + decl_list)
            if (isinstance(elif_type, VarDecl)):
                decl_list.append(elif_type)
        if (ast.elseStmt):
            else_type = self.visitStmt(outer_symbol, ast.elseStmt, parent_env + decl_list)
            if (isinstance(else_type, VarDecl)):
                decl_list.append(else_type)
        return then_type
    #@param_logger(show_args=True)
    def visitFor(self, ast, param):
        """
        # name: Id
        # condExpr: Expr
        # updExpr: Expr
        # body: Stmt
        """
        (parent_env, outer_symbol) = param
        self.move_loop_in()
        name_type = self.get_var_type_by_id(target_id=ast.name,
                                        current_inferred_type=NumberType(),
                                        param=parent_env)
        if (name_type is None):
            raise TypeMismatchInStatement(ast)
        if (isinstance(name_type,UnResolveType)):
            raise TypeCannotBeInferred(ast)
        condition_type = self.visitExpr(BoolType(), ast.condExpr, parent_env)
        if (condition_type is None):
            raise TypeMismatchInStatement(ast)
        if (isinstance(condition_type,UnResolveType)):
            raise TypeCannotBeInferred(ast)
        update_type = self.visitExpr(NumberType(), ast.updExpr, parent_env)
        if (update_type is None):
            raise TypeMismatchInStatement(ast)
        if (isinstance(update_type,UnResolveType)):
            raise TypeCannotBeInferred(ast)
        body_type = self.visitStmt(outer_symbol, ast.body, parent_env)
        self.move_scope_out()
        return body_type
    #@param_logger(show_args=False)
    def visitContinue(self, ast, param):
        if self.in_loop_pointer == 0:
            raise MustInLoop(ast)
    #@param_logger(show_args=False)
    def visitBreak(self, ast, param):
        if self.in_loop_pointer == 0:
            raise MustInLoop(ast)
    #@param_logger(show_args=True)
    def visitReturn(self, ast, param):
        """
        expr: Expr
        """
        '''Return a type object'''
        (parent_env, outer_symbol) = param
        inferred_type = outer_symbol.return_type
        if (isinstance(inferred_type,UnResolveType)):
            inferred_type = None
        print(inferred_type)
        if (ast.expr):
            if (isinstance(outer_symbol.return_type,VoidType)):
                raise TypeMismatchInStatement(ast)
            res = self.visitExpr(inferred_type,ast.expr, parent_env)
            if (res is None):
                raise TypeMismatchInStatement(ast)
            if (isinstance(res,UnResolveType)):
                raise TypeCannotBeInferred(ast)
            if (isinstance(outer_symbol.return_type,UnResolveType)):
                outer_symbol.return_type = res
                return res
            if (not self.compare_type(outer_symbol.return_type,res)):
                raise TypeMismatchInStatement(ast)
        else: 
            if (isinstance(outer_symbol.return_type,UnResolveType)):
                outer_symbol.return_type = VoidType()
                return VoidType()
            if (not self.compare_type(outer_symbol.return_type,VoidType())):
                raise TypeMismatchInStatement(ast)
    #@param_logger(show_args=True)
    def visitAssign(self, ast, param):
        """
        # lhs: Expr
        # rhs: Expr
        """
        (parent_env, outer_symbol) = param
        #*Visit lhs without inferences
        lhs_type = self.visitExpr(None, ast.lhs, parent_env)
        if (lhs_type is None):
            raise TypeMismatchInStatement(ast)
        #*If lhs is unresolved visit rhs without inferences
        if (isinstance(lhs_type,UnResolveType)):
            rhs_type = self.visitExpr(None, ast.rhs, parent_env)
            if (rhs_type is None):
                raise TypeMismatchInStatement(ast)
            #*raise cannot infer the type if rhs also unresolve
            if (isinstance(rhs_type,UnResolveType)):
                raise TypeCannotBeInferred(ast)
            else:
            #*if rhs is resolve visit lhs again with 
            # *inferred type is rhs type, work with the exceptions flow again
                lhs_type = self.visitExpr(rhs_type, ast.lhs, parent_env) 
                if (lhs_type is None):
                    raise TypeMismatchInStatement(ast)
                #*If lhs is unresolved visit rhs without inferences
                if (isinstance(lhs_type,UnResolveType)):
                    raise TypeCannotBeInferred(ast)
        else:
            #*if lhs is resolve just visit rhs with inference
            rhs_type = self.visitExpr(lhs_type, ast.rhs, parent_env)
            if (rhs_type is None):
                raise TypeMismatchInStatement(ast)
            if (isinstance(rhs_type,UnResolveType)):
                raise TypeCannotBeInferred(ast)
            else:
                return VoidType()

    #@param_logger(show_args=True)
    def visitCallStmt(self, ast, param):
        """
        # name: Id
        # args: List[Expr]  # empty list if there is no argument
        """
        (parent_env, outer_symbol) = param
        target_id = ast.name
        args_list = ast.args
        (symbol_type, param_list) = self.get_function_type_by_id(
            target_id=target_id,
            current_inferred_type=VoidType(),
            param=parent_env
        )
        #*Check symbol_type
        if (symbol_type is None):
            raise TypeMismatchInExpression(ast)
        if (not isinstance(symbol_type, VoidType)):
            raise TypeMismatchInExpression(ast)
        if (isinstance(symbol_type, UnResolveType)):
            return UnResolveType()
        #*Compare and inferred args list to parameter list
        if (len(args_list) != len(param_list)):
            raise TypeMismatchInExpression(ast)
        for i in range(len(args_list)):
            args_type = self.visitExpr(param_list[i].value_type, args_list[i], parent_env)
            if (args_type is None):
                raise TypeMismatchInExpression(ast)
            if (isinstance(args_type, UnResolveType)):
                return UnResolveType()
        #Return symbol type if every param and args is checked
        return VoidType()

    def visitNumberLiteral(self, ast, param):
        '''Return Number Type'''
        return NumberType()

    def visitBooleanLiteral(self, ast, param):
        '''Return Bool Type'''
        return BoolType()

    def visitStringLiteral(self, ast, param):
        '''Return String Type'''
        return StringType()
    @param_logger(show_args=True)
    def visitArrayLiteral(self, ast, param):
        """
        # value: List[Expr]
        """
        '''Return Array Type'''
        #TODO: Handle type inference
        (parent_env, inferred_type) = param
        #*outer type is not array type 
        if (inferred_type is not None and
            not isinstance(inferred_type, ArrayType)):
                return None
        
        #*Handle no type inference
        if (inferred_type is None):
            #*Loop through the array to find the first resolved element
            for ele in ast.value[1:]:
                ele_type = self.visitExpr(None, ele ,parent_env)
                if (ele_type is None): 
                    raise TypeMismatchInExpression(ast)
                #*take this type if not an unresolved
                if (not isinstance(ele_type, UnResolveType)):
                    if (isinstance(ele_type, ArrayType)):
                        #*Handle inferred_type if first found resolve type is an ArrayType
                        inferred_type =  ArrayType(
                                size=[len(ast.value)]+ele_type.size,
                                eleType=ele_type.eleType
                            )
                    else:
                        inferred_type = ArrayType(size=[len(ast.value)], eleType=ele_type) 
                    break
            #*If cannot find any resolved element in array lit,
            #*return an unresolved
            if (inferred_type is None):
                return UnResolveType()
            
        #*If array is one dimension inferred type is eleType
        if (len(inferred_type.size) == 1):
            inferred_elem_type = inferred_type.eleType
        #*else inferred elem type should be an array type with same eleType 
        #*and new_size should be size[1:] (strip first elem)
        #*think of : array[2,3,4]is array[2] of array[3,4] and so on.
        else:
            new_size = inferred_type.size[1:]
            inferred_elem_type = ArrayType(size=new_size,eleType=inferred_type.eleType)
        for ele in ast.value[1:]:
            ele_type = self.visitExpr(inferred_elem_type, ele ,parent_env)
            if (ele_type is None):
                # raise TypeMismatchInExpression(ast)
                return None
            if (isinstance(ele_type,UnResolveType)):
                return UnResolveType()
        #*All elements are resolved
        return inferred_type
            
