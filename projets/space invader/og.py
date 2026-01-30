import pyxel
import random

pyxel.init(200,200,title="Poules Invaders (très dangereux)",quit_key=pyxel.KEY_F,fps=60)
pyxel.load("kani.pyxres")
posx=90
posy=160
missile=[]
missile_epic=[]
limited=174
limiteg=10
vitesse=1
points=0
vies=3
score=0
ennemis=[]
ennemis_max=4
cooldown_missile=0
explosions=[]
explosions_epique=[]

"""class Vaisseau:
    def __init__(self,x:int,y:int) -> None:
        self.x=x
        self.y=y
        self.limited=174
        self.limiteg=10
        self.speed=1
    
    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            if self.x<self.limited:
                self.x+=self.speed
            elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
                if self.x>self.limiteg:
                    self.x-=self.speed
    def draw(self) -> None:
            if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
                if self.x < self.limited:
                    pyxel.blt(self.x, self.y, 0, 32, 16, 16, 16)
                else:
                    pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)
            elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
                if self.x > self.limiteg:
                    pyxel.blt(self.x, self.y, 0, 48, 16, 16, 16)
                else:
                    pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)
            else:
                pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)"""

def deplacement():
    global posx
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        if posx<limited:
            posx+=vitesse
            pyxel.blt(posx,posy,0,32,16,16,16)
        else:
            pyxel.blt(posx,posy,0,16,16,16,16)
    elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
        if posx>limiteg:
            posx-=vitesse
            pyxel.blt(posx,posy,0,48,16,16,16)
        else:
            pyxel.blt(posx,posy,0,16,16,16,16)
    else:
        pyxel.blt(posx,posy,0,16,16,16,16)

"""def missiles():
    global missile
    global cooldown_missile
    missilex=posx+7
    missiley=posy
    if pyxel.btnr(pyxel.KEY_SPACE) and cooldown_missile==0:
        missile.append([missilex,missiley])
        pyxel.play(0, 0)
        cooldown_missile=60
    if cooldown_missile>0:
        cooldown_missile-=1
    for m in missile:
        m[1]-=5
        pyxel.rect(m[0],m[1],2,5,10)"""

class missiless():
    def __init__(self,):
        global posx,posy,score,explosions
        self.missile=[]
        self.cooldown=0
        self.x=posx+7
        self.y=posy
    def update(self):
        if pyxel.btnr(pyxel.KEY_SPACE) and self.cooldown==0:
            self.missile.append([self.x,self.y])
            pyxel.play(0,0)
            self.cooldown=60
        if self.cooldown>0:
            self.cooldown-=1
    def draw(self):
        for m in self.missile:
            m[1]-=5
            pyxel.rect(m[0],m[1],2,5,10)

"""class missile_epicsmr():
    def __init__(self) -> None:
        self.missile_epic=[]
        self.vitesse=1 # à changer aussi
        self.x=x+7 # non
        self.y=90

    def update(self):
        if pyxel.btn(pyxel.KEY_R):
            self.missile_epic.append([self.x,self.y])
            self.vitesse=2
        else:
            vitesse=1
    
    def draw(self):
        for m in self.missile_epic:
            m[1]-=5
            pyxel.rect(m[0],m[1],2,5,8)"""



def missile_intercontinental():                                                
    global missile_epic
    global vitesse
    missilex=posx+7
    missiley=posy
    if pyxel.btn(pyxel.KEY_R):
        missile_epic.append([missilex,missiley])
        vitesse=2
    else:
        vitesse=1
    for m in missile_epic:
        m[1]-=5
        pyxel.rect(m[0],m[1],2,5,8)
        
class mechants():
    def __init__(self):
        self.max=5
        self.limiteg=10
        self.limited=174
    
    def update(self):
        if len(ennemis) < self.max:
            self.busy_y=[e[1] for e in ennemis]
            self.free_y=[y for y in range(16,80,16) if y not in self.busy_y]
            if self.free_y:
                ennemis.append([pyxel.rndi(10,174),random.choice(self.free_y),random.choice([-1,1])])

    def draw(self):
        for i in ennemis[:]:
            i[0] += i[2]
            if i[0] <= self.limiteg or i[0] >= self.limited:
                i[2]= -i[2]
            pyxel.blt(i[0], i[1], 0, 0, 64, 16, 16)

"""def mechant():
    if len(ennemis) < ennemis_max:
        occuper_y = [e[1] for e in ennemis]
        libre_y = [y for y in range(16, 80, 16) if y not in occuper_y]
        
        if libre_y:
            ennemis.append([pyxel.rndi(10, 174), random.choice(libre_y), random.choice([-1, 1])])
    
    for i in ennemis[:]:
        i[0] += i[2]
        
        if i[0] <= limiteg or i[0] >= limited:
            i[2] = -i[2]
        pyxel.blt(i[0], i[1], 0, 0, 64, 16, 16)"""

def collision():
    global missile, missile_epic, ennemis, score, explosions
    
    for m in missile[:]:
        for e in ennemis[:]:
            if (m[0] < e[0] + 16 and 
                m[0] + 2 > e[0] and 
                m[1] < e[1] + 16 and 
                m[1] + 5 > e[1]):
                
                # Collision !
                explosions.append([e[0], e[1], 0])
                
                if m in missile:
                    missile.remove(m)
                if e in ennemis:
                    ennemis.remove(e)
                pyxel.play(1, 1)
                score += 10
                break
    for mp in missile_epic[:]:
        for e in ennemis[:]:
            if (mp[0] < e[0] + 16 and 
                mp[0] + 2 > e[0] and 
                mp[1] < e[1] + 16 and 
                mp[1] + 5 > e[1]):
                
                explosions_epique.append([e[0], e[1], 0])
                
                if mp in missile_epic:
                    missile_epic.remove(mp)
                if e in ennemis:
                    ennemis.remove(e)
                pyxel.play(3, 3)
                score += 10
                break

def explosions_f():
    global explosions

    for exp in explosions[:]:
        frame = exp[2]
        duree = 15
        
        if frame < duree:
            sprite_index = frame // 3
            sprite_x = sprite_index * 16
            pyxel.blt(exp[0], exp[1], 0, sprite_x, 112, 16, 16)
            exp[2] += 1 
        else:
            explosions.remove(exp)

def explosions_epic():
    global explosions_epique

    for exp in explosions_epique[:]:
        frame = exp[2]
        duree = 30
        
        if frame < duree:
            sprite_index = frame // 3
            sprite_x = sprite_index * 16
            pyxel.blt(exp[0], exp[1], 0, sprite_x, 144, 16, 16)
            exp[2] += 1 
        else:
            explosions_epique.remove(exp)

class App:
    def __init__(self):
        
        # toutes les classes
        self.mechant=mechants()
        self.missile=missiless()
        #self.missile_epicc=missile_epicsmr()

        # toutes les variables globales
        self.x=90
        self.posy=160
        self.missile_epic=[]
        self.limited=174
        self.limiteg=10
        self.vitesse=1
        self.points=0
        self.score=0
        self.ennemis=[]
        self.ennemis_max=4
        self.cooldown_missile=0
        self.explosions=[]
        self.explosions_epique=[]
    def update(self):
        deplacement()
        #missiles()
        self.missile.update()        
        missile_intercontinental()
        #mechant()
        collision()
        explosions_f()
        explosions_epic()
        self.mechant.update()
        #self.missile_epicc.update()
    def draw(self):
        pyxel.cls(0)
        deplacement()
        self.mechant.draw()
        self.missile.draw()
        #self.missile_epicc.draw()

app = App()
pyxel.run(app.draw, app.update)