# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/Exercise2/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,20,107,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,1,2,1,3,4,3,62,8,3,11,3,12,3,63,1,4,4,4,67,8,4,11,4,
        12,4,68,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,
        1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,
        1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,20,1,20,1,20,0,0,21,1,1,3,2,
        5,3,7,4,9,5,11,0,13,6,15,7,17,8,19,9,21,10,23,11,25,12,27,13,29,
        14,31,15,33,16,35,17,37,18,39,19,41,20,1,0,3,2,0,65,90,97,122,1,
        0,48,57,3,0,9,10,13,13,32,32,107,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,
        0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,
        0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,
        0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,
        0,0,39,1,0,0,0,0,41,1,0,0,0,1,43,1,0,0,0,3,47,1,0,0,0,5,53,1,0,0,
        0,7,61,1,0,0,0,9,66,1,0,0,0,11,70,1,0,0,0,13,73,1,0,0,0,15,76,1,
        0,0,0,17,78,1,0,0,0,19,80,1,0,0,0,21,82,1,0,0,0,23,84,1,0,0,0,25,
        86,1,0,0,0,27,88,1,0,0,0,29,90,1,0,0,0,31,92,1,0,0,0,33,94,1,0,0,
        0,35,96,1,0,0,0,37,98,1,0,0,0,39,100,1,0,0,0,41,104,1,0,0,0,43,44,
        5,105,0,0,44,45,5,110,0,0,45,46,5,116,0,0,46,2,1,0,0,0,47,48,5,102,
        0,0,48,49,5,108,0,0,49,50,5,111,0,0,50,51,5,97,0,0,51,52,5,116,0,
        0,52,4,1,0,0,0,53,54,5,114,0,0,54,55,5,101,0,0,55,56,5,116,0,0,56,
        57,5,117,0,0,57,58,5,114,0,0,58,59,5,110,0,0,59,6,1,0,0,0,60,62,
        7,0,0,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,
        64,8,1,0,0,0,65,67,7,1,0,0,66,65,1,0,0,0,67,68,1,0,0,0,68,66,1,0,
        0,0,68,69,1,0,0,0,69,10,1,0,0,0,70,71,3,37,18,0,71,72,3,9,4,0,72,
        12,1,0,0,0,73,74,3,9,4,0,74,75,3,11,5,0,75,14,1,0,0,0,76,77,5,59,
        0,0,77,16,1,0,0,0,78,79,5,44,0,0,79,18,1,0,0,0,80,81,5,40,0,0,81,
        20,1,0,0,0,82,83,5,41,0,0,83,22,1,0,0,0,84,85,5,123,0,0,85,24,1,
        0,0,0,86,87,5,125,0,0,87,26,1,0,0,0,88,89,5,61,0,0,89,28,1,0,0,0,
        90,91,5,43,0,0,91,30,1,0,0,0,92,93,5,45,0,0,93,32,1,0,0,0,94,95,
        5,42,0,0,95,34,1,0,0,0,96,97,5,47,0,0,97,36,1,0,0,0,98,99,5,46,0,
        0,99,38,1,0,0,0,100,101,7,2,0,0,101,102,1,0,0,0,102,103,6,19,0,0,
        103,40,1,0,0,0,104,105,9,0,0,0,105,106,6,20,1,0,106,42,1,0,0,0,3,
        0,63,68,2,6,0,0,1,20,0
    ]

class BKOOLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    KW_INT = 1
    KW_FLOAT = 2
    KW_RETURN = 3
    ID = 4
    INT_LIT = 5
    FLOAT_LIT = 6
    SEMICOLON = 7
    COMMA = 8
    L_BRACK = 9
    R_BRACK = 10
    L_PAREN = 11
    R_PAREN = 12
    ASSIGN = 13
    ADD = 14
    SUBTRACT = 15
    MULTI = 16
    DIV = 17
    DOT = 18
    WS = 19
    ERROR_CHAR = 20

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'int'", "'float'", "'return'", "';'", "','", "'('", "')'", 
            "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "KW_INT", "KW_FLOAT", "KW_RETURN", "ID", "INT_LIT", "FLOAT_LIT", 
            "SEMICOLON", "COMMA", "L_BRACK", "R_BRACK", "L_PAREN", "R_PAREN", 
            "ASSIGN", "ADD", "SUBTRACT", "MULTI", "DIV", "DOT", "WS", "ERROR_CHAR" ]

    ruleNames = [ "KW_INT", "KW_FLOAT", "KW_RETURN", "ID", "INT_LIT", "FLOATING", 
                  "FLOAT_LIT", "SEMICOLON", "COMMA", "L_BRACK", "R_BRACK", 
                  "L_PAREN", "R_PAREN", "ASSIGN", "ADD", "SUBTRACT", "MULTI", 
                  "DIV", "DOT", "WS", "ERROR_CHAR" ]

    grammarFileName = "BKOOL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[20] = self.ERROR_CHAR_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            raise ErrorToken(self.text)
     


