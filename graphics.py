import pygame

pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

bleu = (0, 0, 255)
rouge = (255, 0, 0)
jaune = (255, 255, 0)
fenetre.fill(bleu)

r = pygame.Rect(300, 0, 100, 200)
pygame.draw.rect(fenetre, jaune, r)

quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
