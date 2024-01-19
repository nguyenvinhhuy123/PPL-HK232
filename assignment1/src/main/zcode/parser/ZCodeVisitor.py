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


    # Visit a parse tree produced by ZCodeParser#main_derclaration.
    def visitMain_derclaration(self, ctx:ZCodeParser.Main_derclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#function.
    def visitFunction(self, ctx:ZCodeParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#code_block.
    def visitCode_block(self, ctx:ZCodeParser.Code_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_declaration.
    def visitVar_declaration(self, ctx:ZCodeParser.Var_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#var_assign.
    def visitVar_assign(self, ctx:ZCodeParser.Var_assignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#expression.
    def visitExpression(self, ctx:ZCodeParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ZCodeParser#operation.
    def visitOperation(self, ctx:ZCodeParser.OperationContext):
        return self.visitChildren(ctx)



del ZCodeParser