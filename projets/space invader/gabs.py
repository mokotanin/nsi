# ============================================================================
# FOX INVADERS - Jeu de tir spatial à la poule personne
# ============================================================================

import pyxel
import random

# Initialisation de Pyxel (moteur graphique)
pyxel.init(200, 200, title="Space Invaders", quit_key=pyxel.KEY_F, fps=60)
pyxel.load("kani.pyxres")

# ============================================================================
# VARIABLES DE JEU
# ============================================================================

# Position du joueur
pos_x = 90
pos_y = 160

# Projectiles
projectiles_joueur = []
projectiles_laser = []
projectiles_ennemis = []

# Limites de l'écran
limite_droite = 174
limite_gauche = 10
limite_bas = 220

# Paramètres de mouvement
vitesse = 1
multiplicateur_vitesse = 0.1

# État du joueur
vies = 3
score = 0
meilleur_score = 0
combo = 0
combo_timer = 0
couleur_combo_texte = 7

# Ennemis
ennemis = []
ennemis_max = 4

# Cooldowns des tirs
attente_tir = 0
attente_tir_ennemi = 0

# Explosions
explosions = []
explosions_laser = []
explosions_impact = []

# Sprites du joueur
sprite_joueur_x = 0
sprite_joueur_y = 208

# États du jeu (0: accueil, 1: jeu, 2: mort)
état = 0


# ============================================================================
# AFFICHAGE D'ACCUEIL
# ============================================================================

def afficher_accueil():
    # Affiche l'écran de titre
    pyxel.blt(75, 70, 0, 0, 224, 46, 16)
    pyxel.text(68, 90, "Press E to start", 15)


# ============================================================================
# GESTION DU JOUEUR
# ============================================================================

def maj_position_joueur():
    global pos_x
    # Déplacement vers la droite
    if pyxel.btn(pyxel.KEY_RIGHT) or pyxel.btn(pyxel.KEY_D):
        if pos_x < limite_droite:
            pos_x += vitesse
        pyxel.blt(pos_x, pos_y, 0, sprite_joueur_x, sprite_joueur_y, 16, 16)
    # Déplacement vers la gauche
    elif pyxel.btn(pyxel.KEY_LEFT) or pyxel.btn(pyxel.KEY_Q):
        if pos_x > limite_gauche:
            pos_x -= vitesse
        pyxel.blt(pos_x, pos_y, 0, sprite_joueur_x, sprite_joueur_y, 16, 16)
    # Affichage du joueur immobile
    else:
        pyxel.blt(pos_x, pos_y, 0, sprite_joueur_x, sprite_joueur_y, 16, 16)


def maj_projectiles_joueur():
    global projectiles_joueur
    global attente_tir
    
    # Coordonnées du nouveau projectile
    projectile_x = pos_x + 7
    projectile_y = pos_y
    
    # Création d'un nouveau projectile si touche ESPACE appuyée et cooldown terminé
    if pyxel.btnr(pyxel.KEY_SPACE) and attente_tir == 0:
        projectiles_joueur.append([projectile_x, projectile_y])
        pyxel.play(0, 0)
        attente_tir = 60
    
    # Décompte du cooldown
    if attente_tir > 0:
        attente_tir -= 1
    
    # Mouvement et affichage des projectiles
    for projectile in projectiles_joueur:
        projectile[1] -= 5
        pyxel.rect(projectile[0], projectile[1], 2, 5, 10)


def maj_projectiles_laser():
    global projectiles_laser
    global vitesse
    
    # Coordonnées du laser
    projectile_x = pos_x + 7
    projectile_y = pos_y
    
    # Création de laser si touche R maintenue - augmente aussi la vitesse
    if pyxel.btn(pyxel.KEY_R):
        projectiles_laser.append([projectile_x, projectile_y])
        vitesse = 2
    else:
        vitesse = 1
    
    # Mouvement et affichage des lasers
    for projectile in projectiles_laser:
        projectile[1] -= 5
        pyxel.rect(projectile[0], projectile[1], 2, 5, 8)


# ============================================================================
# GESTION DES ENNEMIS
# ============================================================================

def maj_ennemis():
    # Création de nouveaux ennemis si la limite maximale n'est pas atteinte
    if len(ennemis) < ennemis_max:
        positions_y_occupees = [e[1] for e in ennemis]
        positions_y_libres = [y for y in range(16, 80, 16) if y not in positions_y_occupees]

        # Placement aléatoire d'un nouvel ennemi à une position libre
        if positions_y_libres:
            ennemis.append(
                [pyxel.rndi(10, 174), random.choice(positions_y_libres), random.choice([-1, 1])]
            )

    # Mise à jour de chaque ennemi
    for ennemi in ennemis[:]:
        # Déplacement horizontal
        ennemi[0] += ennemi[2]

        # Inversion de direction aux limites de l'écran
        if ennemi[0] <= limite_gauche or ennemi[0] >= limite_droite:
            ennemi[2] = -ennemi[2]
        
        # Affichage de l'ennemi
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 176, 16, 16)
        
        # Déplacement vers le bas
        ennemi[1] += multiplicateur_vitesse
        
        # Suppression si l'ennemi dépasse le bas de l'écran
        if ennemi[1] >= limite_bas:
            ennemis.remove(ennemi)


