import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    #creates a new instance anytime the test run
    def setUp(self):
        self.calc = SimpleCalculator()

    #test case for addition
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)

    #test case for subtraction
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(30, 20), 10)
        self.assertEqual(self.calc.subtract(-7, -9), 2)

    #test case for multiplication
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(14, 5), 70)
        self.assertEqual(self.calc.multiply(-9, 0), 0)

    #test case for division
    def test_divide(self):
        self.assertEqual(self.calc.divide(15, 15), 1)
        self.assertEqual(self.calc.divide(-6, 8), -48)

    #test case for ZeroDivision error
    def test_divide(self):
        self.assertIsNone(self.calc.divide(25, 0))

if __name__ == "__main__":
    unittest.main()