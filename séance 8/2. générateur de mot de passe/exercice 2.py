from tkinter import *
from random import *

def NouveauLance():
    nb=randint(1,6)
    Texte.set("Résultats : "+str(nb))

window=Tk()
window.title("Exo2")
window.geometry("200x100")
window.config(bg="white")

BoutonLancer=Button(window,text="Lancer le dé",command=NouveauLance)
BoutonLancer.pack()

Texte=StringVar()
NouveauLance()

LabelResultat=Label(window,textvariable=Texte,bg="white")
LabelResultat.pack(padx=0,pady=0)

BoutonQuitter=Button(window,text="Quitter",command=quit)
BoutonQuitter.pack(padx=15,pady=5)

window.mainloop()