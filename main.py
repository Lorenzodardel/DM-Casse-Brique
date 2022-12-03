import pyxel


pyxel.init(256, 256, title="Casse_Brique")

plateforme_x = 108
plateforme_y = 240
balle = False
x = plateforme_x + 20
y = plateforme_y - 3
vitesse = 3
rayon = 2
balle_liste = [x, y]
vitesse_balle_x = 6
vitesse_balle_y = 5
vie = 3
score = 0
brique_x = [1, 33, 65, 97, 129, 161, 193, 225, 1, 33, 193, 225, 1, 225, 97, 129]
brique_y = [2, 2, 2, 2, 2, 2, 2, 2, 12, 12, 12, 12, 22, 22, 32, 32]
bx = []
by = []
bxx = 0
byy = 0
brique1 = True


def plateforme_deplacement(plateforme_x, plateforme_y):

    if pyxel.btn(pyxel.KEY_RIGHT):
        if plateforme_x < 206:
            plateforme_x += vitesse
    if pyxel.btn(pyxel.KEY_LEFT):
        if plateforme_x > 0:
            plateforme_x -= vitesse
    return plateforme_x, plateforme_y


def balle_deplacement(x, y):

    global vitesse_balle_x, vitesse_balle_y, balle, vie
    x -= vitesse_balle_x
    y -= vitesse_balle_y
    if y <= rayon:
        vitesse_balle_x = vitesse_balle_x
        vitesse_balle_y = -vitesse_balle_y
    elif x <= rayon:
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    elif x >= (256-rayon):
        vitesse_balle_x = -vitesse_balle_x
        vitesse_balle_y = vitesse_balle_y
    elif y >= (240-rayon):
        if (plateforme_x-rayon) < x < (plateforme_x+50-rayon):
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (plateforme_x+40+rayon) < x < (plateforme_x+60-rayon):
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
        elif (plateforme_x-rayon) > x > (plateforme_x-20+rayon):
            vitesse_balle_x = vitesse_balle_x*2
            vitesse_balle_y = -vitesse_balle_y
        elif (plateforme_x+60-rayon) > x:
                vie -= 1
                balle = False
        elif x > (plateforme_x+50-rayon):
                vie -= 1
                balle = False
    return x, y


def brique_supression():

    global x, y, brique_x, brique_y, vitesse_balle_x, vitesse_balle_y, score, brique1
    for i in range(0, len(brique_x)):
        if (brique_x[i]+30+2) >= x >= (brique_x[i]-2) and y == (brique_y[i] + 8+2):
            brique_x.pop(i)
            brique_y.pop(i)
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
            score += 50
            break
        elif (brique_x[i]+30+2) >= x >= (brique_x[i]-2) and (brique_y[i]-2) < y < (brique_y[i] + 8+2):
            brique_x.pop(i)
            brique_y.pop(i)
            vitesse_balle_x = -vitesse_balle_x
            vitesse_balle_y = vitesse_balle_y
            score += 50
            break
        elif (brique_x[i]+30+2) >= x >= (brique_x[i]-2) and (brique_y[i]-2) == y:
            brique_x.pop(i)
            brique_y.pop(i)
            vitesse_balle_x = vitesse_balle_x
            vitesse_balle_y = -vitesse_balle_y
            score += 50
            break
    if len(brique_x) == 0:
        brique1 = False
    return brique_x, brique_y, vitesse_balle_x, vitesse_balle_y


def update():

    global plateforme_x, plateforme_y, balle_liste, x, y, balle, vie, bx, by, bxx, byy, brique_x, brique_y
    plateforme_x, plateforme_y = plateforme_deplacement(plateforme_x, plateforme_y)
    if balle is False:
        x, y = (plateforme_x+20), (plateforme_y-3)
    if pyxel.btnr(pyxel.KEY_SPACE):
        balle = True
    if balle is True:
        x, y = balle_deplacement(x, y)
        brique_supression()


def draw():

    pyxel.cls(0)
    if brique1 is True:
        if vie > 0:
            for n in range(0, len(brique_x)):
                bxx = brique_x[n]
                byy = brique_y[n]
                pyxel.rect(bxx, byy, 30, 8, 3)
            pyxel.text(200, 10, "score : %s " % str(score), 7)
            pyxel.text(200, 20, "vie : %s " % str(vie), 7)
            pyxel.circ(x, y, rayon, 2)
            pyxel.rect(plateforme_x, plateforme_y, 40, 8, 1)
            pyxel.tri(plateforme_x, plateforme_y, plateforme_x, (plateforme_y+7), (plateforme_x-20), (plateforme_y+7), 1)
            pyxel.tri((plateforme_x+40), plateforme_y, (plateforme_x+40), (plateforme_y + 7), (plateforme_x+60), (plateforme_y + 7), 1)
        else:
            pyxel.text(100, 118, "GAME OVER !", 7)
            pyxel.text(98, 128, "Tu as perdu.", 7)
    else:
        pyxel.text(108, 118, "BRAVO !", 7)
        pyxel.text(98, 128, "Tu as gagne.", 7)


pyxel.run(update, draw)
