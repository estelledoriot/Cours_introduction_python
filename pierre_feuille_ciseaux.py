"""
Estelle DORIOT
Jeu pierre feuille ciseaux
"""

from random import randint

actions = ["pierre", "feuille", "ciseaux"]


def choix_joueur() -> str:
    """renvoie le choix du joueur.
    Si le choix n'est pas correct, on redemande au joueur de choisir"""
    choix = input("pierre, feuille ou ciseaux? ")
    while choix not in actions:
        print("Choix incorrect.")
        choix = input("pierre, feuille ou ciseaux? ")
    return choix


def choix_ordinateur() -> str:
    """renvoie le choix de l'ordinateur, pris au hasard dans la liste des actions"""
    return actions[randint(0, 2)]


def qui_gagne(choix1: str, choix2: str) -> int | None:
    """détermine qui est le vainqueur de la manche:
    0 pour le premier joueur, 1 pour le deuxième, None pour une partie nulle"""
    if choix1 == choix2:
        return None
    if choix1 == "ciseaux":
        if choix2 == "pierre":
            return 1
        if choix2 == "feuille":
            return 0
    elif choix1 == "feuille":
        if choix2 == "pierre":
            return 0
        if choix2 == "ciseaux":
            return 1
    elif choix1 == "pierre":
        if choix2 == "feuille":
            return 1
        if choix2 == "ciseaux":
            return 0


def une_manche() -> int | None:
    """Gère le déroulement d'une manche"""
    choix_ordi = choix_ordinateur()
    choix_player = choix_joueur()
    vainqueur = qui_gagne(choix_player, choix_ordi)
    print(f"Tu as choisi {choix_player}")
    print(f"L'ordinateur a choisi {choix_ordi}")
    if vainqueur == 0:
        print("Tu as gagné la manche !")
    elif vainqueur == 1:
        print("Tu as perdu la manche !")
    else:
        print("Manche nulle")
    return vainqueur


def main_game() -> None:
    """Gère une partie entière"""
    points_ordi = 0
    points_joueur = 0

    print("-----------------------------------")
    print("Bienvienue à pierre feuille ciseaux")
    print("-----------------------------------")
    print()

    while points_ordi < 5 and points_joueur < 5:
        vainqueur_tour = une_manche()
        if vainqueur_tour == 0:
            points_joueur += 1
        elif vainqueur_tour == 1:
            points_ordi += 1

        print(f"Score: {points_joueur} - {points_ordi}")
        print()

    if points_joueur == 5:
        print("bravo, tu as gagné la partie")
    else:
        print("zut, perdu ...")


main_game()
