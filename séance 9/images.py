import pyxel

pyxel.init(600,600,title="Mermoz")
pyxel.image(0).load(0,0,"logo_mermoz.png")
pyxel.image(1).load(0,0,"NSI.png")

def update():
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
def draw():
    pyxel.cls(0)
    taille=255
    pyxel.blt(pyxel.width//2-(taille//2),0,0,0,0,taille,236)
    pyxel.blt(pyxel.width//2-(taille//2),300,1,0,0,taille,154)
pyxel.run(update,draw)