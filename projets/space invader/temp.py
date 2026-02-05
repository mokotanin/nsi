import pyxel
import random

pyxel.init(200,200,title="Space Invaders",quit_key=pyxel.KEY_F,fps=60)
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
missile_e=[]
cooldown_e=0
monsieur_renard_x=0
monsieur_renard_y=208
player_hit_timer=0
explosions_omelettee=[]
état=0
def accueil():
    pyxel.blt(75,70,0,0,224,46,16)
    pyxel.text(68,90,'Press E to start',15)
def deplacement():
    global posx
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        if posx<limited:
            posx+=vitesse
            pyxel.blt(posx,posy,0,monsieur_renard_x,monsieur_renard_y,16,16)
        else:
            pyxel.blt(posx,posy,0,monsieur_renard_x,monsieur_renard_y,16,16)
    elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
        if posx>limiteg:
            posx-=vitesse
            pyxel.blt(posx,posy,0,monsieur_renard_x,monsieur_renard_y,16,16)
        else:
            pyxel.blt(posx,posy,0,monsieur_renard_x,monsieur_renard_y,16,16)
    else:
        pyxel.blt(posx,posy,0,monsieur_renard_x,monsieur_renard_y,16,16)

def missiles():
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
        pyxel.rect(m[0],m[1],2,5,10)


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

def mechant():
    if len(ennemis) < ennemis_max:
        occuper_y = [e[1] for e in ennemis]
        libre_y = [y for y in range(16, 80, 16) if y not in occuper_y]
        
        if libre_y:
            ennemis.append([pyxel.rndi(10, 174), random.choice(libre_y), random.choice([-1, 1])])
    
    for i in ennemis[:]:
        i[0] += i[2]
        
        if i[0] <= limiteg or i[0] >= limited:
            i[2] = -i[2]
        pyxel.blt(i[0], i[1], 0, 0, 176, 16, 16)

def missiles_mechant():
    global missile_e, cooldown_e, ennemis
    if ennemis:
        shooter = random.choice(ennemis)
        missilex_e = shooter[0] + 7
        missiley_e = shooter[1] + 16
        if cooldown_e == 0:
            missile_e.append([missilex_e, missiley_e])
            pyxel.play(0, 0)
            cooldown_e = 100
    if cooldown_e > 0:
        cooldown_e -= 1
    for e in missile_e:
        e[1] += 1
        pyxel.rect(e[0], e[1], 2, 5, 7)

def collision():
    global missile, missile_epic, ennemis, score, explosions, player_hit_timer
    
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
                score += 1
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
                score += 5
                break
    
    for me in missile_e[:]:
        if (me[0]<posx+16 and me[0]+2>posx and
            me[1]<posy+16 and me[1]+5>posy):

            explosions_omelettee.append([posx, posy, 0])

            if me in missile_e:
                missile_e.remove(me)
            pyxel.play(2, 2)
            score -=1000
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

def explosions_omelette():
    global explosions_omelette

    for kfc in explosions_omelettee[:]:
        frame = kfc[2]
        duree=400

        if frame < duree:
            oeuf_index = frame // 5
            oeuf_x = oeuf_index * 16
            pyxel.blt(kfc[0], kfc[1], 0, oeuf_x, 224, 16, 16)
            kfc[2] += 1
        else:
            explosions_omelettee.remove(kfc)


def variables():
    pyxel.text(5,5,'SCORE='+str(score),3)
def update():
    global état
    if état==0:
        if pyxel.btnp(pyxel.KEY_E):
            état=1
        elif état==1:
            update_jeu()
def draw():
    pyxel.cls(0)
    if état==0:
        accueil()
    elif état==1:
        draw_jeu()
def update_jeu():
    deplacement()
    missiles()
    missile_intercontinental()
    mechant()
    missiles_mechant()
    collision()
    explosions_f()
    explosions_epic()
    explosions_omelette()

def draw_jeu():
    deplacement()
    missiles()
    missile_intercontinental()
    mechant()
    missiles_mechant()
    collision()
    explosions_f()
    explosions_epic()
    explosions_omelette()
    variables()
pyxel.run(draw,update)