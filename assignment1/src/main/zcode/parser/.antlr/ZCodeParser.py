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
        4,1,45,5,2,0,7,0,1,0,1,0,1,0,0,0,1,0,0,0,3,0,2,1,0,0,0,2,3,1,0,0,
        0,3,1,1,0,0,0,0
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'true'", "'false'", 
                     "'number'", "'bool'", "'string'", "'return'", "'var'", 
                     "'dynamic'", "'func'", "'for'", "'until'", "'by'", 
                     "'break'", "'continue'", "'if'", "'else'", "'elif'", 
                     "'begin'", "'end'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'not'", "'and'", "'or'", "'='", "'<-'", "'!='", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'...'", "<INVALID>", 
                     "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "IDENTIFIER", "NUMBER", "KW_TRUE", "KW_FALSE", 
                      "KW_NUMBER", "KW_BOOL", "KW_STRING", "KW_RETURN", 
                      "KW_VAR", "KW_DYNAMIC", "KW_FUNC", "KW_FOR", "KW_UNTIL", 
                      "KW_BY", "KW_BREAK", "KW_CONTINUE", "KW_IF", "KW_ELSE", 
                      "KW_ELIF", "KW_BEGIN", "KW_END", "OP_ADD", "OP_SUBTRACT", 
                      "OP_MULTI", "OP_DIVIDE", "OP_REMAINDER", "OP_NOT", 
                      "OP_AND", "OP_OR", "OP_EQUAL", "OP_LEFT_ARROW", "OP_NOT_EQUAL", 
                      "OP_SMALLER", "OP_GREATER", "OP_SMALLER_EQUAL", "OP_GREATER_EQUAL", 
                      "OP_EQUAL_COMPARE", "OP_TRIPLE_DOT", "COMMENT", "WS", 
                      "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    IDENTIFIER=1
    NUMBER=2
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
    COMMENT=39
    WS=40
    NEW_LINE=41
    NOT_NEW_LINE=42
    ERROR_CHAR=43
    UNCLOSE_STRING=44
    ILLEGAL_ESCAPE=45

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





