import pyxel
import random

ECRAN_L = 200
ECRAN_H = 200
FPS = 60
CPT_ETOILES = 80

# joueur
posx = 90
posy = 160
vitesse = 1
limited = 174
limiteg = 10

missile = []
missile_epic = []
ennemis = []
explosions = []
etoiles = []

cooldown = 0
ennemi_speed = 0


def creer_etoile():
    # crée une nouvelle étoile
    x = pyxel.rndi(0, ECRAN_L)
    y = pyxel.rndi(0, ECRAN_H)
    color = pyxel.rndi(5, 7)
    speed = (pyxel.rndf(0.0, 1.0) - 4 + color) / 4
    return [x, y, color, speed]


def etoiles_maj():
    # met à jour et dessine les étoiles
    for e in etoiles[:]:
        e[1] += e[3]
        if e[1] > ECRAN_H:
            etoiles.remove(e)
            etoiles.append(creer_etoile())
    for e in etoiles:
        if pyxel.rndi(1, 3) == 1:
            pyxel.pset(e[0], e[1], e[2])


def deplacement():
    # déplacement du vaisseau
    global posx
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        if posx < limited:
            posx += vitesse
            pyxel.blt(posx, posy, 0, 32, 16, 16, 16)
        else:
            pyxel.blt(posx, posy, 0, 16, 16, 16, 16)
    elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
        if posx > limiteg:
            posx -= vitesse
            pyxel.blt(posx, posy, 0, 48, 16, 16, 16)
        else:
            pyxel.blt(posx, posy, 0, 16, 16, 16, 16)
    else:
        pyxel.blt(posx, posy, 0, 16, 16, 16, 16)


def missiles():
    # tir normal avec cooldown
    global missile, cooldown
    missilex = posx + 7
    missiley = posy
    if cooldown > 0:
        cooldown -= 1
    if pyxel.btnr(pyxel.KEY_SPACE) and cooldown == 0:
        missile.append([missilex, missiley])
        cooldown = 60
    for m in missile[:]:
        m[1] -= 2
        if m[1] < 0:
            missile.remove(m)
        else:
            pyxel.rect(m[0], m[1], 2, 5, 10)


def missile_intercontinental():
    # tir épique
    global missile_epic, vitesse
    missilex = posx + 7
    missiley = posy
    if pyxel.btn(pyxel.KEY_R):
        vitesse = 2
        missile_epic.append([missilex, missiley])
    else:
        vitesse = 1
    for m in missile_epic[:]:
        m[1] -= 5
        if m[1] < 0:
            missile_epic.remove(m)
        else:
            pyxel.rect(m[0], m[1], 2, 5, 8)


def creer_ennemi(x, y):
    # crée un nouvel ennemi [x, y, direction, actif]
    return [x, y, 1, True]


def apparition_ennemis():
    # gère l'apparition des ennemis
    ennemis_actifs = sum(1 for e in ennemis if e[3])
    if ennemis_actifs < 5 and random.randint(0, 100) < 3:
        ennemis.append(creer_ennemi(random.randint(10, 174), random.randint(10, 50)))
    if ennemis_actifs == 0:
        ennemis.append(creer_ennemi(random.randint(10, 174), random.randint(10, 50)))


def ennemis_maj():
    # met à jour et dessine les ennemis
    global ennemi_speed
    apparition_ennemis()
    ennemi_speed += 1
    for e in ennemis[:]:
        if e[3]:
            if ennemi_speed % 3 == 0:
                e[0] += e[2]
            if e[0] >= limited or e[0] <= limiteg:
                e[2] *= -1
    for e in ennemis:
        if e[3]:
            pyxel.blt(e[0], e[1], 0, 0, 64, 16, 16)


def explosions_maj():
    # met à jour et dessine les explosions [x, y, frame]
    for ex in explosions[:]:
        ex[2] += 1
        if ex[2] >= 15:
            explosions.remove(ex)
    for ex in explosions:
        sprite_index = ex[2] // 3
        sprite_x = sprite_index * 16
        pyxel.blt(ex[0], ex[1], 0, sprite_x, 112, 16, 16)


def collision_missiles():
    # collisions missiles/ennemis [x, y, direction, actif]
    for m in missile[:]:
        for e in ennemis[:]:
            if e[3] and (e[0] <= m[0] <= e[0] + 16 and e[1] <= m[1] <= e[1] + 16):
                e[3] = False
                explosions.append([e[0], e[1], 0])
                if m in missile:
                    missile.remove(m)
                break

    for m in missile_epic[:]:
        for e in ennemis[:]:
            if e[3] and (e[0] <= m[0] <= e[0] + 16 and e[1] <= m[1] <= e[1] + 16):
                e[3] = False
                explosions.append([e[0], e[1], 0])
                if m in missile_epic:
                    missile_epic.remove(m)
                break


def update():
    deplacement()
    missiles()
    missile_intercontinental()
    ennemis_maj()
    collision_missiles()
    etoiles_maj()
    explosions_maj()


def draw():
    pyxel.cls(0)
    etoiles_maj()
    deplacement()
    missiles()
    missile_intercontinental()
    ennemis_maj()
    explosions_maj()


pyxel.init(200, 200, title="Space Invaders", quit_key=pyxel.KEY_F, fps=60)
pyxel.load("kani.pyxres")

for i in range(CPT_ETOILES):
    etoiles.append(creer_etoile())

pyxel.run(update, draw)