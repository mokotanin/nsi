from tkinter import *
from string import *
from random import *
import tkinter as tk
from tkinter import ttk
import sv_ttk
import pywinstyles, sys
tempo=20

window=Tk()
window.title("Exo8")
window.geometry("500x400")
window.config(background="black")

sv_ttk.set_theme('dark')
style = ttk.Style()

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

def cercle():
    global x,y,depx,depy,tempo
    r=20
    x=x+depx
    y=y+depy
    if x>l-r or y<r:
        depx=-depx
    if y>h-r or y<r:
        depy=-depy
    effacer()
    Canvas.create_oval(x-r,y-r,x+r,y+r,outline='brown',fill='#fafafa')
    window.after(tempo,cercle)

def effacer():
    Canvas.delete(ALL)

l=480
h=320
x=int(l/2)
y=int(h/2)
depx=randint(1,5)
depy=randint(1,5)
Canvas=Canvas(window,width=l,height=h,bg="#1C1C1C")
Canvas.pack(padx=5,pady=5)

def fast():
    global tempo
    if tempo>5:
        tempo=tempo-5
    else:
        tempo=5
def slow():
    global tempo
    tempo=tempo+5

style.configure("button.TButton", font=("Rubik", 10))
go=ttk.Button(window,text="Go",command=cercle,style="button.TButton")
go.pack(side=LEFT,fill=X)

fast=ttk.Button(window,text="Plus vite",command=fast,style="button.TButton")
fast.pack(side=LEFT,fill=X)

slow=ttk.Button(window,text="Plus doucement",command=slow,style="button.TButton")
slow.pack(side=LEFT,fill=X)

window.mainloop()