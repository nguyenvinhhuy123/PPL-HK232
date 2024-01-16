# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/Assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,52,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,1,0,0,
        0,3,1,1,0,0,0,0
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
                     "'='", "'<-'", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'...'", "'('", "')'", "'['", "']'", "','", 
                     "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "NUMBER", "BOOLEN", "STRING", 
                      "KW_TRUE", "KW_FALSE", "KW_NUMBER", "KW_BOOL", "KW_STRING", 
                      "KW_RETURN", "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", 
                      "KW_UNTIL", "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", 
                      "KW_ELSE", "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", 
                      "OP_SUBTRACT", "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", 
                      "OP_NOT", "OP_AND", "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", 
                      "OP_NOT_EQUAL", "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", 
                      "OP_GREATER_EQUAL", "OP_EQUAL_COMPARE", "OP_TRIPLE_DOT", 
                      "SEP_OPEN_PAREN", "SEP_CLOSE_PAREN", "SEP_OPEN_BRACK", 
                      "SEP_CLOSE_BRACK", "SEP_COMA", "COMMENT", "WS", "NEW_LINE", 
                      "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    IDENTIFIER=1
    NUMBER=2
    BOOLEN=3
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
    NOT_NEW_LINE=49
    ERROR_CHAR=50
    UNCLOSE_STRING=51
    ILLEGAL_ESCAPE=52

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ZCodeParser.RULE_program




    def program(self):

        localctx = ZCodeParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





