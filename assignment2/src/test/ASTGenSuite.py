import unittest
from TestUtils import TestAST
from AST import *
#!Import to use intellisense
from main.zcode.utils.AST import *

class ASTGenSuite(unittest.TestCase):
    '''
    Assuming all tc is parser correct?
    '''
    def test_simple_program(self):
        input = """number a <- myfunc()
        """
        expected = str(Program([VarDecl(Id("a"), NumberType(),None, CallExpr(Id("myfunc"), []))]))
        self.assertTrue(TestAST.test(input, expected, 301))
    
    def test_simple_program_main(self):
        """Simple program"""
        input = """func main() return 1
        """
        expected = str(Program(
            [
                FuncDecl(name=Id("main"),
                        param=[],
                        body=Return(NumberLiteral(1.0))
                        )
            ]
        )
        )
        self.assertTrue(TestAST.test(input,expected,302))
    
    def test_simple_program_no_main(self):
        """Simple program with no main function declare"""
        input = """number a
        func foo() return 2
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType()
                ),
                FuncDecl(
                    name=Id("foo"),
                    param=[],
                    body=Return(NumberLiteral(2.0))
                )
            ]
        )
        )
        self.assertTrue(TestAST.test(input,expected,303))
    
    def test_long_program(self):
        """Simple long program"""
        input = """
        func foo(number a)
        begin
            a <- a + 3
            string b <- \"value of a is:\" ... toString(a)
        end
        func main()
        begin
            number target <- 5
            foo(target)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[VarDecl(
                            name=Id("a"),
                            varType=NumberType()
                        )],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=BinaryOp(
                                    op="+",
                                    left = Id("a"),
                                    right = NumberLiteral(3.0)
                                    )
                            ),
                            VarDecl(
                                name=Id("b"),
                                varType=StringType(),
                                varInit=BinaryOp(
                                    op="...",
                                    left=StringLiteral("value of a is:"),
                                    right=CallExpr(name=Id("toString"), args=[Id("a")])
                                )
                            )
                        ]
                    )
                ),
                FuncDecl(name=Id("main"),
                        param=[],
                        body=Block(
                            [
                                VarDecl(
                                        name=Id("target"),
                                        varType=NumberType(),
                                        varInit=NumberLiteral(5.0)
                                    ),
                                CallStmt(name=Id("foo"),args=[Id("target")])
                            ]
                        )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,304))
    
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
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("areDivisors"),
                    param=[
                        VarDecl(
                            name=Id("num1"),
                            varType=NumberType()    
                        ),
                        VarDecl(
                            name=Id("num2"),
                            varType=NumberType()   
                        ),
                    ],
                    body=Return(
                        BinaryOp(
                            op="or",
                            left=BinaryOp(
                                    op="=",
                                    left=BinaryOp(
                                        op="%",
                                        left=Id("num1"),
                                        right=Id("num2")
                                    ),
                                    right=NumberLiteral(0.0)
                            ),
                            right=BinaryOp(
                                    op="=",
                                    left=BinaryOp(
                                        op="%",
                                        left=Id("num2"),
                                        right=Id("num1")
                                    ),
                                    right=NumberLiteral(0.0)
                            )
                        )
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("num1"),
                                modifier="var",
                                varInit=CallExpr(
                                    name=Id("readNumber"),
                                    args=[]
                                )
                            ),
                            VarDecl(
                                name=Id("num2"),
                                modifier="var",
                                varInit=CallExpr(
                                    name=Id("readNumber"),
                                    args=[]
                                )
                            ),
                            If(
                                expr=CallExpr(
                                    name=Id("areDivisors"),
                                    args=[
                                        Id("num1"),
                                        Id("num2")
                                    ]
                                ),
                                thenStmt=CallStmt(
                                    name=Id("writeString"),
                                    args=[StringLiteral("Yes")]
                                ),
                                elifStmt=[],
                                elseStmt=CallStmt(
                                    name=Id("writeString"),
                                    args=[StringLiteral("No")]
                                ),
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,305))

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
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("isPrime"),
                    param=[
                        VarDecl(
                            name=Id("x"),
                            varType=NumberType()
                        )
                    ]
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("x"),
                                varType=NumberType(),
                                varInit=CallExpr(name=Id("readNumber"),args=[])
                            ),
                            If(
                                expr=CallExpr(name=Id("isPrime"),args=[Id("x")]),
                                thenStmt=CallStmt(name=Id("writeString"),
                                                args=[StringLiteral("Yes")]
                                        ),
                                elifStmt=[],
                                elseStmt=CallStmt(name=Id("writeString"),
                                                args=[StringLiteral("No")]
                                        )
                            )
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("isPrime"),
                    param=[
                        VarDecl(
                            name=Id("x"),
                            varType=NumberType()
                        )
                    ],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op="<=",
                                    left=Id("x"),
                                    right=NumberLiteral(1.0)
                                    ),
                                thenStmt=Return(BooleanLiteral(False)),
                                elifStmt=[]
                            ),
                            VarDecl(
                                name=Id("i"),
                                modifier="var",
                                varInit=NumberLiteral(2.0)    
                            ),
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op=">",
                                    left=Id("i"),
                                    right=BinaryOp(
                                        op="/",
                                        left=Id("x"),
                                        right=NumberLiteral(2.0)
                                    )
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=Block(
                                    [
                                        If(
                                            expr=BinaryOp(
                                                op="=",
                                                left=BinaryOp(
                                                    op="%",
                                                    left=Id("x"),
                                                    right=Id("i")
                                                ),
                                                right=NumberLiteral(0.0)
                                            ),
                                            thenStmt=Return(BooleanLiteral(False)),
                                            elifStmt=[]
                                        )
                                    ]    
                                ),
                            ),
                            Return(BooleanLiteral(True))
                        ]
                    )
                ),
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,306))
        
    def test_source_submission_1(self):
        """Source from submission 1"""
        input = """number a
        """
        expected = str(Program([VarDecl(Id("a"), NumberType(), None, None)]))
        self.assertTrue(TestAST.test(input,expected,307))
    
    def test_source_submission_2(self):
        """Source from submission 2"""
        input = """func inc(number a) return a + 1
        func main() begin
        var a <- 1
        inc(a)
        writeNumber(a)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                Id("inc"),
                [VarDecl(Id("a"), NumberType(), None, None)],
                Return(BinaryOp("+", Id("a"), NumberLiteral(1.0)))),
                FuncDecl(
                    Id("main"), 
                    [], 
                    Block(
                        [
                            VarDecl(Id("a"), None, "var", NumberLiteral(1.0)),
                            CallStmt(Id("inc"), [Id("a")]),
                            CallStmt(Id("writeNumber"), [Id("a")])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,308))
    
    def test_simple_program_hello_world(self):
        """Simple hello world"""
        input = """
        func main()
        begin
            string b <- "Hello, World!"
            printString(b)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"), 
                                varType=StringType(),
                                varInit=StringLiteral("Hello, World!")
                            ),
                            CallStmt(name=Id("printString"), args=[Id("b")])
                        ]
                    )      
                ),
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,309))
        
