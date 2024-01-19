# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\65")
        buf.write("\62\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\4\t\t\t\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\b.\n\b\3\t\3\t\3\t\2\2\n\2\4\6\b\n\f")
        buf.write("\16\20\2\3\5\2\32\33\35\36  \2*\2\22\3\2\2\2\4\24\3\2")
        buf.write("\2\2\6\32\3\2\2\2\b \3\2\2\2\n\"\3\2\2\2\f$\3\2\2\2\16")
        buf.write("-\3\2\2\2\20/\3\2\2\2\22\23\13\2\2\2\23\3\3\2\2\2\24\25")
        buf.write("\7\17\2\2\25\26\7\3\2\2\26\27\7+\2\2\27\30\7.\2\2\30\31")
        buf.write("\5\b\5\2\31\5\3\2\2\2\32\33\7\17\2\2\33\34\7\4\2\2\34")
        buf.write("\35\7+\2\2\35\36\7.\2\2\36\37\5\b\5\2\37\7\3\2\2\2 !\3")
        buf.write("\2\2\2!\t\3\2\2\2\"#\13\2\2\2#\13\3\2\2\2$%\7\4\2\2%&")
        buf.write("\7#\2\2&\'\5\16\b\2\'\r\3\2\2\2(.\7\5\2\2)*\7\4\2\2*+")
        buf.write("\5\20\t\2+,\5\16\b\2,.\3\2\2\2-(\3\2\2\2-)\3\2\2\2.\17")
        buf.write("\3\2\2\2/\60\t\2\2\2\60\21\3\2\2\2\3-")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'true'", "'false'", "'number'", "'bool'", "'string'", 
                     "'return'", "'var'", "'dynamic'", "'func'", "'for'", 
                     "'until'", "'by'", "'break'", "'continue'", "'if'", 
                     "'else'", "'elif'", "'begin'", "'end'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", "'='", 
                     "'<-'", "'!='", "'<'", "'>'", "'<='", "'>='", "'=='", 
                     "'...'", "'('", "')'", "'['", "']'", "','", "<INVALID>", 
                     "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "MAIN_TOKEN", "IDENTIFIER", "NUMBER", 
                      "STRING", "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", 
                      "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
                      "KW_FUNC", "KW_FOR", "KW_UNTIL", "KW_BY", "KW_BREAK", 
                      "KW_CONTINUE", "KW_IF", "KW_ELSE", "KW_ELIF", "KW_BEGIN", 
                      "KW_END", "OP_ADD", "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", 
                      "OP_REMAINDER", "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", 
                      "OP_LEFT_ARROW", "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", 
                      "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", "OP_EQUAL_COMPARE", 
                      "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", 
                      "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT", 
                      "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_main_derclaration = 1
    RULE_function = 2
    RULE_code_block = 3
    RULE_var_declaration = 4
    RULE_var_assign = 5
    RULE_expression = 6
    RULE_operation = 7

    ruleNames =  [ "program", "main_derclaration", "function", "code_block", 
                   "var_declaration", "var_assign", "expression", "operation" ]

    EOF = Token.EOF
    MAIN_TOKEN=1
    IDENTIFIER=2
    NUMBER=3
    STRING=4
    KW_TRUE=5
    KW_FALSE=6
    KW_NUMBER=7
    KW_BOOL=8
    KW_STRING=9
    KW_RETURN=10
    KW_VAR=11
    KW_DYNAMIC=12
    KW_FUNC=13
    KW_FOR=14
    KW_UNTIL=15
    KW_BY=16
    KW_BREAK=17
    KW_CONTINUE=18
    KW_IF=19
    KW_ELSE=20
    KW_ELIF=21
    KW_BEGIN=22
    KW_END=23
    OP_ADD=24
    OP_SUBTRACT=25
    OP_MULTI=26
    OP_DIVIDE=27
    OP_REMAINDER=28
    OP_NOT=29
    OP_AND=30
    OP_OR=31
    OP_EQUAL=32
    OP_LEFT_ARROW=33
    OP_NOT_EQUAL=34
    OP_SMALLER=35
    OP_GREATER=36
    OP_SMALLER_EQUAL=37
    OP_GREATER_EQUAL=38
    OP_EQUAL_COMPARE=39
    OP_TRIPLE_DOT=40
    SEP_OPEN_PAREN=41
    SEP_CLOSE_PAREN=42
    SEP_OPEN_BRACK=43
    SEP_CLOSE_BRACK=44
    SEP_COMA=45
    COMMENT=46
    WS=47
    NEW_LINE=48
    ERROR_CHAR=49
    UNCLOSE_STRING=50
    ILLEGAL_ESCAPE=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_derclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def MAIN_TOKEN(self):
            return self.getToken(ZCodeParser.MAIN_TOKEN, 0)

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZCodeParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_main_derclaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_derclaration" ):
                return visitor.visitMain_derclaration(self)
            else:
                return visitor.visitChildren(self)




    def main_derclaration(self):

        localctx = ZCodeParser.Main_derclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_derclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.match(ZCodeParser.KW_FUNC)
            self.state = 19
            self.match(ZCodeParser.MAIN_TOKEN)
            self.state = 20
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 21
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
            self.state = 22
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_FUNC(self):
            return self.getToken(ZCodeParser.KW_FUNC, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def SEP_OPEN_PAREN(self):
            return self.getToken(ZCodeParser.SEP_OPEN_PAREN, 0)

        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def code_block(self):
            return self.getTypedRuleContext(ZCodeParser.Code_blockContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_function

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ZCodeParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(ZCodeParser.KW_FUNC)
            self.state = 25
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 26
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 27
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
            self.state = 28
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Code_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_code_block

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCode_block" ):
                return visitor.visitCode_block(self)
            else:
                return visitor.visitChildren(self)




    def code_block(self):

        localctx = ZCodeParser.Code_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declaration" ):
                return visitor.visitVar_declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_declaration(self):

        localctx = ZCodeParser.Var_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_declaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def OP_LEFT_ARROW(self):
            return self.getToken(ZCodeParser.OP_LEFT_ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = ZCodeParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 35
            self.match(ZCodeParser.OP_LEFT_ARROW)
            self.state = 36
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def operation(self):
            return self.getTypedRuleContext(ZCodeParser.OperationContext,0)


        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 39
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 40
                self.operation()
                self.state = 41
                self.expression()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_ADD(self):
            return self.getToken(ZCodeParser.OP_ADD, 0)

        def OP_AND(self):
            return self.getToken(ZCodeParser.OP_AND, 0)

        def OP_SUBTRACT(self):
            return self.getToken(ZCodeParser.OP_SUBTRACT, 0)

        def OP_REMAINDER(self):
            return self.getToken(ZCodeParser.OP_REMAINDER, 0)

        def OP_DIVIDE(self):
            return self.getToken(ZCodeParser.OP_DIVIDE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_operation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = ZCodeParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.OP_ADD) | (1 << ZCodeParser.OP_SUBTRACT) | (1 << ZCodeParser.OP_DIVIDE) | (1 << ZCodeParser.OP_REMAINDER) | (1 << ZCodeParser.OP_AND))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





