import pyxel
pyxel.init(600, 600, title="Mermoz")
pyxel.image(0).load(0, 0, "NSI.png")
pyxel.image(1).load(0, 0, "logo_mermoz.png")
change=0

def update():
    global change
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    if pyxel.btnp(pyxel.KEY_L):
        change=1

def draw():
    pyxel.cls(0)
    taille_img=(pyxel.image(change).width,pyxel.image(change).height)
    pyxel.blt(pyxel.width//2-(taille_img[0]//2),0,change,0,0,taille_img[0],taille_img[1])
pyxel.run(update, draw)