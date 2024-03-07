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
    def test_simple_func_del(self):
        '''Simple function declaration and call in main'''
        input = """
        func foo() begin
        number a <- 2
        return a
        end
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("a"),
                                varType=NumberType(),
                                varInit=NumberLiteral(2.0)
                            ),
                            Return(Id("a"))
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"),args=[])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,310))
        
    def test_simple_func_del_return(self):
        '''Simple func decl 1 liner'''
        input = """
        func foo() return 2
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[],
                    body=Return(NumberLiteral(2.0))
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                )
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,311))
        
    def test_simple_func_del_block(self):
        '''Function without return or block -> expect error at character a'''
        input = """
        func foo() begin 
        a <- 2 
        end
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=NumberLiteral(2.0)
                            )
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                )
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,312))
        
    def test_simple_func_del_param_case_1(self):
        '''Function with 1 param
        '''
        input = """
        func foo(number a) return 2
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=NumberType()
                        )    
                    ],
                    body=Return(NumberLiteral(2.0))
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                )
                
            ]
        ))
        
        self.assertTrue(TestAST.test(input,expected,313))
        
    def test_simple_func_del_del_param_case_2(self):
        '''Function with wrong declare keyword -> expect error char true'''
        input = """
        func foo(string a) return a ... a
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=StringType()
                        )    
                    ],
                    body=Return(BinaryOp(
                        op="...",
                        left=Id("a"),
                        right=Id("a")
                    ))
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                )
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,314))
    
    def test_func_del_with_multiple_param(self):
        '''Function with multiple param'''
        input = """
        func foo(number a, number b) return (a >= b)
        func main() 
        begin
            bool a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=NumberType()
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=NumberType()
                        )    
                    ],
                    body=Return(BinaryOp(
                        op=">=",
                        left=Id("a"),
                        right=Id("b")
                    ))
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("a"),
                                varType=BoolType(),
                                varInit=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                )
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,315))
        
    def test_forward_declare_case_1(self):
        '''Function forward decl'''
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
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                    ],
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("foo"),
                    param=[
                    ],
                    body=Block([Return(NumberLiteral(2.0))])
                )
            ]
        ))        
        self.assertTrue(TestAST.test(input,expected,316))
    
    def test_forward_declare_case_2(self):
        '''Forward function without 1 paren'''
        input = """
        func foo(number a)
        func main() 
        begin
            a <- foo()
        end
        func foo(number a)
        begin
        return 2 
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=NumberType()                            
                        )
                    ],
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=NumberType()                            
                        )
                    ],
                    body=Block([Return(NumberLiteral(2.0))])
                )
            ]
        ))        
        self.assertTrue(TestAST.test(input,expected,317))
        
    def test_forward_declare_case_3(self):
        '''Function with statement after return'''
        input = """
        func foo()
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                    ],
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                ),
            ]
        ))   
        self.assertTrue(TestAST.test(input,expected,318))
    
    def test_function_1_liner_case_1(self):
        '''Function with 1 liner return'''
        input = """
        func foo() return a
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                    ],
                    body=Return(Id("a"))
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                ),
            ]
        ))   
        self.assertTrue(TestAST.test(input,expected,219))
        
    def test_function_1_liner_case_2(self):
        '''Function with 1 liner block'''
        input = """
        func foo() begin
        end
        func main() 
        begin
            a <- foo()
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                    ],
                    body=Block([])
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=Id("a"),
                                rhs=CallExpr(name=Id("foo"), args=[])
                            )
                        ]
                    )
                ),
            ]
        ))   
        self.assertTrue(TestAST.test(input,expected,219))
    