#     #*Case 210-220: test function declaration
#     def test_simple_func_del(self):
#         '''Simple function declaration and call in main'''
#         input = """
#         func foo() begin
#         a <- 2
#         return a
#         end
#         func main() 
#         begin
#             a <- foo()
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,210))
        
#         def test_simple_func_del_return(self):
#         '''Small description here'''
#         input = """
#         func foo() return 2
#         func main() 
#         begin
#             a <- foo()
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,211))
        
#     def test_simple_func_del_error(self):
#         '''Function without return or block -> expect error at character a'''
#         input = """
#         func foo() a <- 2
#         func main() 
#         begin
#             a <- foo()
#         end
#         """
#         expected = error_msg(2,19,"a")
#         self.assertTrue(TestAST.test(input,expected,212))
        
#     def test_simple_func_del_wrong_keyword_case_1(self):
#         '''Function with wrong declare keyword -> expect Number var declare -> wrong char ('''
#         input = """
#         number foo() return 2
#         func main() 
#         begin
#             a <- foo()
#         end
#         """
#         expected = error_msg(2,18,"(")
#         self.assertTrue(TestAST.test(input,expected,213))
        
#     def test_func_del_wrong_keyword_case_1(self):
#         '''Function with wrong declare keyword -> expect error char true'''
#         input = """
#         true foo() return 2
#         func main() 
#         begin
#             a <- foo()
#         end
#         """
#         expected = error_msg(2,8,"true")
#         self.assertTrue(TestAST.test(input,expected,214))
    
