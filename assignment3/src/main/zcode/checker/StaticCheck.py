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
    ''' Param of a function'''
    param: List[VarDecl]
    ''' define is if a symbol have a definition,
    ie if function is forward declared -> define = false
    ie if var does not have a var init value yet -> define = false
    '''
    define: bool
    '''Return type of symbol,
    None if symbol is funcDecl and have no return stmt 
    if varDecl is scala typed then return type = type declared
    if varDecl is dynamic (var and dynamic kw) then return type = type of Expression
    if if varDecl is dynamic kw and have no expr then return type None'''
    #!None might change to VoidType? 
    #TODO: fix Symbol accordingly
    return_type = Type
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
                return_type = NumberType()
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
        '''target: variable to check, should pass in VarDecl object'''
        '''env: Environment to check'''
        name = target.name
        if self.lookup(name, env, lambda x: x.name):
            raise Redeclared(kind=Variable(),name=name)
    
    def func_redeclared_check(self,target,env):
        '''Check if a variable is declared in the current environment'''
        '''target: function to check, should pass in FuncDecl object'''
        '''env: Environment to check'''
        name = target.name
        look_res = self.lookup(name, env, lambda x: x.name)
        if look_res:
            if (isinstance(look_res,FuncDecl)
                and (look_res.body == None)
                and look_res.params == target.params
                #TODO: write simple param comparision check for this
            ):  #* These condittion verified if a symbol is a forwards declaration
                #*So we should update the body of the function too match the later declaration
                look_res.body == target.body
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
    @param_logger
    def visitProgram(self, ast, param):
        [self.visit(x,param) for x in ast.decl]
        
        self.entry_check(param)
        self.func_definition_check(param)

    @param_logger
    def visitVarDecl(self, ast, param):
        #*param should be a list of current environment variables
        #* look up similar symbol and check var type
        #? should we check for lookups result kind here?
        #? ex: var a lookup res is function a
        self.var_redeclared_check(ast, param)
        
        #TODO: Check variable type mismatch in assignment if any 
        
        #?Should we append to param list here 
        #?or return a VarDecl obj for parent to handle?
        param.append(ast)


    def visitFuncDecl(self, ast, param):
        pass

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

    def visitBlock(self, ast, param):
        pass

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
