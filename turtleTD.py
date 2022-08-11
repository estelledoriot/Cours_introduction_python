################
# Estelle Doriot
# NSI 1ère
# * TD Turtle  *
################

from turtle import *
from time import sleep
from math import *

wait = 2

# * Exercice n°1

# 1. Tracer un carré de côté 40

for i in range(4):
    forward(40)
    right(90)
    
# 2. Ecrire une fonction carré(). On veillera à ce que la tortue retourne à sa position et à son orientation d'origine.

sleep(wait)
reset()

def carré():
    for i in range(4):
        forward(40)
        right(90)

carré()

# 3. Utiliser la fonction carré() écrite à la question précédente pour créer la fonction panneau()

sleep(wait)
reset()

def panneau():
    forward(60)
    left(45)
    carré()
    right(45)
    backward(60)

panneau()

# 4. Utiliser la fonction panneau() pour créer une fonction étoile8()

speed(10)
sleep(wait)
reset()

def étoile8():
    for i in range(8):
        panneau()
        left(360/8)
        
étoile8()

# 5. Réaliser de même une fonction étoile11()

sleep(wait)
reset()

def étoile11():
    for i in range(11):
        panneau()
        left(360/11)
        
étoile11()

# 6. Généraliser le raisonnement précédent pour écrire une fonction étoile(n: int) qui dessine une étoile comportant un nombre quelconque n de panneaux

sleep(wait)
reset()

def étoile(n: int):
    for i in range(n):
        panneau()
        left(360/n)
        
étoile(20)

# * Exercice n°2

# 1. Ecrire une fonction carré(c: int) qui dessine un carré de côté c.

speed(1)
sleep(wait)
reset()

def carré(c: int):
    for i in range(4):
        forward(c)
        right(90)    

carré(20)

# 2. Tracer la figure ci-dessous. Les carrés ont pour côtés 100, 80, 60, 40 et 20.

speed(10)
sleep(wait)
reset()

def branche():
    taille = 100
    for i in range(5):
        carré(taille)
        forward(taille)
        taille -= 20
    backward(100 + 80 + 60 + 40 + 20)

def figure():
    for i in range(4):
        branche()
        left(90)

figure()

# * Exercice n°3

# 1. Ecrire une fonction triangle(c: int) qui dessine un triangle équilatéral de côté c.

sleep(wait)
reset()

def triangle(c: int):
    for i in range(3):
        forward(c)
        left(120)
        
triangle(100)

# 2. Ecrire une fonction heptagone(c: int) qui dessine un heptagone régulier de côté c.

sleep(wait)
reset()

def heptagone(c: int):
    for i in range(7):
        forward(c)
        left(360/7)

heptagone(100)

# 3. Ecrire une fonction polygone(n: int, c: int) qui dessine un polygone régulier à n côtés de taille c quelconque.

sleep(wait)
reset()

def polygone(n: int, c: int):
    for i in range(n):
        forward(c)
        left(360/n)
      
polygone(20, 50)

# 4. Réaliser la figure suivante

sleep(wait)
reset()
penup()
goto(-200, 0)
pendown()

for i in range(3, 11):
    polygone(i, 40)
    forward(40)

# 5. Réaliser une fonction rosace(n: int, c: int) qui réalise les rosaces ci-dessous obtenues par rotation de n polygones réguliers de côté c.

sleep(wait)
reset()

def rosace(n: int, c: int):
    for i in range(n):
        polygone(n, c)
        right(360/n)

rosace(8, 50)

sleep(wait)
reset()

rosace(20, 30)


# * Exercice n°4

# 1. On décide qu’un polygone à 360 côtés est une bonne approximation d’un cercle. Concevoir une fonction cercle(r: float) qui affiche un « cercle » (un polygone à 360 côtés) de rayon r quelconque, ainsi qu’un de ses diamètres.

sleep(wait)
reset()

def cercle(r: float):
    c = 2 * r * cos(pi * (1 / 2 - 1 / 360))
    polygone(360, c)
    left(90)
    forward(2 * r)

cercle(100)

# 2. Ecrire une fonction spirale() qui trace une spirale

sleep(wait)
reset()

def spirale():
    d = 0.01
    for i in range(600):
        forward(d)
        right(5)
        d += 0.01
        
spirale()

# 3. Tracer une spirale carrée

sleep(wait)
reset()

def spirale_carre(n: int):
    taille = 10
    for i in range(n):
        forward(taille)
        right(90)
        taille += 5

spirale_carre(20)

# 4. Écrire une fonction spirale_polygone(n: int, m: int) qui tracer une spirale en forme de polygone à m côtés.

sleep(wait)
reset()

def spirale_polygone(n: int, m: int):
    taille = 10
    for i in range(n):
        forward(taille)
        right(360 / m)
        taille += 5

spirale_polygone(20,  6)

# * Exercice n°5

# 1. Écrire une fonction carré_couleur(taille: int, couleur: str) qui trace un carré de côté taille et de couleur couleur. De même, écrire une fonction triangle_couleur(taille: int, couleur: str) qui dessine un triangle de taille taille et de couleur couleur

def carré_couleur(taille: int, couleur: str):
    pencolor(couleur)
    for i in range(4):
        forward(taille)
        right(90)
        
def triangle_couleur(taille: int, couleur: str):
    pencolor(couleur)
    for i in range(3):
        forward(taille)
        right(120)

# 2.

sleep(wait)
reset()