#     def test_func_del_with_param(self):
#         '''Function with wrong declare keyword -> expect error char true'''
#         input = """
#         func foo(number a, number b) return (a >= b)
#         func main() 
#         begin
#             bool a <- foo()
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,215))
        
#     def test_forward_declare(self):
#         '''Function with wrong declare keyword -> expect error char true'''
#         input = """
#         func foo()
#         func main() 
#         begin
#             a <- foo()
#         end
#         func foo()
#         begin
#         return 2 
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,216))
    
#     def test_error_missing_paren(self):
#         '''Forward function without 1 paren'''
#         input = """
#         func foo)
#         func main() 
#         begin
#             a <- foo()
#         end
#         func foo()
#         begin
#         return 2 
#         end
#         """
#         expected = error_msg(2,16,")")
#         self.assertTrue(TestAST.test(input,expected,217))
        
#     def test_error_statement_after_return(self):
#         '''Function with statement after return'''
#         input = """
#         func foo()
#         func main() 
#         begin
#             a <- foo()
#         end
#         func foo()
#         return a
#         a <- 2
#         """
#         expected = error_msg(9,8,"a")
#         self.assertTrue(TestAST.test(input,expected,218))
    
#     def test_function_1_liner(self):
#         '''Function with 1 liner return'''
#         input = """
#         func foo() return 2
#         func main() 
#         begin
#             a <- foo()
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,220))
    
#     #*Case 221-230: Var declare
#     def test_simple_var_declare(self):
#         '''Simple string and number declare'''
#         input = """
#         number a <- 2
#         func main() 
#         begin
#             string b <- "Hello, World!"
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,221))
        
#     def test_simple_var_declare_wrong_type(self):
#         '''Simple string and number declare wrong type -> still expected success'''
#         input = """
#         number a <- "Hello"
#         func main() 
#         begin
#             string b <- 2
#             bool c <- true
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,222))
        
#     def test_simple_var_declare_no_init(self):
#         '''Simple string and number var declaration with no value init'''
#         input = """
#         number a
#         func main() 
#         begin
#             string b
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,223))
        
#     def test_simple_implicit_var_declare_no_init(self):
#         '''Simple implicit type var declare'''
#         '''Error at line var a -> end_line token bc var a must have declaration'''
#         input = """
#         var a
#         func main() 
#         begin
#             dynamic b
#         end
#         """
#         expected = error_msg(2,13,'\n')
#         self.assertTrue(TestAST.test(input,expected,224))
    
#     def test_simple_array_declare(self):
#         '''Simple array declaration'''
#         input = """
#         number a[2,3] <- [[2,3,4],[2,4,5]]
#         func main() 
#         begin
#             number b[3] <- [true,false,false]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,225))
    
#     def test_simple_array_declare_dim_error(self):
#         '''Simple array declaration with dimension error'''
#         input = """
#         number a[true,3] <- [[2,3,4],[2,4,5]]
#         func main() 
#         begin
#             number b[3] <- [true,false,false]
#         end
#         """
#         expected = error_msg(2,17,"true")
#         self.assertTrue(TestAST.test(input,expected,226))
        
