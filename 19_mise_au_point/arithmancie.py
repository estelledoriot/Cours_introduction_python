import string


def valeur1(chaine):
    s = 0
    for c in chaine:
        if c >= "A" and c <= "Z":
            s = s + ord(c) - ord("A") + 1
    return s


def valeur2(chaine):
    s = 0
    for c in chaine.upper():
        if c >= "A" and c < "Z":
            s = s + ord(c) - ord("A") + 1
    return s


def valeur3(chaine):
    s = 0
    for c in chaine.upper():
        if c in string.ascii_uppercase:
            s = s + string.ascii_uppercase.index(c)
    return s


def valeur(chaine):
    return sum(
        string.ascii_uppercase.index(c) + 1
        for c in chaine.upper()
        if c in string.ascii_uppercase
    )
