"""
Module rue
dessine une rue aléatoire avec plusieurs immeubles
de couleurs et de hauteurs différentes
"""

import turtle
import time
from random import randint, choice, shuffle
from typing import Callable


# Alias de types pour clarifier le code
Couleur = tuple[int, int, int]
Coord = int

# constantes imposées
NIVEAU_MAX = 4
LARGEUR = 140
HAUT_NIV = 60
TAILLE_FEN = 30
LARG_PORTE = 30
HAUT_PORTE = 50
HAUT_PORTE2 = 40
POS_FENETRE = 20
LARG_BALCON = TAILLE_FEN + 10
HAUT_BALCON = TAILLE_FEN
ECART = 10
NB_BAR = 5  # nb barreaux balcon
COULEUR_FENETRE = (200, 200, 200)
COULEUR_TOIT = (0, 0, 0)


def ini_tortue(nb_maisons: int) -> None:
    """
    Place la tortue pour le début du dessin
    """
    turtle.setup(1.5 * nb_maisons * LARGEUR, NIVEAU_MAX * 1.2 * HAUT_NIV * 2)
    turtle.speed(0)
    turtle.hideturtle()
    screen = turtle.Screen()
    screen.colormode(255)


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
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.fillcolor(COULEUR_FENETRE)
    rectangle(x, y + POS_FENETRE, TAILLE_FEN, TAILLE_FEN)
    turtle.end_fill()


def porte1(x: Coord, y: Coord, couleur: Couleur) -> None:
    """
    Porte rectangulaire
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    """
    turtle.pensize(1)
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
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    trait(x - LARG_PORTE // 2, y + HAUT_PORTE2, x - LARG_PORTE // 2, y)
    trait(x - LARG_PORTE // 2, y, x + LARG_PORTE // 2, y)
    trait(x + LARG_PORTE // 2, y, x + LARG_PORTE // 2, y + HAUT_PORTE2)
    turtle.setheading(90)
    turtle.pendown()
    turtle.circle(LARG_PORTE // 2, 180)
    turtle.penup()
    turtle.end_fill()


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
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.fillcolor(COULEUR_FENETRE)
    rectangle(x, y, TAILLE_FEN, TAILLE_FEN + POS_FENETRE)
    turtle.end_fill()
    turtle.pensize(2)
    rectangle(x, y, LARG_BALCON, HAUT_BALCON)
    turtle.pensize(1)
    for i in range(NB_BAR):
        trait(
            x - LARG_BALCON // 2 + (LARG_BALCON * (i + 1)) // (NB_BAR + 1),
            y + HAUT_BALCON,
            x - LARG_BALCON // 2 + (LARG_BALCON * (i + 1)) // (NB_BAR + 1),
            y,
        )


def fenetres() -> list[Callable]:
    """
    Renvoie la liste des fenetres possibles
    """
    return [fenetre, fenetre_balcon]


# ----- Facade avec : couleur + 3 élts d'étages -----


def facade(x: Coord, y_sol: Coord, couleur: Couleur, niveau: int) -> None:
    """
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    """
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.fillcolor(couleur)
    rectangle(x, y_sol + niveau * HAUT_NIV, LARGEUR, HAUT_NIV)
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
    turtle.pensize(1)
    turtle.begin_fill()
    turtle.fillcolor(COULEUR_TOIT)
    trait(
        x - (LARGEUR // 2 + ECART),
        y_sol + HAUT_NIV * niveau,
        x + (LARGEUR // 2 + ECART),
        y_sol + HAUT_NIV * niveau,
    )
    trait(
        x + (LARGEUR // 2 + ECART),
        y_sol + HAUT_NIV * niveau,
        x,
        y_sol + HAUT_NIV * niveau + HAUT_NIV // 2,
    )
    trait(
        x,
        y_sol + HAUT_NIV * niveau + HAUT_NIV // 2,
        x - (LARGEUR // 2 + ECART),
        y_sol + HAUT_NIV * niveau,
    )
    turtle.end_fill()


def toit2(x: Coord, y_sol: Coord, niveau: int) -> None:
    """
    Toit plat
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    """
    turtle.pensize(10)
    trait(
        x - (LARGEUR // 2 + ECART),
        y_sol + HAUT_NIV * niveau,
        x + (LARGEUR // 2 + ECART),
        y_sol + HAUT_NIV * niveau,
    )


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
    facade(x, y_sol, c_facade, 0)
    elements = [fenetre, fenetre, choice(portes())]
    shuffle(elements)
    for i, action in enumerate(elements):
        if action is fenetre:
            action(x + (i - 1) * (TAILLE_FEN + ECART), y_sol)
        else:
            action(x + (i - 1) * (TAILLE_FEN + ECART), y_sol, c_porte)


def etage(x: Coord, y_sol: Coord, couleur: Couleur, niveau: int) -> None:
    """
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    """
    facade(x, y_sol, couleur, niveau)
    elements = [choice(fenetres()) for _ in range(3)]
    for i, action in enumerate(elements):
        action(x + (i - 1) * (TAILLE_FEN + ECART), y_sol + HAUT_NIV * niveau)


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
    turtle.exitonclick()
