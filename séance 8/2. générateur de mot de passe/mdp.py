from tkinter import *
from string import *
from random import *
import tkinter as tk
from tkinter import ttk
import sv_ttk
import pywinstyles, sys

window = Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")

sv_ttk.set_theme("dark")

def apply_theme_to_titlebar(window):
    version = sys.getwindowsversion()

    if version.major == 10 and version.build >= 22000:
        # Set the title bar color to the background color on Windows 11 for better appearance
        pywinstyles.change_header_color(window, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
    elif version.major == 10:
        pywinstyles.apply_style(window, "dark" if sv_ttk.get_theme() == "dark" else "normal")

        # A hacky way to update the title bar's color on Windows 10 (it doesn't update instantly like on Windows 11)
        window.wm_attributes("-alpha", 0.99)
        window.wm_attributes("-alpha", 1)

apply_theme_to_titlebar(window)

def generer_mdp():
    mdp_mini = 6
    mdp_maxi = 12
    c_a = ascii_letters + punctuation + digits
    mdp = "".join(choice(c_a) for _ in range(randint(mdp_mini, mdp_maxi)))
    champ_mdp.delete(0, END)
    champ_mdp.insert(0, mdp)

frame = Frame(window, padx=20, pady=20)
largeur = 300
longueur = 300

image = PhotoImage(file="séance 8\\2. générateur de mot de passe\\login.png").zoom(1).subsample(3)
canvas = Canvas(frame, width=largeur, height=longueur, bd=0, highlightthickness=0)
canvas.create_image(largeur/2, longueur/2, image=image)
canvas.grid(row=0, column=0)

frame_d = Frame(frame, padx=20, pady=20)

# Style titre
style = ttk.Style()
style.configure("Titre.TLabel", font=("Rubik", 24, "bold")) 
titre = ttk.Label(frame_d, text="Mot de passe", style="Titre.TLabel")
titre.pack()

# Style saisie
style.configure("Entry.TEntry", font=("Rubik", 18)) 
champ_mdp = ttk.Entry(frame_d, style="Entry.TEntry")
champ_mdp.pack()

# Style bouton
style.configure("Bouton.TButton", font=("Rubik", 16, "italic"))
BP_mdp = ttk.Button(frame_d, text="Générer le mot de passe", style="Bouton.TButton", command=generer_mdp)
BP_mdp.pack(fill=X, pady=20)

frame_d.grid(row=0, column=1)
frame.pack(expand=YES)

menu_barre = Menu(window)
menu_fichier = Menu(menu_barre, tearoff=0)
menu_fichier.add_command(label="Nouveau", command=generer_mdp)
menu_fichier.add_command(label="Quitter", command=window.quit)
menu_barre.add_cascade(label="Fichier", menu=menu_fichier)
window.config(menu=menu_barre)

window.mainloop()