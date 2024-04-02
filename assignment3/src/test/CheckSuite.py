import unittest
from TestUtils import TestChecker
from AST import *
from main.zcode.checker.StaticError import *
from main.zcode.utils.AST import *

SUCCESSFUL = ""
class CheckSuite(unittest.TestCase):
    
    def test_no_entry_point(self):
        input = """
        func main() 
        begin
            number a[3] <- [1,2,3]
        end
        """
        expect = SUCCESSFUL
        self.assertTrue(TestChecker.test(input, expect, 400))
