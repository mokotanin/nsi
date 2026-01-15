import pyxel

liste_couleurs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

couleur = 0

def carre():
    x = 50
    y = 50
    pyxel.rect(x, y, 50, 50, liste_couleurs[couleur])

def update():
    global couleur
    
    if pyxel.btnp(pyxel.MOUSE_BUTTON_RIGHT):
        couleur = (couleur + 1) % len(liste_couleurs)
    
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
        couleur = (couleur - 1) % len(liste_couleurs)

def draw():
    pyxel.cls(0)
    carre()

pyxel.init(400, 300)
pyxel.run(update, draw)