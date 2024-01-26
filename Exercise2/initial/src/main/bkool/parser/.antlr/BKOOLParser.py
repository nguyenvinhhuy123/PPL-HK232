# Generated from c:/Users/nvhuy/Documents/GitHub/PPl-HK232/Exercise2/initial/src/main/bkool/parser/BKOOL.g4 by ANTLR 4.13.1
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
        4,1,20,191,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        1,0,4,0,56,8,0,11,0,12,0,57,1,0,1,0,1,1,1,1,3,1,64,8,1,1,2,1,2,1,
        2,1,3,1,3,1,4,1,4,1,4,1,5,1,5,1,5,1,6,1,6,1,6,1,6,3,6,81,8,6,1,7,
        1,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,96,8,9,1,10,
        1,10,1,10,1,10,1,10,3,10,103,8,10,1,11,1,11,1,11,1,11,1,12,5,12,
        110,8,12,10,12,12,12,113,9,12,1,13,1,13,3,13,117,8,13,1,14,1,14,
        1,14,3,14,122,8,14,1,14,1,14,1,15,1,15,1,15,1,15,1,16,1,16,1,16,
        1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,3,18,141,8,18,1,19,1,19,
        1,19,1,19,1,19,3,19,148,8,19,1,20,1,20,1,20,1,21,1,21,1,21,3,21,
        156,8,21,1,22,1,22,1,22,1,22,1,22,3,22,163,8,22,1,23,1,23,1,23,1,
        23,1,23,3,23,170,8,23,1,24,1,24,1,24,1,24,1,24,3,24,177,8,24,1,25,
        1,25,1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,189,8,26,1,26,
        0,0,27,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,0,2,1,0,1,2,1,0,16,17,183,0,55,1,0,0,0,2,63,1,
        0,0,0,4,65,1,0,0,0,6,68,1,0,0,0,8,70,1,0,0,0,10,73,1,0,0,0,12,80,
        1,0,0,0,14,82,1,0,0,0,16,87,1,0,0,0,18,95,1,0,0,0,20,102,1,0,0,0,
        22,104,1,0,0,0,24,111,1,0,0,0,26,116,1,0,0,0,28,121,1,0,0,0,30,125,
        1,0,0,0,32,129,1,0,0,0,34,132,1,0,0,0,36,140,1,0,0,0,38,147,1,0,
        0,0,40,149,1,0,0,0,42,155,1,0,0,0,44,162,1,0,0,0,46,169,1,0,0,0,
        48,176,1,0,0,0,50,178,1,0,0,0,52,188,1,0,0,0,54,56,3,2,1,0,55,54,
        1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,59,1,0,0,0,
        59,60,5,0,0,1,60,1,1,0,0,0,61,64,3,4,2,0,62,64,3,14,7,0,63,61,1,
        0,0,0,63,62,1,0,0,0,64,3,1,0,0,0,65,66,3,8,4,0,66,67,5,7,0,0,67,
        5,1,0,0,0,68,69,7,0,0,0,69,7,1,0,0,0,70,71,3,6,3,0,71,72,3,10,5,
        0,72,9,1,0,0,0,73,74,5,4,0,0,74,75,3,12,6,0,75,11,1,0,0,0,76,77,
        5,8,0,0,77,78,5,4,0,0,78,81,3,12,6,0,79,81,1,0,0,0,80,76,1,0,0,0,
        80,79,1,0,0,0,81,13,1,0,0,0,82,83,3,6,3,0,83,84,5,4,0,0,84,85,3,
        16,8,0,85,86,3,22,11,0,86,15,1,0,0,0,87,88,5,9,0,0,88,89,3,18,9,
        0,89,90,5,10,0,0,90,17,1,0,0,0,91,92,3,8,4,0,92,93,3,20,10,0,93,
        96,1,0,0,0,94,96,1,0,0,0,95,91,1,0,0,0,95,94,1,0,0,0,96,19,1,0,0,
        0,97,98,5,7,0,0,98,99,3,8,4,0,99,100,3,20,10,0,100,103,1,0,0,0,101,
        103,1,0,0,0,102,97,1,0,0,0,102,101,1,0,0,0,103,21,1,0,0,0,104,105,
        5,11,0,0,105,106,3,24,12,0,106,107,5,12,0,0,107,23,1,0,0,0,108,110,
        3,26,13,0,109,108,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,
        1,0,0,0,112,25,1,0,0,0,113,111,1,0,0,0,114,117,3,4,2,0,115,117,3,
        28,14,0,116,114,1,0,0,0,116,115,1,0,0,0,117,27,1,0,0,0,118,122,3,
        30,15,0,119,122,3,32,16,0,120,122,3,40,20,0,121,118,1,0,0,0,121,
        119,1,0,0,0,121,120,1,0,0,0,122,123,1,0,0,0,123,124,5,7,0,0,124,
        29,1,0,0,0,125,126,5,4,0,0,126,127,5,13,0,0,127,128,3,42,21,0,128,
        31,1,0,0,0,129,130,5,4,0,0,130,131,3,34,17,0,131,33,1,0,0,0,132,
        133,5,9,0,0,133,134,3,36,18,0,134,135,5,10,0,0,135,35,1,0,0,0,136,
        137,3,42,21,0,137,138,3,38,19,0,138,141,1,0,0,0,139,141,1,0,0,0,
        140,136,1,0,0,0,140,139,1,0,0,0,141,37,1,0,0,0,142,143,5,8,0,0,143,
        144,3,42,21,0,144,145,3,38,19,0,145,148,1,0,0,0,146,148,1,0,0,0,
        147,142,1,0,0,0,147,146,1,0,0,0,148,39,1,0,0,0,149,150,5,3,0,0,150,
        151,3,42,21,0,151,41,1,0,0,0,152,156,3,44,22,0,153,156,3,46,23,0,
        154,156,3,48,24,0,155,152,1,0,0,0,155,153,1,0,0,0,155,154,1,0,0,
        0,156,43,1,0,0,0,157,158,3,46,23,0,158,159,5,14,0,0,159,160,3,44,
        22,0,160,163,1,0,0,0,161,163,3,46,23,0,162,157,1,0,0,0,162,161,1,
        0,0,0,163,45,1,0,0,0,164,165,3,48,24,0,165,166,5,15,0,0,166,167,
        3,48,24,0,167,170,1,0,0,0,168,170,3,48,24,0,169,164,1,0,0,0,169,
        168,1,0,0,0,170,47,1,0,0,0,171,172,3,52,26,0,172,173,3,50,25,0,173,
        174,3,48,24,0,174,177,1,0,0,0,175,177,3,52,26,0,176,171,1,0,0,0,
        176,175,1,0,0,0,177,49,1,0,0,0,178,179,7,1,0,0,179,51,1,0,0,0,180,
        189,5,5,0,0,181,189,5,6,0,0,182,189,5,4,0,0,183,189,3,32,16,0,184,
        185,5,9,0,0,185,186,3,42,21,0,186,187,5,10,0,0,187,189,1,0,0,0,188,
        180,1,0,0,0,188,181,1,0,0,0,188,182,1,0,0,0,188,183,1,0,0,0,188,
        184,1,0,0,0,189,53,1,0,0,0,15,57,63,80,95,102,111,116,121,140,147,
        155,162,169,176,188
    ]

