import pygame

pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

blanc = (255, 255, 255)
noir = (0, 0, 0)

nb_lignes = 8
nb_colonnes = 12
taille = min(largeur // nb_colonnes, hauteur // nb_lignes)

for i in range(nb_lignes):
    for j in range(nb_colonnes):
        rectangle = pygame.Rect(j * taille, i * taille, taille, taille)
        couleur = blanc if (i + j) % 2 == 0 else noir
        pygame.draw.rect(fenetre, couleur, rectangle)


quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
