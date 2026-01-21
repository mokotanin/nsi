import pyxel
import random

pyxel.init(400,300,title="neige",fps=400)
neige=[]

def ajout_neige():
    global neige
    if pyxel.frame_count % 30 == 0:
        taille=random.randint(1,8)
        x=random.randint(0,pyxel.width)
        neige.append([x,0,taille])
def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    global neige
    ajout_neige()
    for flocon in neige:
        flocon[1] += 0.1
        if flocon[1]>pyxel.height:
            neige.remove(flocon)
    neige = [flocon for flocon in neige if flocon[1] < pyxel.height]
def draw():
    pyxel.cls(0)
    for flocon in neige:
        pyxel.circ(flocon[0],flocon[1],flocon[2],7)
pyxel.run(update, draw)