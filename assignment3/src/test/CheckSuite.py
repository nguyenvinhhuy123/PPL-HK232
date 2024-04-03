import unittest
from TestUtils import TestChecker
from AST import *
from main.zcode.checker.StaticError import *
from main.zcode.utils.AST import *

SUCCESSFUL = ""
class CheckSuite(unittest.TestCase):
    #*Case 401 - 410: Simple exception check
    def test_no_entry_point(self):
        input = """
        number a <- 2
        """
        expect = str(NoEntryPoint())
        self.assertTrue(TestChecker.test(input, expect, 401))
    
    def test_normal_flow(self):
        input = """
        number a <- 2
        func main() return 1
        """
        expect = SUCCESSFUL
        self.assertTrue(TestChecker.test(input, expect, 402))
    def test_normal_flow_with_function(self):
        input = """
        func foo(number a) return a
        number a <- 2
        func main() return 1
        """
        expect = SUCCESSFUL
        self.assertTrue(TestChecker.test(input, expect, 403))
    
    #*Case 411-420: function_declared test
    def test_forward_define(self):
        input = """
        func foo(number a)
        number a <- 2
        func main() return 1
        func foo(number a) return a
        """
        expect = SUCCESSFUL
        self.assertTrue(TestChecker.test(input, expect, 411))
    def test_forward_define_err_wrong_param(self):
        input = """
        func foo(number a)
        number a <- 2
        func main() return 1
        func foo(number b) return b
        """
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input, expect, 412))
    
    def test_forward_define_err_more_param(self):
        input = """
        func foo(number a)
        number a <- 2
        func main() return 1
        func foo(number b,number a) return b
        """
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input, expect, 413))
    
    def test_err_redeclare(self):
        input = """
        func foo(number a) return a
        number a <- 2
        func main() return 1
        func foo(number a) return a+1
        """
        expect = str(Redeclared(Function(),"foo"))
        self.assertTrue(TestChecker.test(input, expect, 414))
