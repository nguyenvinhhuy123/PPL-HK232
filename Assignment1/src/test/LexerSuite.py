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
    #*Case 101-110: Simple test for tokens#
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
        self.assertTrue(TestLexer.test("##This is a comment\n","\n,<EOF>", 106))

    def test_simple_comment_line_at_EOF(self):
        """Test simple comment at before EOF"""
        self.assertTrue(TestLexer.test("##This is a comment","<EOF>", 107))
    
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
        '''Keyword with uppercases, expected ids, should look at this with modified ultils for correctness'''
        input = "True vaR faLse"
        expected = "True,vaR,faLse,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,136))
    
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
        
    def test_escape_sequence(self):
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
        input = """\"This is a\rmultiline string\rtestcase with a tab:\r\\t\""""
        expected = """This is a\nmultiline string\ntestcase with a tab:\n\\t,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,147))
        
    def test_complex_string(self):
        """Complex string with multiple complex literals"""
        input = """\"This string '"'" is \\t \\b pretty complex tho!!?\""""
        expected = """This string '"'" is \\t \\b pretty complex tho!!?,<EOF>"""
        self.assertTrue(TestLexer.test(input,expected,148))
    
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
    
    #*Case 161-170
    #*Case 181-190: test case for edge case in forum.
    
    #*Case 191-200: test complex sequence
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
    