penup()
goto(-300, 0)
pendown()
taille = 30
for i in range(5):
    carré_couleur(taille, "red")
    penup()
    forward(taille + 5)
    pendown()
    triangle_couleur(taille, "blue")
    penup()
    forward(taille + 5)
    pendown()
    taille += 15

# 3. Écrire une fonction |étoile(taille: int, couleur: str)| qui dessine une étoile à |n| branche de couleur |couleur|.

sleep(wait)
reset()

def étoile(taille: int, n: int, couleur: str):
    pencolor(couleur)
    for i in range(n):
        forward(taille)
        right(n // 2 * 360 / n)

étoile(100, 5, "red")

# 4. 

sleep(wait)
reset()

penup()
goto(-300, 0)
pendown()
taille = 20
for i in range(4):
    étoile(taille, 5, "blue")
    penup()
    forward(taille + 10)
    pendown()
    taille += 20
for i in range(5):
    étoile(taille, 5, "blue")
    penup()
    forward(taille + 10)
    pendown()
    taille -= 20

# * Exercice n°6

# 1. 

speed(9)
sleep(wait)
reset()

def grille(n: int):
    taille = 400
    d = taille // n
    for i in range(n + 1):
        penup()
        goto(-taille//2 + i * d, taille//2)
        pendown()
        goto(-taille//2 + i * d, -taille//2)
    for i in range(n + 1):
        penup()
        goto(-taille//2, taille//2 - d * i)
        pendown()
        goto(taille//2, taille//2 - d * i)
    
grille(10)

# 2.

sleep(wait)
reset()

def figure2(n: int):
    taille = 400
    angle = 90 / n
    setheading(135)
    for i in range(n + 1):
        penup()
        goto(0, 0)
        pendown()
        while ycor() <= taille // 2:
            forward(1)
        right(angle)
        
figure2(20)

# 3. 

sleep(wait)
reset()

def sablier(n: int):
    taille = 400
    angle = 90 / n
    setheading(135)
    for i in range(n + 1):
        penup()
        goto(0, 0)
        pendown()
        while ycor() <= taille // 2:
            forward(1)
        right(angle)
    setheading(-45)
    for i in range(n + 1):
        penup()
        goto(0, 0)
        pendown()
        while ycor() >= - taille // 2:
            forward(1)
        right(angle)

sablier(20)

# 4.

sleep(wait)
reset()

def soleil(n: int):
    taille = 400
    angle = 90 / n
    for i in range(4 * n):
        penup()
        goto(0, 0)
        pendown()
        while - taille // 2 <= ycor() <= taille // 2 and - taille // 2 <= xcor() <= taille // 2:
            forward(1)
        right(angle)

soleil(20)

# 5. 

sleep(wait)
reset()

def cercles_concentriques(n: int):
    taille = 10
    y = 0
    for i in range(n):
        penup()
        sety(y)
        pendown()
        circle(taille)
        taille += 10
        y -= 10

cercles_concentriques(20)

# 6.

sleep(wait)
reset()

def tri(n: int):
    taille = 400
    d = taille / n
    setheading(-45)
    for i in range(n + 1):
        penup()
        goto(- taille // 2, taille // 2 - d * i)
        pendown()
        while ycor() >= - taille // 2:
            forward(1)
        
tri(20)

# * Exercice n°7

# 1. Ecrire une fonction carré(c: int) qui dessine un carré de côté de longueur quelconque c.

sleep(wait)
reset()

def carré(c: int):
    for i in range(4):
        forward(c)
        left(90)
        
carré(50)

# 3. En déduire une fonction carrés_imbriqués().

sleep(wait)
reset()

def carrés_imbriqués():
    penup()
    goto(-200, -200)
    pendown()
    taille = 400
    while taille >= 1:
        carré(taille)
        forward(taille/2)
        left(45)
        taille /= sqrt(2)

carrés_imbriqués()

# * Exercice n°8

# 1. Ecrire une fonction triangle(c: int) qui trace un triangle de côté c quelconque

sleep(wait)
reset()

def triangle(c: int):
    for i in range(3):
        forward(c)
        left(120)
        
triangle(100)

# 2. Ecrire une fonction triangles_emboités(c: int) qui réalise la figure ci-dessus pour une taille c quelconque du grand triangle.

sleep(wait)
reset()

def triangles_emboités(c: int):
    penup()
    goto(-100, -100)
    pendown()
    taille = c
    while taille >= 1:
        triangle(taille)
        forward(taille/2)
        left(60)
        taille /= 2

triangles_emboités(300)

# 3. Ecrire une fonction triangles_emboités2(c: int, k: float) qui dessine la figure ci-dessus.

sleep(wait)
reset()

def triangles_emboités2(c: int, k: float):
    penup()
    goto(-100, -100)
    pendown()
    taille = c
    angle = atan(k * sqrt(3)/(2 - 3 * k)) * 180 / pi
    while taille >= 1:
        triangle(taille)
        forward(k * taille)
        left(angle)
        taille *= sqrt(3 * k * k - 3 * k + 1)

triangles_emboités2(300, 0.1)

# * Exercice n°9

# 1. 

sleep(wait)
reset()

def losange(c, a):
    for i in range(2):
        forward(c)
        right(a)
        forward(c)
        right(180 - a)

losange(50, 30)

# 2. 

sleep(wait)
reset()

def tore(c):
    for i in range(12):
        a = 15
        for i in range(11):
            losange(c, a)
            forward(c)
            left(15)
            a = a + 15
        for i in range(10):
            right(15)
            backward(c)
        left(15)

tore(20)

exitonclick()

