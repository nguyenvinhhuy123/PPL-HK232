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
        print("Param: ", param)
        print("AST: ", ast)
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

class VariableSymbol(Symbol):
    '''Type of variable'''
    value_type: Type
    def __init__(self, name, kind, scope, value_type):
        super().__init__(name, kind, scope)
        self.value_type = value_type

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
                param = [], define=False, return_type = VoidType()):
        super().__init__(name, kind, scope)
        self.param = param
        self.define = define
        self.return_type = return_type
        
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
        if (not main_check or  (main_check.param is not []) or not main_check.define):
            raise NoEntryPoint()
        
    def var_redeclared_check(self,target,env):
        """Check if a variable is declared in the current environment

        Args:
            target (VariableSymbol): variable to check
            env (List[Symbol]): Environment to check

        Raises:
            Redeclared: if found a symbol witth similar name and scope
        """
        name = target.name
        found = self.lookup(name, reversed(env), lambda x: x.name)
        #!Use reverse to reverser the env list, 
        #!thus the element with match name is the lastest ele
        #*This is a way to "hidden" outer scope elements (!! idk man, wtf)
        if found:
            if (target.scope == found.scope):
                raise Redeclared(kind=Variable(),name=str(name))
    
    def func_redeclared_check(self,target,env):
        """Check if a function is declared in the current environment

        Args:
            target (FunctionSymbol): function to check
            env (List[Symbol]): Environment to check

        Raises:
            Redeclared: if a function symbol with similar name is found 
            with matching parameters and already have a body
        """
        name = target.name
        look_res = self.lookup(name, reversed(env), lambda x: x.name)
        if look_res:
            if (isinstance(look_res,FunctionSymbol)
                and self.compare_parameter_list(look_res.params,target.params)
                and ((look_res.define == False) and (target.define == True))
            ):  #* These condittion verified if a symbol is a forwards declaration
                #*So we should update the body of the function too match the later declaration
                look_res.define = True
            else: 
                raise Redeclared(kind=Function(),name=str(name))
    
    def var_undeclared_check(self, name, env):
        """ Check if variable symbol is declared in the current environment

        Args:
            name (Id): name to check
            env (List[Symbol]): Environment to check

        Raises:
            Undeclared: no Symbol with name = name is declared
            
        Returns: 
            symbol(Symbol): inner most scope symbol with name = name
        """
        symbol = self.lookup(name, reversed(env), lambda x: x.name)
        if not symbol:
            raise Undeclared(kind=Identifier(),name=str(name))
        if not isinstance(symbol, VariableSymbol):
            raise Undeclared(kind=Identifier(),name=str(name))
        return symbol
    
    def func_undeclared_check(self, name, env):
        """Check if func symbol is declared in the current environment

        Args:
            name (Id): func symbol to check
            env (List[Symbol]): Environment to check

        Raises:
            Undeclared: if no symbol found
            Undeclared: found symbol is not a function
        """
        look_res = self.lookup(name, reversed(env), lambda x: x.name)
        if not look_res:
            #*No symbol found
            raise Undeclared(kind=Identifier(),name=str(name))
        if not isinstance(look_res,FuncDecl):
            #*found symbol is not a function
            raise Undeclared(kind=Function(),name=str(name))
        
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
                raise NoDefinition(name=str(func.name))
    
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
    #**********************************#
    #*          VISIT METHOD          *#
    #**********************************#
    #! Every method control it own scope to pass to children via param ref
    #! Children return a symbolic reference of it self, 
    #! or a type for parent to handle
    
    #!Scope env list should be in order [outermost scope, .. innermost scope]
    @param_logger
    def visitProgram(self, ast, param):
        parent_env = param
        decl_list = []
        list(map(lambda symbol : decl_list.append(self.visit(symbol, parent_env + decl_list)), ast.decl))
        self.entry_check(decl_list)
        self.func_definition_check(decl_list)

    @param_logger
    def visitVarDecl(self, ast, param):
        #*param should be a list of current environment variables
        #* look up similar symbol and check var type
        #? should we check for lookups result kind here?
        #? ex: var a lookup res is function a
        parent_env = param
        if (ast.varInit):
            exprType = self.visit(ast.varInit, parent_env)
            if (self.compare_type(exprType, ast.varType)):
                raise TypeMismatchInStatement(ast)
        
        symbol = VariableSymbol(
            name = ast.name,
            kind=Variable(),
            scope=self.scope_pointer,
            value_type=ast.varType
        )
        
        self.var_redeclared_check(symbol, parent_env)

        return symbol

    @param_logger
    def visitFuncDecl(self, ast, param):
        parent_env = param
        self.move_scope_in()
        func_param_list = []
        map(lambda symbol: 
                func_param_list.append(self.visit(symbol, parent_env + func_param_list))
            , ast.param)
        
        for symbol in func_param_list:
            symbol.kind = Parameter()
        
        self.move_scope_out()
        
        if (ast.body):
            define= True
            ret = self.visit(ast.body, parent_env + func_param_list)
        else: 
            define = False
            ret = VoidType()
            
        print(ret)
        symbol = FunctionSymbol(
            name=ast.name,
            kind=Function(),
            scope=self.scope_pointer,
            param=func_param_list,
            define=define,
            return_type=ret
        )
        self.func_redeclared_check(symbol, param)
        return symbol

    def visitNumberType(self, ast, param):
        pass

    def visitBoolType(self, ast, param):
        pass

    def visitStringType(self, ast, param):
        pass

    def visitArrayType(self, ast, param):
        pass

    def visitBinaryOp(self, ast, param):
        pass

    def visitUnaryOp(self, ast, param):
        pass

    def visitCallExpr(self, ast, param):
        pass

    def visitId(self, ast, param):
        '''Return Id'''
        return ast

    def visitArrayCell(self, ast, param):
        pass

    @param_logger
    def visitBlock(self, ast, param):
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
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        if self.in_loop_pointer == 0:
            raise MustInLoop(ast)

    def visitBreak(self, ast, param):
        if self.in_loop_pointer == 0:
            raise MustInLoop(ast)

    def visitReturn(self, ast, param):
        '''Return a type object'''
        if (ast.expr):
            return self.visit(ast.expr, param)
        return VoidType()

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
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
        '''Return Number Type'''
        array_ele_type_list = [self.visit(ele,param) for ele in ast.value]
        initial_type = type(array_ele_type_list[0])
        if (isinstance(initial_type, ArrayType)):
            initial_size = array_ele_type_list[0].size
            if not all(isinstance(x, initial_type) and initial_size == x.size for x in array_ele_type_list):
                raise TypeMismatchInStatement(ast)
            arr_size = [float(len(array_ele_type_list))]+ initial_size
            return ArrayType(size= arr_size, eleType=array_ele_type_list[0])
        if (not all(isinstance(x, initial_type) for x in array_ele_type_list)):
            raise TypeMismatchInStatement(ast)
        arr_size = [float(len(array_ele_type_list))]
        return ArrayType(size=arr_size, eleType=array_ele_type_list[0])
