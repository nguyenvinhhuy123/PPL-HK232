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
def lexer_err_msg(error_token):
    return error_token

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
        input = """func main() begin\n end\n"""
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,201))
        
    def test_simple_program_fail(self):
        """Simple program: int main() {} """
        input = """int main () return 1
        """
        expected = error_msg(1,0,"int")
        self.assertTrue(TestParser.test(input,expected,202))
        
    def test_simple_program_no_main(self):
        """Simple program with no main function declare"""
        input = """number a
        func foo() return 2
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
    
    def test_spec_source_code_1(self):
        """Source from spec"""
        input = """
        func areDivisors(number num1, number num2)
            return ((num1 % num2 = 0) or (num2 % num1 = 0))
        func main()
        begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
        end

        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,205))

    def test_spec_source_code_2(self):
        """Source from spec"""
        input = """
        func isPrime(number x)
        func main()
        begin
            number x <- readNumber()
            if (isPrime(x)) writeString("Yes")
            else writeString("No")
        end
        func isPrime(number x)
        begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
                if (x % i = 0) return false
            end
            return true
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,206))
        
    def test_spec_source_code_1_modified(self):
        """Source from spec"""
        input = """
        func areDivisors(number num1, number num2)
            return (num1 % num2 = 0 or num2 % num1 = 0)
        func main()
        begin
            var num1 <- readNumber()
            var num2 <- readNumber()
            if (areDivisors(num1, num2)) writeString("Yes")
            else writeString("No")
        end

        """
        expected = error_msg(3,51,"=")
        self.assertTrue(TestParser.test(input,expected,207))
    
    def test_spec_source_code_2_modified(self):
        """Source from spec"""
        input = """
        func isPrime(var a[2])
        func main()
        begin
            number x <- readNumber()
            if (isPrime(x)) writeString("Yes")
            else writeString("No")
        end
        func isPrime(number x)
        begin
            if (x <= 1) return false
            var i <- 2
            for i until i > x / 2 by 1
            begin
                if (x % i = 0) return false
            end
            return true
        end
        """
        expected = error_msg(2,21,"var")
        self.assertTrue(TestParser.test(input,expected,208))
    
    def test_simple_program_hello_world(self):
        """Simple hello world"""
        input = """
        func main()
        begin
            string b <- "Hello, World!"
            printString(b)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,209))
        
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
    
    def test_simple_array_declare_dim_error(self):
        '''Simple array declaration with dimension error'''
        input = """
        number a[true,3] <- [[2,3,4],[2,4,5]]
        func main() 
        begin
            number b[3] <- [true,false,false]
        end
        """
        expected = error_msg(2,17,"true")
        self.assertTrue(TestParser.test(input,expected,226))
        
    def test_simple_array_declare_implicit_key_error(self):
        '''Simple array declaration with implicit keyword error'''
        '''expected error at '[' because var a -> recognize as variable decl'''
        input = """
        var a[2,3] <- [[2,3,4],[2,4,5]]
        func main() 
        begin
            number b[3] <- [true,false,false]
        end
        """
        expected = error_msg(2,13,"[")
        self.assertTrue(TestParser.test(input,expected,227))
    
    def test_simple_array_declare_missing_bracket(self):
        '''Simple array declaration with missing bracket'''
        input = """
        number a[2,3 <- [[2,3,4],[2,4,5]]
        func main() 
        begin
            number b[3] <- [true,false,false]
        end
        """
        expected = error_msg(2,21,"<-")
        self.assertTrue(TestParser.test(input,expected,228))
    
    def test_simple_array_declare_null_dimension(self):
        '''Simple array declaration with null dimension size list'''
        input = """
        number a[]<- [[2,3,4],[2,4,5]]
        func main() 
        begin
            number b[3] <- [true,false,false]
        end
        """
        expected = error_msg(2,17,"]")
        self.assertTrue(TestParser.test(input,expected,229))
    
    def test_simple_array_declare_wrong_bracket(self):
        '''Simple array declaration with null dimension size list'''
        '''Lexer error thus expected only the error token'''
        input = """
        number a[2}<- [[2,3,4],[2,4,5]]
        func main() 
        begin
            number b[3] <- [true,false,false]
        end
        """
        expected = lexer_err_msg("}")
        self.assertTrue(TestParser.test(input,expected,230))
        
    #*Case:231-240: Expression testing
    def test_simple_expr(self):
        '''Simple expr in var declaration'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            number b <- (3-4)*5- -foo()
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,231))
    
    def test_simple_boolean_expr(self):
        '''Simple expr in var declaration, bool expr'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >=5) and not(a <= 10)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,232))
        
    def test_simple_string_expr(self):
        '''Simple expr in var declaration, string concat expr'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            string b <- toString(a) ... \" is a number\"
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,233))
        
    def test_simple_array_expr(self):
        '''Simple expr in var declaration, array expr and value assignment'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            number b[2,3]
            b[2,0] <- a
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,234))
    
    def test_simple_expr_error(self):
        '''Simple expr in var declaration, error no paren'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            number b <- (3-4*5-foo()
        end
        """
        expected = error_msg(5,36,'\n')
        self.assertTrue(TestParser.test(input,expected,235))
    
    def test_simple_boolean_expr_err(self):
        '''Simple expr in var declaration, bool expr error no operand'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >=5) and (a <= 10) or
        end
        """
        expected = error_msg(5,46,'\n')
        self.assertTrue(TestParser.test(input,expected,236))
        
    def test_simple_string_expr_err(self):
        '''Simple expr in var declaration, string concat expr error unclose str'''
        input = """
