import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        input = """number a <- myfunc()
        """
        expect = str(Program([VarDecl(Id("a"), NumberType(),None, CallExpr(Id("myfunc"), []))]))
        self.assertTrue(TestAST.test(input, expect, 300))