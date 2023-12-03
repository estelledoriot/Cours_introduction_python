from random import choice

symboles = "♠♥♦♣7Ω"


def choisir_symbole(suite: str) -> str:
    """renvoie un symbole aléatoire parmi une suite de symbole passée en argument"""
    return choice(suite)


def fabriquer_chaine(suite: str, taille: int = 3) -> str:
    """renvoie une chaine aléatoire de dimension taille, à partir de la liste de symbole suite."""
    resultat = ""
    for _ in range(taille):
        resultat += choisir_symbole(suite)
    return resultat


def compte_symboles_identiques(s: str, chaine: str) -> int:
    """renvoie le nombre d'occurences du symbole s au sein de la chaine chaine
    Si le symbole n'est pas présent, renvoie 0"""
    cpt = 0
    for lettre in chaine:
        if lettre == s:
            cpt += 1
    return cpt


def presence_symboles_identiques_multiples(symboles: str, chaine: str) -> bool:
    """renvoie True si l'un des symboles de la chaine symboles est présent plusieurs fois dans chaine, et False sinon"""
    for lettre in symboles:
        if compte_symboles_identiques(lettre, chaine) > 1:
            return True
    return False


def table_gain(chaine: str, mise: int) -> int:
    """renvoie le gain selon la chaine passée en argument
    A titre d'information, l'espérance de gain avec la table donnée est de
    37.5"""
    if chaine == "777":
        return 100 * mise
    if chaine == "ΩΩΩ":
        return 50 * mise
    if chaine in {"♥♥♥", "♠♠♠", "♣♣♣", "♦♦♦"}:
        return 20 * mise
    if (
        compte_symboles_identiques("Ω", chaine) == 2
        and compte_symboles_identiques("7", chaine) == 1
    ):
        return 10 * mise
    if (
        compte_symboles_identiques("♥", chaine) == 2
        or compte_symboles_identiques("♠", chaine) == 2
        or compte_symboles_identiques("♣", chaine) == 2
        or compte_symboles_identiques("♦", chaine) == 2
    ) and compte_symboles_identiques("7", chaine):
        return 5 * mise
    if not presence_symboles_identiques_multiples(symboles, chaine):
        return 1 * mise
    return 0


def saisir_mise(pot: int) -> int:
    """récupère la mise du joueur qui doit être un nombre entier compris entre 10 et pot."""
    print(f"Votre pot actuel est de: {pot} euros.")
    mise = int(input("Veuillez entrer votre mise: "))
    while not 10 <= mise <= pot:
        mise = int(f"Veuillez entrer une mise entre 10 et {pot}: ")
    return mise


def demander_continuer() -> bool:
    """demande au joueur s'il souhaite continuer.
    Le joueur doit pouvoir répondre par oui (ou o) ou par non (ou n).
    """
    reponse = input("Voulez-vous continuer à jouer (oui/non) ? ")
    while reponse not in ["oui", "o", "non", "n"]:
        reponse = input(
            "Veuillez répondre par oui ou par non. Voulez-vous continuer à jouer? "
        )
    return reponse in ["oui", "o"]


def afficher_bandit(chaine: str, gain: int) -> None:
    """
    affiche dans la console le bandit-manchot, avec le tirage obtenu.
    Affiche aussi le gain réalisé."""
    print(
        f"""
-------------
|   |   |   |
| {chaine[0]} | {chaine[1]} | {chaine[2]} |
|   |   |   |
-------------
"""
    )
    print()
    print(f"Vous gagnez {gain}")
    print()


def presentation() -> None:
    """fonction affichant la présentation, et donnant les règles du jeu"""
    print("\n" * 50)
    print(
        """
##############################################
#                                            #
#              Bandit Manchot                #
#                                            #
##############################################
"""
    )
    print("\n" * 5)
    print(
        "Vous disposez d'un capital de départ de 500 € pour jouer au bandit manchot !"
    )
    print("\n" * 2)
    input("(Appuyez sur la touche Entrée...)")


def main_game() -> int:
    """
    Fonction principale du jeu, qui lance une partie, et se poursuiit tant que le joueur souhaite ou peut continuer.
    """
    presentation()
    pot = 500
    continuer = True
    while continuer and pot > 0:
        mise = saisir_mise(pot)
        pot -= mise
        chaine = fabriquer_chaine(symboles)
        gain = table_gain(chaine, mise)
        afficher_bandit(chaine, gain)
        pot += gain
        continuer = demander_continuer()

    return pot


if __name__ == "__main__":
    main_game()
