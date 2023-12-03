import pygame

pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

blanc = (255, 255, 255)
noir = (0, 0, 0)

fenetre.fill(blanc)

taille_max = min(largeur, hauteur)
nb_carres = 20

for i in range(nb_carres):
    taille = taille_max * (1 - i / nb_carres)
    rectangle = pygame.Rect(0, 0, taille, taille)
    rectangle.center = largeur // 2, hauteur // 2
    couleur = noir if i % 2 == 0 else blanc
    pygame.draw.rect(fenetre, couleur, rectangle)


quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