class BKOOLParser ( Parser ):

    grammarFileName = "BKOOL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'int'", "'float'", "'return'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "';'", "','", "'('", "')'", 
                     "'{'", "'}'", "'='", "'+'", "'-'", "'*'", "'/'", "'.'" ]

    symbolicNames = [ "<INVALID>", "KW_INT", "KW_FLOAT", "KW_RETURN", "ID", 
                      "INT_LIT", "FLOAT_LIT", "SEMICOLON", "COMMA", "L_BRACK", 
                      "R_BRACK", "L_PAREN", "R_PAREN", "ASSIGN", "ADD", 
                      "SUBTRACT", "MULTI", "DIV", "DOT", "WS", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_line_var_decl = 2
    RULE_type_def = 3
    RULE_vardecl = 4
    RULE_id_list = 5
    RULE_id_list_tail = 6
    RULE_funcdecl = 7
    RULE_param = 8
    RULE_param_list = 9
    RULE_param_list_tail = 10
    RULE_body = 11
    RULE_inner_scope = 12
    RULE_line = 13
    RULE_statement = 14
    RULE_assignment_stmt = 15
    RULE_call_stmt = 16
    RULE_passing = 17
    RULE_passing_list = 18
    RULE_passing_list_tail = 19
    RULE_return_stmt = 20
    RULE_expr = 21
    RULE_add_expr = 22
    RULE_sub_expr = 23
    RULE_mult_expr = 24
    RULE_mult_op = 25
    RULE_primary_expr = 26

    ruleNames =  [ "program", "decl", "line_var_decl", "type_def", "vardecl", 
                   "id_list", "id_list_tail", "funcdecl", "param", "param_list", 
                   "param_list_tail", "body", "inner_scope", "line", "statement", 
                   "assignment_stmt", "call_stmt", "passing", "passing_list", 
                   "passing_list_tail", "return_stmt", "expr", "add_expr", 
                   "sub_expr", "mult_expr", "mult_op", "primary_expr" ]

    EOF = Token.EOF
    KW_INT=1
    KW_FLOAT=2
    KW_RETURN=3
    ID=4
    INT_LIT=5
    FLOAT_LIT=6
    SEMICOLON=7
    COMMA=8
    L_BRACK=9
    R_BRACK=10
    L_PAREN=11
    R_PAREN=12
    ASSIGN=13
    ADD=14
    SUBTRACT=15
    MULTI=16
    DIV=17
    DOT=18
    WS=19
    ERROR_CHAR=20

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

        def EOF(self):
            return self.getToken(BKOOLParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.DeclContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.DeclContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_program




    def program(self):

        localctx = BKOOLParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 54
                self.decl()
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==2):
                    break

            self.state = 59
            self.match(BKOOLParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line_var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Line_var_declContext,0)


        def funcdecl(self):
            return self.getTypedRuleContext(BKOOLParser.FuncdeclContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_decl




    def decl(self):

        localctx = BKOOLParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 63
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.line_var_decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.funcdecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Line_var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_line_var_decl




    def line_var_decl(self):

        localctx = BKOOLParser.Line_var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_line_var_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.vardecl()
            self.state = 66
            self.match(BKOOLParser.SEMICOLON)
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

        def KW_INT(self):
            return self.getToken(BKOOLParser.KW_INT, 0)

        def KW_FLOAT(self):
            return self.getToken(BKOOLParser.KW_FLOAT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_type_def




    def type_def(self):

        localctx = BKOOLParser.Type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_type_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            _la = self._input.LA(1)
            if not(_la==1 or _la==2):
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


    class VardeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(BKOOLParser.Type_defContext,0)


        def id_list(self):
            return self.getTypedRuleContext(BKOOLParser.Id_listContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_vardecl




    def vardecl(self):

        localctx = BKOOLParser.VardeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_vardecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.type_def()
            self.state = 71
            self.id_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def id_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Id_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_id_list




    def id_list(self):

        localctx = BKOOLParser.Id_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_id_list)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(BKOOLParser.ID)
            self.state = 74
            self.id_list_tail()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Id_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def id_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Id_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_id_list_tail




    def id_list_tail(self):

        localctx = BKOOLParser.Id_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_id_list_tail)
        try:
            self.state = 80
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.match(BKOOLParser.COMMA)
                self.state = 77
                self.match(BKOOLParser.ID)
                self.state = 78
                self.id_list_tail()
                pass
            elif token in [7, 10]:
                self.enterOuterAlt(localctx, 2)

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


    class FuncdeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_def(self):
            return self.getTypedRuleContext(BKOOLParser.Type_defContext,0)


        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def param(self):
            return self.getTypedRuleContext(BKOOLParser.ParamContext,0)


        def body(self):
            return self.getTypedRuleContext(BKOOLParser.BodyContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_funcdecl




    def funcdecl(self):

        localctx = BKOOLParser.FuncdeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcdecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.type_def()
            self.state = 83
            self.match(BKOOLParser.ID)
            self.state = 84
            self.param()
            self.state = 85
            self.body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACK(self):
            return self.getToken(BKOOLParser.L_BRACK, 0)

        def param_list(self):
            return self.getTypedRuleContext(BKOOLParser.Param_listContext,0)


        def R_BRACK(self):
            return self.getToken(BKOOLParser.R_BRACK, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_param




    def param(self):

        localctx = BKOOLParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(BKOOLParser.L_BRACK)
            self.state = 88
            self.param_list()
            self.state = 89
            self.match(BKOOLParser.R_BRACK)
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

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def param_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Param_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list




    def param_list(self):

        localctx = BKOOLParser.Param_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param_list)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.vardecl()
                self.state = 92
                self.param_list_tail()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)

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


    class Param_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def vardecl(self):
            return self.getTypedRuleContext(BKOOLParser.VardeclContext,0)


        def param_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Param_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_param_list_tail




    def param_list_tail(self):

        localctx = BKOOLParser.Param_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_param_list_tail)
        try:
            self.state = 102
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 97
                self.match(BKOOLParser.SEMICOLON)
                self.state = 98
                self.vardecl()
                self.state = 99
                self.param_list_tail()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)

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


    class BodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_PAREN(self):
            return self.getToken(BKOOLParser.L_PAREN, 0)

        def inner_scope(self):
            return self.getTypedRuleContext(BKOOLParser.Inner_scopeContext,0)


        def R_PAREN(self):
            return self.getToken(BKOOLParser.R_PAREN, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_body




    def body(self):

        localctx = BKOOLParser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(BKOOLParser.L_PAREN)
            self.state = 105
            self.inner_scope()
            self.state = 106
            self.match(BKOOLParser.R_PAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Inner_scopeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.LineContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.LineContext,i)


        def getRuleIndex(self):
            return BKOOLParser.RULE_inner_scope




    def inner_scope(self):

        localctx = BKOOLParser.Inner_scopeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_inner_scope)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30) != 0):
                self.state = 108
                self.line()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def line_var_decl(self):
            return self.getTypedRuleContext(BKOOLParser.Line_var_declContext,0)


        def statement(self):
            return self.getTypedRuleContext(BKOOLParser.StatementContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_line




    def line(self):

        localctx = BKOOLParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_line)
        try:
            self.state = 116
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1, 2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 114
                self.line_var_decl()
                pass
            elif token in [3, 4]:
                self.enterOuterAlt(localctx, 2)
                self.state = 115
                self.statement()
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


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(BKOOLParser.SEMICOLON, 0)

        def assignment_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Assignment_stmtContext,0)


        def call_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Call_stmtContext,0)


        def return_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Return_stmtContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_statement




    def statement(self):

        localctx = BKOOLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 118
                self.assignment_stmt()
                pass

            elif la_ == 2:
                self.state = 119
                self.call_stmt()
                pass

            elif la_ == 3:
                self.state = 120
                self.return_stmt()
                pass


            self.state = 123
            self.match(BKOOLParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assignment_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(BKOOLParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_assignment_stmt




    def assignment_stmt(self):

        localctx = BKOOLParser.Assignment_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_assignment_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 125
            self.match(BKOOLParser.ID)
            self.state = 126
            self.match(BKOOLParser.ASSIGN)
            self.state = 127
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Call_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def passing(self):
            return self.getTypedRuleContext(BKOOLParser.PassingContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_call_stmt




    def call_stmt(self):

        localctx = BKOOLParser.Call_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_call_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(BKOOLParser.ID)
            self.state = 130
            self.passing()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PassingContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def L_BRACK(self):
            return self.getToken(BKOOLParser.L_BRACK, 0)

        def passing_list(self):
            return self.getTypedRuleContext(BKOOLParser.Passing_listContext,0)


        def R_BRACK(self):
            return self.getToken(BKOOLParser.R_BRACK, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_passing




    def passing(self):

        localctx = BKOOLParser.PassingContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_passing)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 132
            self.match(BKOOLParser.L_BRACK)
            self.state = 133
            self.passing_list()
            self.state = 134
            self.match(BKOOLParser.R_BRACK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Passing_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def passing_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Passing_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_passing_list




    def passing_list(self):

        localctx = BKOOLParser.Passing_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_passing_list)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4, 5, 6, 9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 136
                self.expr()
                self.state = 137
                self.passing_list_tail()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)

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


    class Passing_list_tailContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMA(self):
            return self.getToken(BKOOLParser.COMMA, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def passing_list_tail(self):
            return self.getTypedRuleContext(BKOOLParser.Passing_list_tailContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_passing_list_tail




    def passing_list_tail(self):

        localctx = BKOOLParser.Passing_list_tailContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_passing_list_tail)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 142
                self.match(BKOOLParser.COMMA)
                self.state = 143
                self.expr()
                self.state = 144
                self.passing_list_tail()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)

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


    class Return_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def KW_RETURN(self):
            return self.getToken(BKOOLParser.KW_RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_return_stmt




    def return_stmt(self):

        localctx = BKOOLParser.Return_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_return_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.match(BKOOLParser.KW_RETURN)
            self.state = 150
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Add_exprContext,0)


        def sub_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Sub_exprContext,0)


        def mult_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Mult_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_expr




    def expr(self):

        localctx = BKOOLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expr)
        try:
            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 152
                self.add_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 153
                self.sub_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 154
                self.mult_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Add_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sub_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Sub_exprContext,0)


        def ADD(self):
            return self.getToken(BKOOLParser.ADD, 0)

        def add_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Add_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_add_expr




    def add_expr(self):

        localctx = BKOOLParser.Add_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_add_expr)
        try:
            self.state = 162
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.sub_expr()
                self.state = 158
                self.match(BKOOLParser.ADD)
                self.state = 159
                self.add_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.sub_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Sub_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mult_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKOOLParser.Mult_exprContext)
            else:
                return self.getTypedRuleContext(BKOOLParser.Mult_exprContext,i)


        def SUBTRACT(self):
            return self.getToken(BKOOLParser.SUBTRACT, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_sub_expr




    def sub_expr(self):

        localctx = BKOOLParser.Sub_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_sub_expr)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.mult_expr()
                self.state = 165
                self.match(BKOOLParser.SUBTRACT)
                self.state = 166
                self.mult_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.mult_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mult_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Primary_exprContext,0)


        def mult_op(self):
            return self.getTypedRuleContext(BKOOLParser.Mult_opContext,0)


        def mult_expr(self):
            return self.getTypedRuleContext(BKOOLParser.Mult_exprContext,0)


        def getRuleIndex(self):
            return BKOOLParser.RULE_mult_expr




    def mult_expr(self):

        localctx = BKOOLParser.Mult_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_mult_expr)
        try:
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.primary_expr()
                self.state = 172
                self.mult_op()
                self.state = 173
                self.mult_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
                self.primary_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mult_opContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MULTI(self):
            return self.getToken(BKOOLParser.MULTI, 0)

        def DIV(self):
            return self.getToken(BKOOLParser.DIV, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_mult_op




    def mult_op(self):

        localctx = BKOOLParser.Mult_opContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_mult_op)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
            _la = self._input.LA(1)
            if not(_la==16 or _la==17):
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


    class Primary_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKOOLParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKOOLParser.FLOAT_LIT, 0)

        def ID(self):
            return self.getToken(BKOOLParser.ID, 0)

        def call_stmt(self):
            return self.getTypedRuleContext(BKOOLParser.Call_stmtContext,0)


        def L_BRACK(self):
            return self.getToken(BKOOLParser.L_BRACK, 0)

        def expr(self):
            return self.getTypedRuleContext(BKOOLParser.ExprContext,0)


        def R_BRACK(self):
            return self.getToken(BKOOLParser.R_BRACK, 0)

        def getRuleIndex(self):
            return BKOOLParser.RULE_primary_expr




    def primary_expr(self):

        localctx = BKOOLParser.Primary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_primary_expr)
        try:
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(BKOOLParser.INT_LIT)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.match(BKOOLParser.FLOAT_LIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.match(BKOOLParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 183
                self.call_stmt()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 184
                self.match(BKOOLParser.L_BRACK)
                self.state = 185
                self.expr()
                self.state = 186
                self.match(BKOOLParser.R_BRACK)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





