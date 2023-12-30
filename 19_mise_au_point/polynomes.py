import math


def racines(a: float, b: float, c: float) -> list:
    """
    Renvoie la liste des racines du polynôme
    ax^2 + bx + c
    """
    if a == 0:
        raise ValueError("Le polynôme n'est pas de degré 2")
    delta = b**2 - 4 * a * c
    if delta < 0:
        return []
    if delta == 0:
        return [-b / (2 * a)]
    x1 = (-b - math.sqrt(delta)) / (2 * a)
    x2 = (-b + math.sqrt(delta)) / (2 * a)
    if a > 0:
        return [x1, x2]
    else:
        return [x2, x1]
