import unittest

from fibo import fibonacci


class TestFibonacci(unittest.TestCase):
    def test_0(self):
        self.assertEqual(fibonacci(0), 0, "F(0) != 0")

    def test_3(self):
        self.assertEqual(fibonacci(3), 2, "F(3) != 2")

    def test_7(self):
        self.assertEqual(fibonacci(7), 13, "F(7) != 13")

    def test_minus1(self):
        self.assertRaises(ValueError, fibonacci, -1)


if __name__ == "__main__":
    unittest.main()
