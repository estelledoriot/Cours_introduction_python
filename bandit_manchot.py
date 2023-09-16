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
    """ Renvoie le gain selon la chaine passée en argument
    A titre d'information, l'espérance de gain avec la table donnée est de 
    37.5"""
    if chaine == "777":
        return 100 * mise
    if chaine == "ΩΩΩ":
        return 50 * mise
    if chaine == "♥♥♥" or chaine == "♠♠♠" or chaine == "♣♣♣" or chaine == "♦♦♦":
        return 20 * mise
    if chaine == "7ΩΩ" or chaine == "Ω7Ω" or chaine == "ΩΩ7":
        return 10 * mise
    if 
    return 0

assert table_gain('777', 20) == 2000
assert table_gain('ΩΩΩ', 20) == 1000
assert table_gain('♥♥♥', 10) == 200
assert table_gain('Ω7Ω', 15) == 150
assert table_gain('♠♠7', 10) == 50
assert table_gain('7♠♠', 10) == 50
assert table_gain('♠7♣', 25) == 25
assert table_gain('♠77', 50) == 0
