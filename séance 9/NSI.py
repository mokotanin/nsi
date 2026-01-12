import pyxel

HAUTEUR = 100
LARGEUR = 40
ESPACE = 10

X_START = 20
Y_START = 20


def nsi():
    x = X_START
    y = Y_START

    # N
    pyxel.line(x, y, x, y + HAUTEUR, 7)
    pyxel.line(x, y, x + LARGEUR, y + HAUTEUR, 7)
    pyxel.line(x + LARGEUR, y, x + LARGEUR, y + HAUTEUR, 7)

    x += LARGEUR + ESPACE

    # S
    pyxel.line(x + LARGEUR, y, x, y, 7)
    pyxel.line(x, y, x, y + HAUTEUR // 2, 7)
    pyxel.line(x, y + HAUTEUR // 2, x + LARGEUR, y + HAUTEUR // 2, 7)
    pyxel.line(x + LARGEUR, y + HAUTEUR // 2, x + LARGEUR, y + HAUTEUR, 7)
    pyxel.line(x + LARGEUR, y + HAUTEUR, x, y + HAUTEUR, 7)

    x += LARGEUR + ESPACE

    # I
    pyxel.line(x, y, x + LARGEUR, y, 7)
    pyxel.line(x + LARGEUR // 2, y, x + LARGEUR // 2, y + HAUTEUR, 7)
    pyxel.line(x, y + HAUTEUR, x + LARGEUR, y + HAUTEUR, 7)


def draw():
    pyxel.cls(0)
    nsi()


def update():
    pass


pyxel.init(220, 160, title="NSI")
pyxel.run(update, draw)
