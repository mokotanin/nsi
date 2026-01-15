import pyxel

posx=10
posy=10

def move():
    global posx,posy
    if pyxel.btn(pyxel.KEY_RIGHT):
        posx+=1
    if pyxel.btn(pyxel.KEY_LEFT):
        posx-=1
    if pyxel.btn(pyxel.KEY_UP):
        posy-=1
    if pyxel.btn(pyxel.KEY_DOWN):
        posy+=1
    if posx>180:
        posx=180
    if posx<0:
        posx=0
    if posy>180:
        posy=180
    if posy<0:
        posy=0

def carre():
    pyxel.rect(posx, posy, 20, 20, 1)

pyxel.init(200, 200)

def draw():
    pyxel.cls(0)
    carre()

def update():
    move()
    pass
pyxel.run(draw,update)