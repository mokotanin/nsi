import pyxel
import random

ECRAN_L = 200
ECRAN_H = 200
FPS = 60
CPT_ETOILES = 80


class Etoiles:
    # arrière plan étoilé

    def __init__(self) -> None:
        self.x = pyxel.rndi(0, ECRAN_L)
        self.y = pyxel.rndi(0, ECRAN_H)
        self.color = pyxel.rndi(5, 7)
        self.speed = (pyxel.rndf(0.0, 1.0) - 4 + self.color) / 4

    def update(self) -> None:
        self.y += self.speed

    def draw(self) -> None:
        if pyxel.rndi(1, 3) == 1:
            pyxel.pset(self.x, self.y, self.color)


class Vaisseau:
    # vaisseau du joueur
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.left_limit = 10
        self.right_limit = 174
        self.speed = 1

    def move(self) -> None:
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            if self.x < self.right_limit:
                self.x += self.speed

        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            if self.x > self.left_limit:
                self.x -= self.speed

    def draw(self) -> None:
        if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
            if self.x < self.right_limit:
                pyxel.blt(self.x, self.y, 0, 32, 16, 16, 16)
            else:
                pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)
        elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
            if self.x > self.left_limit:
                pyxel.blt(self.x, self.y, 0, 48, 16, 16, 16)
            else:
                pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)
        else:
            pyxel.blt(self.x, self.y, 0, 16, 16, 16, 16)


class Missile:
    # missile tiré par le vaisseau

    def __init__(self, x: int, y: int, color: int = 10) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.speed = 5
        self.active = True

    def update(self) -> None:
        self.y -= self.speed
        if self.y < 0:
            self.active = False

    def draw(self) -> None:
        if self.active:
            pyxel.rect(self.x, self.y, 2, 5, self.color)


class Explosion:
    # animation d'explosion

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.frame = 0
        self.duree = 15  # 3 frames * 5 sprites

    def update(self) -> None:
        self.frame += 1

    def draw(self) -> None:
        if self.frame < self.duree:
            sprite_index = self.frame // 3
            sprite_x = sprite_index * 16
            pyxel.blt(self.x, self.y, 0, sprite_x, 112, 16, 16)

    def is_active(self) -> bool:
        return self.frame < self.duree

class Explosion_Epic:
    # animation d'explosion épique

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.frame = 0
        self.duree = 30  # 3 frames * 10 sprites

    def update(self) -> None:
        self.frame += 1

    def draw(self) -> None:
        if self.frame < self.duree:
            sprite_index = self.frame // 3
            sprite_x = sprite_index * 16
            pyxel.blt(self.x, self.y, 0, sprite_x, 144, 32, 32)

    def is_active(self) -> bool:
        return self.frame < self.duree

class Ennemi:
    # ennemi du jeu

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.left_limit = 10
        self.right_limit = 174
        self.direction = 1  # 1 = droite, -1 = gauche
        self.active = True

    def check_collision(self, missile_x: int, missile_y: int) -> bool:
        # vérifie si un missile touche l'ennemi (zone de collision)
        if (self.x <= missile_x <= self.x + 16 and 
            self.y <= missile_y <= self.y + 16):
            self.active = False
            return True
        return False
    
    def update(self) -> None:
        # fait bouger l'ennemi horizontalement
        self.x += self.direction
        if self.x >= self.right_limit or self.x <= self.left_limit:
            self.direction *= -1  # change de direction

    def draw(self) -> None:
        if self.active:
            pyxel.blt(self.x, self.y, 0, 0, 64, 16, 16)

class Jeu:
    # jeu en lui-même

    def __init__(self) -> None:
        pyxel.init(
            ECRAN_L,
            ECRAN_H,
            title="Space Invaders",
            quit_key=pyxel.KEY_F,
            fps=FPS
        )
        pyxel.load("kani.pyxres")

        self.player = Vaisseau(90, 160)
        self.ennemis = []
        self.missiles = []
        self.missile_epic = []
        self.stars = []
        self.explosions = []
        self.missile_cooldown = 0
        self.points = 0
        self.vies = 3
        self.score = 0

        # crée les étoiles
        for i in range(CPT_ETOILES):
            self.stars.append(Etoiles())

        pyxel.run(self.update, self.draw)

    def tirer(self) -> None:
        # gère le cooldown du tir
        if self.missile_cooldown > 0:
            self.missile_cooldown -= 1

    def tirer_epic(self) -> None:
        # gère les tirs épiques et normaux
        if pyxel.btn(pyxel.KEY_R):
            missile_x = self.player.x + 7
            missile_y = self.player.y
            self.player.speed = 2  # augmente la vitesse du vaisseau
            self.missile_epic.append(Missile(missile_x, missile_y, 8))
        else:
            self.player.speed = 1  # réinitialise la vitesse du vaisseau

        if pyxel.btn(pyxel.KEY_SPACE):
            if self.missile_cooldown == 0:
                missile_x = self.player.x + 7
                missile_y = self.player.y
                self.missiles.append(Missile(missile_x, missile_y, 10))
                self.missile_cooldown = 60

    def apparition(self) -> None:
        # gère l'apparition des ennemis
        if len(self.ennemis) < 5:
            if random.randint(0, 100) < 2:  # 2% de chance d'apparition par frame
                new_ennemi_x = random.randint(10, 174)
                new_ennemi_y = random.randint(10, 50)
                self.ennemis.append(Ennemi(new_ennemi_x, new_ennemi_y))

        elif len(self.ennemis) == 0:  # Si aucun ennemi n'est présent, en fait apparaître un nouveau
            new_ennemi_x = random.randint(10, 174)
            new_ennemi_y = random.randint(10, 50)
            self.ennemis.append(Ennemi(new_ennemi_x, new_ennemi_y))

    def check_missile_collisions(self, missile_list: list) -> None:
        # vérifie les collisions entre les missiles et les ennemis
        for missile in missile_list[:]:
            for ennemi in self.ennemis[:]:
                if ennemi.active and ennemi.check_collision(missile.x, missile.y):
                    missile.active = False
                    self.explosions.append(Explosion(ennemi.x, ennemi.y))
                    self.ennemis.remove(ennemi)
                    break
            if not missile.active:
                missile_list.remove(missile)

    def update(self) -> None:
        # met à jour la logique du jeu
        self.player.move()
        for ennemi in self.ennemis:
            ennemi.update()
        self.tirer()
        self.tirer_epic()
        self.apparition()

        # met à jour tous les missiles
        for missile in self.missiles:
            missile.update()
        for missile in self.missile_epic:
            missile.update()

        # vérifie les collisions avec tous les missiles
        self.check_missile_collisions(self.missiles)
        self.check_missile_collisions(self.missile_epic)

        # met à jour les étoiles
        for star in self.stars:
            star.update()
            if star.y > ECRAN_H:
                self.stars.remove(star)
                self.stars.append(Etoiles())

        # met à jour les explosions
        for explosion in self.explosions[:]:
            explosion.update()
            if not explosion.is_active():
                self.explosions.remove(explosion)

    def draw(self) -> None:
        # dessine tous les éléments du jeu
        pyxel.cls(0)
        
        for star in self.stars:
            star.draw()
        
        self.player.draw()
        
        for ennemi in self.ennemis:
            ennemi.draw()

        for missile in self.missiles:
            missile.draw()

        for missile in self.missile_epic:
            missile.draw()

        for explosion in self.explosions:
            explosion.draw()

if __name__ == "__main__":
    Jeu()