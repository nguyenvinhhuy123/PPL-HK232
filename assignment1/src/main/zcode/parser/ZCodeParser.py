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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\66")
        buf.write("\u00b7\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3")
        buf.write("\4\3\4\5\4@\n\4\3\5\3\5\3\5\5\5E\n\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\f\3\f\3\f\5\f")
        buf.write("W\n\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\fc\n\f")
        buf.write("\3\f\5\ff\n\f\3\r\3\r\3\r\3\r\3\16\3\16\5\16n\n\16\3\17")
        buf.write("\3\17\3\17\5\17s\n\17\3\20\3\20\3\20\3\20\3\21\3\21\3")
        buf.write("\21\3\21\5\21}\n\21\3\22\3\22\3\22\5\22\u0082\n\22\3\23")
        buf.write("\3\23\6\23\u0086\n\23\r\23\16\23\u0087\3\23\5\23\u008b")
        buf.write("\n\23\3\23\3\23\3\24\3\24\5\24\u0091\n\24\3\25\3\25\3")
        buf.write("\25\5\25\u0096\n\25\3\26\3\26\3\26\3\26\5\26\u009c\n\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\5\27\u00a3\n\27\3\30\3\30\3")
        buf.write("\30\3\30\5\30\u00a9\n\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u00b3\n\31\3\32\3\32\3\32\2\2\33\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\2\5\3")
        buf.write("\2\7\t\3\2\13\f\5\2\30\31\33\34\36\36\2\u00b0\2\64\3\2")
        buf.write("\2\2\4\66\3\2\2\2\6?\3\2\2\2\bD\3\2\2\2\nF\3\2\2\2\fH")
        buf.write("\3\2\2\2\16J\3\2\2\2\20L\3\2\2\2\22N\3\2\2\2\24P\3\2\2")
        buf.write("\2\26e\3\2\2\2\30g\3\2\2\2\32k\3\2\2\2\34o\3\2\2\2\36")
        buf.write("t\3\2\2\2 x\3\2\2\2\"~\3\2\2\2$\u0083\3\2\2\2&\u008e\3")
        buf.write("\2\2\2(\u0092\3\2\2\2*\u0097\3\2\2\2,\u009d\3\2\2\2.\u00a4")
        buf.write("\3\2\2\2\60\u00b2\3\2\2\2\62\u00b4\3\2\2\2\64\65\13\2")
        buf.write("\2\2\65\3\3\2\2\2\66\67\7\r\2\2\678\7\3\2\289\7)\2\29")
        buf.write(":\7,\2\2:;\5\n\6\2;\5\3\2\2\2<=\7\31\2\2=@\7/\2\2>@\7")
        buf.write("/\2\2?<\3\2\2\2?>\3\2\2\2@\7\3\2\2\2AE\5\6\4\2BE\7\60")
        buf.write("\2\2CE\7\4\2\2DA\3\2\2\2DB\3\2\2\2DC\3\2\2\2E\t\3\2\2")
        buf.write("\2FG\3\2\2\2G\13\3\2\2\2HI\3\2\2\2I\r\3\2\2\2JK\3\2\2")
        buf.write("\2K\17\3\2\2\2LM\t\2\2\2M\21\3\2\2\2NO\t\3\2\2O\23\3\2")
        buf.write("\2\2PQ\7!\2\2QR\5\60\31\2R\25\3\2\2\2ST\5\20\t\2TV\7.")
        buf.write("\2\2UW\5\24\13\2VU\3\2\2\2VW\3\2\2\2WX\3\2\2\2XY\7\63")
        buf.write("\2\2Yf\3\2\2\2Z[\7\13\2\2[\\\7.\2\2\\]\5\24\13\2]^\7\63")
        buf.write("\2\2^f\3\2\2\2_`\7\f\2\2`b\7.\2\2ac\5\24\13\2ba\3\2\2")
        buf.write("\2bc\3\2\2\2cd\3\2\2\2df\7\63\2\2eS\3\2\2\2eZ\3\2\2\2")
        buf.write("e_\3\2\2\2f\27\3\2\2\2gh\7.\2\2hi\5\24\13\2ij\7\63\2\2")
        buf.write("j\31\3\2\2\2km\7/\2\2ln\5\34\17\2ml\3\2\2\2mn\3\2\2\2")
        buf.write("n\33\3\2\2\2op\7-\2\2pr\7/\2\2qs\5\34\17\2rq\3\2\2\2r")
        buf.write("s\3\2\2\2s\35\3\2\2\2tu\7+\2\2uv\5\32\16\2vw\7,\2\2w\37")
        buf.write("\3\2\2\2xy\5\20\t\2yz\7.\2\2z|\5\36\20\2{}\5\"\22\2|{")
        buf.write("\3\2\2\2|}\3\2\2\2}!\3\2\2\2~\u0081\7!\2\2\177\u0082\7")
        buf.write(".\2\2\u0080\u0082\5$\23\2\u0081\177\3\2\2\2\u0081\u0080")
        buf.write("\3\2\2\2\u0082#\3\2\2\2\u0083\u008a\7+\2\2\u0084\u0086")
        buf.write("\5$\23\2\u0085\u0084\3\2\2\2\u0086\u0087\3\2\2\2\u0087")
        buf.write("\u0085\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008b\3\2\2\2")
        buf.write("\u0089\u008b\5\b\5\2\u008a\u0085\3\2\2\2\u008a\u0089\3")
        buf.write("\2\2\2\u008b\u008c\3\2\2\2\u008c\u008d\7,\2\2\u008d%\3")
        buf.write("\2\2\2\u008e\u0090\7.\2\2\u008f\u0091\5(\25\2\u0090\u008f")
        buf.write("\3\2\2\2\u0090\u0091\3\2\2\2\u0091\'\3\2\2\2\u0092\u0093")
        buf.write("\7-\2\2\u0093\u0095\7.\2\2\u0094\u0096\5(\25\2\u0095\u0094")
        buf.write("\3\2\2\2\u0095\u0096\3\2\2\2\u0096)\3\2\2\2\u0097\u0098")
        buf.write("\5\20\t\2\u0098\u0099\7.\2\2\u0099\u009b\3\2\2\2\u009a")
        buf.write("\u009c\5*\26\2\u009b\u009a\3\2\2\2\u009b\u009c\3\2\2\2")
        buf.write("\u009c+\3\2\2\2\u009d\u009e\7-\2\2\u009e\u009f\5\20\t")
        buf.write("\2\u009f\u00a0\7.\2\2\u00a0\u00a2\3\2\2\2\u00a1\u00a3")
        buf.write("\5,\27\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("-\3\2\2\2\u00a4\u00a5\7\r\2\2\u00a5\u00a6\7.\2\2\u00a6")
        buf.write("\u00a8\7)\2\2\u00a7\u00a9\5*\26\2\u00a8\u00a7\3\2\2\2")
        buf.write("\u00a8\u00a9\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00ab\7")
        buf.write(",\2\2\u00ab\u00ac\5\n\6\2\u00ac/\3\2\2\2\u00ad\u00b3\7")
        buf.write("/\2\2\u00ae\u00af\7.\2\2\u00af\u00b0\5\62\32\2\u00b0\u00b1")
        buf.write("\5\60\31\2\u00b1\u00b3\3\2\2\2\u00b2\u00ad\3\2\2\2\u00b2")
        buf.write("\u00ae\3\2\2\2\u00b3\61\3\2\2\2\u00b4\u00b5\t\4\2\2\u00b5")
        buf.write("\63\3\2\2\2\23?DVbemr|\u0081\u0087\u008a\u0090\u0095\u009b")
        buf.write("\u00a2\u00a8\u00b2")
        return buf.getvalue()


class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'...'", "'('", "')'", 
                     "'['", "']'", "','", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "MAIN_TOKEN", "BOOL", "KW_TRUE", "KW_FALSE", 
                      "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", 
                      "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", 
                      "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", "KW_ELSE", 
                      "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", "OP_SUBTRACT", 
                      "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", "OP_NOT", 
                      "OP_AND", "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", "OP_NOT_EQUAL", 
                      "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", 
                      "OP_EQUAL_COMPARE", "OP_TRIPLE_DOT", "SEP_OPEN_PAREN", 
                      "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", "SEP_CLOSE_BRACK", 
                      "SEP_COMA", "IDENTIFIER", "NUMBER", "STRING", "COMMENT", 
                      "WS", "NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_main_def = 1
    RULE_sign_number = 2
    RULE_literal = 3
    RULE_code_block = 4
    RULE_line = 5
    RULE_statement = 6
    RULE_type_def = 7
    RULE_implicit_type_def = 8
    RULE_value_init = 9
    RULE_var_declare = 10
    RULE_var_assign = 11
    RULE_number_list = 12
    RULE_number_list_tail = 13
    RULE_array_dim_list = 14
    RULE_array_declare = 15
    RULE_array_init = 16
    RULE_array_value_init = 17
    RULE_param_list = 18
    RULE_param_list_tail = 19
    RULE_param_def_list = 20
    RULE_param_def_list_tail = 21
    RULE_func_def = 22
    RULE_expression = 23
    RULE_operation = 24

    ruleNames =  [ "program", "main_def", "sign_number", "literal", "code_block", 
                   "line", "statement", "type_def", "implicit_type_def", 
                   "value_init", "var_declare", "var_assign", "number_list", 
                   "number_list_tail", "array_dim_list", "array_declare", 
                   "array_init", "array_value_init", "param_list", "param_list_tail", 
                   "param_def_list", "param_def_list_tail", "func_def", 
                   "expression", "operation" ]

    EOF = Token.EOF
    MAIN_TOKEN=1
    BOOL=2
    KW_TRUE=3
    KW_FALSE=4
    KW_NUMBER=5
    KW_BOOL=6
    KW_STRING=7
    KW_RETURN=8
    KW_VAR=9
    KW_DYNAMIC=10
    KW_FUNC=11
    KW_FOR=12
    KW_UNTIL=13
    KW_BY=14
    KW_BREAK=15
    KW_CONTINUE=16
    KW_IF=17
    KW_ELSE=18
    KW_ELIF=19
    KW_BEGIN=20
    KW_END=21
    OP_ADD=22
    OP_SUBTRACT=23
    OP_MULTI=24
    OP_DIVIDE=25
    OP_REMAINDER=26
    OP_NOT=27
    OP_AND=28
    OP_OR=29
    OP_EQUAL=30
    OP_LEFT_ARROW=31
    OP_NOT_EQUAL=32
    OP_SMALLER=33
    OP_GREATER=34
    OP_SMALLER_EQUAL=35
    OP_GREATER_EQUAL=36
    OP_EQUAL_COMPARE=37
    OP_TRIPLE_DOT=38
    SEP_OPEN_PAREN=39
    SEP_CLOSE_PAREN=40
    SEP_OPEN_BRACK=41
    SEP_CLOSE_BRACK=42
    SEP_COMA=43
    IDENTIFIER=44
    NUMBER=45
    STRING=46
    COMMENT=47
    WS=48
    NEW_LINE=49
    ERROR_CHAR=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52

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
            self.state = 50
            self.matchWildcard()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Main_defContext(ParserRuleContext):
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
            return ZCodeParser.RULE_main_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMain_def" ):
                return visitor.visitMain_def(self)
            else:
                return visitor.visitChildren(self)




    def main_def(self):

        localctx = ZCodeParser.Main_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_main_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(ZCodeParser.KW_FUNC)
            self.state = 53
            self.match(ZCodeParser.MAIN_TOKEN)
            self.state = 54
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 55
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
            self.state = 56
            self.code_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sign_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_SUBTRACT(self):
            return self.getToken(ZCodeParser.OP_SUBTRACT, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_sign_number

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSign_number" ):
                return visitor.visitSign_number(self)
            else:
                return visitor.visitChildren(self)




    def sign_number(self):

        localctx = ZCodeParser.Sign_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sign_number)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_SUBTRACT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ZCodeParser.OP_SUBTRACT)
                self.state = 59
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 60
                self.match(ZCodeParser.NUMBER)
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


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sign_number(self):
            return self.getTypedRuleContext(ZCodeParser.Sign_numberContext,0)


        def STRING(self):
            return self.getToken(ZCodeParser.STRING, 0)

        def BOOL(self):
            return self.getToken(ZCodeParser.BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.OP_SUBTRACT, ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.sign_number()
                pass
            elif token in [ZCodeParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(ZCodeParser.STRING)
                pass
            elif token in [ZCodeParser.BOOL]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(ZCodeParser.BOOL)
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
        self.enterRule(localctx, 8, self.RULE_code_block)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_line

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = ZCodeParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_line)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ZCodeParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_NUMBER(self):
            return self.getToken(ZCodeParser.KW_NUMBER, 0)

        def KW_STRING(self):
            return self.getToken(ZCodeParser.KW_STRING, 0)

        def KW_BOOL(self):
            return self.getToken(ZCodeParser.KW_BOOL, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_type_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_def" ):
                return visitor.visitType_def(self)
            else:
                return visitor.visitChildren(self)




    def type_def(self):

        localctx = ZCodeParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0)):
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


    class Implicit_type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_implicit_type_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImplicit_type_def" ):
                return visitor.visitImplicit_type_def(self)
            else:
                return visitor.visitChildren(self)




    def implicit_type_def(self):

        localctx = ZCodeParser.Implicit_type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_implicit_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==ZCodeParser.KW_VAR or _la==ZCodeParser.KW_DYNAMIC):
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


    class Value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LEFT_ARROW(self):
            return self.getToken(ZCodeParser.OP_LEFT_ARROW, 0)

        def expression(self):
            return self.getTypedRuleContext(ZCodeParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_value_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue_init" ):
                return visitor.visitValue_init(self)
            else:
                return visitor.visitChildren(self)




    def value_init(self):

        localctx = ZCodeParser.Value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(ZCodeParser.OP_LEFT_ARROW)
            self.state = 79
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_declare" ):
                return visitor.visitVar_declare(self)
            else:
                return visitor.visitChildren(self)




    def var_declare(self):

        localctx = ZCodeParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.KW_NUMBER, ZCodeParser.KW_BOOL, ZCodeParser.KW_STRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.type_def()
                self.state = 82
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.OP_LEFT_ARROW:
                    self.state = 83
                    self.value_init()


                self.state = 86
                self.match(ZCodeParser.NEW_LINE)
                pass
            elif token in [ZCodeParser.KW_VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.match(ZCodeParser.KW_VAR)
                self.state = 89
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 90
                self.value_init()
                self.state = 91
                self.match(ZCodeParser.NEW_LINE)
                pass
            elif token in [ZCodeParser.KW_DYNAMIC]:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 94
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==ZCodeParser.OP_LEFT_ARROW:
                    self.state = 95
                    self.value_init()


                self.state = 98
                self.match(ZCodeParser.NEW_LINE)
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


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def NEW_LINE(self):
            return self.getToken(ZCodeParser.NEW_LINE, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_assign

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_assign" ):
                return visitor.visitVar_assign(self)
            else:
                return visitor.visitChildren(self)




    def var_assign(self):

        localctx = ZCodeParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 102
            self.value_init()
            self.state = 103
            self.match(ZCodeParser.NEW_LINE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def number_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Number_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_list" ):
                return visitor.visitNumber_list(self)
            else:
                return visitor.visitChildren(self)




    def number_list(self):

        localctx = ZCodeParser.Number_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_number_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(ZCodeParser.NUMBER)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SEP_COMA:
                self.state = 106
                self.number_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Number_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def NUMBER(self):
            return self.getToken(ZCodeParser.NUMBER, 0)

        def number_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Number_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_number_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumber_list_tail" ):
                return visitor.visitNumber_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def number_list_tail(self):

        localctx = ZCodeParser.Number_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_number_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(ZCodeParser.SEP_COMA)
            self.state = 110
            self.match(ZCodeParser.NUMBER)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SEP_COMA:
                self.state = 111
                self.number_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_dim_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_BRACK(self):
            return self.getToken(ZCodeParser.SEP_OPEN_BRACK, 0)

        def number_list(self):
            return self.getTypedRuleContext(ZCodeParser.Number_listContext,0)


        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_array_dim_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_dim_list" ):
                return visitor.visitArray_dim_list(self)
            else:
                return visitor.visitChildren(self)




    def array_dim_list(self):

        localctx = ZCodeParser.Array_dim_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_dim_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 115
            self.number_list()
            self.state = 116
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_declareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_dim_list(self):
            return self.getTypedRuleContext(ZCodeParser.Array_dim_listContext,0)


        def array_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_declare

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_declare" ):
                return visitor.visitArray_declare(self)
            else:
                return visitor.visitChildren(self)




    def array_declare(self):

        localctx = ZCodeParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.type_def()
            self.state = 119
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 120
            self.array_dim_list()
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.OP_LEFT_ARROW:
                self.state = 121
                self.array_init()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OP_LEFT_ARROW(self):
            return self.getToken(ZCodeParser.OP_LEFT_ARROW, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def array_value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Array_value_initContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_init" ):
                return visitor.visitArray_init(self)
            else:
                return visitor.visitChildren(self)




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 124
            self.match(ZCodeParser.OP_LEFT_ARROW)
            self.state = 127
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.IDENTIFIER]:
                self.state = 125
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 126
                self.array_value_init()
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


    class Array_value_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_OPEN_BRACK(self):
            return self.getToken(ZCodeParser.SEP_OPEN_BRACK, 0)

        def SEP_CLOSE_BRACK(self):
            return self.getToken(ZCodeParser.SEP_CLOSE_BRACK, 0)

        def literal(self):
            return self.getTypedRuleContext(ZCodeParser.LiteralContext,0)


        def array_value_init(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ZCodeParser.Array_value_initContext)
            else:
                return self.getTypedRuleContext(ZCodeParser.Array_value_initContext,i)


        def getRuleIndex(self):
            return ZCodeParser.RULE_array_value_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_value_init" ):
                return visitor.visitArray_value_init(self)
            else:
                return visitor.visitChildren(self)




    def array_value_init(self):

        localctx = ZCodeParser.Array_value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_value_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 136
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.SEP_OPEN_BRACK]:
                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 130
                    self.array_value_init()
                    self.state = 133 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==ZCodeParser.SEP_OPEN_BRACK):
                        break

                pass
            elif token in [ZCodeParser.BOOL, ZCodeParser.OP_SUBTRACT, ZCodeParser.NUMBER, ZCodeParser.STRING]:
                self.state = 135
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 138
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list" ):
                return visitor.visitParam_list(self)
            else:
                return visitor.visitChildren(self)




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 142
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SEP_COMA:
                self.state = 141
                self.param_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_list_tail" ):
                return visitor.visitParam_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_list_tail(self):

        localctx = ZCodeParser.Param_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(ZCodeParser.SEP_COMA)
            self.state = 145
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==ZCodeParser.SEP_COMA:
                self.state = 146
                self.param_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_def_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_def_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def_list" ):
                return visitor.visitParam_def_list(self)
            else:
                return visitor.visitChildren(self)




    def param_def_list(self):

        localctx = ZCodeParser.Param_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param_def_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.type_def()
            self.state = 150
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0):
                self.state = 152
                self.param_def_list()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Param_def_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEP_COMA(self):
            return self.getToken(ZCodeParser.SEP_COMA, 0)

        def type_def(self):
            return self.getTypedRuleContext(ZCodeParser.Type_defContext,0)


        def IDENTIFIER(self):
            return self.getToken(ZCodeParser.IDENTIFIER, 0)

        def param_def_list_tail(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_list_tailContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_param_def_list_tail

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam_def_list_tail" ):
                return visitor.visitParam_def_list_tail(self)
            else:
                return visitor.visitChildren(self)




    def param_def_list_tail(self):

        localctx = ZCodeParser.Param_def_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param_def_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(ZCodeParser.SEP_COMA)

            self.state = 156
            self.type_def()
            self.state = 157
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 159
                self.param_def_list_tail()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Func_defContext(ParserRuleContext):
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


        def param_def_list(self):
            return self.getTypedRuleContext(ZCodeParser.Param_def_listContext,0)


        def getRuleIndex(self):
            return ZCodeParser.RULE_func_def

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunc_def" ):
                return visitor.visitFunc_def(self)
            else:
                return visitor.visitChildren(self)




    def func_def(self):

        localctx = ZCodeParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            self.match(ZCodeParser.KW_FUNC)
            self.state = 163
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 164
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ZCodeParser.KW_NUMBER) | (1 << ZCodeParser.KW_BOOL) | (1 << ZCodeParser.KW_STRING))) != 0):
                self.state = 165
                self.param_def_list()


            self.state = 168
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
            self.state = 169
            self.code_block()
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
        self.enterRule(localctx, 46, self.RULE_expression)
        try:
            self.state = 176
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [ZCodeParser.NUMBER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [ZCodeParser.IDENTIFIER]:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 173
                self.operation()
                self.state = 174
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
        self.enterRule(localctx, 48, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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





