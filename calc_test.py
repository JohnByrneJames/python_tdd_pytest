import pytest
import unittest
from calc import Calc  # Install everything

class Calc_Test(unittest.TestCase):

    simple_calc = Calc()

    def test_add(self):
        self.assertEqual(self.simple_calc.add(2, 2), 4)

    def test_subtract(self):
        self.assertEqual(self.simple_calc.subtract(3, 1), 2)

    def test_multiply(self):
        self.assertEqual(self.simple_calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.simple_calc.divide(9, 3), 3)

# Create tests for cm to inches and modulus

    def test_cm_to_inch(self):
        self.assertEqual(self.simple_calc.cm_to_inch(10), 3.94)

    def test_modulus(self):
        self.assertEqual(self.simple_calc.modulus(20, 3), 2)

