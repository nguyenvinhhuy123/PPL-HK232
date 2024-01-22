# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/assignment1/src/main/zcode/parser/ZCode.g4 by ANTLR 4.13.1
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
        4,1,52,175,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,1,0,1,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,2,1,2,1,2,3,2,62,8,2,1,3,1,3,1,3,3,3,67,8,3,1,4,1,
        4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,3,10,
        85,8,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,93,8,10,3,10,95,8,10,
        1,11,1,11,1,11,1,12,1,12,3,12,102,8,12,1,13,1,13,1,13,3,13,107,8,
        13,1,14,1,14,1,14,1,14,1,15,1,15,1,15,1,15,3,15,117,8,15,1,16,1,
        16,1,16,3,16,122,8,16,1,17,1,17,4,17,126,8,17,11,17,12,17,127,1,
        17,3,17,131,8,17,1,17,1,17,1,18,1,18,3,18,137,8,18,1,19,1,19,1,19,
        3,19,142,8,19,1,20,1,20,1,20,1,20,3,20,148,8,20,1,21,1,21,1,21,1,
        21,1,21,3,21,155,8,21,1,22,1,22,1,22,1,22,3,22,161,8,22,1,22,1,22,
        1,22,1,23,1,23,1,23,1,23,1,23,3,23,171,8,23,1,24,1,24,1,24,0,0,25,
        0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,
        46,48,0,3,1,0,8,10,1,0,12,13,3,0,25,26,28,29,31,31,168,0,50,1,0,
        0,0,2,52,1,0,0,0,4,61,1,0,0,0,6,66,1,0,0,0,8,68,1,0,0,0,10,70,1,
        0,0,0,12,72,1,0,0,0,14,74,1,0,0,0,16,76,1,0,0,0,18,78,1,0,0,0,20,
        94,1,0,0,0,22,96,1,0,0,0,24,99,1,0,0,0,26,103,1,0,0,0,28,108,1,0,
        0,0,30,112,1,0,0,0,32,118,1,0,0,0,34,123,1,0,0,0,36,134,1,0,0,0,
        38,138,1,0,0,0,40,143,1,0,0,0,42,149,1,0,0,0,44,156,1,0,0,0,46,170,
        1,0,0,0,48,172,1,0,0,0,50,51,9,0,0,0,51,1,1,0,0,0,52,53,5,14,0,0,
        53,54,5,1,0,0,54,55,5,42,0,0,55,56,5,45,0,0,56,57,3,8,4,0,57,3,1,
        0,0,0,58,59,5,26,0,0,59,62,5,3,0,0,60,62,5,3,0,0,61,58,1,0,0,0,61,
        60,1,0,0,0,62,5,1,0,0,0,63,67,3,4,2,0,64,67,5,4,0,0,65,67,5,5,0,
        0,66,63,1,0,0,0,66,64,1,0,0,0,66,65,1,0,0,0,67,7,1,0,0,0,68,69,1,
        0,0,0,69,9,1,0,0,0,70,71,1,0,0,0,71,11,1,0,0,0,72,73,1,0,0,0,73,
        13,1,0,0,0,74,75,7,0,0,0,75,15,1,0,0,0,76,77,7,1,0,0,77,17,1,0,0,
        0,78,79,5,34,0,0,79,80,3,46,23,0,80,19,1,0,0,0,81,82,3,14,7,0,82,
        84,5,2,0,0,83,85,3,18,9,0,84,83,1,0,0,0,84,85,1,0,0,0,85,95,1,0,
        0,0,86,87,5,12,0,0,87,88,5,2,0,0,88,95,3,18,9,0,89,90,5,13,0,0,90,
        92,5,2,0,0,91,93,3,18,9,0,92,91,1,0,0,0,92,93,1,0,0,0,93,95,1,0,
        0,0,94,81,1,0,0,0,94,86,1,0,0,0,94,89,1,0,0,0,95,21,1,0,0,0,96,97,
        5,2,0,0,97,98,3,18,9,0,98,23,1,0,0,0,99,101,5,3,0,0,100,102,3,26,
        13,0,101,100,1,0,0,0,101,102,1,0,0,0,102,25,1,0,0,0,103,104,5,46,
        0,0,104,106,5,3,0,0,105,107,3,26,13,0,106,105,1,0,0,0,106,107,1,
        0,0,0,107,27,1,0,0,0,108,109,5,44,0,0,109,110,3,24,12,0,110,111,
        5,45,0,0,111,29,1,0,0,0,112,113,3,14,7,0,113,114,5,2,0,0,114,116,
        3,28,14,0,115,117,3,32,16,0,116,115,1,0,0,0,116,117,1,0,0,0,117,
        31,1,0,0,0,118,121,5,34,0,0,119,122,5,2,0,0,120,122,3,34,17,0,121,
        119,1,0,0,0,121,120,1,0,0,0,122,33,1,0,0,0,123,130,5,44,0,0,124,
        126,3,34,17,0,125,124,1,0,0,0,126,127,1,0,0,0,127,125,1,0,0,0,127,
        128,1,0,0,0,128,131,1,0,0,0,129,131,3,6,3,0,130,125,1,0,0,0,130,
        129,1,0,0,0,131,132,1,0,0,0,132,133,5,45,0,0,133,35,1,0,0,0,134,
        136,5,2,0,0,135,137,3,38,19,0,136,135,1,0,0,0,136,137,1,0,0,0,137,
        37,1,0,0,0,138,139,5,46,0,0,139,141,5,2,0,0,140,142,3,38,19,0,141,
        140,1,0,0,0,141,142,1,0,0,0,142,39,1,0,0,0,143,144,3,14,7,0,144,
        145,5,2,0,0,145,147,1,0,0,0,146,148,3,40,20,0,147,146,1,0,0,0,147,
        148,1,0,0,0,148,41,1,0,0,0,149,150,5,46,0,0,150,151,3,14,7,0,151,
        152,5,2,0,0,152,154,1,0,0,0,153,155,3,42,21,0,154,153,1,0,0,0,154,
        155,1,0,0,0,155,43,1,0,0,0,156,157,5,14,0,0,157,158,5,2,0,0,158,
        160,5,42,0,0,159,161,3,40,20,0,160,159,1,0,0,0,160,161,1,0,0,0,161,
        162,1,0,0,0,162,163,5,45,0,0,163,164,3,8,4,0,164,45,1,0,0,0,165,
        171,5,3,0,0,166,167,5,2,0,0,167,168,3,48,24,0,168,169,3,46,23,0,
        169,171,1,0,0,0,170,165,1,0,0,0,170,166,1,0,0,0,171,47,1,0,0,0,172,
        173,7,2,0,0,173,49,1,0,0,0,17,61,66,84,92,94,101,106,116,121,127,
        130,136,141,147,154,160,170
    ]

