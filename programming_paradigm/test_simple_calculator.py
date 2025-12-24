import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    #creates a new instance anytime the test run
    def setUp(self):
        self.calc = SimpleCalculator()

    #test case for addition
    def test_addition(self):
        result = self.calc.add(10, 3)
        self.assertEqual(result, 13)

    #test case for subtraction
    def test_subtraction(self):
        result = self.calc.subtract(30, 20)
        self.assertEqual(result, 10)

    #test case for multiplication
    def test_multiply(self):
        result = self.calc.multiply(14, 5)
        self.assertEqual(result, 70)

    #test case for division
    def test_divide(self):
        result = self.calc.divide(15, 15)
        self.assertEqual(result, 1)

    #test case for ZeroDivision error
    def test_divide(self):
        result = self.calc.divide(25, 0)
        self.assertIsNone(result)
if __name__ == "__main__":
    unittest.main()