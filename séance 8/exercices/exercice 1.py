import tkinter as tk
from tkinter import *

window=Tk()
window.title("Exo1")
window.geometry("300x100")

Frame=Frame(window,bg="white")
Frame.pack()
Label=Label(Frame,text="Bonjour tout le monde")
Label.pack()
Button=Button(Frame,text="Quitter",command=quit)
Button.pack()
window.mainloop()