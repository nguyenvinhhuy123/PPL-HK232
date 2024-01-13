# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/Assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
    return [
        4,0,8,63,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,4,1,25,8,1,11,1,12,1,26,
        1,1,5,1,30,8,1,10,1,12,1,33,9,1,1,2,1,2,1,2,1,3,1,3,3,3,40,8,3,1,
        3,1,3,1,3,1,3,1,4,4,4,47,8,4,11,4,12,4,48,1,4,1,4,1,5,1,5,1,6,1,
        6,1,7,1,7,1,7,1,8,1,8,1,9,1,9,0,0,10,1,0,3,1,5,0,7,2,9,3,11,4,13,
        5,15,6,17,7,19,8,1,0,4,3,0,65,90,95,95,97,122,3,0,48,57,65,90,97,
        122,3,0,8,9,12,13,32,32,1,0,10,10,64,0,3,1,0,0,0,0,7,1,0,0,0,0,9,
        1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,
        1,0,0,0,1,21,1,0,0,0,3,24,1,0,0,0,5,34,1,0,0,0,7,37,1,0,0,0,9,46,
        1,0,0,0,11,52,1,0,0,0,13,54,1,0,0,0,15,56,1,0,0,0,17,59,1,0,0,0,
        19,61,1,0,0,0,21,22,7,0,0,0,22,2,1,0,0,0,23,25,3,1,0,0,24,23,1,0,
        0,0,25,26,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,31,1,0,0,0,28,30,
        7,1,0,0,29,28,1,0,0,0,30,33,1,0,0,0,31,29,1,0,0,0,31,32,1,0,0,0,
        32,4,1,0,0,0,33,31,1,0,0,0,34,35,5,35,0,0,35,36,5,35,0,0,36,6,1,
        0,0,0,37,39,3,5,2,0,38,40,3,13,6,0,39,38,1,0,0,0,39,40,1,0,0,0,40,
        41,1,0,0,0,41,42,3,11,5,0,42,43,1,0,0,0,43,44,6,3,0,0,44,8,1,0,0,
        0,45,47,7,2,0,0,46,45,1,0,0,0,47,48,1,0,0,0,48,46,1,0,0,0,48,49,
        1,0,0,0,49,50,1,0,0,0,50,51,6,4,0,0,51,10,1,0,0,0,52,53,5,10,0,0,
        53,12,1,0,0,0,54,55,8,3,0,0,55,14,1,0,0,0,56,57,9,0,0,0,57,58,6,
        7,1,0,58,16,1,0,0,0,59,60,9,0,0,0,60,18,1,0,0,0,61,62,9,0,0,0,62,
        20,1,0,0,0,5,0,26,31,39,48,2,6,0,0,1,7,0
    ]

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
            "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "COMMENT", "WS", "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDENTIFIER_HEAD", "IDENTIFIER", "COMMENT_HEAD", "COMMENT", 
                  "WS", "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "ZCode.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[7] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


