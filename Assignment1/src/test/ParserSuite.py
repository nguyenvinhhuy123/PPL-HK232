import unittest
from TestUtils import TestParser, TestLexer

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() begin end\n"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_simple_program_fail(self):
        """Simple program: int main() {} """
        input = """int main () return 1
        """
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,202))
        
    def test_simple_program_no_main(self):
        """Simple program with no main function declare"""
        input = """number a
        func foo() return 2\n
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,203))
    
    def test_long_program(self):
        """Simple long program"""
        input = """
        func foo(number a)
        begin
            a <- a + 3
            string b<- \"value of a is:\" + toString(a)
        end
        func main()
        begin
            number target <- 5
            foo(target)
        end
        """
        expected = """successful"""
        self.assertTrue(TestParser.test(input,expected,204))