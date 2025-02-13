import unittest
from incubytes_tdd import add  # Import the function

class TestStringCalculator(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(add(""), 0)

    def test_single_number(self):
        self.assertEqual(add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(add("1,5"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(add("1,2,3,4"), 10)

    def test_newline_separator(self):
        self.assertEqual(add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(add("//;\n1;2"), 3)

    def test_multiple_delimiter(self):
        self.assertEqual(add("//[*][%]\n1*2%3"), 6)

    def test_long_delimiter(self):
        self.assertEqual(add("//[***]\n1***2***3"), 6)

    def test_limit_1000(self):
        self.assertEqual(add("//[***]\n1***2000***3"), 4)
    
    def test_negative_number(self):
        with self.assertRaises(ValueError) as context:
            add("1,-2,3,-4")
        self.assertEqual(str(context.exception), "Negative numbers are not allowed [-2, -4]")

if __name__ == '__main__':
    unittest.main()