class ZCodeParser ( Parser ):

    grammarFileName = "ZCode.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'true'", "'false'", "'number'", "'bool'", 
                     "'string'", "'return'", "'var'", "'dynamic'", "'func'", 
                     "'for'", "'until'", "'by'", "'break'", "'continue'", 
                     "'if'", "'else'", "'elif'", "'begin'", "'end'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'not'", "'and'", "'or'", 
                     "'='", "'<-'", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'=='", "'...'", "'('", "')'", "'['", "']'", "','", 
                     "<INVALID>", "<INVALID>", "'\\n'" ]

    symbolicNames = [ "<INVALID>", "MAIN_TOKEN", "IDENTIFIER", "NUMBER", 
                      "STRING", "BOOLEN", "KW_TRUE", "KW_FALSE", "KW_NUMBER", 
                      "KW_BOOL", "KW_STRING", "KW_RETURN", "KW_VAR", "KW_DYNAMIC", 
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
    IDENTIFIER=2
    NUMBER=3
    STRING=4
    BOOLEN=5
    KW_TRUE=6
    KW_FALSE=7
    KW_NUMBER=8
    KW_BOOL=9
    KW_STRING=10
    KW_RETURN=11
    KW_VAR=12
    KW_DYNAMIC=13
    KW_FUNC=14
    KW_FOR=15
    KW_UNTIL=16
    KW_BY=17
    KW_BREAK=18
    KW_CONTINUE=19
    KW_IF=20
    KW_ELSE=21
    KW_ELIF=22
    KW_BEGIN=23
    KW_END=24
    OP_ADD=25
    OP_SUBTRACT=26
    OP_MULTI=27
    OP_DIVIDE=28
    OP_REMAINDER=29
    OP_NOT=30
    OP_AND=31
    OP_OR=32
    OP_EQUAL=33
    OP_LEFT_ARROW=34
    OP_NOT_EQUAL=35
    OP_SMALLER=36
    OP_GREATER=37
    OP_SMALLER_EQUAL=38
    OP_GREATER_EQUAL=39
    OP_EQUAL_COMPARE=40
    OP_TRIPLE_DOT=41
    SEP_OPEN_PAREN=42
    SEP_CLOSE_PAREN=43
    SEP_OPEN_BRACK=44
    SEP_CLOSE_BRACK=45
    SEP_COMA=46
    COMMENT=47
    WS=48
    NEW_LINE=49
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




    def sign_number(self):

        localctx = ZCodeParser.Sign_numberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_sign_number)
        try:
            self.state = 61
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.match(ZCodeParser.OP_SUBTRACT)
                self.state = 59
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [3]:
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

        def BOOLEN(self):
            return self.getToken(ZCodeParser.BOOLEN, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_literal




    def literal(self):

        localctx = ZCodeParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_literal)
        try:
            self.state = 66
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.sign_number()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.match(ZCodeParser.STRING)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 65
                self.match(ZCodeParser.BOOLEN)
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




    def type_def(self):

        localctx = ZCodeParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0)):
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




    def implicit_type_def(self):

        localctx = ZCodeParser.Implicit_type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_implicit_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            _la = self._input.LA(1)
            if not(_la==12 or _la==13):
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

        def value_init(self):
            return self.getTypedRuleContext(ZCodeParser.Value_initContext,0)


        def KW_VAR(self):
            return self.getToken(ZCodeParser.KW_VAR, 0)

        def KW_DYNAMIC(self):
            return self.getToken(ZCodeParser.KW_DYNAMIC, 0)

        def getRuleIndex(self):
            return ZCodeParser.RULE_var_declare




    def var_declare(self):

        localctx = ZCodeParser.Var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_var_declare)
        self._la = 0 # Token type
        try:
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8, 9, 10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 81
                self.type_def()
                self.state = 82
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 84
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 83
                    self.value_init()


                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(ZCodeParser.KW_VAR)
                self.state = 87
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 88
                self.value_init()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.match(ZCodeParser.KW_DYNAMIC)
                self.state = 90
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==34:
                    self.state = 91
                    self.value_init()


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


        def getRuleIndex(self):
            return ZCodeParser.RULE_var_assign




    def var_assign(self):

        localctx = ZCodeParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 97
            self.value_init()
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




    def number_list(self):

        localctx = ZCodeParser.Number_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_number_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(ZCodeParser.NUMBER)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 100
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




    def number_list_tail(self):

        localctx = ZCodeParser.Number_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_number_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(ZCodeParser.SEP_COMA)
            self.state = 104
            self.match(ZCodeParser.NUMBER)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 105
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




    def array_dim_list(self):

        localctx = ZCodeParser.Array_dim_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array_dim_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 109
            self.number_list()
            self.state = 110
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




    def array_declare(self):

        localctx = ZCodeParser.Array_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_array_declare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.type_def()
            self.state = 113
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 114
            self.array_dim_list()
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==34:
                self.state = 115
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




    def array_init(self):

        localctx = ZCodeParser.Array_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_array_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(ZCodeParser.OP_LEFT_ARROW)
            self.state = 121
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 119
                self.match(ZCodeParser.IDENTIFIER)
                pass
            elif token in [44]:
                self.state = 120
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




    def array_value_init(self):

        localctx = ZCodeParser.Array_value_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_array_value_init)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(ZCodeParser.SEP_OPEN_BRACK)
            self.state = 130
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [44]:
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 124
                    self.array_value_init()
                    self.state = 127 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==44):
                        break

                pass
            elif token in [3, 4, 5, 26]:
                self.state = 129
                self.literal()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 132
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




    def param_list(self):

        localctx = ZCodeParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_param_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 135
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




    def param_list_tail(self):

        localctx = ZCodeParser.Param_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_param_list_tail)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(ZCodeParser.SEP_COMA)
            self.state = 139
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 140
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




    def param_def_list(self):

        localctx = ZCodeParser.Param_def_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_param_def_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.type_def()
            self.state = 144
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 146
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




    def param_def_list_tail(self):

        localctx = ZCodeParser.Param_def_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_param_def_list_tail)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(ZCodeParser.SEP_COMA)

            self.state = 150
            self.type_def()
            self.state = 151
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 154
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 153
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




    def func_def(self):

        localctx = ZCodeParser.Func_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_func_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(ZCodeParser.KW_FUNC)
            self.state = 157
            self.match(ZCodeParser.IDENTIFIER)
            self.state = 158
            self.match(ZCodeParser.SEP_OPEN_PAREN)
            self.state = 160
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1792) != 0):
                self.state = 159
                self.param_def_list()


            self.state = 162
            self.match(ZCodeParser.SEP_CLOSE_BRACK)
            self.state = 163
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




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expression)
        try:
            self.state = 170
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.match(ZCodeParser.IDENTIFIER)
                self.state = 167
                self.operation()
                self.state = 168
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




    def operation(self):

        localctx = ZCodeParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3053453312) != 0)):
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





