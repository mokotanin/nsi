import random
import pyxel

cercles = []

def cercle(): # cercle aléatoire
    x=random.randint(50,350)
    y=random.randint(50,250)
    r=random.randint(10,50)
    col=random.randint(1,15)
    cercles.append((x, y, r, col))

def nya():
    if pyxel.btnp(pyxel.KEY_SPACE): # crée des cercles
        cercle()
    if pyxel.btnp(pyxel.KEY_BACKSPACE) and cercles: # supprimer des cercles
        cercles.pop(random.randint(0,len(cercles)-1))

pyxel.init(400, 300)

def draw():
    pyxel.cls(0)
    for x, y, r, col in cercles:
        pyxel.circ(x, y, r, col)
        
def update():
    nya()
    
pyxel.run(update, draw)