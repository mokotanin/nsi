from tkinter import *

def plus():
    Valeur.set(str(int(Valeur.get())+10))
def moins():
    Valeur.set(str(int(Valeur.get())-10))

window= Tk()
window.title("Exo 4") #titre de la fenêtre
window.geometry("400x200") #dimensions de la fenêtre
window.config(bg='white') #couleur du fond en RGB en hexadécimal
Valeur=StringVar()
Valeur.set(50)
echelle = Scale(window,from_=-100,to=100,resolution=10,orient=HORIZONTAL,length=300,
width=20, tickinterval=20, label="Curseur",variable=Valeur)

echelle.pack(padx=10,pady=10)
BP_plus=Button(window,text="+",command=plus)
BP_plus.pack(padx=0,pady=0)
BP_moins=Button(window,text="-",command=moins)
BP_moins.pack(padx=10,pady=10)
window.mainloop()