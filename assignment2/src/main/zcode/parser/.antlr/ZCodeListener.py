# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/assignment2/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .ZCodeParser import ZCodeParser
else:
    from ZCodeParser import ZCodeParser

# This class defines a complete listener for a parse tree produced by ZCodeParser.
class ZCodeListener(ParseTreeListener):

    # Enter a parse tree produced by ZCodeParser#program.
    def enterProgram(self, ctx:ZCodeParser.ProgramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#program.
    def exitProgram(self, ctx:ZCodeParser.ProgramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#main_def.
    def enterMain_def(self, ctx:ZCodeParser.Main_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#main_def.
    def exitMain_def(self, ctx:ZCodeParser.Main_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forward_func.
    def enterForward_func(self, ctx:ZCodeParser.Forward_funcContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forward_func.
    def exitForward_func(self, ctx:ZCodeParser.Forward_funcContext):
        pass


    # Enter a parse tree produced by ZCodeParser#define.
    def enterDefine(self, ctx:ZCodeParser.DefineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#define.
    def exitDefine(self, ctx:ZCodeParser.DefineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#inner_scope.
    def enterInner_scope(self, ctx:ZCodeParser.Inner_scopeContext):
        pass

    # Exit a parse tree produced by ZCodeParser#inner_scope.
    def exitInner_scope(self, ctx:ZCodeParser.Inner_scopeContext):
        pass


    # Enter a parse tree produced by ZCodeParser#lines.
    def enterLines(self, ctx:ZCodeParser.LinesContext):
        pass

    # Exit a parse tree produced by ZCodeParser#lines.
    def exitLines(self, ctx:ZCodeParser.LinesContext):
        pass


    # Enter a parse tree produced by ZCodeParser#line.
    def enterLine(self, ctx:ZCodeParser.LineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#line.
    def exitLine(self, ctx:ZCodeParser.LineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#decl.
    def enterDecl(self, ctx:ZCodeParser.DeclContext):
        pass

    # Exit a parse tree produced by ZCodeParser#decl.
    def exitDecl(self, ctx:ZCodeParser.DeclContext):
        pass


    # Enter a parse tree produced by ZCodeParser#assign.
    def enterAssign(self, ctx:ZCodeParser.AssignContext):
        pass

    # Exit a parse tree produced by ZCodeParser#assign.
    def exitAssign(self, ctx:ZCodeParser.AssignContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement_line.
    def enterStatement_line(self, ctx:ZCodeParser.Statement_lineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement_line.
    def exitStatement_line(self, ctx:ZCodeParser.Statement_lineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#statement.
    def enterStatement(self, ctx:ZCodeParser.StatementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#statement.
    def exitStatement(self, ctx:ZCodeParser.StatementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#type_def.
    def enterType_def(self, ctx:ZCodeParser.Type_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#type_def.
    def exitType_def(self, ctx:ZCodeParser.Type_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#implicit_type_def.
    def enterImplicit_type_def(self, ctx:ZCodeParser.Implicit_type_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#implicit_type_def.
    def exitImplicit_type_def(self, ctx:ZCodeParser.Implicit_type_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var_def.
    def enterVar_def(self, ctx:ZCodeParser.Var_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var_def.
    def exitVar_def(self, ctx:ZCodeParser.Var_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var_def_for_param.
    def enterVar_def_for_param(self, ctx:ZCodeParser.Var_def_for_paramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var_def_for_param.
    def exitVar_def_for_param(self, ctx:ZCodeParser.Var_def_for_paramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#value_init.
    def enterValue_init(self, ctx:ZCodeParser.Value_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#value_init.
    def exitValue_init(self, ctx:ZCodeParser.Value_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_val_init.
    def enterOptional_val_init(self, ctx:ZCodeParser.Optional_val_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_val_init.
    def exitOptional_val_init(self, ctx:ZCodeParser.Optional_val_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#static_var_def.
    def enterStatic_var_def(self, ctx:ZCodeParser.Static_var_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#static_var_def.
    def exitStatic_var_def(self, ctx:ZCodeParser.Static_var_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dynamic_var_def.
    def enterDynamic_var_def(self, ctx:ZCodeParser.Dynamic_var_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dynamic_var_def.
    def exitDynamic_var_def(self, ctx:ZCodeParser.Dynamic_var_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#var_assign.
    def enterVar_assign(self, ctx:ZCodeParser.Var_assignContext):
        pass

    # Exit a parse tree produced by ZCodeParser#var_assign.
    def exitVar_assign(self, ctx:ZCodeParser.Var_assignContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dim_list.
    def enterDim_list(self, ctx:ZCodeParser.Dim_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dim_list.
    def exitDim_list(self, ctx:ZCodeParser.Dim_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#dim_list_tail.
    def enterDim_list_tail(self, ctx:ZCodeParser.Dim_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#dim_list_tail.
    def exitDim_list_tail(self, ctx:ZCodeParser.Dim_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_dim.
    def enterArray_dim(self, ctx:ZCodeParser.Array_dimContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_dim.
    def exitArray_dim(self, ctx:ZCodeParser.Array_dimContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_def.
    def enterArray_def(self, ctx:ZCodeParser.Array_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_def.
    def exitArray_def(self, ctx:ZCodeParser.Array_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_def_for_param.
    def enterArray_def_for_param(self, ctx:ZCodeParser.Array_def_for_paramContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_def_for_param.
    def exitArray_def_for_param(self, ctx:ZCodeParser.Array_def_for_paramContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_identifier.
    def enterArray_identifier(self, ctx:ZCodeParser.Array_identifierContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_identifier.
    def exitArray_identifier(self, ctx:ZCodeParser.Array_identifierContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_static_def.
    def enterArray_static_def(self, ctx:ZCodeParser.Array_static_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_static_def.
    def exitArray_static_def(self, ctx:ZCodeParser.Array_static_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_init.
    def enterArray_init(self, ctx:ZCodeParser.Array_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_init.
    def exitArray_init(self, ctx:ZCodeParser.Array_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_array_init.
    def enterOptional_array_init(self, ctx:ZCodeParser.Optional_array_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_array_init.
    def exitOptional_array_init(self, ctx:ZCodeParser.Optional_array_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_value_init_list.
    def enterArray_value_init_list(self, ctx:ZCodeParser.Array_value_init_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_value_init_list.
    def exitArray_value_init_list(self, ctx:ZCodeParser.Array_value_init_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_value_init_tail.
    def enterArray_value_init_tail(self, ctx:ZCodeParser.Array_value_init_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_value_init_tail.
    def exitArray_value_init_tail(self, ctx:ZCodeParser.Array_value_init_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_value_elem.
    def enterArray_value_elem(self, ctx:ZCodeParser.Array_value_elemContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_value_elem.
    def exitArray_value_elem(self, ctx:ZCodeParser.Array_value_elemContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_value.
    def enterArray_value(self, ctx:ZCodeParser.Array_valueContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_value.
    def exitArray_value(self, ctx:ZCodeParser.Array_valueContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_assign.
    def enterArray_assign(self, ctx:ZCodeParser.Array_assignContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_assign.
    def exitArray_assign(self, ctx:ZCodeParser.Array_assignContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_elem_assign.
    def enterArray_elem_assign(self, ctx:ZCodeParser.Array_elem_assignContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_elem_assign.
    def exitArray_elem_assign(self, ctx:ZCodeParser.Array_elem_assignContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_elem_init.
    def enterArray_elem_init(self, ctx:ZCodeParser.Array_elem_initContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_elem_init.
    def exitArray_elem_init(self, ctx:ZCodeParser.Array_elem_initContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_def_list.
    def enterParam_def_list(self, ctx:ZCodeParser.Param_def_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_def_list.
    def exitParam_def_list(self, ctx:ZCodeParser.Param_def_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_def_list_tail.
    def enterParam_def_list_tail(self, ctx:ZCodeParser.Param_def_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_def_list_tail.
    def exitParam_def_list_tail(self, ctx:ZCodeParser.Param_def_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param.
    def enterParam(self, ctx:ZCodeParser.ParamContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param.
    def exitParam(self, ctx:ZCodeParser.ParamContext):
        pass


    # Enter a parse tree produced by ZCodeParser#param_def.
    def enterParam_def(self, ctx:ZCodeParser.Param_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#param_def.
    def exitParam_def(self, ctx:ZCodeParser.Param_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_def.
    def enterFunc_def(self, ctx:ZCodeParser.Func_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_def.
    def exitFunc_def(self, ctx:ZCodeParser.Func_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#forward_func_def.
    def enterForward_func_def(self, ctx:ZCodeParser.Forward_func_defContext):
        pass

    # Exit a parse tree produced by ZCodeParser#forward_func_def.
    def exitForward_func_def(self, ctx:ZCodeParser.Forward_func_defContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expressions.
    def enterExpressions(self, ctx:ZCodeParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expressions.
    def exitExpressions(self, ctx:ZCodeParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by ZCodeParser#expression.
    def enterExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#expression.
    def exitExpression(self, ctx:ZCodeParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#string_expr.
    def enterString_expr(self, ctx:ZCodeParser.String_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#string_expr.
    def exitString_expr(self, ctx:ZCodeParser.String_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#string_op.
    def enterString_op(self, ctx:ZCodeParser.String_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#string_op.
    def exitString_op(self, ctx:ZCodeParser.String_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relation_expr.
    def enterRelation_expr(self, ctx:ZCodeParser.Relation_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relation_expr.
    def exitRelation_expr(self, ctx:ZCodeParser.Relation_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#relational_op.
    def enterRelational_op(self, ctx:ZCodeParser.Relational_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#relational_op.
    def exitRelational_op(self, ctx:ZCodeParser.Relational_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logic_expr.
    def enterLogic_expr(self, ctx:ZCodeParser.Logic_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logic_expr.
    def exitLogic_expr(self, ctx:ZCodeParser.Logic_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#logic_op.
    def enterLogic_op(self, ctx:ZCodeParser.Logic_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#logic_op.
    def exitLogic_op(self, ctx:ZCodeParser.Logic_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#add_expr.
    def enterAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#add_expr.
    def exitAdd_expr(self, ctx:ZCodeParser.Add_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#add_op.
    def enterAdd_op(self, ctx:ZCodeParser.Add_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#add_op.
    def exitAdd_op(self, ctx:ZCodeParser.Add_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multi_expr.
    def enterMulti_expr(self, ctx:ZCodeParser.Multi_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multi_expr.
    def exitMulti_expr(self, ctx:ZCodeParser.Multi_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#multi_op.
    def enterMulti_op(self, ctx:ZCodeParser.Multi_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#multi_op.
    def exitMulti_op(self, ctx:ZCodeParser.Multi_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#negate_expr.
    def enterNegate_expr(self, ctx:ZCodeParser.Negate_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#negate_expr.
    def exitNegate_expr(self, ctx:ZCodeParser.Negate_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#negate_op.
    def enterNegate_op(self, ctx:ZCodeParser.Negate_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#negate_op.
    def exitNegate_op(self, ctx:ZCodeParser.Negate_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#sign_expr.
    def enterSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#sign_expr.
    def exitSign_expr(self, ctx:ZCodeParser.Sign_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_expr.
    def enterArray_expr(self, ctx:ZCodeParser.Array_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_expr.
    def exitArray_expr(self, ctx:ZCodeParser.Array_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#array_element_expr.
    def enterArray_element_expr(self, ctx:ZCodeParser.Array_element_exprContext):
        pass

    # Exit a parse tree produced by ZCodeParser#array_element_expr.
    def exitArray_element_expr(self, ctx:ZCodeParser.Array_element_exprContext):
        pass


    # Enter a parse tree produced by ZCodeParser#indexer.
    def enterIndexer(self, ctx:ZCodeParser.IndexerContext):
        pass

    # Exit a parse tree produced by ZCodeParser#indexer.
    def exitIndexer(self, ctx:ZCodeParser.IndexerContext):
        pass


    # Enter a parse tree produced by ZCodeParser#index_op.
    def enterIndex_op(self, ctx:ZCodeParser.Index_opContext):
        pass

    # Exit a parse tree produced by ZCodeParser#index_op.
    def exitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        pass


    # Enter a parse tree produced by ZCodeParser#primary_expression.
    def enterPrimary_expression(self, ctx:ZCodeParser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#primary_expression.
    def exitPrimary_expression(self, ctx:ZCodeParser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#term.
    def enterTerm(self, ctx:ZCodeParser.TermContext):
        pass

    # Exit a parse tree produced by ZCodeParser#term.
    def exitTerm(self, ctx:ZCodeParser.TermContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_statement.
    def enterIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_statement.
    def exitIf_statement(self, ctx:ZCodeParser.If_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_clause.
    def enterIf_clause(self, ctx:ZCodeParser.If_clauseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_clause.
    def exitIf_clause(self, ctx:ZCodeParser.If_clauseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#elif_clause.
    def enterElif_clause(self, ctx:ZCodeParser.Elif_clauseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#elif_clause.
    def exitElif_clause(self, ctx:ZCodeParser.Elif_clauseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#else_clause.
    def enterElse_clause(self, ctx:ZCodeParser.Else_clauseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#else_clause.
    def exitElse_clause(self, ctx:ZCodeParser.Else_clauseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#if_condition.
    def enterIf_condition(self, ctx:ZCodeParser.If_conditionContext):
        pass

    # Exit a parse tree produced by ZCodeParser#if_condition.
    def exitIf_condition(self, ctx:ZCodeParser.If_conditionContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_statement.
    def enterFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_statement.
    def exitFor_statement(self, ctx:ZCodeParser.For_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#for_clause.
    def enterFor_clause(self, ctx:ZCodeParser.For_clauseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#for_clause.
    def exitFor_clause(self, ctx:ZCodeParser.For_clauseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#condition_clause.
    def enterCondition_clause(self, ctx:ZCodeParser.Condition_clauseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#condition_clause.
    def exitCondition_clause(self, ctx:ZCodeParser.Condition_clauseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#update_clause.
    def enterUpdate_clause(self, ctx:ZCodeParser.Update_clauseContext):
        pass

    # Exit a parse tree produced by ZCodeParser#update_clause.
    def exitUpdate_clause(self, ctx:ZCodeParser.Update_clauseContext):
        pass


    # Enter a parse tree produced by ZCodeParser#break_statement.
    def enterBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#break_statement.
    def exitBreak_statement(self, ctx:ZCodeParser.Break_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#continue_statement.
    def enterContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#continue_statement.
    def exitContinue_statement(self, ctx:ZCodeParser.Continue_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#return_statement.
    def enterReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#return_statement.
    def exitReturn_statement(self, ctx:ZCodeParser.Return_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#passing_arg.
    def enterPassing_arg(self, ctx:ZCodeParser.Passing_argContext):
        pass

    # Exit a parse tree produced by ZCodeParser#passing_arg.
    def exitPassing_arg(self, ctx:ZCodeParser.Passing_argContext):
        pass


    # Enter a parse tree produced by ZCodeParser#passing_list.
    def enterPassing_list(self, ctx:ZCodeParser.Passing_listContext):
        pass

    # Exit a parse tree produced by ZCodeParser#passing_list.
    def exitPassing_list(self, ctx:ZCodeParser.Passing_listContext):
        pass


    # Enter a parse tree produced by ZCodeParser#passing_list_tail.
    def enterPassing_list_tail(self, ctx:ZCodeParser.Passing_list_tailContext):
        pass

    # Exit a parse tree produced by ZCodeParser#passing_list_tail.
    def exitPassing_list_tail(self, ctx:ZCodeParser.Passing_list_tailContext):
        pass


    # Enter a parse tree produced by ZCodeParser#func_call.
    def enterFunc_call(self, ctx:ZCodeParser.Func_callContext):
        pass

    # Exit a parse tree produced by ZCodeParser#func_call.
    def exitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        pass


    # Enter a parse tree produced by ZCodeParser#block_statement.
    def enterBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        pass

    # Exit a parse tree produced by ZCodeParser#block_statement.
    def exitBlock_statement(self, ctx:ZCodeParser.Block_statementContext):
        pass


    # Enter a parse tree produced by ZCodeParser#literal.
    def enterLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass

    # Exit a parse tree produced by ZCodeParser#literal.
    def exitLiteral(self, ctx:ZCodeParser.LiteralContext):
        pass


    # Enter a parse tree produced by ZCodeParser#boolean.
    def enterBoolean(self, ctx:ZCodeParser.BooleanContext):
        pass

    # Exit a parse tree produced by ZCodeParser#boolean.
    def exitBoolean(self, ctx:ZCodeParser.BooleanContext):
        pass


    # Enter a parse tree produced by ZCodeParser#optional_end_line.
    def enterOptional_end_line(self, ctx:ZCodeParser.Optional_end_lineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#optional_end_line.
    def exitOptional_end_line(self, ctx:ZCodeParser.Optional_end_lineContext):
        pass


    # Enter a parse tree produced by ZCodeParser#end_line.
    def enterEnd_line(self, ctx:ZCodeParser.End_lineContext):
        pass

    # Exit a parse tree produced by ZCodeParser#end_line.
    def exitEnd_line(self, ctx:ZCodeParser.End_lineContext):
        pass



del ZCodeParser