number a <- 2*5-3
func main() 
begin
    string b <- toString(a) ... \" is a number\'\"
end
"""
        expected = lexer_err_msg(""" is a number\'\"
end
""") #!I Cannot print EOF token here? thus this tc is always wrong
        self.assertTrue(TestParser.test(input,expected,237))
        
    def test_simple_array_expr_err(self):
        '''Simple expr in var declaration, array expr error missing bracket'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            number b[2,3]
            b[2,0 <- a
        end
        """
        expected = error_msg(6,18,'<-')
        self.assertTrue(TestParser.test(input,expected,238))
        
    def test_simple_relation_expr(self):
        '''Simple expr in var declaration, relational expr'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >= 5 + 5 - 2)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,239))
        
    def test_simple_relation_expr_err(self):
        '''Simple expr in var declaration, rela expr error, relational is none assoc'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >= 5 + 5 - 2 <= b)
        end
        """
        expected = error_msg(5,38,"<=")
        self.assertTrue(TestParser.test(input,expected,240))
        
    #*Case 241-260: statement testing
    def test_simple_if_statement(self):
        '''Simple if stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            if (a > 3) printString("Yes")
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,241))
    
    def test_simple_if_elif_else_statement(self):
        '''Simple if else stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            if (a > 3) 
                printString(">3")
            elif(a > 5)
                printString(">5")
            elif(a > 7)
                printString(">7")
            elif(a)
                printString("a")
            else
                printString("lmao")
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,242))
        
    def test_simple_if_statement_error(self):
        '''Simple if else stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            if (a > 3
                printString(">3")
            elif(a > 5)
                printString(">5")
            elif(a > 7)
                printString(">7")
            elif(a)
                printString("a")
            else
                printString("lmao")
        end
        """
        expected = error_msg(5,21,"\n")
        self.assertTrue(TestParser.test(input,expected,243))
        
    def test_simple_if_statement_no_condition_error(self):
        '''Simple if else stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            if ()
                printString(">3")
            elif(a > 5)
                printString(">5")
            elif(a > 7)
                printString(">7")
            elif(a)
                printString("a")
            else
                printString("lmao")
        end
        """
        expected = error_msg(5,16,")")
        self.assertTrue(TestParser.test(input,expected,244))
        
    def test_simple_if_statement_no_execute_stmt_error(self):
        '''Simple if else stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            if (a = 1)
            elif(a > 5)
                printString(">5")
            elif(a > 7)
                printString(">7")
            elif(a)
                printString("a")
            else
                printString("lmao")
        end
        """
        expected = error_msg(6,12,"elif")
        self.assertTrue(TestParser.test(input,expected,244))
    
    def test_nested_if_statement(self):
        '''Simple if else stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            if (a > 1)
                if (a = 2) printString("is 2")
                elif (a = 5) printString("is 5")
                else printString("lmao")
            elif(a > 7)
                printString(">7")
            elif(a)
                printString("a")
            else
                printString("lmao")
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,245))
        
    def test_simple_for_statement(self):
        '''Simple for stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            number i <- 0
            for i until i = 10 by 1
            printString(i)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,246))
    
    def test_simple_for_statement_err(self):
        '''Simple for stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for number i <- 0 until i = 10 by 1
            printString(i)
        end
        """
        expected = error_msg(5,16,"number")
        self.assertTrue(TestParser.test(input,expected,247))
    
    def test_simple_for_statement_edge_case(self):
        '''Simple for stmt until true weird case, infinite loop'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until true by 1
            printString(i)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,248))
        
    def test_simple_for_statement_missing_by(self):
        '''Simple for stmt missing by statement'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until isPrime(i)
            printString(i)
        end
        """
        expected = error_msg(5,34,"\n")
        self.assertTrue(TestParser.test(input,expected,249))
        
    def test_simple_for_statement_missing_until(self):
        '''Simple for stmt missing until statement'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i by 1
            printString(i)
        end
        """
        expected = error_msg(5,18,"by")
        self.assertTrue(TestParser.test(input,expected,250))
    
    def test_simple_break(self):
        '''Simple break stmt '''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until true by 1
            if (isPrime(i))
            break
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,251))
        
    def test_simple_continue(self):
        '''Simple continue stmt '''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until i >= 10 by 1
                if (not inFibo(i))
                    continue
                else
                    printString(i)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,252))
    
    def test_simple_break_err(self):
        '''Simple break stmt err'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until true by 1
            if (isPrime(i))
            Break
        end
        """
        expected = error_msg(7,17,"\n")
        self.assertTrue(TestParser.test(input,expected,253))
        
    def test_simple_continue_err(self):
        '''Simple continue stmt err'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until i >= 10 by 1
                if (not inFibo(i))
                    continue a
                else
                    printString(i)
        end
        """
        expected = error_msg(7,29,"a")
        self.assertTrue(TestParser.test(input,expected,254))
    
    def test_simple_block_in_others(self):
        '''Simple block stmt in others stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until i >= 10 by 1
                begin
                for j until j >= 10 by 1
                    a[i,j] <- 0
                printString(j)
                end    
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,255))
    
    def test_simple_block_err(self):
        '''Simple block stmt in missing end'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until i >= 10 by 1
                begin
                for j until j >= 10 by 1
                    a[i,j] <- 0
                printString(j)   
        end
        """
        expected = error_msg(11,8, "<EOF>")
        self.assertTrue(TestParser.test(input,expected,256))
    
    def test_simple_block_empty(self):
        '''Simple block empty'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until i >= 10 by 1
                begin
                
                
                
                end   
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,257))
        
    def test_simple_block_no_begin(self):
        '''Simple block empty'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            for i until i >= 10 by 1
                end   
        end
        """
        expected = error_msg(6,16,"end")
        self.assertTrue(TestParser.test(input,expected,258))

    def test_simple_return(self):
        '''Simple return stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            return
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,259))
        
    def test_simple_return_error(self):
        '''Simple return stmt err'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            return break
        end
        """
        expected = error_msg(5,19,"break")
        self.assertTrue(TestParser.test(input,expected,260))
    #*Case: 261 - 270: Parameter in function
    def test_simple_param(self):
        '''Simple func with param'''
        input = """
        func foo(number a, number b) return a + b
        func main() 
        begin
            foo(1,2)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,261))
        
    def test_simple_array_param(self):
        '''Simple func with array param'''
        input = """
        func foo(number a[2], number b) return a[1] + b
        func main() 
        begin
            foo([1,2],2)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,262))
        
    def test_simple_implicit_param_err(self):
        '''Simple func with implicit param'''
        input = """
        func foo(var a, number b) return a + b
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = error_msg(2,17,"var")
        self.assertTrue(TestParser.test(input,expected,263))
    
    def test_simple_implicit_param_err_case_2(self):
        '''Simple func with implicit param'''
        input = """
        func foo(implicit a, number b) return a + b
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = error_msg(2,17,"implicit")
        self.assertTrue(TestParser.test(input,expected,264))    
    
    def test_complex_array_param(self):
        '''Simple func with array params'''
        input = """
        func foo(string a[2,3,4], bool b[2,3]) return
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,265))    
    
    def test_multiline_param(self):
        '''Simple func with array params'''
        input = """
        func foo(string a[2,3,4],
        bool b[2,3]) return
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = error_msg(2,33,'\n')
        self.assertTrue(TestParser.test(input,expected,266))   
        
    def test_forward_decl_param(self):
        '''Simple forward func with array params'''
        input = """
        func foo(string a[2,3,4],bool b[2,3])
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,267))   
    
    def test_func_param_missing_coma(self):
        '''Simple forward func with array params err missing coma'''
        input = """
        func foo(string a[2,3,4] bool b[2,3]) return
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = error_msg(2,33,"bool")
        self.assertTrue(TestParser.test(input,expected,268))  
    
    def test_func_param_semi_err(self):
        '''Simple forward func with array params mistake semicol'''
        input = """
        func foo(string a[2,3,4]; bool b[2,3]) return
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = lexer_err_msg(";")
        self.assertTrue(TestParser.test(input,expected,269))  
    
    def test_func_param_missing_paren_err(self):
        '''Simple forward func with missing param'''
        input = """
        func foo(string a[2,3,4], bool b[2,3] return
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = error_msg(2,46,"return")
        self.assertTrue(TestParser.test(input,expected,270))  
    
    #*Case 271- 280: complex var decl and assignment
    def test_long_var_decl(self):
        '''Long array, var declare'''
        input = """
        var a <- 2*3-foo()+b[2,3]
        func main() 
        begin
            number b[2,3] <- [2,a*2/f,foo(2),true,[2,3]]
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,271))
        
    def test_long_var_decl_dimension_expr_err(self):
        '''Long implicit type var declare'''
        input = """
        var a <- 2*3-foo()+b[2,3]
        func main() 
        begin
            number b[foo(2),3] <- [2,a*2/f,foo(2),true,[2,3]]
        end
        """
        expected = error_msg(5,21,"foo")
        self.assertTrue(TestParser.test(input,expected,272))
    
    def test_elem_expr_assignment(self):
        '''Long implicit type var declare'''
        input = """
        var a <- 2*3-foo()+b[2,3]
        func main() 
        begin
            number b[2,3]
            b[a,foo(2)] <- b[foo(2),a]
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,273))
    
    def test_long_var_decl_dimension_with_float(self):
        '''Long implicit type var declare'''
        input = """
        var a <- 2*3-foo()+b[2,3]
        func main() 
        begin
            number b[2.293E21,3] <- [2,a*2/f,foo(2),true,[2,3]]
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,274))
    
    def test_long_var_decl_dimension_with_string(self):
        '''Long implicit type var declare'''
        input = """
        var a <- 2*3-foo()+b[2,3]
        func main() 
        begin
            number b["string",3] <- [2,a*2/f,foo(2),true,[2,3]]
        end
        """
        expected = error_msg(5,21,"string")
        self.assertTrue(TestParser.test(input,expected,275))
    
    def test_elem_expr_assignment(self):
        '''Long implicit type var declare'''
        input = """
        var a <- 2*3-foo()+b[2,3]
        func main() 
        begin
            number b[2,3]
            b["string",2.123E-32] <- b[foo(2),a]
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,276))
    #*Case 291 - 300 : Random test
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
        self.assertTrue(TestParser.test(input,expected,291))
    
    def test_simple_if_else_statement(self):
        '''Simple if else stmt'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            if (a > 3) 
                printString("Yes")
            else 
                printString("No")
        end
        """
        expected = SUCCESSFUL
        self.assertTrue(TestParser.test(input,expected,292))