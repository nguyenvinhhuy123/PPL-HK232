from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *
#!!new import for convention:
# from parser.ZCodeVisitor import ZCodeVisitor
# from parser.ZCodeParser import ZCodeParser
# from utils.AST import *
class ASTGeneration(ZCodeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    #*Parser rule: program:optional_end_line (forward_func | define)* EOF;
    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        #*List of forward func and others define
        #! EOF is child then childe count should > 2 
        if ctx.getChildCount() > 2:
            def_list = []
            for i in range(1, ctx.getChildCount()-1):
                def_list.append(ctx.getChild(i).accept(self)) #* we dont care about if child is forward def or normal def 
        
        res = Program(def_list)
        return res
    
    # Visit a parse tree produced by ZCodeParser#forward_func.
    #*Parser rule: forward_func: forward_func_def end_line; 
    def visitForward_func(self, ctx:ZCodeParser.Forward_funcContext):
        res = ctx.forward_func_def().accept(self)
        return res

    # Visit a parse tree produced by ZCodeParser#main_def.
    #*Parser rule: main_def: KW_FUNC MAIN_TOKEN SEP_OPEN_PAREN SEP_CLOSE_PAREN optional_end_line inner_scope;
    def visitMain_def(self, ctx:ZCodeParser.Main_defContext):
        res = FuncDecl(Id(ctx.MAIN_TOKEN.getText()), [], ctx.inner_scope.accept(self))
        return res

    # Visit a parse tree produced by ZCodeParser#define.
    #*Parser rule: define: func_def | decl end_line | main_def;
    def visitDefine(self, ctx:ZCodeParser.DefineContext):
        if ctx.getChildCount() == 2: 
            return ctx.decl().accept(self)
        else:
            return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#inner_scope.
    #* Parser rule: inner_scope: block_statement end_line | return_statement end_line;
    def visitInner_scope(self, ctx:ZCodeParser.Inner_scopeContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#lines.
    #*Parser rule: lines: (line|statement_line)*;
    def visitLines(self, ctx:ZCodeParser.LinesContext):
        #list of line/stmt to visit
        res = []
        for i in range(ctx.getChildCount()):
            res.append(ctx.getChild(i).accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#line.
    #*Parser rule: line: (decl | assign) end_line ;
    def visitLine(self, ctx:ZCodeParser.LineContext):
        res = ctx.getChild(0).accept(self)
        return res


    # Visit a parse tree produced by ZCodeParser#decl.
    #*Parser rule: decl: (var_def | array_def);
    def visitDecl(self, ctx:ZCodeParser.DeclContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#assign.
    #*Parser rule: assign: (var_assign | array_assign | array_elem_assign);
    def visitAssign(self, ctx:ZCodeParser.AssignContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#statement_line.
    #*Parser rule: statement_line: statement end_line;
    def visitStatement_line(self, ctx:ZCodeParser.Statement_lineContext):
        res = ctx.statement().accept(self)
        return res


    # Visit a parse tree produced by ZCodeParser#statement.
    #*Parser rule: statement: 
    '''
    (if_statement
	| for_statement
	| break_statement
	| continue_statement
	| return_statement
	| block_statement
	| func_call
	| decl
	| assign)
	; '''
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return ctx.getChild(0).accept(self);


    # Visit a parse tree produced by ZCodeParser#type_def.
    #*Parser rule: type_def: KW_NUMBER | KW_STRING | KW_BOOL;
    def visitType_def(self, ctx:ZCodeParser.Type_defContext):
        #*Lexer token only rule
        if (ctx.KW_NUMBER()): return NumberType()
        if (ctx.KW_STRING()): return StringType()
        return BoolType()


    # Visit a parse tree produced by ZCodeParser#implicit_type_def.
    #* implicit_type_def: KW_VAR | KW_DYNAMIC;
    def visitImplicit_type_def(self, ctx:ZCodeParser.Implicit_type_defContext):
        #*Lexer token only rule
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by ZCodeParser#var_def.
    #* Parser rule: var_def: static_var_def | dynamic_var_def ;
    def visitVar_def(self, ctx:ZCodeParser.Var_defContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#var_def_for_param.
    #* Parser rule: var_def_for_param: type_def IDENTIFIER;
    def visitVar_def_for_param(self, ctx:ZCodeParser.Var_def_for_paramContext):
        res = VarDecl(name=Id(ctx.IDENTIFIER().getText()), varType=ctx.type_def().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#value_init.
    #*Parser rule: value_init: OP_ASSIGN expression;
    def visitValue_init(self, ctx:ZCodeParser.Value_initContext):
        return ctx.expression().accept(self)

    # Visit a parse tree produced by ZCodeParser#optional_val_init.
    #*Parser rule: optional_val_init: value_init |;
    def visitOptional_val_init(self, ctx:ZCodeParser.Optional_val_initContext):
        if (ctx.getChildCount() == 1): return ctx.value_init().accept(self)
        return []


    # Visit a parse tree produced by ZCodeParser#static_var_def.
    #*Parser rule: static_var_def: (type_def IDENTIFIER optional_val_init);
    def visitStatic_var_def(self, ctx:ZCodeParser.Static_var_defContext):
        res = VarDecl(name=Id(ctx.IDENTIFIER().getText()), varType=ctx.type_def().accept(self), varInit=ctx.optional_val_init().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#dynamic_var_def.
    #*Parser rule:
    '''
    dynamic_var_def:
	(KW_VAR IDENTIFIER value_init)
	| (KW_DYNAMIC IDENTIFIER optional_val_init)
    ;'''
    def visitDynamic_var_def(self, ctx:ZCodeParser.Dynamic_var_defContext):
        if (ctx.KW_VAR()):
            res = VarDecl(Id(ctx.IDENTIFIER().getText()) , None, ctx.KW_VAR().getText(),ctx.value_init().accept(self))
        else:
            res = VarDecl(Id(ctx.IDENTIFIER().getText()), None, ctx.KW_DYNAMIC().getText(),ctx.optional_val_init().accept(self))
        return res

    # Visit a parse tree produced by ZCodeParser#var_assign.
    #* Parser rule: var_assign: IDENTIFIER value_init;
    def visitVar_assign(self, ctx:ZCodeParser.Var_assignContext):
        res = Assign(Id(ctx.IDENTIFIER().getText()), ctx.value_init().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#dim_list.
    #* Parser rule: dim_list: NUMBER dim_list_tail;
    def visitDim_list(self, ctx:ZCodeParser.Dim_listContext):
        '''
        return a list of float 
        dim list tail should return a number list as well
        '''
        num = float(ctx.NUMBER().getText())
        dimension = [num] + ctx.dim_list_tail().accept(self) 
        # concat with dim_list_tail
        return dimension


    # Visit a parse tree produced by ZCodeParser#dim_list_tail.
    #*Parser rule: dim_list_tail: SEP_COMA NUMBER dim_list_tail |;
    def visitDim_list_tail(self, ctx:ZCodeParser.Dim_list_tailContext):
        '''
        return a list of integer 
        dim list tail should return a number list as well
        '''
        if (not ctx.dim_list_tail()): return []
        num = float(ctx.NUMBER().getText())
        dimension = [num] + ctx.dim_list_tail().accept(self)
        # concat with dim_list_tail
        return dimension


    # Visit a parse tree produced by ZCodeParser#array_dim.
    #* Parser rule: array_dim: SEP_OPEN_BRACK dim_list SEP_CLOSE_BRACK;
    def visitArray_dim(self, ctx:ZCodeParser.Array_dimContext):
        return ctx.dim_list().accept(self)


    # Visit a parse tree produced by ZCodeParser#array_def.
    #*Parser rule: array_def: array_static_def;
    def visitArray_def(self, ctx:ZCodeParser.Array_defContext):
        return ctx.array_static_def().accept(self)


    # Visit a parse tree produced by ZCodeParser#array_def_for_param.
    #*Parser rule: array_def_for_param: type_def array_identifier;
    def visitArray_def_for_param(self, ctx:ZCodeParser.Array_def_for_paramContext):
        (array_id, dimension) = ctx.array_identifier().accept(self)
        res = VarDecl(array_id, ArrayType(dimension, ctx.type_def().accept(self)), None, None)
        return res

    # Visit a parse tree produced by ZCodeParser#array_identifier.
    #*Parser rule: array_identifier: IDENTIFIER array_dim;
    def visitArray_identifier(self, ctx:ZCodeParser.Array_identifierContext):
        '''
        Return a tuple of ID and dimension
        '''
        res = (Id(ctx.IDENTIFIER().getText()), ctx.array_dim().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#array_static_def.
    #*Parser rule: array_static_def: type_def array_identifier optional_array_init;
    def visitArray_static_def(self, ctx:ZCodeParser.Array_static_defContext):
        (array_id, dimension) = ctx.array_identifier().accept(self)
        res = VarDecl(array_id, ArrayType(dimension, ctx.type_def().accept(self)), None, ctx.optional_array_init().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#array_init.
    #*Parser rule: array_init: OP_ASSIGN (expression);
    def visitArray_init(self, ctx:ZCodeParser.Array_initContext):
        res = ctx.expression().accept(self)
        return res


    # Visit a parse tree produced by ZCodeParser#optional_array_init.
    #*Parser rule: optional_array_init: array_init |;
    def visitOptional_array_init(self, ctx:ZCodeParser.Optional_array_initContext):
        if (ctx.getChildCount() != 0): return ctx.array_init().accept(self)
        return None


    # Visit a parse tree produced by ZCodeParser#array_value_init_list.
    #*Parser rule: array_value_init_list: array_value_elem array_value_init_tail;
    def visitArray_value_init_list(self, ctx:ZCodeParser.Array_value_init_listContext):
        "Return list of elements"
        elem_list = [ctx.array_value_elem().accept(self)] + ctx.array_value_init_tail().accept(self)
        return elem_list


    # Visit a parse tree produced by ZCodeParser#array_value_init_tail.
    #*Parser rule: array_value_init_tail: (SEP_COMA array_value_init_list) | ;
    def visitArray_value_init_tail(self, ctx:ZCodeParser.Array_value_init_tailContext):
        "Return list of elements if no child return null list"
        if (ctx.getChildCount() == 0 ): return []
        elem_list = [ctx.array_value_elem().accept(self)] + ctx.array_value_init_tail().accept(self)
        return elem_list


    # Visit a parse tree produced by ZCodeParser#array_value_elem.
    #*Parser rule: array_value_elem: (expression);
    def visitArray_value_elem(self, ctx:ZCodeParser.Array_value_elemContext):
        return ctx.expression().accept(self)


    # Visit a parse tree produced by ZCodeParser#array_value.
    #*Parser rule: array_value: SEP_OPEN_BRACK array_value_init_list SEP_CLOSE_BRACK;
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        res = ArrayLiteral(ctx.array_value_init_list().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#array_assign.
    #*Parser rule: array_assign: IDENTIFIER array_init;
    def visitArray_assign(self, ctx:ZCodeParser.Array_assignContext):
        res = Assign(Id(ctx.IDENTIFIER().getText()), ctx.array_init().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#array_elem_assign.
    #Parser rule: array_elem_assign: array_element_expr array_elem_init;
    def visitArray_elem_assign(self, ctx:ZCodeParser.Array_elem_assignContext):
        res = Assign(ctx.array_element_expr().accept(self), ctx.array_elem_init().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#array_elem_init.
    #*Parser rule: array_elem_init: OP_ASSIGN expression;
    def visitArray_elem_init(self, ctx:ZCodeParser.Array_elem_initContext):
        return ctx.expression().accept(self)


    # Visit a parse tree produced by ZCodeParser#param_def_list.
    #*Parser rule: param_def_list: param optional_end_line param_def_list_tail |;
    def visitParam_def_list(self, ctx:ZCodeParser.Param_def_listContext):
        '''
        Return list of param def
        '''
        if (ctx.getChildCount() == 0): return [] 
        res = [ctx.param().accept(self)] + ctx.param_def_list_tail().accept(self)
        return res


    # Visit a parse tree produced by ZCodeParser#param_def_list_tail.
    #*Parser rule: param_def_list_tail: SEP_COMA param param_def_list_tail|; 
    def visitParam_def_list_tail(self, ctx:ZCodeParser.Param_def_list_tailContext):
        if (ctx.getChildCount() == 0): return [] 
        res = [ctx.param().accept(self)] + ctx.param_def_list_tail().accept(self)
        return res


    # Visit a parse tree produced by ZCodeParser#param.
    #* Parser rule: param: array_def_for_param | var_def_for_param;
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#param_def.
    #*Parser rule: param_def: SEP_OPEN_PAREN param_def_list SEP_CLOSE_PAREN;
    def visitParam_def(self, ctx:ZCodeParser.Param_defContext):
        return ctx.param_def_list().accept(self)


    # Visit a parse tree produced by ZCodeParser#func_def.
    #*Parser rule: func_def: KW_FUNC IDENTIFIER param_def optional_end_line inner_scope;
    def visitFunc_def(self, ctx:ZCodeParser.Func_defContext):
        res = FuncDecl(Id(ctx.IDENTIFIER().getText()), ctx.param_def().accept(self), ctx.inner_scope().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#forward_func_def.
    #*Parser rule: forward_func_def: KW_FUNC IDENTIFIER param_def;
    def visitForward_func_def(self, ctx:ZCodeParser.Forward_func_defContext):
        res = FuncDecl(Id(ctx.IDENTIFIER().getText()), ctx.param_def().accept(self), None)
        return res


    # Visit a parse tree produced by ZCodeParser#expressions.
    #!remove?
    # #*Parser rule: expressions: (expression)*;
    # def visitExpressions(self, ctx:ZCodeParser.ExpressionsContext):
    #     return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    #*Parser rule: expression: string_expr;
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return ctx.string_expr().accept(self)


    # Visit a parse tree produced by ZCodeParser#string_expr.
    #*Parser rule: string_expr: relation_expr string_op relation_expr | relation_expr;
    def visitString_expr(self, ctx:ZCodeParser.String_exprContext):
        if (ctx.getChildCount() == 1): return ctx.relation_expr(0).accept(self)
        res = BinaryOp(ctx.string_op().accept(self), ctx.relation_expr(0).accept(self), ctx.relation_expr(1).accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#string_op.
    #*Parser rule: string_op: OP_STRING_CONCAT;
    def visitString_op(self, ctx:ZCodeParser.String_opContext):
        return ctx.OP_STRING_CONCAT().getText()


    # Visit a parse tree produced by ZCodeParser#relation_expr.
    #*Parser rule: relation_expr: logic_expr relational_op logic_expr | logic_expr;
    def visitRelation_expr(self, ctx:ZCodeParser.Relation_exprContext):
        if (ctx.getChildCount() == 1): return ctx.logic_expr(0).accept(self)
        res = BinaryOp(ctx.relational_op().accept(self), ctx.logic_expr(0).accept(self), ctx.logic_expr(1).accept(self))
        return res

    # Visit a parse tree produced by ZCodeParser#relational_op.
    #*Parser rule: relational_op: (OP_GREATER | OP_GREATER_EQUAL | OP_EQUAL | OP_NOT_EQUAL | OP_SMALLER | OP_SMALLER_EQUAL | OP_STRING_EQUAL);
    def visitRelational_op(self, ctx:ZCodeParser.Relational_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by ZCodeParser#logic_expr.
    #*Parser rule: logic_expr: logic_expr logic_op add_expr | add_expr;
    def visitLogic_expr(self, ctx:ZCodeParser.Logic_exprContext):
        if (ctx.getChildCount() == 1): return ctx.add_expr().accept(self)
        res = BinaryOp(ctx.logic_op().accept(self), ctx.logic_expr().accept(self), ctx.add_expr().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#logic_op.
    #*Parser rule: logic_op: (OP_AND | OP_OR);
    def visitLogic_op(self, ctx:ZCodeParser.Logic_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by ZCodeParser#add_expr.
    #*Parser rule: add_expr: add_expr add_op multi_expr | multi_expr;
    def visitAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        if (ctx.getChildCount() == 1): return ctx.multi_expr().accept(self)
        res = BinaryOp(ctx.add_op().accept(self), ctx.add_expr().accept(self), ctx.multi_expr().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#add_op.
    #*Parser rule: add_op: (OP_ADD | OP_SUBTRACT);
    def visitAdd_op(self, ctx:ZCodeParser.Add_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by ZCodeParser#multi_expr.
    #*Parser rule: multi_expr: multi_expr multi_op negate_expr | negate_expr;
    def visitMulti_expr(self, ctx:ZCodeParser.Multi_exprContext):
        if (ctx.getChildCount() == 1): return ctx.negate_expr().accept(self)
        res = BinaryOp(ctx.multi_op().accept(self), ctx.multi_expr().accept(self), ctx.negate_expr().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#multi_op.
    #*Parser rule: multi_op: (OP_MULTI | OP_DIVIDE | OP_REMAINDER);
    def visitMulti_op(self, ctx:ZCodeParser.Multi_opContext):
        return ctx.getChild(0).getText()


    # Visit a parse tree produced by ZCodeParser#negate_expr.
    #*Parser rule: negate_expr: negate_op negate_expr | sign_expr;
    def visitNegate_expr(self, ctx:ZCodeParser.Negate_exprContext):
        if (ctx.getChildCount() == 1): return ctx.sign_expr().accept(self)
        res = UnaryOp(ctx.negate_op().accept(self), ctx.negate_expr().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#negate_op.
    #*Parser rule: negate_op: OP_NOT;
    def visitNegate_op(self, ctx:ZCodeParser.Negate_opContext):
        return ctx.OP_NOT().getText()


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    #*Parser rule: sign_expr: (OP_SUBTRACT) sign_expr | array_expr;
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        if (ctx.getChildCount() == 1): return ctx.array_expr().accept(self)
        res = UnaryOp(ctx.OP_SUBTRACT().getText(), ctx.sign_expr().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#array_expr.
    #*Parser rule: array_expr: array_element_expr | primary_expression;
    def visitArray_expr(self, ctx:ZCodeParser.Array_exprContext):
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#array_element_expr.
    #*Parser rule: array_element_expr: primary_expression indexer;
    def visitArray_element_expr(self, ctx:ZCodeParser.Array_element_exprContext):
        res = ArrayCell(ctx.primary_expression().accept(self), ctx.indexer().accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#indexer.
    #*Parser rule: indexer: SEP_OPEN_BRACK index_op SEP_CLOSE_BRACK;
    def visitIndexer(self, ctx:ZCodeParser.IndexerContext):
        return ctx.index_op().accept(self)


    # Visit a parse tree produced by ZCodeParser#index_op.
    #*Parser rule: index_op: expression (SEP_COMA index_op | );
    def visitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        '''
        Return a list of expression
        '''
        res = [ctx.expression().accept(self)]
        if (ctx.getChildCount() == 3): res = res + ctx.index_op().accept(self)
        return res

    # Visit a parse tree produced by ZCodeParser#primary_expression.
    #*Parser rule: 
    '''primary_expression:
	SEP_OPEN_PAREN expression SEP_CLOSE_PAREN
	| literal
	| term
	;'''
    def visitPrimary_expression(self, ctx:ZCodeParser.Primary_expressionContext):
        return ctx.expression().accept(self) if (ctx.expression()) else ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#term.
    #*Parser rule: term: IDENTIFIER | func_call ;
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        if (ctx.IDENTIFIER()): return Id(ctx.IDENTIFIER().getText())
        #*if appear in term (or in expression overall)
        #* func call should be defined by class CallExpr
        #*however parser rule func_call visitor return CallStmt
        #*thus this should be modified by term visitor 
        func_result = ctx.func_call().accept(self)
        func_expr = CallExpr(func_result.name, func_result.args)
        return func_expr


    # Visit a parse tree produced by ZCodeParser#if_statement.
    #*Parser rule: if_statement: 
    #*if_clause (end_line elif_clause)* (end_line else_clause | );
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        (if_expr, if_stmt) = ctx.if_clause().accept(self)
        elif_cls = list(map(lambda x: x.accept(self), ctx.elif_clause()))
        else_stmt = ctx.else_clause().accept(self) if ctx.else_clause() else None
        res = If(if_expr, if_stmt, elif_cls, else_stmt)
        return res


    # Visit a parse tree produced by ZCodeParser#if_clause.
    # *Parser rule: if_clause: KW_IF if_condition optional_end_line statement;
    def visitIf_clause(self, ctx:ZCodeParser.If_clauseContext):
        '''
        Return a tuple (Expression, Stmt)
        '''
        return (ctx.if_condition().accept(self), ctx.statement().accept(self))

    # Visit a parse tree produced by ZCodeParser#elif_clause.
    #* Parser rule: elif_clause: KW_ELIF if_condition optional_end_line statement;
    def visitElif_clause(self, ctx:ZCodeParser.Elif_clauseContext):
        '''
        Return a tuple (Expression, Stmt)
        '''
        return (ctx.if_condition().accept(self), ctx.statement().accept(self))


    # Visit a parse tree produced by ZCodeParser#else_clause.
    #*Parser rule: else_clause: KW_ELSE optional_end_line statement;
    def visitElse_clause(self, ctx:ZCodeParser.Else_clauseContext):
        '''
        Return an expression
        '''
        return ctx.statement().accept(self)


    # Visit a parse tree produced by ZCodeParser#if_condition.
    #*Parser rule: if_condition: SEP_OPEN_PAREN expression SEP_CLOSE_PAREN;
    def visitIf_condition(self, ctx:ZCodeParser.If_conditionContext):
        return ctx.expression().accept(self)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    #*Parser rule: for_statement: for_clause condition_clause update_clause optional_end_line statement;
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        for_var = ctx.for_clause().accept(self)
        condition_expr = ctx.condition_clause().accept(self)
        update_expr =ctx.update_clause().accept(self)
        body = ctx.statement().accept(self)
        res = For(for_var, condition_expr, update_expr, body)
        return res


    # Visit a parse tree produced by ZCodeParser#for_clause.
    #*Parser rule: for_clause:KW_FOR IDENTIFIER;
    def visitFor_clause(self, ctx:ZCodeParser.For_clauseContext):
        '''Return an Id'''
        return Id(ctx.IDENTIFIER().getText())


    # Visit a parse tree produced by ZCodeParser#condition_clause.
    #*Parser rule: condition_clause:KW_UNTIL expression;
    def visitCondition_clause(self, ctx:ZCodeParser.Condition_clauseContext):
        '''Return an expression'''
        return ctx.expression().accept(self)


    # Visit a parse tree produced by ZCodeParser#update_clause.
    #*Parser rule: update_clause:KW_BY expression;
    def visitUpdate_clause(self, ctx:ZCodeParser.Update_clauseContext):
        '''return an expression'''
        return ctx.expression().accept(self)

    # Visit a parse tree produced by ZCodeParser#break_statement.
    #*Parser rule: break_statement: KW_BREAK;
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return Break()


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    #*Parser rule: continue_statement:KW_CONTINUE;
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return Continue()


    # Visit a parse tree produced by ZCodeParser#return_statement.
    #*Parser rule: return_statement: KW_RETURN (expression| );
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return Return(ctx.expression().accept(self)) if ctx.expression() else Return(None)


    # Visit a parse tree produced by ZCodeParser#passing_arg.
    #*Parser rule: passing_arg: SEP_OPEN_PAREN passing_list SEP_CLOSE_PAREN;
    def visitPassing_arg(self, ctx:ZCodeParser.Passing_argContext):
        '''Return a list of argument'''
        return ctx.passing_list().accept(self)


    # Visit a parse tree produced by ZCodeParser#passing_list.
    #*Parser rule: passing_list: expression passing_list_tail | 
    def visitPassing_list(self, ctx:ZCodeParser.Passing_listContext):
        '''Return a list of argument'''
        if ( ctx.getChildCount() == 0 ): return []
        arg_list = [ctx.expression().accept(self)] + ctx.passing_list_tail().accept(self)
        return arg_list


    # Visit a parse tree produced by ZCodeParser#passing_list_tail.
    # *Parser rule: passing_list_tail: SEP_COMA expression passing_list_tail | ;
    def visitPassing_list_tail(self, ctx:ZCodeParser.Passing_list_tailContext):
        if ( ctx.getChildCount() == 0 ): return []
        arg_list = [ctx.expression().accept(self)] + ctx.passing_list_tail().accept(self)
        return arg_list


    # Visit a parse tree produced by ZCodeParser#func_call.
    #*Parser rule: func_call: IDENTIFIER passing_arg;
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        func_id = Id(ctx.IDENTIFIER().getText())
        arguments = ctx.passing_arg().accept(self)
        res = CallStmt(func_id, arguments)
        return res


    # Visit a parse tree produced by ZCodeParser#block_statement.
    #*Parser rule: block_statement: KW_BEGIN end_line lines optional_end_line KW_END;
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return Block(ctx.lines().accept(self))


    # Visit a parse tree produced by ZCodeParser#literal.
    #*Parser rule: literal: NUMBER | STRING | boolean | array_value;
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        if (ctx.NUMBER()): return NumberLiteral(float(ctx.NUMBER().getText()))
        if (ctx.STRING()): return StringLiteral(ctx.STRING().getText())
        return ctx.getChild(0).accept(self)


    # Visit a parse tree produced by ZCodeParser#boolean.
    #*Parser rule: boolean: KW_TRUE | KW_FALSE;
    def visitBoolean(self, ctx:ZCodeParser.BooleanContext):
        return BooleanLiteral(True) if ctx.KW_TRUE() else BooleanLiteral(False)


    # Visit a parse tree produced by ZCodeParser#optional_end_line.
    def visitOptional_end_line(self, ctx:ZCodeParser.Optional_end_lineContext):
        '''Not use'''
        pass


    # Visit a parse tree produced by ZCodeParser#end_line.
    def visitEnd_line(self, ctx:ZCodeParser.End_lineContext):
        '''Not use'''
        pass

        

    
