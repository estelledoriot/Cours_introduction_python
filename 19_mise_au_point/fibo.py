"""
module fibo pour calculer la suite de Fibonacci
"""


def fibonacci(n: int) -> int:
    """calcule le n-ième terme de la suite de Fibonacci définie par:
    F(0) = 0
    F(1) = 1
    F(n+2) = F(n+1) + F(n)
    lève l'exception:
    - TypeError si l'argment n'est pas un entier
    - ValueError si l'argument est négatif
    >>> fibonacci(0)
    0
    >>> fibonacci(3)
    2
    >>> fibonacci(7)
    13
    """
    if not isinstance(n, int):
        raise TypeError
    elif n < 0:
        raise ValueError
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
