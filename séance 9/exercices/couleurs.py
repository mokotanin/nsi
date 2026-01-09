import pyxel
pyxel.init(320, 320, title="couleurs")

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()

def draw():
    pyxel.cls(0)
    for i in range(16):
        pyxel.rect(20*i, 0, 20, 20, i)

pyxel.run(update, draw)