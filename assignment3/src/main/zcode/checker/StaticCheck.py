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
    #TODO: fix Symbol accordingly
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
    
    
    def entry_check(self, env):
        '''Check if environment have entry point'''
        '''env: Environment to check'''
        if not self.lookup(name=Id("main"),lst=env,func=lambda x: x.name):
            raise NoEntryPoint()
        
    def var_redeclared_check(self,target,env):
        '''Check if a variable is declared in the current environment'''
        '''target: variable to check, should pass in VarSymbol object'''
        '''env: Environment to check'''
        name = target.name
        found = self.lookup(name, env, lambda x: x.name)
        if found:
            if (target.scope == found.scope):
                raise Redeclared(kind=Variable(),name=name)
    
    def func_redeclared_check(self,target,env):
        '''Check if a variable is declared in the current environment'''
        '''target: function to check, should pass in FuncSymbol object'''
        '''env: Environment to check'''
        name = target.name
        look_res = self.lookup(name, env, lambda x: x.name)
        if look_res:
            if (isinstance(look_res,FunctionSymbol)
                and (look_res.body == None)
                and look_res.params == target.params
                #TODO: write simple param comparision check for this
            ):  #* These condittion verified if a symbol is a forwards declaration
                #*So we should update the body of the function too match the later declaration
                look_res.define = True
            else: 
                raise Redeclared(kind=Function(),name=name)
    
    def var_undeclared_check(self, name, env):
        '''Check if variable symbol is declared in the current environment'''
        '''name: variable symbol to check, should pass in ID object'''
        '''env: Environment to check'''
        if not self.lookup(name, env, lambda x: x.name):
            raise Undeclared(kind=Identifier(),name=name)
    
    def func_undeclared_check(self, name, env):
        '''Check if func symbol is declared in the current environment'''
        '''name: func  symbol to check, should pass in ID object'''
        '''env: Environment to check'''
        look_res = self.lookup(name, env, lambda x: x.name)
        if not look_res:
            #*No symbol found
            raise Undeclared(kind=Identifier(),name=name)
        if not isinstance(look_res,FuncDecl):
            #*found symbol is not a function
            raise Undeclared(kind=Function(),name=name)
        
    def func_definition_check(self, env):
        '''Check if all functions are defined'''
        '''env: Environment to check'''
        for func in env:
            if not isinstance(func,FuncDecl):
                continue
            if not func.body:
                raise NoDefinition(name=func.name)
    #**********************************#
    #*          VISIT METHOD          *#
    #**********************************#
    #! Every method control it own scope to pass to children via param ref
    #! Children return a symbolic reference of it self, 
    #! or a type for parent to handle
   # @param_logger
    def visitProgram(self, ast, param):
        scope = param
        decl_list = []
        list(map(lambda symbol : decl_list.append(self.visit(symbol, decl_list + scope)), ast.decl))
        self.entry_check(decl_list)
        self.func_definition_check(decl_list)

    #@param_logger
    def visitVarDecl(self, ast, param):
        #*param should be a list of current environment variables
        #* look up similar symbol and check var type
        #? should we check for lookups result kind here?
        #? ex: var a lookup res is function a
        if (ast.varInit):
            exprType = self.visit(ast.varInit, param)
            if (type(exprType) != type(ast.varType)):
                raise TypeMismatchInStatement(ast)
            #TODO: Type mismatch checking here
        
        symbol = VariableSymbol(
            name = ast.name,
            kind=Variable(),
            scope=self.scope_pointer,
            value_type=ast.varType
        )
        
        self.var_redeclared_check(symbol, param)

        return symbol

    #@param_logger
    def visitFuncDecl(self, ast, param):
        
        self.scope_pointer += 1
        scope = param
        func_param_list = []
        map(lambda symbol: 
                func_param_list.append(self.visit(symbol, scope + func_param_list))
            , ast.param)
        
        for symbol in func_param_list:
            symbol.kind = Parameter()
        scope = scope + func_param_list
        if (ast.body):
            define= True
            ret = self.visit(ast.body, scope)
        else: 
            define = False
            ret = VoidType()
        self.scope_pointer -= 1
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
        pass

    def visitArrayCell(self, ast, param):
        pass

    #@param_logger
    def visitBlock(self, ast, param):
        '''Return type of return stmt if any else return VoidType'''
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
        #TODO: Return Type of body
        return return_type

    def visitIf(self, ast, param):
        pass

    def visitFor(self, ast, param):
        pass

    def visitContinue(self, ast, param):
        pass

    def visitBreak(self, ast, param):
        pass

    def visitReturn(self, ast, param):
        pass

    def visitAssign(self, ast, param):
        pass

    def visitCallStmt(self, ast, param):
        pass

    def visitNumberLiteral(self, ast, param):
        pass

    def visitBooleanLiteral(self, ast, param):
        pass

    def visitStringLiteral(self, ast, param):
        pass

    def visitArrayLiteral(self, ast, param):
        pass
