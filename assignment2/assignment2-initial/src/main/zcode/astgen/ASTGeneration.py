from ZCodeVisitor import ZCodeVisitor
from ZCodeParser import ZCodeParser
from AST import *

class ASTGeneration(ZCodeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    #*Parser rule: program:optional_end_line (forward_func | define)* EOF;
    def visitProgram(self,ctx:ZCodeParser.ProgramContext):
        #*List of forward func and others define
        #! EOF is child then childe count should > 2 
        if ctx.getChildCount() > 2:
            def_list = []
            for i in range(1, ctx.getChildCount()-1):
                def_list += ctx.getChild(i).accept() #* we dont care about if child is forward def or normal def 
        
        res = [ctx.optional_end_line().accept(self),Program(def_list)]
        return res
    
    # Visit a parse tree produced by ZCodeParser#forward_func.
    #*Parser rule: forward_func: forward_func_def end_line; 
    def visitForward_func(self, ctx:ZCodeParser.Forward_funcContext):
        res = [ctx.forward_func_def().accept(self),ctx.end_line().accept(self)]
        return res

    # Visit a parse tree produced by ZCodeParser#main_def.
    #*Parser rule: main_def: KW_FUNC MAIN_TOKEN SEP_OPEN_PAREN SEP_CLOSE_PAREN optional_end_line inner_scope;
    def visitMain_def(self, ctx:ZCodeParser.Main_defContext):
        res = FuncDecl(ctx.MAIN_TOKEN.getText(), [], ctx.inner_scope.accept(self))
        return res


    # Visit a parse tree produced by ZCodeParser#define.
    #*Parser rule: define: func_def | decl end_line | main_def;
    def visitDefine(self, ctx:ZCodeParser.DefineContext):
        if ctx.getChildCount() == 2: 
            return [ctx.decl().accept(self),ctx.end_line().accept(self)]
        else:
            return ctx.getChild(0).accept()


    # Visit a parse tree produced by ZCodeParser#inner_scope.
    #* Parser rule: inner_scope: block_statement end_line | return_statement end_line;
    def visitInner_scope(self, ctx:ZCodeParser.Inner_scopeContext):
        return [ctx.getChild(0).accept(self),ctx.end_line().accept(self)]


    # Visit a parse tree produced by ZCodeParser#lines.
    #*Parser rule: lines: (line|statement_line)*;
    def visitLines(self, ctx:ZCodeParser.LinesContext):
        #list of line/stmt to visit
        res = []
        for i in range(0, ctx.getChildCount()-1):
            res += ctx.getChild(i).accept(self)
        return res


    # Visit a parse tree produced by ZCodeParser#line.
    #*Parser rule: line: (decl | assign) end_line ;
    def visitLine(self, ctx:ZCodeParser.LineContext):
        res = [ctx.getChild(0).accept(self), ctx.end_line().accept(self)]
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
        res = [ctx.statement().accept(self), ctx.end_line().accept(self)]
        return res


    # Visit a parse tree produced by ZCodeParser#statement.
    def visitStatement(self, ctx:ZCodeParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#type_def.
    def visitType_def(self, ctx:ZCodeParser.Type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#implicit_type_def.
    def visitImplicit_type_def(self, ctx:ZCodeParser.Implicit_type_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_def.
    def visitVar_def(self, ctx:ZCodeParser.Var_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_def_for_param.
    def visitVar_def_for_param(self, ctx:ZCodeParser.Var_def_for_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#value_init.
    def visitValue_init(self, ctx:ZCodeParser.Value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_val_init.
    def visitOptional_val_init(self, ctx:ZCodeParser.Optional_val_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#static_var_def.
    def visitStatic_var_def(self, ctx:ZCodeParser.Static_var_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dynamic_var_def.
    def visitDynamic_var_def(self, ctx:ZCodeParser.Dynamic_var_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_assign.
    def visitVar_assign(self, ctx:ZCodeParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dim_list.
    def visitDim_list(self, ctx:ZCodeParser.Dim_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#dim_list_tail.
    def visitDim_list_tail(self, ctx:ZCodeParser.Dim_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_dim.
    def visitArray_dim(self, ctx:ZCodeParser.Array_dimContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_def.
    def visitArray_def(self, ctx:ZCodeParser.Array_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_def_for_param.
    def visitArray_def_for_param(self, ctx:ZCodeParser.Array_def_for_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_identifier.
    def visitArray_identifier(self, ctx:ZCodeParser.Array_identifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_static_def.
    def visitArray_static_def(self, ctx:ZCodeParser.Array_static_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_init.
    def visitArray_init(self, ctx:ZCodeParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_array_init.
    def visitOptional_array_init(self, ctx:ZCodeParser.Optional_array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value_init_list.
    def visitArray_value_init_list(self, ctx:ZCodeParser.Array_value_init_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value_init_tail.
    def visitArray_value_init_tail(self, ctx:ZCodeParser.Array_value_init_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value_elem.
    def visitArray_value_elem(self, ctx:ZCodeParser.Array_value_elemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value.
    def visitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_assign.
    def visitArray_assign(self, ctx:ZCodeParser.Array_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_elem_assign.
    def visitArray_elem_assign(self, ctx:ZCodeParser.Array_elem_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_elem_init.
    def visitArray_elem_init(self, ctx:ZCodeParser.Array_elem_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_def_list.
    def visitParam_def_list(self, ctx:ZCodeParser.Param_def_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_def_list_tail.
    def visitParam_def_list_tail(self, ctx:ZCodeParser.Param_def_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param.
    def visitParam(self, ctx:ZCodeParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_def.
    def visitParam_def(self, ctx:ZCodeParser.Param_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_def.
    def visitFunc_def(self, ctx:ZCodeParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forward_func_def.
    def visitForward_func_def(self, ctx:ZCodeParser.Forward_func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expressions.
    def visitExpressions(self, ctx:ZCodeParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_expr.
    def visitString_expr(self, ctx:ZCodeParser.String_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_op.
    def visitString_op(self, ctx:ZCodeParser.String_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relation_expr.
    def visitRelation_expr(self, ctx:ZCodeParser.Relation_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_op.
    def visitRelational_op(self, ctx:ZCodeParser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logic_expr.
    def visitLogic_expr(self, ctx:ZCodeParser.Logic_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logic_op.
    def visitLogic_op(self, ctx:ZCodeParser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_expr.
    def visitAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_op.
    def visitAdd_op(self, ctx:ZCodeParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multi_expr.
    def visitMulti_expr(self, ctx:ZCodeParser.Multi_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multi_op.
    def visitMulti_op(self, ctx:ZCodeParser.Multi_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#negate_expr.
    def visitNegate_expr(self, ctx:ZCodeParser.Negate_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#negate_op.
    def visitNegate_op(self, ctx:ZCodeParser.Negate_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_expr.
    def visitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_expr.
    def visitArray_expr(self, ctx:ZCodeParser.Array_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_element_expr.
    def visitArray_element_expr(self, ctx:ZCodeParser.Array_element_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#indexer.
    def visitIndexer(self, ctx:ZCodeParser.IndexerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_op.
    def visitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#primary_expression.
    def visitPrimary_expression(self, ctx:ZCodeParser.Primary_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#term.
    def visitTerm(self, ctx:ZCodeParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_statement.
    def visitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_clause.
    def visitIf_clause(self, ctx:ZCodeParser.If_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#elif_clause.
    def visitElif_clause(self, ctx:ZCodeParser.Elif_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#else_clause.
    def visitElse_clause(self, ctx:ZCodeParser.Else_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#if_condition.
    def visitIf_condition(self, ctx:ZCodeParser.If_conditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_statement.
    def visitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#for_clause.
    def visitFor_clause(self, ctx:ZCodeParser.For_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#condition_clause.
    def visitCondition_clause(self, ctx:ZCodeParser.Condition_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#update_clause.
    def visitUpdate_clause(self, ctx:ZCodeParser.Update_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#break_statement.
    def visitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#continue_statement.
    def visitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#return_statement.
    def visitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#passing_arg.
    def visitPassing_arg(self, ctx:ZCodeParser.Passing_argContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#passing_list.
    def visitPassing_list(self, ctx:ZCodeParser.Passing_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#passing_list_tail.
    def visitPassing_list_tail(self, ctx:ZCodeParser.Passing_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#block_statement.
    def visitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#boolean.
    def visitBoolean(self, ctx:ZCodeParser.BooleanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_end_line.
    def visitOptional_end_line(self, ctx:ZCodeParser.Optional_end_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#end_line.
    def visitEnd_line(self, ctx:ZCodeParser.End_lineContext):
        return self.visitChildren(ctx)

        

    