#     #*Case 221-230: Var declare
    def test_simple_var_declare(self):
        '''Simple string and number declare'''
        input = """
        number a <- 2
        func main() 
        begin
            string b <- "Hello, World!"
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=NumberLiteral(2.0)
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=StringType(),
                                varInit=StringLiteral("Hello, World!")
                            )
                        ]
                    )
                ),
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,321))
        
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
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=StringLiteral("Hello")
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=StringType(),
                                varInit=NumberLiteral(2.0)
                            ),
                            VarDecl(
                                name=Id("c"),
                                varType=BoolType(),
                                varInit=BooleanLiteral(True)
                            )
                        ]
                    )
                ),
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,322))
        
    def test_simple_var_declare_no_init(self):
        '''Simple string and number var declaration with no value init'''
        input = """
        number a
        func main() 
        begin
            string b
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=StringType(),
                            ),
                        ]
                    )
                ),
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,323))
        
    def test_simple_implicit_var_declare(self):
        '''Simple implicit type var declare'''
        '''Error at line var a -> end_line token bc var a must have declaration'''
        input = """
        var a <- 2
        func main() 
        begin
            dynamic b <- a
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    modifier="var",
                    varInit=NumberLiteral(2.0)
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                modifier="dynamic",
                                varInit=Id("a")
                            ),
                        ]
                    )
                ),
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,324))
    
    def test_simple_array_declare(self):
        '''Simple array declaration'''
        input = """
        number a[2,3] <- [[2,3,4],[2,4,5]]
        func main() 
        begin
            number b[3] <- [true,false,false]
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=ArrayType([2.0,3.0], NumberType()),
                    varInit=ArrayLiteral([
                        ArrayLiteral([
                            NumberLiteral(2.0),
                            NumberLiteral(3.0),
                            NumberLiteral(4.0)
                        ]),
                        ArrayLiteral([
                            NumberLiteral(2.0),
                            NumberLiteral(4.0),
                            NumberLiteral(5.0)
                        ])
                    ])
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=ArrayType([3.0], NumberType()),
                                varInit=ArrayLiteral([
                                    BooleanLiteral(True),
                                    BooleanLiteral(False),
                                    BooleanLiteral(False)
                                ])
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,325))
    
    def test_simple_array_declare_case_2(self):
        '''Simple array declaration Case 2'''
        input = """
        string a[3] <- ["Im", "a", "dev"]
        func main() 
        begin
            number b[3] <- a
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=ArrayType([3.0], StringType()),
                    varInit=ArrayLiteral([ 
                            StringLiteral("Im"),
                            StringLiteral("a"),
                            StringLiteral("dev")
                    ])
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=ArrayType([3.0], NumberType()),
                                varInit=Id("a")
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,326))
        
    def test_simple_array_declare_with_array_cell_expr(self):
        '''Simple array declaration with array cell expr'''
        input = """
        number a[2,3]
        func main() 
        begin
            number b[3] <- a[1]
        end
        """
        expected = expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=ArrayType([2.0, 3.0], NumberType()),
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=ArrayType([3.0], NumberType()),
                                varInit=ArrayCell(
                                    arr=Id("a"),
                                    idx=[NumberLiteral(1.0)]
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,327))
    
    def test_array_declare_with_complex_arr_cell(self):
        '''Simple array declaration with missing bracket'''
        input = """
        number a[2,3]
        func main() 
        begin
            number b[3] <- a[foo(2), 3+5*2,1]
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=ArrayType([2.0, 3.0], NumberType()),
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=ArrayType([3.0], NumberType()),
                                varInit=ArrayCell(
                                    arr=Id("a"),
                                    idx=[
                                        CallExpr(name=Id("foo"), args=[NumberLiteral(2.0)]),
                                        BinaryOp(
                                            op="+",
                                            left=NumberLiteral(3.0),
                                            right=BinaryOp(
                                                op="*",
                                                left=NumberLiteral(5.0),
                                                right=NumberLiteral(2.0),
                                            )
                                        ),
                                        NumberLiteral(1.0)
                                    ]
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,328))
    
    def test_simple_array_declare_complex_arr_cell_case_2(self):
        '''Simple array declaration with complex arr cell'''
        input = """
        number a[2]<- [a ... b, true and false]
        func main() 
        begin
            return 1
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=ArrayType([2.0], NumberType()),
                    varInit=ArrayLiteral(
                        [
                            BinaryOp(
                                op="...",
                                left=Id("a"),
                                right=Id("b")
                            ),
                            BinaryOp(
                                op="and",
                                left=BooleanLiteral(True),
                                right=BooleanLiteral(False)
                            )
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block([Return(NumberLiteral(1.0))])
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,329))
    
    def test_simple_array_declare_complex_arr_cell_case_3(self):
        '''Simple array declaration with complex arr cell'''
        input = """
        number a[2,3]<- [[a ... b, true],[2,4*3,5 >= c]]
        func main() 
        begin
            return 1
        end
        """
        expected = expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=ArrayType([2.0, 3.0], NumberType()),
                    varInit=ArrayLiteral(
                        [
                            ArrayLiteral([
                                BinaryOp(
                                    op="...",
                                    left=Id("a"),
                                    right=Id("b")
                                ),
                                BooleanLiteral(True)
                            ]),
                            ArrayLiteral([
                                NumberLiteral(2.0),
                                BinaryOp(
                                    op="*",
                                    left=NumberLiteral(4.0),
                                    right=NumberLiteral(3.0)
                                ),
                                BinaryOp(
                                    op=">=",
                                    left=NumberLiteral(5.0),
                                    right=Id("c")
                                ),
                            ])
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block([Return(NumberLiteral(1.0))])
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,330))
        
#     #*Case:231-240: Expression testing
    def test_simple_expr(self):
        '''Simple expr in var declaration'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            number b <- (3-4)*5- -foo()
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=NumberType(),
                                varInit=BinaryOp(
                                    op="-",
                                    left=BinaryOp(
                                        op="*",
                                        left=BinaryOp(
                                            op="-",
                                            left=NumberLiteral(3.0),
                                            right=NumberLiteral(4.0)
                                        ),
                                        right=NumberLiteral(5.0)
                                    ),
                                    right=UnaryOp(
                                        op="-",
                                        operand=CallExpr(name=Id("foo"), args=[])
                                    )
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,331))
    
    def test_simple_boolean_expr(self):
        '''Simple expr in var declaration, bool expr'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >=5) and not(a <= 10)
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=BoolType(),
                                varInit=BinaryOp(
                                    op="and",
                                    left=BinaryOp(
                                        op=">=",
                                        left=Id("a"),
                                        right=NumberLiteral(5.0)
                                    ),
                                    right=UnaryOp(
                                        op="not",
                                        operand=BinaryOp(
                                        op="<=",
                                        left=Id("a"),
                                        right=NumberLiteral(10.0)
                                    )   
                                    )
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,332))
        
    def test_simple_string_expr(self):
        '''Simple expr in var declaration, string concat expr'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            string b <- toString(a) ... \" is a number\"
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=StringType(),
                                varInit=BinaryOp(
                                    op="...",
                                    left=CallExpr(name=Id("toString"), args=[Id("a")]),
                                    right=StringLiteral(" is a number")
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,333))
        
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
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=ArrayType([2.0, 3.0], NumberType()),
                            ),
                            Assign(
                                lhs=ArrayCell(
                                    arr=Id("b"),
                                    idx=[NumberLiteral(2.0), NumberLiteral(0.0)]
                                ),
                                rhs=Id("a")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,334))
    
    def test_simple_expr_case_2(self):
        '''Simple expr in var declaration case 2'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            number b <- (3-4*5-foo())
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=NumberType(),
                                varInit=BinaryOp(
                                    op="-",
                                    left=BinaryOp(
                                        op="-",
                                        left=NumberLiteral(3.0),
                                        right=BinaryOp(
                                            op="*",
                                            left=NumberLiteral(4.0),
                                            right=NumberLiteral(5.0)
                                        )
                                    ),
                                    right=CallExpr(name=Id("foo"), args=[])
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,335))
    
    def test_simple_boolean_expr_case_2(self):
        '''Simple expr in var declaration, bool expr case 2'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >=5) and (a <= 10) or c
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=BoolType(),
                                varInit=BinaryOp(
                                    op="or",
                                    left=BinaryOp(
                                        op="and",
                                        left=BinaryOp(
                                            op=">=",
                                            left=Id("a"),
                                            right=NumberLiteral(5.0)
                                        ),
                                        right=BinaryOp(
                                            op="<=",
                                            left=Id("a"),
                                            right=NumberLiteral(10.0)
                                        ),
                                    ),
                                    right=Id("c")
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,336))
        
    def test_simple_string_expr_case_2(self):
        '''Simple expr in var declaration'''
        input = """
        func main() 
        begin
            string b <- (toString(a) ... \" \'\"is a number\'\" \") ... toString(b)
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
                                varInit=BinaryOp(
                                    op="...",
                                    left=BinaryOp(
                                        op="...",
                                        left=CallExpr(name=Id("toString"), args=[Id("a")]),
                                        right=StringLiteral(" \'\"is a number\'\" ")
                                    ),
                                    right=CallExpr(name=Id("toString"), args=[Id("b")])
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,337))
        
    def test_simple_array_expr_case_2(self):
        '''Simple expr in var declaration, array expr case 2'''
        input = """
        func main() 
        begin
            number b[2,3]
            foo()[2,0] <- a
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
                                varType=ArrayType([2.0, 3.0], NumberType()),
                            ),
                            Assign(
                                lhs=ArrayCell(
                                    arr=CallExpr(name=Id("foo"), args=[]),
                                    idx=[NumberLiteral(2.0), NumberLiteral(0.0)]
                                ),
                                rhs=Id("a")
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,338))
        
    def test_simple_relation_expr(self):
        '''Simple expr in var declaration, relational expr'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >= 5 + 5 - 2)
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=BoolType(),
                                varInit=BinaryOp(
                                    op=">=",
                                    left=Id("a"),
                                    right=BinaryOp(
                                        op="-",
                                        left=BinaryOp(
                                            op="+",
                                            left=NumberLiteral(5.0),
                                            right=NumberLiteral(5.0)
                                        ),
                                        right=NumberLiteral(2.0)
                                    )
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,339))
        
    def test_simple_relation_expr_case_2(self):
        '''Simple expr in var declaration, rela expr case 2'''
        input = """
        number a <- 2*5-3
        func main() 
        begin
            bool b <- (a >= 5) and not (5 - 2 <= b)
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    varType=NumberType(),
                    varInit=BinaryOp(
                        op="-",
                        left=BinaryOp(
                            op="*",
                            left=NumberLiteral(2.0),
                            right=NumberLiteral(5.0),
                        ),
                        right=NumberLiteral(3.0)
                    )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=BoolType(),
                                varInit=BinaryOp(
                                    op="and",
                                    left=BinaryOp(
                                            op=">=",
                                            left=Id("a"),
                                            right=NumberLiteral(5.0)
                                        ),
                                    right=UnaryOp(
                                        op="not",
                                        operand=BinaryOp(
                                            op="<=",
                                            left=BinaryOp(
                                                op="-",
                                                left=NumberLiteral(5.0),
                                                right=NumberLiteral(2.0)
                                            ),
                                            right=Id("b")
                                        )
                                    )
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,340))
        