#     def test_simple_array_declare_implicit_key_error(self):
#         '''Simple array declaration with implicit keyword error'''
#         '''expected error at '[' because var a -> recognize as variable decl'''
#         input = """
#         var a[2,3] <- [[2,3,4],[2,4,5]]
#         func main() 
#         begin
#             number b[3] <- [true,false,false]
#         end
#         """
#         expected = error_msg(2,13,"[")
#         self.assertTrue(TestAST.test(input,expected,227))
    
#     def test_simple_array_declare_missing_bracket(self):
#         '''Simple array declaration with missing bracket'''
#         input = """
#         number a[2,3 <- [[2,3,4],[2,4,5]]
#         func main() 
#         begin
#             number b[3] <- [true,false,false]
#         end
#         """
#         expected = error_msg(2,21,"<-")
#         self.assertTrue(TestAST.test(input,expected,228))
    
#     def test_simple_array_declare_null_dimension(self):
#         '''Simple array declaration with null dimension size list'''
#         input = """
#         number a[]<- [[2,3,4],[2,4,5]]
#         func main() 
#         begin
#             number b[3] <- [true,false,false]
#         end
#         """
#         expected = error_msg(2,17,"]")
#         self.assertTrue(TestAST.test(input,expected,229))
    
#     def test_simple_array_declare_wrong_bracket(self):
#         '''Simple array declaration with null dimension size list'''
#         '''Lexer error thus expected only the error token'''
#         input = """
#         number a[2}<- [[2,3,4],[2,4,5]]
#         func main() 
#         begin
#             number b[3] <- [true,false,false]
#         end
#         """
#         expected = lexer_err_msg("}")
#         self.assertTrue(TestAST.test(input,expected,230))
        
#     #*Case:231-240: Expression testing
#     def test_simple_expr(self):
#         '''Simple expr in var declaration'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             number b <- (3-4)*5- -foo()
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,231))
    
#     def test_simple_boolean_expr(self):
#         '''Simple expr in var declaration, bool expr'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             bool b <- (a >=5) and not(a <= 10)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,232))
        
#     def test_simple_string_expr(self):
#         '''Simple expr in var declaration, string concat expr'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             string b <- toString(a) ... \" is a number\"
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,233))
        
#     def test_simple_array_expr(self):
#         '''Simple expr in var declaration, array expr and value assignment'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             number b[2,3]
#             b[2,0] <- a
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,234))
    
#     def test_simple_expr_error(self):
#         '''Simple expr in var declaration, error no paren'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             number b <- (3-4*5-foo()
#         end
#         """
#         expected = error_msg(5,36,'\n')
#         self.assertTrue(TestAST.test(input,expected,235))
    
#     def test_simple_boolean_expr_err(self):
#         '''Simple expr in var declaration, bool expr error no operand'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             bool b <- (a >=5) and (a <= 10) or
#         end
#         """
#         expected = error_msg(5,46,'\n')
#         self.assertTrue(TestAST.test(input,expected,236))
        
#     def test_simple_string_expr_err(self):
#         '''Simple expr in var declaration, string concat expr error unclose str'''
#         input = """
# number a <- 2*5-3
# func main() 
# begin
#     string b <- toString(a) ... \" is a number\'\"
# end
# """
#         expected = lexer_err_msg(""" is a number\'\"""") #!I Cannot print EOF token here? thus this tc is always wrong
#         self.assertTrue(TestAST.test(input,expected,237))
        
#     def test_simple_array_expr_err(self):
#         '''Simple expr in var declaration, array expr error missing bracket'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             number b[2,3]
#             b[2,0 <- a
#         end
#         """
#         expected = error_msg(6,18,'<-')
#         self.assertTrue(TestAST.test(input,expected,238))
        
#     def test_simple_relation_expr(self):
#         '''Simple expr in var declaration, relational expr'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             bool b <- (a >= 5 + 5 - 2)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,239))
        
#     def test_simple_relation_expr_err(self):
#         '''Simple expr in var declaration, rela expr error, relational is none assoc'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             bool b <- (a >= 5 + 5 - 2 <= b)
#         end
#         """
#         expected = error_msg(5,38,"<=")
#         self.assertTrue(TestAST.test(input,expected,240))
        
