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
        4,1,51,48,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,
        2,1,3,1,3,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,3,6,44,8,6,
        1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,1,3,0,24,25,27,28,30,30,40,
        0,16,1,0,0,0,2,18,1,0,0,0,4,24,1,0,0,0,6,30,1,0,0,0,8,32,1,0,0,0,
        10,34,1,0,0,0,12,43,1,0,0,0,14,45,1,0,0,0,16,17,9,0,0,0,17,1,1,0,
        0,0,18,19,5,13,0,0,19,20,5,1,0,0,20,21,5,41,0,0,21,22,5,44,0,0,22,
        23,3,6,3,0,23,3,1,0,0,0,24,25,5,13,0,0,25,26,5,2,0,0,26,27,5,41,
        0,0,27,28,5,44,0,0,28,29,3,6,3,0,29,5,1,0,0,0,30,31,1,0,0,0,31,7,
        1,0,0,0,32,33,9,0,0,0,33,9,1,0,0,0,34,35,5,2,0,0,35,36,5,33,0,0,
        36,37,3,12,6,0,37,11,1,0,0,0,38,44,5,3,0,0,39,40,5,2,0,0,40,41,3,
        14,7,0,41,42,3,12,6,0,42,44,1,0,0,0,43,38,1,0,0,0,43,39,1,0,0,0,
        44,13,1,0,0,0,45,46,7,0,0,0,46,15,1,0,0,0,1,43
    ]

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
                     "<INVALID>", "'\\n'" ]

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




    def expression(self):

        localctx = ZCodeParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression)
        try:
            self.state = 43
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 38
                self.match(ZCodeParser.NUMBER)
                pass
            elif token in [2]:
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




    def operation(self):

        localctx = ZCodeParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1526726656) != 0)):
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





