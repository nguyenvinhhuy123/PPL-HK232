import unittest
from TestUtils import TestChecker
from AST import *
from main.zcode.checker.StaticError import *
from main.zcode.utils.AST import *

SUCCESSFUL = ""
class CheckSuite(unittest.TestCase):
    #*Case 401 - 410: Simple exception check
    # def test_no_entry_point(self):
    #     input = """
    #     number a <- 2
    #     """
    #     expect = str(NoEntryPoint())
    #     self.assertTrue(TestChecker.test(input, expect, 401))
    
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
    #     number b
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
    
    # def test_build_in_redeclare(self):
    #     input = """
    #     number a <- 2
    #     func main() return 1
    #     func writeBool(number a) return a
    #     """
    #     expect = str(Redeclared(Function(), "writeBool"))
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
    #         return 1
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = SUCCESSFUL
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
    
    # def test_var_redeclare_in_if(self):
    #     input = """
    #     func foo(number a)
    #     begin 
    #         number b <- 2
    #         if (a < b) number b <- 3
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = str(Redeclared(Variable(), "b"))
    #     self.assertTrue(TestChecker.test(input, expect, 428))
    
    # def test_var_redeclare_in_for(self):
    #     input = """
    #     func foo(number a)
    #     begin 
    #         number b <- 2
    #         bool c <- true
    #         for b until b > 10 by 2
    #             bool c <- false
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = str(Redeclared(Variable(), "c"))
    #     self.assertTrue(TestChecker.test(input, expect, 429))
    
    # def test_var_redeclare_in_if_and_for_with_block(self):
    #     input = """
    #     func foo(number a)
    #     begin 
    #         number b <- 2
    #         bool c <- true
    #         if (a < b) begin 
    #             number b <- 3
    #         end
    #         for b until b > 10 by 2
    #         begin
    #             bool c <- false
    #         end
    #     end
    #     func main()
    #     begin
    #         number a <- 3
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 430))
    
    # #*Case 431-440: Type inference for variables
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
    
    # def test_type_mismatch_in_stmt_after_inferred(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number a <- b
    #         b <- "string"
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(Id("b"),
    #         StringLiteral("string"))
    #         ))
    #     self.assertTrue(TestChecker.test(input, expect, 432))
    
    # def test_type_mismatch_in_expr_after_inferred(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number a <- b
    #         string c <- b..."str"
    #     end
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         BinaryOp(
    #             op="...",
    #             left=Id("b"),
    #             right=StringLiteral("str")
    #         )
    #         ))
    #     self.assertTrue(TestChecker.test(input, expect, 433))
    
    # def test_type_inferred_success_in_binop(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number a <- b + 2
    #         b <- 2
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 434))
        
    # def test_type_inferred_failed_in_binop(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number a <- b + 2
    #         b <- "str"
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(
    #         Id("b"),
    #         StringLiteral("str")
    #     )))
    #     self.assertTrue(TestChecker.test(input, expect, 435))
        
    # def test_type_inferred_success_in_unop(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number a <- -b
    #         b <- 2
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 436))
        
    # def test_type_inferred_failed_in_unop(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         bool a <- not b
    #         b <- "str"
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(
    #         Id("b"),
    #         StringLiteral("str")
    #     )))
    #     self.assertTrue(TestChecker.test(input, expect, 437))

    # #TODO: Recheck array lit related tests
    # def test_type_inferred_success_array_type(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number x[2,2]<- b
    #         b <- [[2,3],[2,3]]
    #         dynamic c
    #         bool y[2]<- c
    #         c <- [true,false]
    #         dynamic d
    #         string z[1,1,1]<- d
    #         d <- [[["hehe"]]]
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 438))
        
    # def test_type_inferred_failed_ele_type_mismatch(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         number x[2,2]<- b
    #         b <- [[true, true], [true, true]]
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(Assign(
    #         Id("b"),
    #         ArrayLiteral([ArrayLiteral([BooleanLiteral(True), BooleanLiteral(True)])
    #                     , ArrayLiteral([BooleanLiteral(True), BooleanLiteral(True)])])
    #     )))
    #     self.assertTrue(TestChecker.test(input, expect, 439))
        
    # def test_type_inferred_failed_cannot_inferred_in_array(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         dynamic c
    #         b <- [[c, c], [c, c]]
    #     end
    #     """
    #     expect = str(TypeCannotBeInferred(Assign(
    #         Id("b"),
    #         ArrayLiteral([ArrayLiteral([Id("c"), Id("c")])
    #                     , ArrayLiteral([Id("c"), Id("c")])])
    #     )))
    #     self.assertTrue(TestChecker.test(input, expect, 440))
    
    # #*Case 441-450: Type inference for function
    # def test_func_type_inferred_in_call_expr(self):
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         number a <- foo()
    #     end
    #     func foo () return 2
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 441))

    # def test_func_type_inferred_failed_type_mismatch(self):
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         number a <- foo()
    #     end
    #     func foo () return true
    #     """
    #     expect = str(TypeMismatchInStatement(Return(BooleanLiteral(True))))
    #     self.assertTrue(TestChecker.test(input, expect, 442))
    
    # def test_func_type_inferred_failed_void_type_mismatch(self):
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         number a <- foo()
    #     end
    #     func foo () return
    #     """
    #     expect = str(TypeMismatchInStatement(Return()))
    #     self.assertTrue(TestChecker.test(input, expect, 443))
    
    # def test_func_type_multiple_return(self):
    #     input = """
    #     func foo(bool c)
    #     begin
    #         if (c) return 2
    #         else return 3
    #     end
    #     func main()
    #     begin
    #         number a <- foo(true)
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 444))
    
    # def test_func_type_failed_multiple_return(self):
    #     input = """
    #     func foo(bool c)
    #     begin
    #         if (c) return 2
    #         else return true
    #     end
    #     func main()
    #     begin
    #         number a <- foo(true)
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #             Return(BooleanLiteral(True))
    #         ))
    #     self.assertTrue(TestChecker.test(input, expect, 445))
    
    # def test_func_expr_void_type_mismatch(self):
    #     input = """
    #     func foo(bool c)
    #     begin
    #         if (c) c <- true
    #     end
    #     func main()
    #     begin
    #         bool a
    #         a <- foo(true)
    #     end
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         CallExpr(Id("foo"), [BooleanLiteral(True)]
    #     )))
    #     self.assertTrue(TestChecker.test(input, expect, 446))
    
    # def test_func_stmt_non_void_type_mismatch(self):
    #     input = """
    #     func foo(bool c)
    #     begin
    #         return c
    #     end
    #     func main()
    #     begin
    #         foo(true)
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         CallStmt(Id("foo"), [BooleanLiteral(True)]
    #     )))
    #     self.assertTrue(TestChecker.test(input, expect, 447))

    # def test_func_type_inferred_in_call_stmt(self):
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         foo()
    #     end
    #     func foo () return
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 448))
    
    # def test_func_type_inferred_in_call_stmt_func_no_return(self):
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         foo()
    #     end
    #     func foo() 
    #     begin
    #         number a <- 2
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 449))

    # def test_func_type_inferred_in_call_stmt_fail_return_non_void(self):
    #     input = """
    #     func foo()
    #     func main()
    #     begin
    #         foo()
    #     end
    #     func foo() return 2
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Return(NumberLiteral(2.0))
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 450))
    
    
    # #*Case 451-455: If stmt type check and type inference
    # def test_if_normal_flow(self):
    #     input = """
    #     func main()
    #     begin
    #         if (2 > 3) writeString("a")
    #         elif (3 > 4) writeString("b")
    #         else writeString("b")
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 451))
    
    # def test_if_expr_is_not_bool(self):
    #     input = """
    #     func main()
    #     begin
    #         if (2+ 3) writeString("a")
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         If(
    #             expr=BinaryOp("+", 
    #                         NumberLiteral(2.0),
    #                         NumberLiteral(3.0)),
    #             thenStmt=CallStmt(Id("writeString"), 
    #                             [StringLiteral("a")]),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 452))
    
    # def test_if_expr_type_inference(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         if (a) writeString("a")
    #         a <- 2
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(
    #             Id("a"),
    #             NumberLiteral(2.0)
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 453))
    
    # def test_elif_expr_type_is_not_bool(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         if (a) writeString("a")
    #         elif (2 + 3) writeString("b")
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         If(
    #             expr=Id("a"),
    #             thenStmt=CallStmt(Id("writeString"), 
    #                             [StringLiteral("a")]),
    #             elifStmt=[
    #                     (
    #                     BinaryOp("+", 
    #                         NumberLiteral(2.0),
    #                         NumberLiteral(3.0)),
    #                     CallStmt(Id("writeString"), 
    #                             [StringLiteral("b")]),
    #                     )
    #                 ]
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 454))
    
    # def test_elif_expr_type_inference(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         if (2 > 3) writeString("a")
    #         elif (a) writeString("b")
    #         a <- 2
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(
    #             Id("a"),
    #             NumberLiteral(2.0)
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 455))
    
    # #*Case 456-465: For stmt type check and type inference
    
    # def test_for_normal_flow(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         for a until a > 10 by a 
    #         writeNumber(a)
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 456))

    # def test_for_until_condition_not_bool(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         for a until a by a 
    #         writeNumber(a)
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         For(
    #             Id("a"),
    #             Id("a"),
    #             Id("a"),
    #             CallStmt(Id("writeNumber"), [Id("a")]),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 457))
    
    # def test_for_var_is_not_number_type(self):
    #     input = """
    #     func main()
    #     begin
    #         bool a
    #         for a until a > 10 by 1 
    #         writeNumber(a)
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         For(
    #             Id("a"),
    #             BinaryOp(">", Id("a"), NumberLiteral(10.0)),
    #             NumberLiteral(1.0),
    #             CallStmt(Id("writeNumber"), [Id("a")]),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 458))
    
    # def test_for_update_expr_is_not_number_type(self):
    #     input = """
    #     func main()
    #     begin
    #         number a
    #         for a until a > 10 by a = 1
    #         writeNumber(a)
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         For(
    #             Id("a"),
    #             BinaryOp(">", Id("a"), NumberLiteral(10.0)),
    #             BinaryOp("=", Id("a"), NumberLiteral(1.0)),
    #             CallStmt(Id("writeNumber"), [Id("a")]),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 459))
    
    # def test_for_type_inference(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         dynamic b
    #         dynamic c
    #         for a until b by c
    #         writeNumber(a)
    #         a <- 1
    #         b <- true
    #         c <- 2
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 460))
    
    # def test_for_type_inference_failed_for_var_not_var(self):
    #     input = """
    #     func foo() return 1
    #     func main()
    #     begin
    #         dynamic a
    #         dynamic b
    #         dynamic c
    #         for foo until b by c
    #         writeNumber(a)
    #         a <- 1
    #         b <- true
    #         c <- 2
    #     end
    #     """
    #     expect = str(Undeclared(Identifier(),"foo"))
    #     self.assertTrue(TestChecker.test(input, expect, 461))
    
    # def test_for_type_inference_failed_for_var_not_number(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         dynamic b
    #         dynamic c
    #         for a until b by c
    #         writeNumber(a)
    #         a <- true
    #         b <- true
    #         c <- 2
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(
    #             Id("a"),
    #             BooleanLiteral(True),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 462))
        
    # def test_for_type_inference_failed_for_condExpr_not_bool(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         dynamic b
    #         dynamic c
    #         for a until b by c
    #         writeNumber(a)
    #         a <- 1
    #         b <- 2
    #         c <- 2
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #          Assign(
    #             Id("b"),
    #             NumberLiteral(2.0),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 463))
    
    # def test_for_type_inference_failed_for_update_not_number(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         dynamic b
    #         dynamic c
    #         for a until b by c
    #         writeNumber(a)
    #         a <- 1
    #         b <- true
    #         c <- true
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #          Assign(
    #             Id("c"),
    #             BooleanLiteral(True),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 464))

    # def test_for_type_inference_in_body(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic a
    #         dynamic b
    #         dynamic c
    #         for a until b by c
    #             a <- 1
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 465))
        
    ##*Case 466 - 475: Type inference for array literals
    
    # def test_array_lit_type_inference(self):
    #     input = """
    #     func main()
    #     begin
    #         var a <- [[1,2],[3,4]]
    #         a <- [[1,2],[3,5]]
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 466))
    
    # def test_array_lit_type_inference_failed_wrong_ele_type(self):
    #     input = """
    #     func main()
    #     begin
    #         var a <- [[1,2],[3,4]]
    #         a <- [[true,false],[true,false]]
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(
    #             Id("a"),
    #             ArrayLiteral(
    #                 [
    #                     ArrayLiteral(
    #                         [
    #                             BooleanLiteral(True),
    #                             BooleanLiteral(False),
    #                         ],
    #                     ),
    #                     ArrayLiteral(
    #                         [
    #                             BooleanLiteral(True),
    #                             BooleanLiteral(False),
    #                         ],
    #                     ),
    #                 ],
    #             ),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 467))

    # def test_array_lit_type_inference_failed_wrong_array_dim(self):
    #     input = """
    #     func main()
    #     begin
    #         var a <- [[1,2],[3,4]]
    #         a <- [1,2]
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(
    #             Id("a"),
    #             ArrayLiteral(
    #                 [
    #                     NumberLiteral(1.0),
    #                     NumberLiteral(2.0),
    #                 ],
    #             ),
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 468))
        
    # def test_array_lit_failed_ele_not_same_type(self):
    #     input = """
    #     func main()
    #     begin
    #         var a <- [[1,true],[3,4]]
    #     end
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         ArrayLiteral(
    #             [
    #                 NumberLiteral(1.0),
    #                 BooleanLiteral(True),
    #             ]
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 469))
    
    # def test_array_lit_type_inferred_in_ele(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         var a <- [[1,b],[3,4]]
    #         b <- 2
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 470))
    
    # def test_array_lit_type_inferred_in_ele_failed(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         var a <- [[1,b],[3,4]]
    #         var c <- [[true,b],[true,true]]
    #     end
    #     """
    #     expect = str(TypeMismatchInExpression(
    #         ArrayLiteral(
    #             [
    #                 BooleanLiteral(True),
    #                 Id("b")
    #             ]
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 471))
    
    # def test_array_lit_type_inferred_in_ele_array_type_inferred(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         var a <- [b,[3,4]]
    #         b <- [2,3]
    #     end
    #     """
    #     expect = SUCCESSFUL
    #     self.assertTrue(TestChecker.test(input, expect, 472))

    # def test_array_lit_type_inferred_in_ele_array_type_inferred_failed(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         var a <- [b,[3,4]]
    #         b <- [[2,3]]
    #     end
    #     """
    #     expect = str(TypeMismatchInStatement(
    #         Assign(
    #             Id("b"),
    #             ArrayLiteral(
    #                 [ArrayLiteral(
    #                     [    
    #                         NumberLiteral(2.0),
    #                         NumberLiteral(3.0)
    #                     ]
    #                 )]
    #             )
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 473))
    
    # def test_array_lit_type_cannot_inferred_all_element_is_not_resolved(self):
    #     input = """
    #     func main()
    #     begin
    #         dynamic b
    #         var a <- [b,b]
    #     end
    #     """
    #     expect = str(TypeCannotBeInferred(
    #         VarDecl(
    #             Id("a"),
    #             None,
    #             "var",
    #             ArrayLiteral(
    #                 [
    #                     Id("b"),
    #                     Id("b"),
    #                 ]               
    #             )
    #         )
    #     ))
    #     self.assertTrue(TestChecker.test(input, expect, 474))
    
    def test_array_lit_type_cannot_inferred_element_is_void(self):
        input = """
        func foo() return
        func main()
        begin
            dynamic b
            var a <- [b,foo()]
        end
        """
        expect = str(TypeMismatchInExpression(
            CallExpr(
                Id("foo"),
                []
            )
        ))
        self.assertTrue(TestChecker.test(input, expect, 475))