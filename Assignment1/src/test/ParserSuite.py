import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """func main () return 1
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,201))
        
    def test_simple_program_fail(self):
        """Simple program: int main() {} """
        input = """int main () return 1
        """
        expect = "Error on line 1 col 0: int"
        self.assertTrue(TestParser.test(input,expect,202))