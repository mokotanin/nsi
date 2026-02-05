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
meilleur_score=0
ennemis=[]
ennemis_max=4
cooldown_missile=0
explosions=[]
explosions_epique=[]
renardcanardé=[]
missile_e=[]
cooldown_e=0
monsieur_renard_x=0
monsieur_renard_y=208
état=0
frame=0
duree=30
x = 200
y = 92
bouge = False
last_trigger = -1

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

def missiles(): # fonction des missiles tirés par le renard
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

def missile_intercontinental(): # fonction du missile rayon laser tiré par le renard
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

def mechant(): # fonction de déplacement des ennemis et de leur affichage
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

def missiles_mechant(): # fonction des oeufs tirés par les ennemis
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
        pyxel.blt(e[0], e[1], 0, 6, 197,4,6)

def collision(): # fonction de collision entre les missiles du joueur et les ennemis, et entre les missiles des ennemis et le joueur
    global missile, missile_epic, ennemis, score, explosions, player_hit_timer, combo, combo_timer, poule_de_la_vitesse, vies
    
    for m in missile[:]: # quand le renard touche un ennemi avec un missile classique
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
    for mp in missile_epic[:]: # quand le renard touche un ennemi avec un missile intercontinental
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
    
    for me in missile_e[:]: # quand un oeuf touche le renard
        if (me[0]<posx+16 and me[0]+2>posx and
            me[1]<posy+16 and me[1]+5>posy):

            renardcanardé.append([posx,posy,0])

            if me in missile_e:
                missile_e.remove(me)
            pyxel.play(2, 2)
            vies-=1
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

def renardcanarde():
    global renardcanardé

    for exp in renardcanardé[:]:
        frame=exp[2]
        duree=30
    
        if frame < duree:
            pyxel.blt(exp[0],exp[1],0,16,208,16,16)
            exp[2]+=1
        else:
            renardcanardé.remove(exp)

def VIES():
    global vies,état,score
    if vies==3:
        pyxel.blt(5,5,0,0,3,20,10)
    elif vies==2:
        pyxel.blt(5,5,0,5,3,20,10)
    elif vies==1:
        pyxel.blt(5,5,0,12,3,20,10)
    elif vies==0:
        état=2
        vies=3
        score=0

def mort():
    pyxel.blt(63,70,0,0,240,80,16)
    pyxel.text(65,130,'Press E to restart',10)

def SCORE():
    pyxel.text(140,5,'SCORE='+str(score),3)

def MEILLEURSCORE():
    global score, meilleur_score
    if meilleur_score>=score:
        pyxel.text(50,5,'MEILLEUR SCORE='+str(meilleur_score),3)
    elif meilleur_score<score:
        meilleur_score=score
        pyxel.text(50,5,'MEILLEUR SCORE='+str(meilleur_score),3)

'''def kfcbonus():
    global score,x,y,bouge,last_trigger
    current_trigger = score // 12
    if (score % 12 == 0 and current_trigger != last_trigger and not bouge):
        bouge = True
        x = 200  
        last_trigger = current_trigger
        if bouge:
            x -= 2
            if x < -16:  
                bouge = False
        if bouge:
            pyxel.blt(x,y,0,33,162,16,16)'''

def update():
    global état
    if état==0:
        if pyxel.btnp(pyxel.KEY_E):
            état=1
    elif état==1:
            update_jeu()
    elif état==2:
        if pyxel.btnp(pyxel.KEY_E):
            état=1

def draw():
    pyxel.cls(0)
    if état==0:
        accueil()
    elif état==1:
        draw_jeu()
    elif état==2:
        mort()

def update_jeu():
    deplacement()
    missiles()
    missile_intercontinental()
    mechant()
    missiles_mechant()
    collision()
    explosions_f()
    explosions_epic()
    renardcanarde()
    VIES()
    MEILLEURSCORE()
    #kfcbonus()
def draw_jeu():
    deplacement()
    missiles()
    missile_intercontinental()
    mechant()
    missiles_mechant()
    collision()
    explosions_f()
    explosions_epic()
    renardcanarde()
    SCORE()
    VIES()
    MEILLEURSCORE()
    #kfcbonus()
pyxel.run(draw,update)