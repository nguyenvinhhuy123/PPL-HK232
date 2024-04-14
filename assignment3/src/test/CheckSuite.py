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
    
    # def test_normal_flow(self):
    #     input = """
    #     number a <- 2
    #     func main() return 1
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 402))
    # def test_normal_flow_with_function(self):
    #     input = """
    #     func foo(number a) return a
    #     number a <- 2
    #     func main() return 1
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 403))
    
    # def test_must_in_loop(self):
    #     input = """
    #     number a <- 2
    #     func main() 
    #     begin
    #         continue
    #     end
    #     """
    #     expect = str(MustInLoop(Continue()))
    #     self.assertTrue(TestChecker.test(input, expect, 404))
    
    # def test_type_mismatch_stmt(self):
    #     input = """
    #     number a <- 2
    #     func main() 
    #     begin
    #         a <- "b"
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(lhs=Id("a"), rhs=StringLiteral("b"))
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 405))
    
    # def test_type_mismatch_expr(self):
    #     input = """
    #     number a <- 2*"b"
    #     func main() 
    #     begin
    #         return 1
    #     end
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp(op="*",left=NumberLiteral(2.0), right=StringLiteral("b"))
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 406))
    
    # def test_type_cannot_inferred(self):
    #     input = """
    #     dynamic a
    #     dynamic b
    #     func main() 
    #     begin
    #         a <- b
    #     end
    #     """
    #     expect = str(TypeCannotBeInferred(
    #         Assign(lhs=Id("a"), rhs=Id("b"))
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 407))
    
    # def test_no_definition(self):
    #     input = """
    #     dynamic a
    #     dynamic b
    #     func foo()
    #     func main() 
    #     begin
    #         a <- b
    #     end
    #     """
    #     expect = str(NoDefinition("foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 408))
    
    # def test_redeclare(self):
    #     input = """
    #     number a <- 2
    #     number a <- 3
    #     func main() 
    #     begin
    #         return 1
    #     end
    #     """
    #     expect = str(Redeclared(
    #         kind=Variable(),
    #         name="a"
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 409))
    
    # def test_undeclare(self):
    #     input = """
    #     func main() 
    #     begin
    #         a <- 2
    #     end
    #     """
    #     expect = str(Undeclared(
    #         kind=Identifier(),
    #         name="a"
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 410))
    
    # #*Case 411-420: function_declared test
    # def test_forward_define(self):
    #     input = """
    #     func foo(number a)
    #     number a <- 2
    #     func main() return 1
    #     func foo(number a) return a
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 411))
    # def test_forward_define_err_wrong_param(self):
    #     input = """
    #     func foo(number a)
    #     number a <- 2
    #     func main() return 1
    #     func foo(number b) return b
    #     """
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 412))
    
    # def test_forward_define_err_more_param(self):
    #     input = """
    #     func foo(number a)
    #     number a <- 2
    #     func main() return 1
    #     func foo(number b,number a) return b
    #     """
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 413))
    
    # def test_err_redeclare(self):
    #     input = """
    #     func foo(number a) return a
    #     number a <- 2
    #     func main() return 1
    #     func foo(number a) return a+1
    #     """
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 414))
    
    # def test_forward_redeclare(self):
    #     input = """
    #     func foo(number a)
    #     func foo(number a)
    #     number a <- 2
    #     func main() return 1
    #     func foo(number a) return a+1
    #     """
    #     expect = str(Redeclared(Function(),"foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 415))
    
    # def test_main_redeclare(self):
    #     input = """
    #     number a <- 2
    #     func main() return 1
    #     func main(number a) return a+1
    #     """
    #     expect = str(Redeclared(Function(),"main"))
    #     self.assertTrue(TestChecker.test(input, expect, 416))
    
    # def test_no_definition(self):
    #     input = """
    #     number a <- 2
    #     func main() return 1
    #     func foo(number a)
    #     """
    #     expect = str(NoDefinition("foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 417))
        
    # def test_no_definition_main(self):
    #     input = """
    #     number a <- 2
    #     func main() 
    #     """
    #     expect = str(NoDefinition("main"))
    #     self.assertTrue(TestChecker.test(input, expect, 418))
    
    # def test_main_with_param(self):
    #     input = """
    #     number a <- 2
    #     func main(number a) return a 
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expect, 419))
    
    # def test_main_forward_declare(self):
    #     input = """
    #     number a <- 2
    #     func main()
    #     func main() return 2
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 420))
    
    # #*Case 421-430: Var Declaration test
    
    # def test_var_re_declare(self):
    #     input = """
    #     number a <- 2
    #     number a <- 3
    #     func main() return 2
    #     """
    #     expect = str(Redeclared(Variable(),"a"))
    #     self.assertTrue(TestChecker.test(input, expect, 421))
    
    # def test_var_re_declare_inner_scope(self):
    #     input = """
    #     number a <- 2

    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 422))
        
    # def test_param_re_declare(self):
    #     input = """
    #     func foo(number a, number a)
    #     begin 
    #         return a+a
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = str(Redeclared(Parameter(), "a"))
    #     self.assertTrue(TestChecker.test(input, expect, 423))

    # def test_param_re_declare_same_name_with_func(self):
    #     input = """
    #     func foo(number foo)
    #     begin 
    #         return a+a
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = str(Redeclared(Parameter(), "foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 424))
    
    # def test_var_redeclare_in_inner_scope_same_name_with_func(self):
    #     input = """
    #     func foo(number a)
    #     begin 
    #         bool foo <- true
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 425))
    
    # def test_var_redeclare_in_inner_scope_same_name_with_param(self):
    #     input = """
    #     func foo(number a)
    #     begin 
    #         bool a <- true
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 426))
    
    # def test_var_redeclare_in_nested_inner(self):
    #     input = """
    #     func foo(number a)
    #     begin 
    #         bool a <- true
    #         begin 
    #             string a <- "hehe"
    #             begin 
    #                 string a <- "hehehe"
    #             end
    #         end
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 427))
    
    #*Case 431-440: Type inference for variables
    # def test_var_type_inference(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number a <- b
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 431))