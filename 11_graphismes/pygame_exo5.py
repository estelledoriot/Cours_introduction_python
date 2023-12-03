import pygame

pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

blanc = (255, 255, 255)
fenetre.fill(blanc)

for i in range(256):
    rectangle = pygame.Rect(largeur // 2 - 256 // 2 + i, 0, 1, hauteur)
    couleur = (i, 0, 255 - i)
    pygame.draw.rect(fenetre, couleur, rectangle)


quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
