from tkinter import *

window=Tk()
window.title("Exo3")
window.geometry("300x100")

def carre():
    Resultat.set("Carré ="+str(float(Valeur.get())**2))

Valeur=StringVar()
Valeur.set(5.0)

boite=Spinbox(window,from_=0.0,to=100.0,increment=0.5,textvariable=Valeur,width=5,command=carre)
boite.place(x=100,y=0)

Resultat=StringVar()
carre()
Resultatat=Label(window,textvariable=Resultat)
Resultatat.place(x=100,y=30)

window.mainloop()