#     #*Case 241-260: statement testing
#     def test_simple_if_statement(self):
#         '''Simple if stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             if (a > 3) printString("Yes")
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,241))
    
#     def test_simple_if_elif_else_statement(self):
#         '''Simple if else stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             if (a > 3) 
#                 printString(">3")
#             elif(a > 5)
#                 printString(">5")
#             elif(a > 7)
#                 printString(">7")
#             elif(a)
#                 printString("a")
#             else
#                 printString("lmao")
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,242))
        
#     def test_simple_if_statement_error(self):
#         '''Simple if else stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             if (a > 3
#                 printString(">3")
#             elif(a > 5)
#                 printString(">5")
#             elif(a > 7)
#                 printString(">7")
#             elif(a)
#                 printString("a")
#             else
#                 printString("lmao")
#         end
#         """
#         expected = error_msg(5,21,"\n")
#         self.assertTrue(TestAST.test(input,expected,243))
        
#     def test_simple_if_statement_no_condition_error(self):
#         '''Simple if else stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             if ()
#                 printString(">3")
#             elif(a > 5)
#                 printString(">5")
#             elif(a > 7)
#                 printString(">7")
#             elif(a)
#                 printString("a")
#             else
#                 printString("lmao")
#         end
#         """
#         expected = error_msg(5,16,")")
#         self.assertTrue(TestAST.test(input,expected,244))
        
#     def test_simple_if_statement_no_execute_stmt_error(self):
#         '''Simple if else stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             if (a = 1)
#             elif(a > 5)
#                 printString(">5")
#             elif(a > 7)
#                 printString(">7")
#             elif(a)
#                 printString("a")
#             else
#                 printString("lmao")
#         end
#         """
#         expected = error_msg(6,12,"elif")
#         self.assertTrue(TestAST.test(input,expected,244))
    
#     def test_nested_if_statement(self):
#         '''Simple if else stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             if (a > 1)
#                 if (a = 2) printString("is 2")
#                 elif (a = 5) printString("is 5")
#                 else printString("lmao")
#             elif(a > 7)
#                 printString(">7")
#             elif(a)
#                 printString("a")
#             else
#                 printString("lmao")
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,245))
        
#     def test_simple_for_statement(self):
#         '''Simple for stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             number i <- 0
#             for i until i = 10 by 1
#             printString(i)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,246))
    
#     def test_simple_for_statement_err(self):
#         '''Simple for stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for number i <- 0 until i = 10 by 1
#             printString(i)
#         end
#         """
#         expected = error_msg(5,16,"number")
#         self.assertTrue(TestAST.test(input,expected,247))
    
#     def test_simple_for_statement_edge_case(self):
#         '''Simple for stmt until true weird case, infinite loop'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until true by 1
#             printString(i)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,248))
        
#     def test_simple_for_statement_missing_by(self):
#         '''Simple for stmt missing by statement'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until isPrime(i)
#             printString(i)
#         end
#         """
#         expected = error_msg(5,34,"\n")
#         self.assertTrue(TestAST.test(input,expected,249))
        
#     def test_simple_for_statement_missing_until(self):
#         '''Simple for stmt missing until statement'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i by 1
#             printString(i)
#         end
#         """
#         expected = error_msg(5,18,"by")
#         self.assertTrue(TestAST.test(input,expected,250))
    
#     def test_simple_break(self):
#         '''Simple break stmt '''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until true by 1
#             if (isPrime(i))
#             break
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,251))
        
#     def test_simple_continue(self):
#         '''Simple continue stmt '''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until i >= 10 by 1
#                 if (not inFibo(i))
#                     continue
#                 else
#                     printString(i)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,252))
    
#     def test_simple_break_err(self):
#         '''Simple break stmt err'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until true by 1
#             if (isPrime(i))
#             Break
#         end
#         """
#         expected = error_msg(7,17,"\n")
#         self.assertTrue(TestAST.test(input,expected,253))
        
