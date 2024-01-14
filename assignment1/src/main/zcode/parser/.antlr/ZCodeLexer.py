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
        4,0,11,101,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,1,0,1,0,1,1,4,1,35,8,1,11,1,12,1,36,1,1,5,1,40,
        8,1,10,1,12,1,43,9,1,1,2,1,2,1,3,1,3,4,3,49,8,3,11,3,12,3,50,1,4,
        4,4,54,8,4,11,4,12,4,55,1,4,3,4,59,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,
        6,1,7,1,7,1,7,1,8,1,8,5,8,73,8,8,10,8,12,8,76,9,8,1,8,1,8,3,8,80,
        8,8,1,8,1,8,1,9,4,9,85,8,9,11,9,12,9,86,1,9,1,9,1,10,1,10,1,11,1,
        11,1,12,1,12,1,12,1,13,1,13,1,14,1,14,0,0,15,1,0,3,1,5,0,7,0,9,2,
        11,3,13,4,15,0,17,5,19,6,21,7,23,8,25,9,27,10,29,11,1,0,6,3,0,65,
        90,95,95,97,122,3,0,48,57,65,90,97,122,1,0,48,57,1,0,46,46,3,0,8,
        9,12,13,32,32,1,0,10,10,104,0,3,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,
        0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,1,31,1,0,0,0,3,34,1,0,0,0,
        5,44,1,0,0,0,7,46,1,0,0,0,9,53,1,0,0,0,11,60,1,0,0,0,13,65,1,0,0,
        0,15,67,1,0,0,0,17,70,1,0,0,0,19,84,1,0,0,0,21,90,1,0,0,0,23,92,
        1,0,0,0,25,94,1,0,0,0,27,97,1,0,0,0,29,99,1,0,0,0,31,32,7,0,0,0,
        32,2,1,0,0,0,33,35,3,1,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,
        0,0,36,37,1,0,0,0,37,41,1,0,0,0,38,40,7,1,0,0,39,38,1,0,0,0,40,43,
        1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,4,1,0,0,0,43,41,1,0,0,0,44,
        45,7,2,0,0,45,6,1,0,0,0,46,48,7,3,0,0,47,49,3,5,2,0,48,47,1,0,0,
        0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,8,1,0,0,0,52,54,3,
        5,2,0,53,52,1,0,0,0,54,55,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,
        58,1,0,0,0,57,59,3,7,3,0,58,57,1,0,0,0,58,59,1,0,0,0,59,10,1,0,0,
        0,60,61,5,109,0,0,61,62,5,97,0,0,62,63,5,105,0,0,63,64,5,110,0,0,
        64,12,1,0,0,0,65,66,1,0,0,0,66,14,1,0,0,0,67,68,5,35,0,0,68,69,5,
        35,0,0,69,16,1,0,0,0,70,74,3,15,7,0,71,73,3,23,11,0,72,71,1,0,0,
        0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,79,1,0,0,0,76,74,
        1,0,0,0,77,80,3,21,10,0,78,80,5,0,0,1,79,77,1,0,0,0,79,78,1,0,0,
        0,80,81,1,0,0,0,81,82,6,8,0,0,82,18,1,0,0,0,83,85,7,4,0,0,84,83,
        1,0,0,0,85,86,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,88,1,0,0,0,
        88,89,6,9,1,0,89,20,1,0,0,0,90,91,5,10,0,0,91,22,1,0,0,0,92,93,8,
        5,0,0,93,24,1,0,0,0,94,95,9,0,0,0,95,96,6,12,2,0,96,26,1,0,0,0,97,
        98,9,0,0,0,98,28,1,0,0,0,99,100,9,0,0,0,100,30,1,0,0,0,9,0,36,41,
        50,55,58,74,79,86,3,1,8,1,6,0,0,1,12,0
    ]

class ZCodeLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    IDENTIFIER = 1
    NUMBER = 2
    KEYWORD = 3
    Operator = 4
    COMMENT = 5
    WS = 6
    NEW_LINE = 7
    NOT_NEW_LINE = 8
    ERROR_CHAR = 9
    UNCLOSE_STRING = 10
    ILLEGAL_ESCAPE = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'\\n'" ]

    symbolicNames = [ "<INVALID>",
            "IDENTIFIER", "NUMBER", "KEYWORD", "Operator", "COMMENT", "WS", 
            "NEW_LINE", "NOT_NEW_LINE", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "IDENTIFIER_HEAD", "IDENTIFIER", "DIGIT", "FLOATING_POINT", 
                  "NUMBER", "KEYWORD", "Operator", "COMMENT_HEAD", "COMMENT", 
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
            actions[8] = self.COMMENT_action 
            actions[12] = self.ERROR_CHAR_action 
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
     


