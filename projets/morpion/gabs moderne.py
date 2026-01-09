from tkinter import*
from tkinter import messagebox
from tkinter import ttk
import sv_ttk
import pywinstyles, sys

class Theme: #classe pour les couleurs
    dark_bg="#1c1c1c"

morpion = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]#variable morpion et joueur
joueur = 1

def Effacer():#fonction effaçant la grille
    canvas.delete("all")

def Grille(morpion):
    Effacer()
    for i in range(1, 3):#dessine la grille
        canvas.create_line(0, i*200, 600, i*200, width=3,fill="white")
        canvas.create_line(i*200, 0, i*200, 600, width=3,fill="white")
    for d in range(3):#affiche à tour de rôle, rond, croix
        for j in range(3):
            x = j * 200
            y = d * 200
            if morpion[d][j] == 1: #rond
                canvas.create_oval(x+20, y+20, x+180, y+180, width=4, outline="blue")
            elif morpion[d][j] == 2: #croix
                canvas.create_line(x+20, y+20, x+180, y+180, width=4, fill="red")
                canvas.create_line(x+180, y+20, x+20, y+180, width=4, fill="red")

def pointeur(event):
    global joueur
    ligne = event.y // 200
    colonne = event.x // 200
    print("Case choisie :", ligne, colonne)#affiche dans la console les cases choisies
    if morpion[ligne][colonne] == 0:#si la case sélectionnée est vide(=0), alors
        morpion[ligne][colonne] = joueur
        if joueur == 1:#passage joueur 1 à 2
            joueur = 2
        else:
            joueur = 1
        Grille(morpion)#exécute fonction grille
        g = gagnant(morpion)#affiche les différents issues par messagebox
        if g == 1:
            messagebox.showinfo("Fin de partie", "Le joueur 1 a gagné !")
        elif g == 2:
            messagebox.showinfo("Fin de partie", "Le joueur 2 a gagné !")
        elif g == 3:
            messagebox.showinfo("Fin de partie", "Match nul !")

    else:
        messagebox.showwarning("Coup interdit", "Cette case est déjà occupée !")

def Rejouer():#remet variables à zero, relance programme, quand boutton rejouer appyué
    global morpion, joueur
    morpion = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
    joueur = 1
    Grille(morpion)

def gagnant(morpion):
    for i in range(3):#quand lignes ou colonnes complètes par un joueur
        if morpion[i][0] == morpion[i][1] == morpion[i][2] != 0:
            Rejouer()  # relance automatiquement après victoire
            return morpion[i][0]
        if morpion[0][i] == morpion[1][i] == morpion[2][i] != 0:
            Rejouer()  # relance automatiquement après victoire
            return morpion[0][i]
    if morpion[0][0] == morpion[1][1] == morpion[2][2] != 0:#quand diagonales complètes par un joueur
        Rejouer()  # relance automatiquement après victoire
        return morpion[0][0]
    if morpion[0][2] == morpion[1][1] == morpion[2][0] != 0:
        Rejouer()  # relance automatiquement après victoire
        return morpion[0][2]
    for ligne in morpion:#match nul
        if 0 in ligne:
            return 0

    Rejouer()  # relance automatiquement après match nul
    return 3
#programme principal
window =Tk()
window.title("Morpion")
window.geometry("700x700")
sv_ttk.set_theme("dark")

def apply_theme_to_titlebar(window): #style de la barre de titre
    version = sys.getwindowsversion()

    if version.major == 10 and version.build >= 22000:
        pywinstyles.change_header_color(window, Theme.dark_bg if sv_ttk.get_theme() == "dark" else "#fafafa")
    elif version.major == 10:
        pywinstyles.apply_style(window, "dark" if sv_ttk.get_theme() == "dark" else "normal")
        window.wm_attributes("-alpha", 0.99)
        window.wm_attributes("-alpha", 1)
apply_theme_to_titlebar(window)

style = ttk.Style()
style.configure("canvas.TFrame", background=Theme.dark_bg)
canvas =Canvas(window, width=600, height=600, bg=Theme.dark_bg,relief=SUNKEN)
canvas.pack()

canvas.bind("<Button-1>", pointeur)#attribution souris à variable pointeur

frame = ttk.Frame(window)
frame.pack(pady=10)

bouttonrejouer = ttk.Button(frame, text="Rejouer", command=Rejouer)#bouttons
bouttonrejouer.pack(side="left", padx=10)

bouttonquitter = ttk.Button(frame, text="Quitter", command=window.destroy)
bouttonquitter.pack(side="left", padx=10)

Grille(morpion)#lancement du programme
window.mainloop()