import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    """
    Test function template:
    def test_TEST_NAME(self):
        '''Small description here'''
        input = ""
        expected = ""
        test_ID = 1xx
        self.assertTrue(TestLexer.test(input,expected,test_ID))
    """
    #*Case 101-110: Simple test for tokens#
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("\"Yanxi Palace - 2018\"","Yanxi Palace - 2018,<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("\"isn\\\'t\"","isn\\\'t,<EOF>",102))
        
    def test_simple_identifier(self):
        """test simple identifier"""
        self.assertTrue(TestLexer.test("_myID","_myID,<EOF>",105))
        
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
        self.assertTrue(TestLexer.test("\"This string is not close", "Unclosed String: This string is not close", 110))
        
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
        input = "\n_myIdent1\n_myIdent2"
        expected = "\n,_myIdent1,\n,_myIdent2,<EOF>"
        self.assertTrue(TestLexer.test(input,expected,116))