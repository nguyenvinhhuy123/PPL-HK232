import unittest
from TestUtils import TestChecker
from AST import *
from main.zcode.checker.StaticError import *
from main.zcode.utils.AST import *

SUCCESSFUL = ""
class CheckerSuite(unittest.TestCase):
    
    def test_no_entry_point(self):
        input = """number a
        func main() 
        begin
            number a <- 2
        end
        """
        expect = SUCCESSFUL
        self.assertTrue(TestChecker.test(input, expect, 400))
