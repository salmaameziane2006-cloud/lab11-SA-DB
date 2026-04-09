import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-2, 7), 5)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -2), -1)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################
    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_divide(self):
        self.assertEqual(div(2, 10), 5)


    ######## Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)  # your div does b / a → a = 0 triggers error

    def test_logarithm(self):
        self.assertEqual(log(10, 10), 1)
        self.assertEqual(log(math.e, math.e), 1)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(0, 10)
        with self.assertRaises(ValueError):
            log(-2, 10)
        with self.assertRaises(ValueError):
            log(10, -5)

    ######## Partner 1
    def test_log_invalid_argument(self):
            with self.assertRaises(ValueError):
                logarithm(-1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3)

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()