import pyxel
import random

couleurs= {
    'rouge':8,
    'vert':11,
    'bleu':12,
    'jaune':10,
    'rose':14,
}

def genere_jeu(nombre_couleur,taille):
    combinaison=[]
    nombre_couleur=len(couleurs)
    taille=5
    for i in range(taille):
        combinaison.append(random.choice(list(couleurs.values())))
    return combinaison

def sasie_utilisateur(taille):
    combinaison_utilisateur=[]
    couleur=input("saisissez une couleur")
    for i in range(taille):
        combinaison_utilisateur.append(couleur)
    return combinaison_utilisateur

def couleurBienPlace(jeu,saisie,tab):

def couleurMalPlace(jeu,saisie,tab):

def nbJetonPlace(jeu,saisie):

def jeu():
