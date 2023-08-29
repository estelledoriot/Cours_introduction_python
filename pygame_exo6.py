from random import randint
import pygame


pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

bleu = (0, 0, 255)
fenetre.fill(bleu)
pikachu = pygame.image.load("pika.png").convert_alpha()
pika_rect = pikachu.get_rect()

quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    fenetre.fill(bleu)
    pika_rect = pikachu.get_rect(
        topleft=(
            randint(0, largeur - pikachu.get_width()),
            randint(0, hauteur - pikachu.get_height()),
        )
    )
    fenetre.blit(pikachu, pika_rect)
    pygame.display.flip()
    pygame.time.delay(1000)
    clock.tick(60)

pygame.quit()
