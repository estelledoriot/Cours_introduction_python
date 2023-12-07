import pygame
from random import randint
from typing import Self

pygame.init()

largeur, hauteur = (640, 480)
fenetre = pygame.display.set_mode((largeur, hauteur))
fenetre.fill([0, 0, 0])
taille = 10
clock = pygame.time.Clock()


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

    def __init__(self):
        self.x: int = randint(taille, largeur - taille)
        self.y: int = randint(taille, hauteur - taille)
        self.dx: int = randint(-5, 5)
        self.dy: int = randint(-5, 5)
        self.color: tuple[int, int, int] = (
            randint(0, 255),
            randint(0, 255),
            randint(0, 255),
        )
        self.taille: int = taille
        self.malade: bool = False

    def contamine(self, b: Self):
        if self.malade or b.malade:
            self.malade = True
            b.malade = True

    def move(self) -> None:
        # mouvement de la balle
        self.x += self.dx
        self.y += self.dy

        # rebond de la balle sur les bords de l'écran
        if self.x <= self.taille or self.x >= largeur - self.taille:
            self.dx *= -1
        if self.y <= self.taille or self.y >= hauteur - self.taille:
            self.dy *= -1

        # collision de la balle self avec les autres balles
        for b in liste_balles:
            if (
                (b.x - self.x) ** 2 + (b.y - self.y) ** 2
            ) ** 0.5 < self.taille + b.taille:
                # on échange les dx
                b.dx, self.dx = self.dx, b.dx
                # on échange les dy
                b.dy, self.dy = self.dy, b.dy
                # les balles se contaminent
                self.contamine(b)

    def draw(self) -> None:
        pygame.draw.circle(
            fenetre, self.color, (self.x, self.y), self.taille, 2 if self.malade else 0
        )


liste_balles = [Balle() for _ in range(50)]
liste_balles[0].malade = True
en_cours = True

while en_cours:
    fenetre.fill([0, 0, 0])
    for b in liste_balles:
        b.move()
        b.draw()

    pygame.display.flip()

    # routine pour pouvoir fermer «proprement» la fenêtre Pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            en_cours = False

    clock.tick(60)

pygame.quit()
