import unittest
from TestUtils import TestParser
#! Include Lexer to debug case if needed
from TestUtils import TestLexer

#*successful msg for expected output
SUCCESSFUL = "successful"
#*Return formatted error msg for expected output
def error_msg(error_line, error_col, error_word):
    #*Remember to count all space in that line (1 tab = 4 space)
    return "Error on line %a col %a: %s" % (error_line, error_col, error_word)

class ParserSuite(unittest.TestCase):
    
    """
    Test function template:
    def test_TEST_NAME(self):
        '''Small description here'''
        input = """"""
        expected = 
        self.assertTrue(TestParser.test(input,expected,test_ID))
    """
    #*Case 201-210: Simple test
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main() begin end\n"""
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,201))
        
    def test_simple_program_fail(self):
        """Simple program: int main() {} """
        input = """int main () return 1
        """
        expected = error_msg(1,0,"int")
        print(expected)
        self.assertTrue(TestParser.test(input,expected,202))
        
    def test_simple_program_no_main(self):
        """Simple program with no main function declare"""
        input = """number a
        func foo() return 2\n
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,203))
    
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
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,204))
        
    #*Case 210-220: test function declaration
    def test_simple_func_del(self):
        '''Simple function declaration and call in main'''
        input = """
        func foo() begin
        a <- 2
        return a
        end
        func main() 
        begin
            a <- foo()
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,210))

    def test_simple_func_del_return(self):
        '''Small description here'''
        input = """
        func foo() return 2
        func main() 
        begin
            a <- foo()
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,211))
        
    def test_simple_func_del_error(self):
        '''Function without return or block -> expect error at character a'''
        input = """
        func foo() a <- 2
        func main() 
        begin
            a <- foo()
        end
        """
        expected = error_msg(2,19,"a")
        self.assertTrue(TestParser.test(input,expected,212))
        
    def test_simple_func_del_wrong_keyword_case_1(self):
        '''Function with wrong declare keyword -> expect Number var declare -> wrong char ('''
        input = """
        number foo() return 2
        func main() 
        begin
            a <- foo()
        end
        """
        expected = error_msg(2,18,"(")
        self.assertTrue(TestParser.test(input,expected,213))
        
    def test_func_del_wrong_keyword_case_1(self):
        '''Function with wrong declare keyword -> expect error char true'''
        input = """
        true foo() return 2
        func main() 
        begin
            a <- foo()
        end
        """
        expected = error_msg(2,8,"true")
        self.assertTrue(TestParser.test(input,expected,214))
    
    def test_func_del_with_param(self):
        '''Function with wrong declare keyword -> expect error char true'''
        input = """
        func foo(number a, number b) return (a >= b)
        func main() 
        begin
            bool a <- foo()
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,215))
        
    def test_forward_declare(self):
        '''Function with wrong declare keyword -> expect error char true'''
        input = """
        func foo()
        func main() 
        begin
            a <- foo()
        end
        func foo()
        begin
        return 2 
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,216))
    
    def test_error_missing_paren(self):
        '''Forward function without 1 paren'''
        input = """
        func foo)
        func main() 
        begin
            a <- foo()
        end
        func foo()
        begin
        return 2 
        end
        """
        expected = error_msg(2,16,")")
        self.assertTrue(TestParser.test(input,expected,217))
        
    def test_error_statement_after_return(self):
        '''Function with statement after return'''
        input = """
        func foo()
        func main() 
        begin
            a <- foo()
        end
        func foo()
        return a
        a <- 2
        """
        expected = error_msg(9,8,"a")
        self.assertTrue(TestParser.test(input,expected,218))
    
    def test_function_1_liner(self):
        '''Function with 1 liner return'''
        input = """
        func foo() return 2
        func main() 
        begin
            a <- foo()
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,220))
    
    #*Case 221-230: Var declare
    def test_simple_var_declare(self):
        '''Simple string and number declare'''
        input = """
        number a <- 2
        func main() 
        begin
            string b <- "Hello, World!"
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,221))
        
    def test_simple_var_declare_wrong_type(self):
        '''Simple string and number declare wrong type -> still expected success'''
        input = """
        number a <- "Hello"
        func main() 
        begin
            string b <- 2
            bool c <- true
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,222))
        
    def test_simple_var_declare_no_init(self):
        '''Simple string and number var declaration with no value init'''
        input = """
        number a
        func main() 
        begin
            string b
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,223))
        
    def test_simple_implicit_var_declare(self):
        '''Simple implicit type var declare'''
        input = """
        var a <- 2
        func main() 
        begin
            dynamic b <- "String"
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,223))
        
    def test_simple_implicit_var_declare_no_init(self):
        '''Simple implicit type var declare'''
        '''Error at line var a -> end_line token bc var a must have declaration'''
        input = """
        var a
        func main() 
        begin
            dynamic b
        end
        """
        expected = error_msg(2,13,'\n')
        self.assertTrue(TestParser.test(input,expected,224))
    
    def test_simple_array_declare(self):
        '''Simple array declaration'''
        input = """
        number a[2,3] <- [[2,3,4],[2,4,5]]
        func main() 
        begin
            number b[3] <- [true,false,false]
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,225))