def maj_projectiles_ennemis():
    global projectiles_ennemis, attente_tir_ennemi, ennemis
    
    # Sélection aléatoire d'un ennemi qui tire
    if ennemis:
        tireur = random.choice(ennemis)
        projectile_x = tireur[0] + 7
        projectile_y = tireur[1] + 16
        
        # Création d'un projectile si le cooldown est écoulé
        if attente_tir_ennemi == 0:
            projectiles_ennemis.append([projectile_x, projectile_y])
            pyxel.play(0, 0)
            attente_tir_ennemi = 100
    
    # Décompte du cooldown
    if attente_tir_ennemi > 0:
        attente_tir_ennemi -= 1
    
    # Mouvement et affichage des projectiles ennemis
    for projectile in projectiles_ennemis:
        projectile[1] += 1
        pyxel.blt(projectile[0], projectile[1], 0, 0, 32, 10, 10, 0)


# ============================================================================
# GESTION DES COLLISIONS
# ============================================================================

def verifier_collisions():
    global projectiles_joueur, projectiles_laser, ennemis, score, explosions
    global explosions_laser, projectiles_ennemis, explosions_impact, combo, combo_timer
    global multiplicateur_vitesse, vies

    # Collision entre projectiles normaux et ennemis
    for projectile in projectiles_joueur[:]:
        for ennemi in ennemis[:]:
            if (
                projectile[0] < ennemi[0] + 16
                and projectile[0] + 2 > ennemi[0]
                and projectile[1] < ennemi[1] + 16
                and projectile[1] + 5 > ennemi[1]
            ):
                # Création d'une explosion
                explosions.append([ennemi[0], ennemi[1], 0])
                if projectile in projectiles_joueur:
                    projectiles_joueur.remove(projectile)
                if ennemi in ennemis:
                    ennemis.remove(ennemi)
                pyxel.play(1, 1)
                # Augmentation du combo et score
                combo += 1
                if combo % 10 == 0:
                    multiplicateur_vitesse += 0.1
                combo_timer = 120
                score += 1
                break

    # Collision entre projectiles laser et ennemis (points bonus)
    for projectile_laser in projectiles_laser[:]:
        for ennemi in ennemis[:]:
            if (
                projectile_laser[0] < ennemi[0] + 16
                and projectile_laser[0] + 2 > ennemi[0]
                and projectile_laser[1] < ennemi[1] + 16
                and projectile_laser[1] + 5 > ennemi[1]
            ):
                # Création d'une explosion laser
                explosions_laser.append([ennemi[0], ennemi[1], 0])
                if projectile_laser in projectiles_laser:
                    projectiles_laser.remove(projectile_laser)
                if ennemi in ennemis:
                    ennemis.remove(ennemi)
                pyxel.play(3, 3)
                # Augmentation du combo et score (5 points au lieu de 1)
                combo += 1
                if combo % 10 == 0:
                    multiplicateur_vitesse += 0.1
                combo_timer = 120
                score += 5
                break

    # Collision entre projectiles ennemis et joueur
    for projectile_ennemi in projectiles_ennemis[:]:
        if (
            projectile_ennemi[0] < pos_x + 16
            and projectile_ennemi[0] + 2 > pos_x
            and projectile_ennemi[1] < pos_y + 16
            and projectile_ennemi[1] + 5 > pos_y
        ):
            # Dégâts au joueur
            explosions_impact.append([pos_x, pos_y, 0])
            if projectile_ennemi in projectiles_ennemis:
                projectiles_ennemis.remove(projectile_ennemi)
            pyxel.play(2, 2)
            combo = 0
            vies -= 1
            break

    # Collision directe entre ennemi et joueur
    for ennemi in ennemis[:]:
        if (
            ennemi[0] < pos_x + 16
            and ennemi[0] + 16 > pos_x
            and ennemi[1] < pos_y + 16
            and ennemi[1] + 16 > pos_y
        ):
            # Dégâts au joueur
            explosions_impact.append([pos_x, pos_y, 0])
            if ennemi in ennemis:
                ennemis.remove(ennemi)
            pyxel.play(2, 2)
            combo = 0
            vies -= 1
            break


# ============================================================================
# GESTION DES EXPLOSIONS
# ============================================================================

def afficher_explosions():
    global explosions
    for explosion in explosions[:]:
        frame = explosion[2]
        duree = 60

        # Animation de l'explosion (4 sprites différents)
        if frame < duree:
            sprite_index = frame // 10
            sprite_x = sprite_index * 16
            pyxel.blt(explosion[0], explosion[1], 0, sprite_x, 112, 16, 16)
            explosion[2] += 1
        # Suppression de l'explosion quand l'animation est terminée
        else:
            explosions.remove(explosion)


