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


    # Visit a parse tree produced by ZCodeParser#define.
    def visitDefine(self, ctx:ZCodeParser.DefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#code_block.
    def visitCode_block(self, ctx:ZCodeParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#line.
    def visitLine(self, ctx:ZCodeParser.LineContext):
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


    # Visit a parse tree produced by ZCodeParser#value_init.
    def visitValue_init(self, ctx:ZCodeParser.Value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_def.
    def visitVar_def(self, ctx:ZCodeParser.Var_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_assign.
    def visitVar_assign(self, ctx:ZCodeParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_list.
    def visitNumber_list(self, ctx:ZCodeParser.Number_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#number_list_tail.
    def visitNumber_list_tail(self, ctx:ZCodeParser.Number_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_dim_list.
    def visitArray_dim_list(self, ctx:ZCodeParser.Array_dim_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_def.
    def visitArray_def(self, ctx:ZCodeParser.Array_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_init.
    def visitArray_init(self, ctx:ZCodeParser.Array_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#array_value_init.
    def visitArray_value_init(self, ctx:ZCodeParser.Array_value_initContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list.
    def visitParam_list(self, ctx:ZCodeParser.Param_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_list_tail.
    def visitParam_list_tail(self, ctx:ZCodeParser.Param_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_def_list.
    def visitParam_def_list(self, ctx:ZCodeParser.Param_def_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_def_list_tail.
    def visitParam_def_list_tail(self, ctx:ZCodeParser.Param_def_list_tailContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#param_def.
    def visitParam_def(self, ctx:ZCodeParser.Param_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_def.
    def visitFunc_def(self, ctx:ZCodeParser.Func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#foward_func_def.
    def visitFoward_func_def(self, ctx:ZCodeParser.Foward_func_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#func_call.
    def visitFunc_call(self, ctx:ZCodeParser.Func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#index_op.
    def visitIndex_op(self, ctx:ZCodeParser.Index_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#negate_op.
    def visitNegate_op(self, ctx:ZCodeParser.Negate_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#multi_op.
    def visitMulti_op(self, ctx:ZCodeParser.Multi_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#add_op.
    def visitAdd_op(self, ctx:ZCodeParser.Add_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#logic_op.
    def visitLogic_op(self, ctx:ZCodeParser.Logic_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#relational_op.
    def visitRelational_op(self, ctx:ZCodeParser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#string_op.
    def visitString_op(self, ctx:ZCodeParser.String_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#sign_number.
    def visitSign_number(self, ctx:ZCodeParser.Sign_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#literal.
    def visitLiteral(self, ctx:ZCodeParser.LiteralContext):
        return self.visitChildren(ctx)



del ZCodeParser