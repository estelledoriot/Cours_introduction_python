from random import randint
import pygame


pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

bleu = (0, 0, 255)
# rouge = (255, 0, 0)
# jaune = (255, 255, 0)
fenetre.fill(bleu)

# surface_rouge = pygame.Surface((150, 150))
# surface_rouge.fill(rouge)
pikachu = pygame.image.load("pika.png").convert_alpha()
pika_rect = pikachu.get_rect()
# pika_tourne = pygame.transform.rotate(pikachu, 90)

# fenetre.blit(surface_rouge, (0, 0))
# fenetre.blit(pikachu, (0, 0))
# fenetre.blit(pika_tourne, (250, 250))

# r = pygame.Rect(300, 0, 100, 200)
# pygame.draw.rect(fenetre, jaune, r)

quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    fenetre.fill(bleu)
    pika_rect = pikachu.get_rect(topleft=(randint(0, 480), randint(0, 270)))
    fenetre.blit(pikachu, pika_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
