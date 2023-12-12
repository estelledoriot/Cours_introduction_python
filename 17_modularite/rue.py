"""
Module rue
dessine une rue aléatoire avec plusieurs immeubles
de couleurs et de hauteurs différentes
"""

from turtle import Turtle
import turtle as tl
import time
from random import randint, choice
from typing import Callable


# Alias de types pour clarifier le code
Octet = int
Couleur = tuple[Octet, Octet, Octet]
Coord = int

# constantes imposées
NIVEAU_MAX = 4
LARGEUR = 140
HAUT_NIV = 60
TAILLE_FEN = 30
LARG_PORTE = 30
HAUT_PORTE = 50
POS_FENETRE = 20
NB_BAR = 5  # nb barreaux balcon
turtle = Turtle()


def ini_tortue(nb_maisons: int) -> None:
    """
    Place la tortue pour le début du dessin
    """
    tl.setup(1.2 * nb_maisons * LARGEUR, NIVEAU_MAX * 1.2 * HAUT_NIV)
    turtle.speed(0)
    turtle.hideturtle()


def couleur_aleatoire() -> Couleur:
    """
    Renvoie un triplet d'octets pour définir une couleur.
    """
    return (randint(0, 255), randint(0, 255), randint(0, 255))


def trait(x1: Coord, y1: Coord, x2: Coord, y2: Coord) -> None:
    """
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    """
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    turtle.penup()


def rectangle(x: Coord, y: Coord, w: Coord, h: Coord) -> None:
    """
    Paramètres
        x, y : coordonnées du centre de la base de rectangle
        w : largeur du rectangle
        h : hauteur du rectangle
    """
    trait(x - w // 2, y, x - w // 2, y + h)
    trait(x - w // 2, y + h, x + w // 2, y + h)
    trait(x + w // 2, y + h, x + w // 2, y)
    trait(x + w // 2, y, x - w // 2, y)


def fenetre(x: Coord, y: Coord) -> None:
    """
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    """
    rectangle(x, y + POS_FENETRE, TAILLE_FEN, TAILLE_FEN)


def porte1(x: Coord, y: Coord, couleur: Couleur) -> None:
    """
    Porte rectangulaire
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    """
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    rectangle(x, y, LARG_PORTE, HAUT_PORTE)
    turtle.end_fill()


def porte2(x: Coord, y: Coord, couleur: Couleur) -> None:
    """
    Porte arondie
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    """
    # TODO


def portes() -> list[Callable]:
    """
    Renvoie la liste des portes possibles
    """
    return [porte1, porte2]


# ----- Elements des étages : Balcon -----


def fenetre_balcon(x: Coord, y: Coord) -> None:
    """
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    """
    # TODO


# ----- Facade avec : couleur + 3 élts d'étages -----


def facade(x: Coord, y_sol: Coord, couleur: Couleur, niveau: int) -> None:
    """
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    """
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    rectangle(x, y_sol, LARGEUR, HAUT_NIV)
    turtle.end_fill()


# ----- Toits -----


def toit1(x: Coord, y_sol: Coord, niveau: int) -> None:
    """
    Toit 2 pentes
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    """
    # TODO


def toit2(x: Coord, y_sol: Coord, niveau: int) -> None:
    """
    Toit plat
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    """
    # TODO


def toits() -> list[Callable]:
    """
    Renvoie la liste des toits possibles
    """
    return [toit1, toit2]


# ----- RDC, Etage et Toit


def rdc(x: Coord, y_sol: Coord, c_facade: Couleur, c_porte: Couleur) -> None:
    """
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    """
    # TODO


def etage(x: Coord, y_sol: Coord, couleur: Couleur, niveau: int) -> None:
    """
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    """
    # TODO


def toit(x: Coord, y_sol: Coord, niveau: int) -> None:
    """
    Paramètres
        x : abscisse du centre de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    """
    choice(toits())(x, y_sol, niveau)


# ----- Immeuble -----


def immeuble(x: Coord, y_sol: Coord) -> None:
    """
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
    """
    # Nombre d'étage (aléatoire)
    nb_etages = randint(0, NIVEAU_MAX)
    # Couleurs des éléments (aléatoire)
    couleur_facade = couleur_aleatoire()
    couleur_porte = couleur_aleatoire()
    # Dessin du RDC
    rdc(x, y_sol, couleur_facade, couleur_porte)
    # Dessin des étages
    niveau = 1
    while niveau <= nb_etages:
        etage(x, y_sol, couleur_facade, niveau)
        niveau += 1
    # Dessin du toit
    toit(x, y_sol, niveau)


# ----- Sol de la rue -----
def sol(y_sol: Coord, nb_maisons: int) -> Coord:
    """
    Paramètres
        y_sol : ordonnée du sol du la rue
    """
    x_sol = LARGEUR // 10 + int((LARGEUR * 1.2 * nb_maisons) // 2)
    turtle.pensize(3)
    trait(-x_sol, y_sol, x_sol, y_sol)
    return x_sol


def dessin(nb_maisons: int) -> None:
    """
    Paramètres
        nb_maisons : nombre de maisons sur la rue
    """
    ini_tortue(nb_maisons)
    y_sol = -2 * HAUT_NIV
    # Dessin du sol de la rue
    x_sol = sol(y_sol, nb_maisons)
    # Dessin des immeubles
    for i in range(nb_maisons):
        immeuble(int(LARGEUR * 1.2 // 2) - x_sol + int(i * LARGEUR * 1.2), y_sol)
    time.sleep(5)


# ------------------------------
# ------------------------------
# ------------------------------

if __name__ == "__main__":
    n = int(input("\n nombre de maisons ?  "))
    dessin(n)
    tl.exitonclick()
