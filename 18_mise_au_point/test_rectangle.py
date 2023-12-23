import unittest
from rectangle_complet import Rectangle


class TestRectangle(unittest.TestCase):
    """Tests des méthodes de la classe Rectangle"""

    def setUp(self) -> None:
        self.rect5x3 = Rectangle(5, 3)
        self.rect6x6 = Rectangle(6, 6)
        self.rect4x7 = Rectangle(4, 7)
        self.rect7x4 = Rectangle(7, 4)

    def test_getlargeur(self):
        """Tests de l'accesseur get_largeur"""
        self.assertEqual(self.rect5x3.get_largeur(), 5, "rect5x3 a pour largeur 5")
        self.assertEqual(self.rect6x6.get_largeur(), 6, "rect6x6 a pour largeur 6")

    def test_gethauteur(self):
        """Tests de l'accesseur get_hauteur"""
        self.assertEqual(self.rect5x3.get_hauteur(), 3, "rect5x3 a pour hauteur 3")
        self.assertEqual(self.rect6x6.get_hauteur(), 6, "rect6x6 a pour hauteur 6")

    def test_setlargeur_positif(self):
        """Tests du mutateur set_largeur avec un nombre positif"""
        self.rect5x3.set_largeur(1)
        self.assertEqual(self.rect5x3.get_largeur(), 1, "la largeur doit être modifiée")

    def test_setlargeur_negatif(self):
        """Test du mutateur set_largeur avec un nombre négatif"""
        self.assertRaises(ValueError, Rectangle.set_largeur, self.rect5x3, -1)
        self.assertRaises(ValueError, Rectangle.set_largeur, self.rect5x3, 0)

    def test_setlargeur_chaine(self):
        """Test du mutateur set_largeur avec une valeur non entière"""
        self.assertRaises(
            TypeError,
            self.rect5x3.set_largeur,
            "toto",
            "la largeur doit être une valeur entière",
        )
        self.assertRaises(
            TypeError,
            self.rect5x3.set_largeur,
            3.25,
            "la largeur doit être une valeur entière",
        )

    def test_sethauteur_positif(self):
        """Tests du mutateur set_largeur avec un nombre positif"""
        self.rect5x3.set_hauteur(1)
        self.assertEqual(self.rect5x3.get_hauteur(), 1, "la hauteur doit être modifiée")

    def test_sethauteur_negatif(self):
        """Test du mutateur set_hauteur avec un nombre négatif"""
        self.assertRaises(
            ValueError,
            self.rect5x3.set_hauteur,
            -1,
        )
        self.assertRaises(
            ValueError,
            self.rect5x3.set_hauteur,
            0,
        )

    def test_sethauteur_chaine(self):
        """Test du mutateur set_hauteur avec une valeur non entière"""
        self.assertRaises(
            TypeError,
            self.rect5x3.set_hauteur,
            "toto",
            "la hauteur doit être une valeur entière",
        )
        self.assertRaises(
            TypeError,
            self.rect5x3.set_hauteur,
            3.25,
            "la hauteur doit être une valeur entière",
        )

    def test_constructeur(self):
        """Tests du constructeur avec des valeurs négatives"""
        with self.assertRaises(Exception, msg="Pas de valeurs négatives"):
            r = Rectangle(-3, -3)
        with self.assertRaises(Exception, msg="Pas de valeurs nulles"):
            r = Rectangle(0, 0)
        with self.assertRaises(Exception, msg="Que des entiers en paramètres"):
            r = Rectangle(5.0, 6.5)

    def test_perimetre(self):
        """Tests de la méthode calculer_perimetre"""
        self.assertEqual(
            self.rect5x3.calculer_perimetre(), 16, "rect5x3 a un périmètre de 16"
        )
        self.assertEqual(
            self.rect6x6.calculer_perimetre(), 24, "rect6x6 a un périmètre de 24"
        )

    def test_aire(self):
        """Tests de la méthode calculer_aire"""
        self.assertEqual(self.rect5x3.calculer_aire(), 15, "rect5x3 a une aire de 15")
        self.assertEqual(self.rect6x6.calculer_aire(), 36, "rect6x6 a une aire de 36")

    def test_diagonale(self):
        """Tests de la fonction calculer_diagonale"""
        self.assertAlmostEqual(
            self.rect5x3.calculer_diagonale(),
            5.831,
            3,
            "rect5x3 a une diagonale de 5.831",
        )
        self.assertAlmostEqual(
            self.rect6x6.calculer_diagonale(), 8.485, 3, "rect6x6 a une aire de 8.485"
        )

    def test_ratio(self):
        """Tests unitaires de calculer_ratio()"""
        self.assertAlmostEqual(
            self.rect5x3.calculer_ratio(), 0.6, 3, "rect5x3 a un ratio de 0.6"
        )
        self.assertAlmostEqual(
            self.rect6x6.calculer_ratio(), 1.0, 3, "rect6x6 a un ratio de 1.0"
        )

    def test_carre_positif(self):
        """Test unitaires de calculer_ratio()"""
        self.assertTrue(self.rect6x6.etre_carre(), "rect6x6 est carré")

    def test_carre_negatif(self):
        """Test unitaires de calculer_ratio()"""
        self.assertFalse(self.rect5x3.etre_carre(), "rect5x3 n'est pas carré")

    def test_horizontal_positif(self):
        """Tests unitaires de etre_horizontal()"""
        self.assertTrue(self.rect5x3.etre_horizontal(), "rect5x3 est horizontal")
        self.assertTrue(self.rect6x6.etre_horizontal(), "rect6x6 est horizontal")

    def test_horizontal_negatif(self):
        """Tests unitaires de etre_horizontal()"""
        self.assertFalse(self.rect4x7.etre_horizontal(), "rect4x7 est vertical")

    def test_similaire(self):
        """Tests unitaires de etre_similaire()"""
        self.assertTrue(
            self.rect4x7.etre_similaire(self.rect7x4), "rect4x7 est similaire à rect7x4"
        )
        self.assertFalse(
            self.rect4x7.etre_similaire(self.rect5x3),
            "rect4x7 n'est pas similaire à rect5x3",
        )
        with self.assertRaises(
            Exception,
            msg="On ne peux pas utiliser autre chose qu'un rectangle en paramètre",
        ):
            self.rect4x7.etre_similaire("un rectangle")

    def test_plus_grand(self):
        """Tests unitaires de etre_plus_grand_que()"""
        self.assertTrue(
            self.rect4x7.etre_plus_grand_que(self.rect5x3),
            "rect4x7 est plus grand rect5x3",
        )
        self.assertFalse(
            self.rect4x7.etre_plus_grand_que(self.rect6x6),
            "rect4x7 n'est pas plus grand que rect6x6",
        )
        with self.assertRaises(
            Exception,
            msg="On ne peux pas utiliser autre chose qu'un rectangle en paramètre",
        ):
            self.rect4x7.etre_plus_grand_que("un rectangle")

    def test_contenir(self):
        """Tests unitaires de pouvoir_contenir()"""
        self.assertTrue(
            self.rect6x6.pouvoir_contenir(self.rect5x3), "rect6x6 peut contenir rect5x3"
        )
        self.assertFalse(
            self.rect4x7.pouvoir_contenir(self.rect6x6),
            "rect4x7 ne peut pas contenir rect6x6",
        )
        with self.assertRaises(
            Exception,
            msg="On ne peux pas utiliser autre chose qu'un rectangle en paramètre",
        ):
            self.rect4x7.pouvoir_contenir("un rectangle")

    def test_representation_simple(self):
        """Tests unitaires de creer_representation()"""
        self.assertEqual(
            self.rect5x3.creer_representation(version="simple"),
            "#####\n#####\n#####\n",
            "Pas la bonne forme",
        )

    def test_representation_complexe(self):
        """Tests unitaires de creer_representation()"""
        self.assertEqual(
            self.rect5x3.creer_representation(version="complexe"),
            "+---+\n|   |\n+---+\n",
            "Pas la bonne forme",
        )


# Lancement des tests
if __name__ == "__main__":
    unittest.main()