#     def test_simple_continue_err(self):
#         '''Simple continue stmt err'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until i >= 10 by 1
#                 if (not inFibo(i))
#                     continue a
#                 else
#                     printString(i)
#         end
#         """
#         expected = error_msg(7,29,"a")
#         self.assertTrue(TestAST.test(input,expected,254))
    
#     def test_simple_block_in_others(self):
#         '''Simple block stmt in others stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until i >= 10 by 1
#                 begin
#                 for j until j >= 10 by 1
#                     a[i,j] <- 0
#                 printString(j)
#                 end    
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,255))
    
#     def test_simple_block_err(self):
#         '''Simple block stmt in missing end'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until i >= 10 by 1
#                 begin
#                 for j until j >= 10 by 1
#                     a[i,j] <- 0
#                 printString(j)   
#         end
#         """
#         expected = error_msg(11,8, "<EOF>")
#         self.assertTrue(TestAST.test(input,expected,256))
    
#     def test_simple_block_empty(self):
#         '''Simple block empty'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until i >= 10 by 1
#                 begin
                
                
                
#                 end   
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,257))
        
#     def test_simple_block_no_begin(self):
#         '''Simple block empty'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             for i until i >= 10 by 1
#                 end   
#         end
#         """
#         expected = error_msg(6,16,"end")
#         self.assertTrue(TestAST.test(input,expected,258))

#     def test_simple_return(self):
#         '''Simple return stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             return
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,259))
        
#     def test_simple_return_error(self):
#         '''Simple return stmt err'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             return break
#         end
#         """
#         expected = error_msg(5,19,"break")
#         self.assertTrue(TestAST.test(input,expected,260))
    
#     #*Case: 261 - 270: Parameter in function
#     def test_simple_param(self):
#         '''Simple func with param'''
#         input = """
#         func foo(number a, number b) return a + b
#         func main() 
#         begin
#             foo(1,2)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,261))
        
#     def test_simple_array_param(self):
#         '''Simple func with array param'''
#         input = """
#         func foo(number a[2], number b) return a[1] + b
#         func main() 
#         begin
#             foo([1,2],2)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,262))
        
#     def test_simple_implicit_param_err(self):
#         '''Simple func with implicit param'''
#         input = """
#         func foo(var a, number b) return a + b
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = error_msg(2,17,"var")
#         self.assertTrue(TestAST.test(input,expected,263))
    
#     def test_simple_implicit_param_err_case_2(self):
#         '''Simple func with implicit param'''
#         input = """
#         func foo(implicit a, number b) return a + b
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = error_msg(2,17,"implicit")
#         self.assertTrue(TestAST.test(input,expected,264))    
    
#     def test_complex_array_param(self):
#         '''Simple func with array params'''
#         input = """
#         func foo(string a[2,3,4], bool b[2,3]) return
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,265))    
    
#     def test_multiline_param(self):
#         '''Simple func with array params'''
#         input = """
#         func foo(string a[2,3,4],
#         bool b[2,3]) return
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = error_msg(2,33,'\n')
#         self.assertTrue(TestAST.test(input,expected,266))   
        
#     def test_forward_decl_param(self):
#         '''Simple forward func with array params'''
#         input = """
#         func foo(string a[2,3,4],bool b[2,3])
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,267))   
    
#     def test_func_param_missing_coma(self):
#         '''Simple forward func with array params err missing coma'''
#         input = """
#         func foo(string a[2,3,4] bool b[2,3]) return
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = error_msg(2,33,"bool")
#         self.assertTrue(TestAST.test(input,expected,268))  
    
#     def test_func_param_semi_err(self):
#         '''Simple forward func with array params mistake semicol'''
#         input = """
#         func foo(string a[2,3,4]; bool b[2,3]) return
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = lexer_err_msg(";")
#         self.assertTrue(TestAST.test(input,expected,269))  
    
#     def test_func_param_missing_paren_err(self):
#         '''Simple forward func with missing param'''
#         input = """
#         func foo(string a[2,3,4], bool b[2,3] return
#         func main() 
#         begin
#             foo(2,2)
#         end
#         """
#         expected = error_msg(2,46,"return")
#         self.assertTrue(TestAST.test(input,expected,270))  
    
