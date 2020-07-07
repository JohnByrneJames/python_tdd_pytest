import pytest
import unittest
from exercise import Exercise

class ExerciseTest(unittest.TestCase):

    # This runs a test against the sqrt method in the exercise class
    # Ran 1 tests in 0.004s
    # Failed
    # self.assertEqual(Exercise.find_sqrt(2), 1.4)
    # Expected : 1.41
    # Actual : 1.4
    def test_find_sqrt(self):
        self.assertEqual(Exercise.find_sqrt(2), 1.41)  # This is the correct answer so will pass

    # This runs a test against the ceil method in the exercise class
    # Ran 2 tests in 0.004s
    # Failed
    # self.assertEqual(Exercise.find_sqrt(2.4), 2)
    # Expected : 3
    # Actual : 2
    def test_find_ceil(self):
        self.assertEqual(Exercise.find_ceil(2.4), 3)  # both tests are successful

