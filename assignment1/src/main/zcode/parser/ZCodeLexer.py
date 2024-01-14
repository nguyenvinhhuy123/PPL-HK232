# Generated from main/zcode/parser/ZCode.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *
#MSSV: 2152597



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\n")
        buf.write("F\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\6\3\33")
        buf.write("\n\3\r\3\16\3\34\3\3\7\3 \n\3\f\3\16\3#\13\3\3\4\3\4\3")
        buf.write("\4\3\5\3\5\7\5*\n\5\f\5\16\5-\13\5\3\5\3\5\5\5\61\n\5")
        buf.write("\3\5\3\5\3\6\6\6\66\n\6\r\6\16\6\67\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\n\3\n\3\13\3\13\2\2\f\3\2\5\3\7\2")
        buf.write("\t\4\13\5\r\6\17\7\21\b\23\t\25\n\3\2\6\5\2C\\aac|\5\2")
        buf.write("\62;C\\c|\5\2\n\13\16\17\"\"\3\2\f\f\2H\2\5\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3\2\2\2\5\32\3")
        buf.write("\2\2\2\7$\3\2\2\2\t\'\3\2\2\2\13\65\3\2\2\2\r;\3\2\2\2")
        buf.write("\17=\3\2\2\2\21?\3\2\2\2\23B\3\2\2\2\25D\3\2\2\2\27\30")
        buf.write("\t\2\2\2\30\4\3\2\2\2\31\33\5\3\2\2\32\31\3\2\2\2\33\34")
        buf.write("\3\2\2\2\34\32\3\2\2\2\34\35\3\2\2\2\35!\3\2\2\2\36 \t")
        buf.write("\3\2\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2")
        buf.write("\"\6\3\2\2\2#!\3\2\2\2$%\7%\2\2%&\7%\2\2&\b\3\2\2\2\'")
        buf.write("+\5\7\4\2(*\5\17\b\2)(\3\2\2\2*-\3\2\2\2+)\3\2\2\2+,\3")
        buf.write("\2\2\2,\60\3\2\2\2-+\3\2\2\2.\61\5\r\7\2/\61\7\2\2\3\60")
        buf.write(".\3\2\2\2\60/\3\2\2\2\61\62\3\2\2\2\62\63\b\5\2\2\63\n")
        buf.write("\3\2\2\2\64\66\t\4\2\2\65\64\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("\65\3\2\2\2\678\3\2\2\289\3\2\2\29:\b\6\3\2:\f\3\2\2\2")
        buf.write(";<\7\f\2\2<\16\3\2\2\2=>\n\5\2\2>\20\3\2\2\2?@\13\2\2")
        buf.write("\2@A\b\t\4\2A\22\3\2\2\2BC\13\2\2\2C\24\3\2\2\2DE\13\2")
        buf.write("\2\2E\26\3\2\2\2\b\2\34!+\60\67\5\3\5\3\b\2\2\3\t\2")
        return buf.getvalue()


class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    COMMENT = 2
    WS = 3
    NEW_LINE = 4
    NOT_NEW_LINE = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "COMMENT", "WS", "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDENTIFIER_HEAD", "IDENTIFIER", "COMMENT_HEAD", "COMMENT", 
                  "WS", "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[3] = self.COMMENT_action 
            actions[7] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def COMMENT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            skip()
     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


