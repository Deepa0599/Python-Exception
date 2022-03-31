import unittest

def checkDivisibility7(x):
    if x%7 == 0:
        return True
    else:
        return False

class Divisibility(unittest.TestCase):
    def test_case_divisible(self):
        x = 14
        result = checkDivisibility7(x)
        self.assertTrue(result)

    def test_case_divisible1(self):
        x = 9
        result = checkDivisibility7(x)
        self.assertFalse(result)
