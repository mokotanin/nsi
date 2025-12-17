from tkinter import *
from time import *

def h():
    heure.set(strftime('%H:%M:%S'))
    window.after(1000,h)

window=Tk()
window.title=("Exo7")
window.geometry("200x50")
window.config(background='#1C1C1C')

heure = StringVar()
aff_h=Label(window,font=('Rubik',20,),bg="#1C1C1C",fg='white',textvariable=heure)
aff_h.pack(ipadx=50,ipady=50)
h()
window.mainloop()