#     #*Case 271- 280: complex var decl and assignment
#     def test_long_var_decl(self):
#         '''Long array, var declare'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[2,3] <- [2,a*2/f,foo(2),true,[2,3]]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,271))
        
#     def test_long_var_decl_dimension_expr_err(self):
#         '''Long implicit type var declare'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[foo(2),3] <- [2,a*2/f,foo(2),true,[2,3]]
#         end
#         """
#         expected = error_msg(5,21,"foo")
#         self.assertTrue(TestAST.test(input,expected,272))
    
#     def test_elem_expr_assignment(self):
#         '''Long implicit type var declare'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[2,3]
#             b[a,foo(2)] <- b[foo(2),a]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,273))
    
#     def test_long_var_decl_dimension_with_float(self):
#         '''floating point dim'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[2.293E21,3] <- [2,a*2/f,foo(2),true,[2,3]]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,274))
    
#     def test_long_var_decl_dimension_with_string(self):
#         '''Long string dim error'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b["string",3] <- [2,a*2/f,foo(2),true,[2,3]]
#         end
#         """
#         expected = error_msg(5,21,"string")
#         self.assertTrue(TestAST.test(input,expected,275))
    
#     def test_elem_expr_assignment(self):
#         '''element expr assignment'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[2,3]
#             b["string",2.123E-32] <- b[foo(2),a]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,276))
    
#     def test_array_assign_with_id(self):
#         '''Long array assign case 1'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[2,3] <- a
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,277))
    
#     def test_array_assign_with_function(self):
#         '''Long array assign case 2'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[2,3] <- foo(2)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,278))
    
#     def test_number_assign_with_array_val(self):
#         '''test number var assign with array value'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b <- [2,3]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,279))
    
#     def test_complex_array_value(self):
#         '''Long implicit type var declare'''
#         input = """
#         var a <- 2*3-foo()+b[2,3]
#         func main() 
#         begin
#             number b[2,3] <- [[2,foo(3)], [23.1237E-2,[1237,232]], 123, a[1,foo(3)]]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,280))
    
#     #*Case 281-290: Complex expression testing
#     def test_complex_expr_case_1(self):
#         '''Complex expr case 1'''
#         input = """
#         func main() 
#         begin
#             var a <- (num1 - num2 / 2 * 3 = 0) or (num1 - -num2*5/2+3 >= 0)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,281))
    
#     def test_complex_expr_case_1_err(self):
#         '''Complex expr case 1 err'''
#         input = """
#         func main() 
#         begin
#             var a <- (num1 - num2 / 2 * 3 = 0) or (num1 - +num2*5/2+3 >= 0)
#         end
#         """
#         expected = error_msg(4,58,"+")
#         self.assertTrue(TestAST.test(input,expected,282))
    
#     def test_complex_expr_case_2(self):
#         '''Complex expr case 2'''
#         input = """
#         func main() 
#         begin
#             var a <- (bool1 or (bool2 and not bool3 )) or (isFoo(a) and not isFoo(b))
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,283))
    
#     def test_complex_expr_case_2_err(self):
#         '''Complex expr case 2 err'''
#         input = """
#         func main() 
#         begin
#             var a <- (bool1 or (bool2 and and bool3 )) or (isFoo(a) and not isFoo(b))
#         end
#         """
#         expected = error_msg(4,42,"and")
#         self.assertTrue(TestAST.test(input,expected,284))
    
#     def test_complex_expr_case_3(self):
#         '''Complex expr case 3 '''
#         input = """
#         func main() 
#         begin
#             var a <- (bool1 or (var1 + var2 >= 3 )) + (isFoo(a) and not isFoo(b,a[2]))
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,285))
    
