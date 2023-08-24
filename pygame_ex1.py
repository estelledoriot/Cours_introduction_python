import pygame

pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

bleu = (0, 0, 255)
blanc = (255, 255, 255)
rouge = (255, 0, 0)

largeur_rectangle = largeur // 3
hauteur_rectangle = hauteur

rect_1 = pygame.Rect(0, 0, largeur_rectangle, hauteur_rectangle)
rect_2 = pygame.Rect(largeur_rectangle, 0, largeur_rectangle, hauteur_rectangle)
rect_3 = pygame.Rect(2 * largeur_rectangle, 0, largeur_rectangle, hauteur_rectangle)

pygame.draw.rect(fenetre, bleu, rect_1)
pygame.draw.rect(fenetre, blanc, rect_2)
pygame.draw.rect(fenetre, rouge, rect_3)

quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