def afficher_explosions_laser():
    global explosions_laser
    for explosion in explosions_laser[:]:
        frame = explosion[2]
        duree = 60

        # Animation de l'explosion laser
        if frame < duree:
            sprite_index = frame // 5
            sprite_x = sprite_index * 16
            pyxel.blt(explosion[0], explosion[1], 0, sprite_x, 144, 16, 16)
            explosion[2] += 1
        else:
            explosions_laser.remove(explosion)


def afficher_explosions_impact():
    global explosions_impact
    for explosion in explosions_impact[:]:
        frame = explosion[2]
        duree = 60

        # Animation d'impact centrée sur le joueur
        if frame < duree:
            explosion[0] = pos_x
            explosion[1] = pos_y
            sprite_x = 16
            pyxel.blt(explosion[0], explosion[1], 0, sprite_x, 208, 16, 16)
            explosion[2] += 1
        else:
            explosions_impact.remove(explosion)


# ============================================================================
# AFFICHAGE DE L'INTERFACE
# ============================================================================

def afficher_interface():
    global combo_timer, combo, couleur_combo_texte, score, vies, état
    
    # Affichage des vies restantes
    for i in range(vies):
        pyxel.blt(5 + i * 5, 25, 0, 0, 3, 10, 10, 0)

    # Gestion de la fin de partie
    if vies == 0:
        état = 2
        vies = 3
        score = 0


def afficher_ecran_mort():
    # Affichage du texte Game Over
    pyxel.blt(63, 70, 0, 0, 240, 80, 16)
    pyxel.text(65, 130, "Press E to restart", 10)


def afficher_score():
    # Affichage du score
    pyxel.text(140, 5, "SCORE=" + str(score), 3)


def afficher_meilleur_score():
    global score, meilleur_score, combo, combo_timer, couleur_combo_texte
    
    # Mise à jour du meilleur score
    if meilleur_score >= score:
        pyxel.text(50, 5, "MEILLEUR SCORE=" + str(meilleur_score), 3)
    elif meilleur_score < score:
        meilleur_score = score
        pyxel.text(50, 5, "MEILLEUR SCORE=" + str(meilleur_score), 3)
    
    # Changement de couleur du texte selon le combo (arc-en-ciel)
    if combo < 10:
        couleur_combo_texte = 7  # Blanc
    elif combo < 20:
        couleur_combo_texte = 10  # Jaune
    elif combo < 30:
        couleur_combo_texte = 9  # Orange
    elif combo < 40:
        couleur_combo_texte = 8  # Rouge
    elif combo < 50:
        couleur_combo_texte = 14  # Rose
    else:
        # Animation arc-en-ciel rapide pour les très hauts combos
        couleurs_arc_en_ciel = [8, 9, 10, 11, 12, 13, 14, 15]
        couleur_combo_texte = couleurs_arc_en_ciel[
            (combo // 5) % len(couleurs_arc_en_ciel)
        ]

    # Affichage du score et du combo
    pyxel.text(5, 5, "SCORE=" + str(score), 3)
    pyxel.text(5, 15, "COMBO=" + str(combo), couleur_combo_texte)

    # Décrément du timer du combo
    if combo_timer > 0:
        combo_timer -= 1
    # Réinitialisation du combo si le timer expire
    else:
        combo = 0


# ============================================================================
# BOUCLES PRINCIPALES
# ============================================================================

def mettre_a_jour():
    global état
    
    # État 0: Écran d'accueil
    if état == 0:
        if pyxel.btnp(pyxel.KEY_E):
            état = 1
    # État 1: Jeu en cours
    elif état == 1:
        mettre_a_jour_jeu()
    # État 2: Écran de mort
    elif état == 2:
        if pyxel.btnp(pyxel.KEY_E):
            état = 1


def dessiner():
    global multiplicateur_vitesse
    
    # Effacement de l'écran
    pyxel.cls(0)
    
    # État 0: Écran d'accueil
    if état == 0:
        afficher_accueil()
    # État 1: Jeu en cours
    elif état == 1:
        dessiner_jeu()
    # État 2: Écran de mort
    elif état == 2:
        afficher_ecran_mort()
        ennemis.clear()
        multiplicateur_vitesse = 0.1


def mettre_a_jour_jeu():
    # Mise à jour de tous les objets du jeu
    maj_position_joueur()
    maj_projectiles_joueur()
    maj_projectiles_laser()
    maj_ennemis()
    maj_projectiles_ennemis()
    verifier_collisions()
    afficher_explosions()
    afficher_explosions_laser()
    afficher_explosions_impact()
    afficher_interface()
    afficher_meilleur_score()


def dessiner_jeu():
    # Mise à jour et affichage de tous les objets
    maj_position_joueur()
    maj_projectiles_joueur()
    maj_projectiles_laser()
    maj_ennemis()
    maj_projectiles_ennemis()
    verifier_collisions()
    afficher_explosions()
    afficher_explosions_laser()
    afficher_explosions_impact()
    afficher_score()
    afficher_interface()
    afficher_meilleur_score()


# ============================================================================
# LANCEMENT DU JEU
# ============================================================================
# Boucle principale: dessiner() pour l'affichage, mettre_a_jour() pour la logique
pyxel.run(dessiner, mettre_a_jour)
