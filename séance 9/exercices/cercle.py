import random
import pyxel

cercles = []

def cercle():
    x=random.randint(50,350)
    y=random.randint(50,250)
    r=random.randint(10,50)
    col=random.randint(1,15)
    cercles.append((x, y, r, col))

def nya():
    if pyxel.btnp(pyxel.KEY_SPACE):
        cercle()
    if pyxel.btnp(pyxel.KEY_KP_MEMSUBTRACT) and cercles:
        cercles.pop()

pyxel.init(400, 300)

def draw():
    pyxel.cls(0)
    for x, y, r, col in cercles:
        pyxel.circ(x, y, r, col)
        
def update():
    nya()
    
pyxel.run(update, draw)