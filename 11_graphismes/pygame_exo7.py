import pygame


pygame.init()

largeur = 600
hauteur = 400
fenetre = pygame.display.set_mode((largeur, hauteur))
clock = pygame.time.Clock()

bleu = (0, 0, 255)
fenetre.fill(bleu)
pikachu = pygame.image.load("pika.png").convert_alpha()
pika_rect = pikachu.get_rect(center=(largeur // 2, hauteur // 2))
vitesse = 10

quitter = False
while not quitter:
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT:
            quitter = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and pika_rect.top > 0:
        pika_rect.y -= vitesse
    if pressed[pygame.K_DOWN] and pika_rect.bottom < hauteur:
        pika_rect.y += vitesse
    if pressed[pygame.K_RIGHT] and pika_rect.right < largeur:
        pika_rect.x += vitesse
    if pressed[pygame.K_LEFT] and pika_rect.left > 0:
        pika_rect.x -= vitesse

    fenetre.fill(bleu)
    fenetre.blit(pikachu, pika_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
