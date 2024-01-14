import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_simple_string(self):
        """test simple string"""
        self.assertTrue(TestLexer.test("'Yanxi Palace - 2018'","'Yanxi Palace - 2018',<EOF>",101))

    def test_complex_string(self):
        """test complex string"""
        self.assertTrue(TestLexer.test("'isn''t'","'isn''t',<EOF>",102))
        
    def test_simple_identifier(self):
        """test simple identifier"""
        self.assertTrue(TestLexer.test("_myID","_myID,<EOF>",105))
        
    def test_simple_comment_line(self):
        """Test simple comment"""
        self.assertTrue(TestLexer.test("##This is a comment\n","##This is a comment\n,<EOF>", 106))

    def test_simple_comment_line_at_EOF(self):
        """Test simple comment at before EOF"""
        self.assertTrue(TestLexer.test("##This is a comment","##This is a comment,<EOF>", 107))
    