from tkinter import *
from tkinter import messagebox

# Variables globales
joueur_actuel = "X"
grille = [""] * 9  # 9 cases vides
boutons = []

def cliquer_case(numero_case):
    """Quand un joueur clique sur une case"""
    global joueur_actuel
    
    # Si la case est vide
    if grille[numero_case] == "":
        # Mettre le symbole du joueur dans la case
        grille[numero_case] = joueur_actuel
        boutons[numero_case].config(text=joueur_actuel)
        
        # Vérifier si ce joueur a gagné
        if verifier_victoire():
            messagebox.showinfo("Fin du jeu", f"Le joueur {joueur_actuel} gagne !")
            return
        
        # Vérifier si la grille est pleine (match nul)
        if "" not in grille:
            messagebox.showinfo("Fin du jeu", "Match nul !")
            return
        
        # Changer de joueur
        joueur_actuel = "O" if joueur_actuel == "X" else "X"
        label_info.config(text=f"Tour du joueur {joueur_actuel}")

def verifier_victoire():
    """Vérifie si le joueur actuel a gagné"""
    # Toutes les combinaisons gagnantes possibles
    lignes_gagnantes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Lignes horizontales
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Lignes verticales
        [0, 4, 8], [2, 4, 6]               # Diagonales
    ]
    
    # Vérifier chaque ligne gagnante
    for ligne in lignes_gagnantes:
        if (grille[ligne[0]] == joueur_actuel and 
            grille[ligne[1]] == joueur_actuel and 
            grille[ligne[2]] == joueur_actuel):
            return True
    return False

def nouvelle_partie():
    """Recommencer une nouvelle partie"""
    global joueur_actuel, grille
    
    joueur_actuel = "X"
    grille = [""] * 9
    
    # Vider tous les boutons
    for bouton in boutons:
        bouton.config(text="")
    
    label_info.config(text="Tour du joueur X")

# Créer la fenêtre
fenetre = Tk()
fenetre.title("Morpion")
fenetre.geometry("1000x700")

# Titre
Label(fenetre, text="Morpion", font=("Arial", 24, "bold")).pack(pady=10)

# Cadre pour la grille de jeu
cadre_grille = Frame(fenetre)
cadre_grille.pack(pady=10)

# Créer les 9 boutons de la grille (3x3)
for i in range(9):
    bouton = Button(cadre_grille, text="", width=10, height=5,
                   font=("Arial", 18, "bold"),
                   command=lambda num=i: cliquer_case(num))
    ligne = i // 3  # Calculer la ligne (0, 1, ou 2)
    colonne = i % 3  # Calculer la colonne (0, 1, ou 2)
    bouton.grid(row=ligne, column=colonne, padx=2, pady=2)
    boutons.append(bouton)

# Label pour afficher quel joueur doit jouer
label_info = Label(fenetre, text="Tour du joueur X", font=("Arial", 14))
label_info.pack(pady=10)

# Bouton pour recommencer
Button(fenetre, text="Nouvelle Partie", font=("Arial", 12), 
       bg="lightblue", command=nouvelle_partie).pack(pady=5)

# Lancer la fenêtre
fenetre.mainloop()
