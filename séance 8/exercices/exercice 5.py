from tkinter import *
from random import *

def nl():
    NbDes=int(Valeur.get())
    resultat=""
    total=0
    max=int(nfd.get())
    for i in range(0,NbDes):
        nb=randint(1,max)
        total=total+nb
        resultat=resultat+str(nb)
        if i<NbDes-1:
            resultat=resultat+', '
    Texte.set('Résultat -> '+resultat+' = '+str(total))
window=Tk()
window.title("Exo5")
window.geometry("200x200")
window.config(background="black")

Frame1 = Frame(window,borderwidth=2,relief=GROOVE)
Frame1.pack(side=LEFT,padx=10,pady=10)

Frame2 = Frame(window,borderwidth=2,relief=GROOVE,width=400)
Frame2.pack(side=LEFT,padx=10,pady=10)

Label(Frame1,text="Choix du nombre de dés :").pack(padx=10,pady=10)
Valeur=StringVar()
Valeur.set(3.0)

boite=Spinbox(Frame1,from_=1,to=6,increment=1,textvariable=Valeur,width=5)
boite.pack(padx=30,pady=10)

nfd=StringVar()
echelle=Scale(Frame1,from_=6,to=20,resolution=1,orient=HORIZONTAL,length=200,width=20,label="Choix du nombre de faces de dés",tickinterval=20,variable=nfd)
echelle.pack(padx=10,pady=10)

Texte=StringVar()
nl()
LabelResultat=Label(Frame2,textvariable=Texte,fg='red',background="black")
LabelResultat.pack(side=TOP,padx=60,pady=35)
BoutonL=Button(Frame2,text='Lancer',command=nl)
BoutonL.pack(side=LEFT,padx=15,pady=15)
BoutonQ=Button(Frame2,text='Quitter',command=quit)
BoutonQ.pack(side=RIGHT,padx=15,pady=33)

window.mainloop()