#     def test_complex_expr_case_3_err(self):
#         '''Complex expr case 3 err '''
#         input = """
#         func main() 
#         begin
#             var a <- (bool1 or (var1 + var2 >= 3 < 5 )) + (isFoo(a) and not isFoo(b,a[2]))
#         end
#         """
#         expected = error_msg(4,49,"<")
#         self.assertTrue(TestAST.test(input,expected,286))
    
#     def test_complex_expr_case_4(self):
#         '''Complex expr case 4 '''
#         input = """
#         func main() 
#         begin
#             string a <- toString(b) + toString(c) ... d[2,3] == str(123825) + d[23,54]
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,286))
    
#     def test_complex_expr_case_5(self):
#         '''Complex expr case 5 err '''
#         input = """
#         func main() 
#         begin
#             bool b <- str(a) ... str(b) == (a >= b/c)
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,287))
    
#     def test_complex_expr_case_5_err(self):
#         '''Complex expr case 5 err '''
#         input = """
#         func main() 
#         begin
#             bool b <- str(a) ... str(b) == (a >= b/c]
#         end
#         """
#         expected = error_msg(4,52,"]")
#         self.assertTrue(TestAST.test(input,expected,288))
    
#     def test_complex_expr_case_6_stmt_in_assign(self):
#         '''Complex expr case 6 err '''
#         input = """
#         func main() 
#         begin
#             bool b <- if a do(b)
#         end
#         """
#         expected = error_msg(4,22,"if")
#         self.assertTrue(TestAST.test(input,expected,289))
    
#     def test_complex_expr_case_7_empty_array_val(self):
#         '''Complex expr case 7 err '''
#         input = """
#         func main() 
#         begin
#             bool b <- [[[[]]]]
#         end
#         """
#         expected = error_msg(4,26,"]")
#         self.assertTrue(TestAST.test(input,expected,290))
    
#     #*Case 291 - 300 : Random test
#     def test_simple_implicit_var_declare(self):
#         '''Simple implicit type var declare'''
#         input = """
#         var a <- 2
#         func main() 
#         begin
#             dynamic b <- "String"
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,291))
    
#     def test_simple_if_no_paren(self):
#         '''Simple if else stmt'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#             if a > 3
#                 printString("Yes")
#             else 
#                 printString("No")
#         end
#         """
#         expected = error_msg(5,15,"a")
#         self.assertTrue(TestAST.test(input,expected,292))
    
#     def test_begin_no_newline(self):
#         '''Simple begin stmt no newline'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin end
#         """
#         expected = error_msg(4,14,"end")
#         self.assertTrue(TestAST.test(input,expected,293))
    
#     def test_simple_comment(self):
#         '''Simple program with comment'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#         number b <- 2 ##This is a comment
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,294))
    
#     def test_simple_comment_weird_char(self):
#         '''Simple comment with weird char'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#         number b <- 2 ##This is a comment with weird character \a
#         end
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,295))
    
#     def test_simple_comment_error(self):
#         '''Simple comment program'''
#         input = """
#         number a <- 2*5-3
#         func main() 
#         begin
#         number b <- 2 ##This is a 
#         comment
#         end
#         """
#         expected = error_msg(6,15,"\n")
#         self.assertTrue(TestAST.test(input,expected,296))
    
#     def test_simple_program_no_func(self):
#         '''Simple program no function'''
#         input = """
#         number a <- 2*5-3
#         number b <- 2 ##This is a 
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,297))
    
#     def test_simple_program_no_func_with_outside_stmt(self):
#         '''Simple outside stmt error'''
#         input = """
#         number a <- 2*5-3
#         number b <- 2 ##This is a 
#         if a do(B)
#         """
#         expected = error_msg(4,8,"if")
#         self.assertTrue(TestAST.test(input,expected,298))
    
#     def test_comment_only_program(self):
#         '''Program with comment only'''
#         input = """
#         ##number b <- 2 ##This is a 
#         ##if a do(B)
#         """
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,299))
    
#     def test_empty_program(self):
#         '''Empty program'''
#         input = """"""
#         expected = SUCCESSFUL
#         self.assertTrue(TestAST.test(input,expected,300))