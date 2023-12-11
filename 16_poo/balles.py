"""
Simulation de transmission de maladie
"""

from random import randint
from typing import Self
import pygame

pygame.init()

largeur, hauteur = (640, 480)
fenetre = pygame.display.set_mode((largeur, hauteur))
fenetre.fill([0, 0, 0])
clock = pygame.time.Clock()
TAILLE = 10


class Balle:
    """Classe Balle
    x = abscisse de la balle, entier entre 0 et la largeur de l'écran
    y = ordonnée de la balle, entier entre 0 et la hauteur de l'écran
    dx = vitesse horizontale de la balle, entier entre -5 et 5
    dy = vitesse verticale de la balle, entier entre -5 et 5
    color = couleur de la balle
    taille = rayon de la balle
    malade = état de la balle
    """

    def __init__(self) -> None:
        self.x: int = randint(TAILLE, largeur - TAILLE)
        self.y: int = randint(TAILLE, hauteur - TAILLE)
        self.dx: int = randint(-5, 5)
        self.dy: int = randint(-5, 5)
        self.color: tuple[int, int, int] = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255),
        )
        self.taille: int = TAILLE
        self.malade: bool = False

    def contamine(self, other: Self) -> None:
        """lorsqu'une balle malade rentre en collision avec une autre balle, elle la contamine"""
        if self.malade or other.malade:
            self.malade = True
            other.malade = True

    def move(self) -> None:
        """gère le mouvement et les collisions entre les balles"""
        # mouvement de la balle
        self.x += self.dx
        self.y += self.dy

        # rebond de la balle sur les bords de l'écran
        if self.x <= self.taille or self.x >= largeur - self.taille:
            self.dx *= -1
        if self.y <= self.taille or self.y >= hauteur - self.taille:
            self.dy *= -1

        # collision de la balle self avec les autres balles
        for balle in liste_balles:
            if (
                (balle.x - self.x) ** 2 + (balle.y - self.y) ** 2
            ) ** 0.5 < self.taille + balle.taille:
                # on échange les dx
                balle.dx, self.dx = self.dx, balle.dx
                # on échange les dy
                balle.dy, self.dy = self.dy, balle.dy
                # les balles se contaminent
                self.contamine(balle)

    def draw(self) -> None:
        """affiche la balle à l'écran"""
        pygame.draw.circle(
            fenetre, self.color, (self.x, self.y), self.taille, 2 if self.malade else 0
        )


liste_balles = [Balle() for _ in range(50)]
liste_balles[0].malade = True
RUNNING = True

while RUNNING:
    fenetre.fill([0, 0, 0])
    for b in liste_balles:
        b.move()
        b.draw()

    pygame.display.flip()

    # fermeture de la fenêtre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False

    clock.tick(60)

pygame.quit()
