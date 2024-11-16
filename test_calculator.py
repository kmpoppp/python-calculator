import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(1, 4), 5)

    def  test_subtract(self):
        self.assertEqual(self.calc.subtract(1,5),-4)
        self.assertEqual(self.calc.subtract(9900,1),9899)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,3),6)
        self.assertEqual(self.calc.multiply(4,3),12)

    def test_divide(self):
        self.assertEqual(self.calc.divide(5,2),2)
        self.assertEqual(self.calc.divide(6,2),3)
    
    def test_mod(self):
        self.assertEqual(self.calc.modulo(7,2),1)
        self.assertEqual(self.calc.modulo(8,2),0)
    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main()