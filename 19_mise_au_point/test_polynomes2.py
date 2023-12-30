import unittest

from polynomes import racines


class TestRacines(unittest.TestCase):
    def test_zero_racines(self):
        racs = racines(1, 0, 1)
        self.assertEqual(racs, [])

    def test_une_racines(self):
        racs = racines(1, 0, 0)
        rac = racs[0]
        self.assertEqual(len(racs), 1)
        self.assertAlmostEqual(rac, 0)

    def test_deux_racines(self):
        racs = racines(1, 0, -1)
        rac1, rac2 = racs
        self.assertEqual(len(racs), 2)
        self.assertAlmostEqual(rac1, -1)
        self.assertAlmostEqual(rac2, 1)


if __name__ == "__main__":
    unittest.main()