#     #*Case 241-260: statement testing
    def test_simple_if_statement(self):
        '''Simple if stmt'''
        input = """
        func main() 
        begin
            if (a > 3) printString("Yes")
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op=">",
                                    left=Id("a"),
                                    right=NumberLiteral(3.0)
                                ),
                                thenStmt=CallStmt(name=Id("printString"), args=[StringLiteral("Yes")])
                                
                            )
                        ]
                    )
                )
            ]
        )) 
        self.assertTrue(TestAST.test(input,expected,341))
    
    def test_simple_if_elif_else_statement(self):
        '''Simple if else stmt'''
        input = """
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
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op=">",
                                    left=Id("a"),
                                    right=NumberLiteral(3.0)
                                ),
                                thenStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral(">3")]),
                                elifStmt=
                                [
                                    (   
                                        BinaryOp(
                                            op=">",
                                            left=Id("a"),
                                            right=NumberLiteral(5.0)
                                        ),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral(">5")])
                                    ),
                                    (   
                                        BinaryOp(
                                            op=">",
                                            left=Id("a"),
                                            right=NumberLiteral(7.0)
                                        ),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral(">7")])
                                    ),
                                    (   
                                        Id("a"),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral("a")])
                                    )
                                ],
                                elseStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral("lmao")])
                            )
                        ]
                    )
                )
            ]
        )) 
        self.assertTrue(TestAST.test(input,expected,342))
        
    def test_simple_if_statement_no_else(self):
        '''Simple if else stmt'''
        input = """
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
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op=">",
                                    left=Id("a"),
                                    right=NumberLiteral(3.0)
                                ),
                                thenStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral(">3")]),
                                elifStmt=
                                [
                                    (   
                                        BinaryOp(
                                            op=">",
                                            left=Id("a"),
                                            right=NumberLiteral(5.0)
                                        ),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral(">5")])
                                    ),
                                    (   
                                        BinaryOp(
                                            op=">",
                                            left=Id("a"),
                                            right=NumberLiteral(7.0)
                                        ),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral(">7")])
                                    ),
                                    (   
                                        Id("a"),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral("a")])
                                    )
                                ],
                            )
                        ]
                    )
                )
            ]
        )) 
        self.assertTrue(TestAST.test(input,expected,343))
        
    def test_simple_if_statement_no_elif(self):
        '''Simple if else stmt'''
        input = """
        func main() 
        begin
            if (2*4)
                printString(">3")
            else
                printString("lmao")
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op="*",
                                    left=NumberLiteral(2.0),
                                    right=NumberLiteral(4.0)
                                ),
                                thenStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral(">3")]),
                                elseStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral("lmao")])
                            )
                        ]
                    )
                )
            ]
        )) 
        self.assertTrue(TestAST.test(input,expected,344))
    
    def test_nested_if_statement(self):
        '''Simple if else stmt nested'''
        input = """
        func main() 
        begin
            if (a > 1)
                if (a = 2) printString("is 2")
                elif (a = 5) printString("is 5")
                else printString("lmao")
            elif(a)
                printString("a")
            else
                printString("lmao")
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op=">",
                                    left=Id("a"),
                                    right=NumberLiteral(1.0)
                                ),
                                thenStmt=If(
                                    expr=BinaryOp(
                                        op="=",
                                        left=Id("a"),
                                        right=NumberLiteral(2.0)
                                    ),
                                    thenStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral("is 2")]), 
                                    elifStmt=[
                                        (
                                            BinaryOp(
                                                op="=",
                                                left=Id("a"),
                                                right=NumberLiteral(5.0)
                                            ),
                                            CallStmt(name=Id("printString"),
                                                args=[StringLiteral("is 5")]), 
                                        )
                                    ],
                                    elseStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral("lmao")]),
                                ),
                                elifStmt=
                                [
                                    (   
                                        Id("a"),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral("a")])
                                    ),
                                ],
                                elseStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral("lmao")])
                            )
                        ]
                    )
                )
            ]
        )) 
        self.assertTrue(TestAST.test(input,expected,345))
        
    def test_simple_for_statement(self):
        '''Simple for stmt'''
        input = """
        func main() 
        begin
            number i <- 0
            for i until i = 10 by 1
            printString(i)
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
                                name=Id("i"),
                                varType=NumberType(),
                                varInit=NumberLiteral(0.0)
                            ),
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op="=",
                                    left=Id("i"),
                                    right=NumberLiteral(10.0)
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=CallStmt(name=Id("printString"), args=[Id("i")])
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,346))
    
    def test_simple_for_statement_case_2(self):
        '''Simple for stmt'''
        input = """
        func main() 
        begin
            for i until (i < -10*(i-2)) by i*i
            printString(i)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op="<",
                                    left=Id("i"),
                                    right=BinaryOp(
                                        op="*",
                                        left=UnaryOp(
                                            op="-",
                                            operand=NumberLiteral(10.0)
                                        ),
                                        right=BinaryOp(
                                            op="-",
                                            left=Id("i"),
                                            right=NumberLiteral(2.0)
                                        )
                                    )
                                ),
                                updExpr=BinaryOp(
                                    op="*",
                                    left=Id("i"),
                                    right=Id("i")
                                ),
                                body=CallStmt(name=Id("printString"), args=[Id("i")])
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,347))
    
    def test_simple_for_statement_edge_case(self):
        '''Simple for stmt until true weird case, infinite loop'''
        input = """
        func main() 
        begin
            for i until true by 1
            printString(i)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BooleanLiteral(True),
                                updExpr=NumberLiteral(1.0),
                                body=CallStmt(name=Id("printString"), args=[Id("i")])
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,348))
        
    def test_simple_for_statement_case_3(self):
        '''Simple for stmt statement case 2'''
        input = """
        func main() 
        begin
            for i until isPrime(i) by adjust(i)
            printString(i)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=CallExpr(name=Id("isPrime"), args=[Id("i")]),
                                updExpr=CallExpr(name=Id("adjust"), args=[Id("i")]),
                                body=CallStmt(name=Id("printString"), args=[Id("i")])
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,349))
        
    def test_simple_for_statement_nested(self):
        '''Simple for stmt statement nested'''
        input = """
        func main() 
        begin
            for i until i > 10 by 1 
            for j until j > 10 by 2
            printString(i, j)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op=">",  
                                    left=Id("i"),
                                    right=NumberLiteral(10.0)
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=For(
                                    name=Id("j"),
                                    condExpr=BinaryOp(
                                        op=">",  
                                        left=Id("j"),
                                        right=NumberLiteral(10.0)
                                    ),
                                    updExpr=NumberLiteral(2.0),
                                    body=CallStmt(name=Id("printString"), args=[Id("i"), Id("j")])
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,350))
    
    def test_simple_break(self):
        '''Simple break stmt '''
        input = """
        func main() 
        begin
            for i until true by 1
            if (isPrime(i))
            break
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BooleanLiteral(True),
                                updExpr=NumberLiteral(1.0),
                                body=If(
                                    expr=CallExpr(name=Id("isPrime"), args=[Id("i")]),
                                    thenStmt=Break()
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,351))
        
    def test_simple_continue(self):
        '''Simple continue stmt '''
        input = """
        func main() 
        begin
            for i until i >= 10 by 1
                if (not inFibo(i))
                    continue
                else
                    printString(i)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op=">=",  
                                    left=Id("i"),
                                    right=NumberLiteral(10.0)
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=If(
                                    expr=UnaryOp(
                                        op="not",
                                        operand=CallExpr(name=Id("inFibo"), args=[Id("i")]),
                                    ),
                                    thenStmt=Continue(),
                                    elseStmt=CallStmt(name=Id("printString"), args=[Id("i")])
                                )
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,352))
    
    def test_nested_if_statement_case_2(self):
        '''Simple if else stmt nested'''
        input = """
        func main() 
        begin
            if (a > 1)
                if (a = 2) printString("is 2")
                elif (a = 5) printString("is 5")
            elif(a)
                printString("a")
            else
                printString("lmao")
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op=">",
                                    left=Id("a"),
                                    right=NumberLiteral(1.0)
                                ),
                                thenStmt=If(
                                    expr=BinaryOp(
                                        op="=",
                                        left=Id("a"),
                                        right=NumberLiteral(2.0)
                                    ),
                                    thenStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral("is 2")]), 
                                    elifStmt=[
                                        (
                                            BinaryOp(
                                                op="=",
                                                left=Id("a"),
                                                right=NumberLiteral(5.0)
                                            ),
                                            CallStmt(name=Id("printString"),
                                                args=[StringLiteral("is 5")]), 
                                        ),
                                        (   
                                        Id("a"),
                                        CallStmt(name=Id("printString"),
                                                args=[StringLiteral("a")])
                                        ),
                                    ],
                                    elseStmt=CallStmt(name=Id("printString"),
                                                args=[StringLiteral("lmao")]),
                                ),
                                elifStmt=
                                [
                                    
                                ],
                            )
                        ]
                    )
                )
            ]
        )) 
        self.assertTrue(TestAST.test(input,expected,353))
    
    def test_simple_block_in_for(self):
        '''Simple continue stmt err'''
        input = """
        func main() 
        begin
            for i until i >= 10 by 1
            begin
                if (i = 3) break
                else return a
            end
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op=">=",  
                                    left=Id("i"),
                                    right=NumberLiteral(10.0)
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=Block([
                                    If(
                                        expr= BinaryOp(
                                            op="=",
                                            left=Id("i"),
                                            right=NumberLiteral(3.0)
                                        ),
                                        thenStmt=Break(),
                                        elseStmt=Return(Id("a"))
                                        
                                    )
                                ])
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,354))
    
    def test_simple_block_in_if(self):
        '''Simple block stmt in others stmt'''
        input = """
        func main() 
        begin
            if (a = 3)
            begin
            printString("hahaha")
            return 1
            end    
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            If(
                                expr=BinaryOp(
                                    op="=",
                                    left=Id("a"),
                                    right=NumberLiteral(3.0),
                                ),
                                thenStmt=Block(
                                    [
                                        CallStmt(name=Id("printString"), args=[StringLiteral("hahaha")]),
                                        Return(NumberLiteral(1.0))
                                    ]
                                )
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,355))
    
    def test_simple_block_empty(self):
        '''Simple block stmt in missing end'''
        input = """
        func main() 
        begin
            for i until i >= 10 by 1
                begin 
                end
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op=">=",
                                    left=Id("i"),
                                    right=NumberLiteral(10.0)
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=Block([])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,356))
    
    def test_simple_block_empty_nested(self):
        '''Simple nested block empty'''
        input = """
        func main() 
        begin
            for i until i >= 10 by 1
                begin
                    begin
                    end
                end   
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op=">=",
                                    left=Id("i"),
                                    right=NumberLiteral(10.0)
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=Block([Block([])])
                            )
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,357))
        
    def test_simple_block_case_2(self):
        '''Simple block stmt case 2'''
        input = """
        func main() 
        begin
            for i until i >= 10 by 1
                begin
                    a <- 3
                    return a
                end   
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            For(
                                name=Id("i"),
                                condExpr=BinaryOp(
                                    op=">=",  
                                    left=Id("i"),
                                    right=NumberLiteral(10.0)
                                ),
                                updExpr=NumberLiteral(1.0),
                                body=Block([
                                    Assign(lhs=Id("a"), rhs=NumberLiteral(3.0)),
                                    Return(Id("a"))
                                ])
                            ),
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,358))

    def test_simple_return(self):
        '''Simple return stmt'''
        input = """
        func main() 
        begin
            return
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Return()
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,359))
        
    def test_simple_return_with_expr(self):
        '''Simple return stmt err'''
        input = """
        func main() 
        begin
            return 2*3
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Return(BinaryOp(
                                op="*",
                                left=NumberLiteral(2.0),
                                right=NumberLiteral(3.0)
                            ))
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,360))
    
