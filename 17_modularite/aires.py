"""
Module qui permet le calcul d'aires de certaines figures géométriques
"""

pi = 3.14159


def aire_disque(rayon: float) -> float:
    """calcule l'aire d'un disque en fonction de son rayon"""
    return pi * rayon * rayon


def aire_rectangle(largeur: float, longueur: float) -> float:
    """calcule l'aire d'un rectangle en fonction de sa largeur et de sa longueur"""
    return largeur * longueur


def triangle(base: float, hauteur: float) -> float:
    """calcule l'aire d'un triangle en fonction de sa base et de sa hauteur"""
    return base * hauteur / 2


print(__name__)
if __name__ == "__main__":
    print(f"Aire d'un disque de rayon 10: {aire_disque(10)}")
