import unittest
from TestUtils import TestLexer

UNCLOSED_STRING = "Unclosed String: " 
ERROR_CHAR = "Error Token "
ILLEGAL_ESC= "Illegal Escape In String: "

class LexerSuite(unittest.TestCase):
    """
    Test function template:
    def test_TEST_NAME(self):
        '''Small description here'''
        input = ""
        expected = ",<EOF>"
        self.assertTrue(TestLexer.test(input,expected,test_ID))
    """
    #*Case 101-110: Simple test for tokens
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"Yanxi Palace - 2018\"","Yanxi Palace - 2018,<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("\"isn\\\'t\"","isn\\\'t,<EOF>",102))
        
    def test_identifier(self):
        """test simple identifier"""
        self.assertTrue(TestLexer.test("_myID","_myID,<EOF>",103))
        
    def test_simple_comment_line(self):
        """Test simple comment"""
        self.assertTrue(TestLexer.test("##This is a comment\n","\n,<EOF>", 104))

    def test_simple_comment_line_at_EOF(self):
        """Test simple comment at before EOF"""
        self.assertTrue(TestLexer.test("##This is a comment","<EOF>", 105))
    
    def test_comment_between_line(self):
        input = """number a <- 3
        ##This is a comment
        string b <- "Hello"
        """
        expected = "number,a,<-,3,\n,\n,string,b,<-,Hello,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,106))
    
    def test_simple_array(self):
        input = """number _myArray[2,3]"""
        expected = "number,_myArray,[,2,,,3,],<EOF>"
        self.assertTrue(TestLexer.test(input,expected,107))
        
    def test_simple_variable_declare(self):
        """Test simple variable declare"""
        self.assertTrue(TestLexer.test(
            "var _myVar = 5",
            "var,_myVar,=,5,<EOF>",
            108
        ))
        
    def test_simple_error_token(self):
        """test simple error token input (case #) throw error token"""
        self.assertTrue(TestLexer.test("#", "Error Token #",109))
    
    def test_unclose_string(self):
        """Test unclose string error"""
        self.assertTrue(TestLexer.test("\"This string is not close", UNCLOSED_STRING + "This string is not close", 110))
    
    #*Case 111-120: Identifier recognition#
    def test_simple_identifier(self):
        """Simple ident token"""
        self.assertTrue(TestLexer.test("_myIdent", "_myIdent,<EOF>", 111))
        
    def test_identifier_with_number(self):
        """Simple ident token with number"""
        self.assertTrue(TestLexer.test("_myIdent123", "_myIdent123,<EOF>", 112))
        
    def test_complex_identifier(self):
        """Complex ident token with number and more"""
        self.assertTrue(TestLexer.test("_myIDE_nt123num", "_myIDE_nt123num,<EOF>", 113))
        
    def test_identifier_with_error_token(self):
        '''identifier with error token'''
        input = "_myError#_ident"
        expected = "_myError,Error Token #"
        self.assertTrue(TestLexer.test(input,expected,114))
        
    def test_identifier_with_number_before(self):
        '''identifier with number token before it'''
        input = "123_myiDent"
        expected = "123,_myiDent,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,115))
        
    def test_identifier_with_newline_token(self):
        '''identifier with newline_token before and after'''
        input = "\n_myIdent1\n_myIdent2" # _myIdent2_myIdent1
        expected = "\n,_myIdent1,\n,_myIdent2,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,116))
    
    def test_identifier_similar_to_keyword(self):
        '''identifier with newline_token before and after'''
        input = "dynaMic"
        expected = "dynaMic,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,117))
    
    def test_identifier_with_wrong_char_case_1(self):
        '''identifier with incorrect character !'''
        input = "_myVar!"
        expected = "_myVar," + ERROR_CHAR + "!"
        self.assertTrue(TestLexer.test(input,expected,118))
    
    def test_identifier_similar_wrong_char_case_2(self):
        '''identifier with incorrect character @'''
        input = "_myVar@"
        expected = "_myVar," + ERROR_CHAR + "@"
        self.assertTrue(TestLexer.test(input,expected,119))
    
    def test_identifier_similar_wrong_char_case_3(self):
        '''identifier with incorrect character ~'''
        input = "_myVar~"
        expected = "_myVar," + ERROR_CHAR + "~"
        self.assertTrue(TestLexer.test(input,expected,120))
    #*Case 121-130: Operation recognition
    def test_simple_assignment(self):
        '''simple assignment'''
        input = "_myVar <- 5 + 3"
        expected = "_myVar,<-,5,+,3,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,121))
    
    def test_complex_assignment(self):
        '''complex assignment'''
        input = "_myVar <- (5 + 3)*2/_myOtherVar"
        expected = "_myVar,<-,(,5,+,3,),*,2,/,_myOtherVar,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,122))
        
    def test_string_assignment(self):
        '''string assignment'''
        input = "_myVar <- \"This is my string\""
        expected = "_myVar,<-,This is my string,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,123))
        
    def test_comparison(self):
        '''simple comparison statement'''
        input = " _myVar <= 2"
        expected = "_myVar,<=,2,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,124))
        
    def test_complex_comparison(self):
        '''complex comparison statement'''
        input = "_myVar >= (2+3)*_myOther"
        expected = "_myVar,>=,(,2,+,3,),*,_myOther,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,125))

    def test_string_compare(self):
        '''string comparison statement'''
        input = "_myVar >= \"This is a compared string\""
        expected = "_myVar,>=,This is a compared string,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,126))
    
    def test_logic_operator(self):
        '''logic operator statement'''
        input = "_myLogic <- _myVar and _myOther"
        expected = "_myLogic,<-,_myVar,and,_myOther,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,127))
    
    def test_string_concat(self):
        '''string concat operator statement'''
        input = "_myLogic <- \"String number 1\" ... \"String number 2\""
        expected = "_myLogic,<-,String number 1,...,String number 2,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,128))
    
    def test_string_concat_error_token(self):
        '''string concat operator statement error token (2 dot only)'''
        input = "_myString <- \"String number 1\" .. \"String number 2\""
        expected = "_myString,<-,String number 1," + ERROR_CHAR + "."
        self.assertTrue(TestLexer.test(input,expected,129))
    
    def test_multiple_logic(self):
        '''multiple logic operator'''
        input = "_myLogic <- a and b or (num1 + num2 >= 0)"
        expected = "_myLogic,<-,a,and,b,or,(,num1,+,num2,>=,0,),<EOF>"
        self.assertTrue(TestLexer.test(input,expected,130))
    
    #*Case 131 -> 140: Keyword recognition#
    def test_simple_keyword(self):
        '''Simple keyword recognition: Case dynamic,var,true'''
        input = "dynamic var true"
        expected = "dynamic,var,true,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,131))
        
    def test_2_keyword_with_no_space(self):
        '''2 kw with no space, suppose to recognise as id'''
        input = "truevar"
        expected = "truevar,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,132))
        
    def test_more_keyword(self):
        '''More keyword in 1 input'''
        input = "true false func number bool if for elif"
        expected = "true,false,func,number,bool,if,for,elif,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,133))
    
    def test_keyword_in_multiline(self):
        '''Same with 133 but have a newline'''
        input = """true false func number 
        bool if for elif"""
        expected = "true,false,func,number,\n,bool,if,for,elif,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,134))
    
    def test_keyword_in_string(self):
        '''Keyword include in a string token'''
        input = "\"This string have keyword: dynamic var true \""
        expected = "This string have keyword: dynamic var true ,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,135))
    
    def test_keyword_with_uppercase(self):
        '''Keyword with uppercase, expected ids, should look at this with modified ultils for correctness'''
        input = "True vaR faLse"
        expected = "True,vaR,faLse,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,136))
    
    def test_more_keyword_case_1(self):
        '''More keyword recognition'''
        input = "var a <- true"
        expected = "var,a,<-,true,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,137))
    
    def test_more_keyword_case_2(self):
        '''More keyword recognition'''
        input = "if (a) do(B)"
        expected = "if,(,a,),do,(,B,),<EOF>"
        self.assertTrue(TestLexer.test(input,expected,138))
        
    def test_more_keyword_case_3(self):
        '''More keyword recognition'''
        input = "for i until i < 1 by -1"
        expected = "for,i,until,i,<,1,by,-,1,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,139))
    
    def test_more_keyword_case_4(self):
        '''More keyword recognition'''
        input = "dymanic a[2,3]"
        expected = "dymanic,a,[,2,,,3,],<EOF>"
        self.assertTrue(TestLexer.test(input,expected,140))
    
    #*Case 141-150: test for strings 
    def test_string_err(self):
        '''Unclose string cases'''
        self.assertTrue(TestLexer.test("\"\'\"", UNCLOSED_STRING + "\'\"", 141))
        
    def test_edge_case(self):
        '''edge case mentions in forum'''
        input = "\" \' \""
        expected = " \' ,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,142))
        
    def test_escape_sequence(self):
        '''test escape sequence'''
        input = "\"This string has multiple allowed escape seq: \\t \\b ,\\n \""
        expected = "This string has multiple allowed escape seq: \\t \\b ,\\n ,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,143))
        
    def test_escape_sequence_err(self):
        '''test illegal escape sequence'''
        input = "\"This string has multiple allowed escape seq: \\a \\b ,\\n \""
        expected =  ILLEGAL_ESC + "This string has multiple allowed escape seq: \\a"
        self.assertTrue(TestLexer.test(input,expected,144))
    
    def test_unclose_string_edge_case(self):
        '''test illegal escape sequence'''
        input = "\" \\\\'\""
        expected = UNCLOSED_STRING + " \\\\'\""
        self.assertTrue(TestLexer.test(input,expected,145))
        
    def test_escape_edge_case(self):
        '''test escape sequence edge case'''
        input = "\"\\'\""
        expected =  "\\',<EOF>"
        self.assertTrue(TestLexer.test(input,expected,146))
    
    def test_multiline_string(self):
        '''Multiline string'''
        #!Weird output give 2 newline char instead of 1?
        input = """\"This is a\nmultiline string\ntestcase with a tab:\n\\t\""""
        expected = """This is a\nmultiline string\ntestcase with a tab:\n\\t,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,147))
        
    def test_complex_long_string(self):
        """Complex string with multiple complex literals"""
        input = """\"This string '"'" is \\t \\b pretty complex tho!!?\""""
        expected = """This string '"'" is \\t \\b pretty complex tho!!?,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,148))
    
    def test_complex_string_illegal_escape(self):
        """Complex string with multiple complex literals and an error escape"""
        input = """\"This string '"'" is \\a \\b pretty complex tho!!?\""""
        expected = ILLEGAL_ESC + """This string '"'" is \\a"""
        self.assertTrue(TestLexer.test(input,expected,149))
        
    def test_complex_string_unclosed_string(self):
        """Complex string with multiple complex literals and unclose error"""
        input = """\"This string '"'" is \\t \\b pretty complex tho!!?"""
        expected = UNCLOSED_STRING + """This string '"'" is \\t \\b pretty complex tho!!?"""
        self.assertTrue(TestLexer.test(input,expected,150))
    
    #*Case 151-160: Number recognition
    def test_simple_number(self):
        '''Simple number test'''
        input = "123456"
        expected = "123456,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,151))
        
    def test_simple_number_before_identifier(self):
        '''Simple number test before an ident'''
        input = "123_var4"
        expected = "123,_var4,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,152))
        
    def test_simple_float(self):
        '''Simple float number'''
        input = "0123.4560"
        expected = "0123.4560,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,153))
        
    def test_simple_expo(self):
        '''Simple expo number'''
        input = "0123e456"
        expected = "0123e456,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,154))
        
    def test_simple_expo_uppercase(self):
        '''Simple expo number, uppercase, subtract sign'''
        input = "0123E-456"
        expected = "0123E-456,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,155))
    
    def test_complex_number(self):
        '''Complex number'''
        input = "0123.456E798"
        expected = "0123.456E798,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,156))  

    def test_complex_number_edge_case(self):
        '''Complex number edge case'''
        input = "0123.E798"
        expected = "0123.E798,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,157))   
    
    def test_complex_number_edge_case_no_digit(self):
        '''Complex number edge case 2 with no decimal and expo digit'''
        '''Suppose to have 3 token because exponential should have at least 1 digit'''
        input = "0123.E+"
        expected = "0123.,E,+,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,158))  
    
    def test_complex_number_error(self):
        '''Complex number error case'''
        input = "0123.#"
        expected = "0123.," + ERROR_CHAR + "#"
        self.assertTrue(TestLexer.test(input,expected,159))   
    
    def test_complex_number_before_id(self):
        '''Complex number error case'''
        input = "0123.E-1A"
        expected = "0123.E-1,A,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,160))  
    
    #*Case 161-170:Test separator
    def test_simple_bracket(self):
        '''Simple bracket token'''
        input = "a[1]"
        expected = "a,[,1,],<EOF>"
        self.assertTrue(TestLexer.test(input,expected,161))
    
    def test_multiple_bracket(self):
        '''Multiple bracket token'''
        input = "a[b[1],c[2]]"
        expected = "a,[,b,[,1,],,,c,[,2,],],<EOF>"
        self.assertTrue(TestLexer.test(input,expected,162))
    
    def test_simple_paren(self):
        '''Simple bracket token'''
        input = "(num1 + num2)"
        expected = "(,num1,+,num2,),<EOF>"
        self.assertTrue(TestLexer.test(input,expected,163))
    
    def test_multiple_paren(self):
        '''Multiple bracket token'''
        input = "((num1 + (num2 + num3)))"
        expected = "(,(,num1,+,(,num2,+,num3,),),),<EOF>"
        self.assertTrue(TestLexer.test(input,expected,164))
    
    def test_multiple_paren_bracket(self):
        '''Multiple bracket token'''
        input = "a[b[2,3], (num1+2(num3+num4))]"
        expected = "a,[,b,[,2,,,3,],,,(,num1,+,2,(,num3,+,num4,),),],<EOF>"
        self.assertTrue(TestLexer.test(input,expected,165))
    
    def test_newline(self):
        """simple newline token"""
        input = "\n"
        expected = "\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,166))
    
    def test_multiple_newline(self):
        """multiple newline token"""
        input = "\n\n\n"
        expected = "\n,\n,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,167))
    
    def test_window_newline(self):
        """window newline token CRLF and CR -> to LF"""
        input = """\ra"""
        expected = "\n,a,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,168))
        
    def test_window_multiple_newline(self):
        """multiple newline token"""
        input = """\r\n\na
        """
        expected = "\n,\n,\n,a,\n,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,169))
    
    def test_paren_error(self):
        """multiple newline token"""
        input = """{a + b = 3}"""
        expected = ERROR_CHAR + "{"
        self.assertTrue(TestLexer.test(input,expected,170))
    
    #*Case 171-185: test_error_character
    def test_error_character_case_1(self):
        """case 1: !"""
        input = """!"""
        expected = ERROR_CHAR + "!"
        self.assertTrue(TestLexer.test(input,expected,171))
    
    def test_error_character_case_2(self):
        """case 2: @"""
        input = """@"""
        expected = ERROR_CHAR + "@"
        self.assertTrue(TestLexer.test(input,expected,172))
    
    def test_error_character_case_3(self):
        """case 3: #"""
        input = """#"""
        expected = ERROR_CHAR + "#"
        self.assertTrue(TestLexer.test(input,expected,173))
        
    def test_error_character_case_4(self):
        """case 4: $"""
        input = """$"""
        expected = ERROR_CHAR + "$"
        self.assertTrue(TestLexer.test(input,expected,174))
        
    def test_error_character_case_5(self):
        """case 5: |"""
        input = """|"""
        expected = ERROR_CHAR + "|"
        self.assertTrue(TestLexer.test(input,expected,175))
        
    def test_error_character_case_6(self):
        """case 6: `"""
        input = """`"""
        expected = ERROR_CHAR + "`"
        self.assertTrue(TestLexer.test(input,expected,176))
        
    def test_error_character_case_7(self):
        """case 7: ~"""
        input = """~"""
        expected = ERROR_CHAR + "~"
        self.assertTrue(TestLexer.test(input,expected,177))
        
    def test_error_character_case_8(self):
        """case 8: ."""
        input = """."""
        expected = ERROR_CHAR + "."
        self.assertTrue(TestLexer.test(input,expected,178))
        
    def test_error_character_case_9(self):
        """case 9: ?"""
        input = """?"""
        expected = ERROR_CHAR + "?"
        self.assertTrue(TestLexer.test(input,expected,179))
    
    def test_error_character_case_10(self):
        """case 10: &"""
        input = """&"""
        expected = ERROR_CHAR + "&"
        self.assertTrue(TestLexer.test(input,expected,180))
    
    def test_error_character_case_11(self):
        """case 10: ^"""
        input = """^"""
        expected = ERROR_CHAR + "^"
        self.assertTrue(TestLexer.test(input,expected,181))
        
    def test_error_character_case_12(self):
        """case 12: :"""
        input = """:"""
        expected = ERROR_CHAR + ":"
        self.assertTrue(TestLexer.test(input,expected,182))
        
    def test_error_character_case_13(self):
        """case 13: \\"""
        input = """\\"""
        expected = ERROR_CHAR + "\\"
        self.assertTrue(TestLexer.test(input,expected,183))
        
    def test_error_character_case_14(self):
        """case 13: {}"""
        input = """{}"""
        expected = ERROR_CHAR + "{"
        self.assertTrue(TestLexer.test(input,expected,184))
        
    def test_error_character_case_15(self):
        """case 13: \a"""
        input = """\a"""
        expected = ERROR_CHAR + "\a"
        self.assertTrue(TestLexer.test(input,expected,185))
        
    #*Case 186-200: random test case
    def test_more_multiple_newline(self):
        self.assertTrue(TestLexer.test("a\n\n\n#","a,\n,\n,\n,Error Token #",186))  
    
    def test_array_value(self):
        input = """[[1, 2], [4, 5], [3, 5]]"""
        expected = """[,[,1,,,2,],,,[,4,,,5,],,,[,3,,,5,],],<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,187))
    
    def test_more_array(self):
        input = """a[1,2,foo()]"""
        expected = """a,[,1,,,2,,,foo,(,),],<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,188))
    
    def test_more_identifier_1(self):
        input = """_aoiwnidqnf08"""
        expected = """_aoiwnidqnf08,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,189))
    
    def test_more_identifier_2(self):
        input = """_aotrueiwnidqnf08"""
        expected = """_aotrueiwnidqnf08,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,190))
        
    def test_program_like_sequence(self):
        """Simple program like stream of sequence"""
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
        expected = """
,func,foo,(,number,a,),
,begin,
,a,<-,a,+,3,
,string,b,<-,value of a is:,+,toString,(,a,),
,end,
,func,main,(,),
,begin,
,number,target,<-,5,
,foo,(,target,),
,end,
,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,191))
    
    def test_unclosed_string_1(self):
        input = """\"qwifmoqi\'\'\""""
        expected = UNCLOSED_STRING + "qwifmoqi\'\'\""
        self.assertTrue(TestLexer.test(input,expected,192))
    
    def test_unclosed_string_2(self):
        input = """\"qwifmoqi\'\"\'\"\'"""
        expected = UNCLOSED_STRING + "qwifmoqi\'\"\'\"\'"
        self.assertTrue(TestLexer.test(input,expected,193))
    
    def test_more_comment(self):
        input = """##Comment iz riel\n"""
        expected = """\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,194))
    
    def test_more_comment_weird_char(self):
        input = """##Comment iz riel\a\b\n"""
        expected = """\n,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,195))
        
    def test_illegal_esc_1(self):
        input = """\"\\a\""""
        expected = ILLEGAL_ESC + "\\a"
        self.assertTrue(TestLexer.test(input,expected,196))
    
    def test_illegal_esc_2(self):
        input = """\"qwnfqwiofnqowif\\ lmao\""""
        expected = ILLEGAL_ESC + """qwnfqwiofnqowif\\ """
        self.assertTrue(TestLexer.test(input,expected,197))
    
    def test_string_char_edge_case_2(self):
        input = """\"\' \""""
        expected = """\' ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,198))
    
    def test_string_char_edge_case_3(self):
        input = """\"\\\' \""""
        expected = """\\\' ,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,199))
        
    def test_empty_input(self):
        input = """"""
        expected = """<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,200))