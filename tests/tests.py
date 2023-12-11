import unittest
from src.ans import whitespace_analyzer

class TestWhitespaceAnalyzer(unittest.TestCase):
    def test_whitespace_analysis(self):
        input_string = "\t  Hello World \n"
        leading, trailing, modified = whitespace_analyzer(input_string)
        self.assertEqual(leading, {' ': 2, '\t': 1})
        self.assertEqual(trailing, {' ': 1, '\n': 1})
        self.assertEqual(modified, "Hello World")

# Additional tests could include strings with no whitespace, only leading or trailing whitespace, etc.


if __name__ == '__main__':
    unittest.main()
