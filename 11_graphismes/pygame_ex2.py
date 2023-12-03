import pygame

pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

bleu = (0, 0, 255)
blanc = (255, 255, 255)
rouge = (255, 0, 0)
noir = (0, 0, 0)
vert = (0, 255, 0)

fenetre.fill(blanc)

taille_max = min(largeur, hauteur)
nb_carres = 4
couleurs = [noir, bleu, vert, rouge]

for i in range(nb_carres):
    taille = taille_max * (1 - i / nb_carres)
    rectangle = pygame.Rect(0, 0, taille, taille)
    rectangle.center = largeur // 2, hauteur // 2
    pygame.draw.rect(fenetre, couleurs[i], rectangle)


quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
