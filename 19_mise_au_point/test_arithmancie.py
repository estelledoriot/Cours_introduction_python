import unittest
from arithmancie import valeur1, valeur2, valeur3, valeur


class TestValeur1(unittest.TestCase):
    def test_Zero(self):
        self.assertEqual(valeur1("Zero"), 64)


class TestValeur2(unittest.TestCase):
    def test_Zero(self):
        self.assertEqual(valeur2("Zero"), 64)


class TestValeur3(unittest.TestCase):
    def test_Zero(self):
        self.assertEqual(valeur3("Zero"), 64)


class TestValeur(unittest.TestCase):
    def test_vide(self):
        self.assertEqual(valeur(""), 0)

    def test_speciaux(self):
        self.assertEqual(valeur("$èéù.,"), 0)

    def test_minuscules(self):
        self.assertEqual(valeur("a"), 1)
        self.assertEqual(valeur("z"), 26)
        self.assertEqual(valeur("toto"), 70)

    def test_majuscule(self):
        self.assertEqual(valeur("A"), 1)
        self.assertEqual(valeur("Z"), 26)
        self.assertEqual(valeur("TOTO"), 70)

    def test_mixte(self):
        self.assertEqual(valeur("tOtO"), 70)
        self.assertEqual(valeur("Zero"), 64)


if __name__ == "__main__":
    unittest.main()
