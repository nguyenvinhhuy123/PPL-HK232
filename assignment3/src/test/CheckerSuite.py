import unittest
from TestUtils import TestChecker
from AST import *
from main.zcode.checker.StaticError import *
from main.zcode.utils.AST import *

class CheckerSuite(unittest.TestCase):
    def test_no_entry_point(self):
        input = """number a
        number a
        func main() return 1
        """
        expect = str(Redeclared(Variable(), Id("a")))
        self.assertTrue(TestChecker.test(input, expect, 400))