#     #*Case: 261 - 270: Parameter in function
    def test_simple_param(self):
        '''Simple func with param'''
        input = """
        func foo(number a, number b) return a + b
        func main() 
        begin
            foo(1,2)
        end
        """
        expected =  str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=NumberType()    
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=NumberType()        
                        ),
                    ],
                    body= Return(
                                BinaryOp(
                                    op="+",
                                    left=Id("a"),
                                    right=Id("b")
                                )
                            )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(name=Id("foo"), 
                                    args=
                                    [
                                        NumberLiteral(1.0), 
                                        NumberLiteral(2.0)
                                    ])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,361))
        
    def test_simple_array_param(self):
        '''Simple func with array param'''
        input = """
        func foo(number a[2], number b) return a[1] + b
        func main() 
        begin
            foo([1,2],2)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=ArrayType(
                                size=[2.0],
                                eleType=NumberType()
                            )    
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=NumberType()        
                        ),
                    ],
                    body= Return(
                                BinaryOp(
                                    op="+",
                                    left=ArrayCell(arr=Id("a"),
                                                idx=[NumberLiteral(1.0)]),
                                    right=Id("b")
                                )
                            )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(name=Id("foo"), 
                                    args=
                                    [
                                        ArrayLiteral([
                                            NumberLiteral(1.0),
                                            NumberLiteral(2.0)    
                                        ]), 
                                        NumberLiteral(2.0)
                                    ])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,362))
        
    def test_simple_param_case_2(self):
        '''Simple func with implicit param'''
        input = """
        func foo(bool a, number b) return a + b
        func main() 
        begin
            foo(true,2)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=BoolType()
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=NumberType()        
                        ),
                    ],
                    body= Return(
                                BinaryOp(
                                    op="+",
                                    left=Id("a"),
                                    right=Id("b")
                                )
                            )
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(name=Id("foo"), 
                                    args=
                                    [
                                        BooleanLiteral(True), 
                                        NumberLiteral(2.0)
                                    ])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,363))
    
    def test_simple_array_param_case_2(self):
        '''Simple func with implicit param'''
        input = """
        func foo(string a[3,2], number b)
        func main() 
        begin
            foo([2,3],2)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=ArrayType(
                                size=[3.0, 2.0],
                                eleType=StringType()
                            )    
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=NumberType()        
                        ),
                    ],
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(name=Id("foo"), 
                                    args=
                                    [
                                        ArrayLiteral([
                                            NumberLiteral(2.0),
                                            NumberLiteral(3.0)    
                                        ]), 
                                        NumberLiteral(2.0)
                                    ])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,364))    
    
    def test_complex_array_param(self):
        '''Simple func with array params'''
        input = """
        func foo(string a[2,3,4], bool b[2,3]) return
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=ArrayType(
                                size=[2.0,3.0,4.0],
                                eleType=StringType()
                            )    
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=ArrayType(
                                size=[2.0,3.0],
                                eleType=BoolType()
                            )
                        ),
                    ],
                    body=Return()
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(name=Id("foo"), 
                                    args=
                                    [
                                        NumberLiteral(2.0), 
                                        NumberLiteral(2.0)
                                    ])
                        ]
                    )
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,365))    
    
    def test_forward_decl_after_main(self):
        '''Simple func with array params'''
        input = """
        func main() 
        begin
            foo(2,2)
        end
        func foo(string a[2,3,4],bool b[2,3]) return
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(name=Id("foo"), 
                                    args=
                                    [
                                        NumberLiteral(2.0), 
                                        NumberLiteral(2.0)
                                    ])
                        ]
                    )
                ),
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=ArrayType(
                                size=[2.0,3.0,4.0],
                                eleType=StringType()
                            )    
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=ArrayType(
                                size=[2.0,3.0],
                                eleType=BoolType()
                            )
                        ),
                    ],
                    body=Return()
                ),
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,366))   
        
    def test_forward_decl_param(self):
        '''Simple forward func with array params'''
        input = """
        func foo(string a[2,3,4],bool b[2,3])
        func main() 
        begin
            foo(2,2)
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("foo"),
                    param=[
                        VarDecl(
                            name=Id("a"),
                            varType=ArrayType(
                                size=[2.0,3.0,4.0],
                                eleType=StringType()
                            )    
                        ),
                        VarDecl(
                            name=Id("b"),
                            varType=ArrayType(
                                size=[2.0,3.0],
                                eleType=BoolType()
                            )
                        ),
                    ],
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(name=Id("foo"), 
                                    args=
                                    [
                                        NumberLiteral(2.0), 
                                        NumberLiteral(2.0)
                                    ])
                        ]
                    )
                ),
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,367))   
    
    def test_func_call_expr(self):
        '''Function expression'''
        input = """
        func main() 
        begin
            var a <- foo(2,2)
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
                                name=Id("a"),
                                modifier="var",
                                varInit=CallExpr(name=Id("foo"), 
                                                args=[NumberLiteral(2.0),NumberLiteral(2.0)])  
                            ),
                        ]
                    )
                ),
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,368))  
    
    def test_func_call_stmt(self):
        '''function statement'''
        input = """
        func main() 
        begin
            dynamic a <- 2
            foo(a)
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
                                name=Id("a"),
                                modifier="dynamic",
                                varInit=NumberLiteral(2.0)
                            ),
                            CallStmt(name=Id("foo"), args=[Id("a")])
                        ]
                    )
                ),
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,369))  
    
    def test_func_in_func_call(self):
        '''Simple forward func with missing param'''
        input = """
        func main() 
        begin
            foo(foo(2))
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            CallStmt(
                                name=Id("foo"),
                                args=[CallExpr(name=Id("foo"), args=[NumberLiteral(2.0)])]
                            )
                        ]
                    )
                ),
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,370))  
    
#     #*Case 271- 280: complex var decl and assignment
    def test_long_var_decl(self):
        '''Long array, var declare'''
        input = """
        var a <- 2*3-foo()+b[2,3]
        func main() 
        begin
            number b[2.e45,3] <- [2,a*2/f,foo(2),true,[2,3]]
        end
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    modifier="var",
                    varInit=BinaryOp(
                        op='+',
                        left=BinaryOp(                          
                            op="-",
                            left=BinaryOp(
                                op="*",
                                left=NumberLiteral(2.0),
                                right=NumberLiteral(3.0)    
                            ),
                            right=CallExpr(name=Id("foo"), args=[])
                        ),
                        right=ArrayCell(
                            arr=Id("b"),
                            idx=[
                                NumberLiteral(2.0),
                                NumberLiteral(3.0)
                            ]
                        )
                    ),
                ),
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            VarDecl(
                                name=Id("b"),
                                varType=ArrayType(
                                    size=[2.0e45,3.0],
                                    eleType=NumberType()
                                ),
                                varInit=ArrayLiteral(
                                    [
                                        NumberLiteral(2.0),
                                        BinaryOp(
                                            op="/",
                                            left=BinaryOp(
                                                op="*",
                                                left=Id("a"),
                                                right=NumberLiteral(2.0)
                                            ),
                                            right=Id("f")
                                        ),
                                        CallExpr(name=Id("foo"), args=[NumberLiteral(2.0)]),
                                        BooleanLiteral(True),
                                        ArrayLiteral([
                                            NumberLiteral(2.0),
                                            NumberLiteral(3.0)
                                        ])
                                    ]
                                )
                            )
                        ]
                    )
                    
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,371))
        
    def test_dynamic_var_no_assign(self):
        '''Long implicit type var declare'''
        input = """
        dynamic a
        """
        expected = str(Program(
            [
                VarDecl(
                    name=Id("a"),
                    modifier="dynamic"
                )
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,372))
    
    def test_elem_expr_assignment(self):
        '''Long implicit type var declare'''
        input = """
        func main() 
        begin
            b[a,foo(2)] <- b[foo(2),a]
        end
        """
        expected = str(Program(
            [
                FuncDecl(
                    name=Id("main"),
                    param=[],
                    body=Block(
                        [
                            Assign(
                                lhs=ArrayCell(
                                    arr=Id("b"),
                                    idx=[
                                        Id("a"),
                                        CallExpr(name=Id("foo"), args=[NumberLiteral(2.0)])
                                    ]
                                ),
                                rhs=ArrayCell(
                                    arr=Id("b"),
                                    idx=[
                                        CallExpr(name=Id("foo"), args=[NumberLiteral(2.0)]),
                                        Id("a"),
                                    ]
                                ),
                            )
                        ]
                    )
                ),
                
            ]
        ))
        self.assertTrue(TestAST.test(input,expected,373))
    
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
#         expected = str(Program([]))
#         self.assertTrue(TestAST.test(input,expected,299))
    
    # def test_empty_program(self):
    #     '''Empty program'''
    #     input = """"""
    #     expected = str(Program([]))
    #     self.assertTrue(TestAST.test(input,expected,400))
    