import pyxel
import random

neige_list = []

def ajout_neige():
    x = random.randint(0, pyxel.width)
    y = 0
    size = random.randint(1, 3)
    neige_list.append({"x": x, "y": y, "size": size})

def update():
    if pyxel.frame_count % 1 == 0:
        ajout_neige()
    
    for flocon in neige_list:
        flocon["y"] += flocon["size"] * 0.5
    
    neige_list[:] = [flocon for flocon in neige_list if flocon["y"] < pyxel.height]

def draw():
    pyxel.cls(0)
    
    for flocon in neige_list:
        pyxel.pset(flocon["x"], flocon["y"], 7)

pyxel.init(128, 128)
pyxel.run(update, draw)