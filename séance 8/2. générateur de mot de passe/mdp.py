from tkinter import *
from string import *
from random import *

window=Tk()
window.title("Générateur de mot de passe")
window.geometry("720x480")
window.config(background="#406599")

def generer_mdp():
    mdp_mini=6
    mdp_maxi=12
    c_a=ascii_letters + punctuation + digits
    mdp="".join(choice(c_a)for _ in range(randint(mdp_mini,mdp_maxi)))
    champ_mdp.delete(0,END)
    champ_mdp.insert(0,mdp)

frame=Frame(window, bg="#406599")
largeur=300
longueur=300
image=PhotoImage(file="login.png").zoom(1).subsample(3)
canvas=Canvas(frame,width=largeur,height=longueur,bg="#406599",bd=0,highlightthickness=0)
canvas.create_image(largeur/2,longueur/2,image=image)
canvas.grid(row=0,column=0)

frame_d=Frame(frame,bg="#406599")
titre=Label(frame_d,text="Mot de passe",font=("Courrier",20),bg="#406599",fg="white")
titre.pack()
champ_mdp=Entry(frame_d,font=("Courrier",20),bg="white",fg="black")
champ_mdp.pack()

BP_mdp=Button(frame_d,text="Générer le mot de passe",font=("Courrier",15),bg="#406599",fg="white",command=generer_mdp)
BP_mdp.pack(fill=X,pady=20)

frame_d.grid(row=0,column=1)
frame.pack(expand=YES)

menu_barre=Menu(window)
menu_fichier=Menu(menu_barre,tearoff=0)
menu_fichier.add_command(label="Nouveau",command=generer_mdp)
menu_fichier.add_command(label="Quitter",command=window.quit)
menu_barre.add_cascade(label="Fichier",menu=menu_fichier)
window.config(menu=menu_barre)

window.mainloop()