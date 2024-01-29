# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete generic visitor for a parse tree produced by ZCodeParser.

class ZCodeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ZCodeParser#program.
    def visitProgram(self, ctx:ZCodeParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#main_def.
    def visitMain_def(self, ctx:ZCodeParser.Main_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#forward_func.
    def visitForward_func(self, ctx:ZCodeParser.Forward_funcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#define.
    def visitDefine(self, ctx:ZCodeParser.DefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#inner_scope.
    def visitInner_scope(self, ctx:ZCodeParser.Inner_scopeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#lines.
    def visitLines(self, ctx:ZCodeParser.LinesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#line.
    def visitLine(self, ctx:ZCodeParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#def_line.
    def visitDef_line(self, ctx:ZCodeParser.Def_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#assign_line.
    def visitAssign_line(self, ctx:ZCodeParser.Assign_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expr_line.
    def visitExpr_line(self, ctx:ZCodeParser.Expr_lineContext):
        return self.visitChildren(ctx)


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


    # Visit a parse tree produced by ZCodeParser#array_implicit_def.
    def visitArray_implicit_def(self, ctx:ZCodeParser.Array_implicit_defContext):
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


    # Visit a parse tree produced by ZCodeParser#array_value_init.
    def visitArray_value_init(self, ctx:ZCodeParser.Array_value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_assign.
    def visitArray_assign(self, ctx:ZCodeParser.Array_assignContext):
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


    # Visit a parse tree produced by ZCodeParser#end_line.
    def visitEnd_line(self, ctx:ZCodeParser.End_lineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#optional_end_line.
    def visitOptional_end_line(self, ctx:ZCodeParser.Optional_end_lineContext):
        return self.visitChildren(ctx)



del ZCodeParser