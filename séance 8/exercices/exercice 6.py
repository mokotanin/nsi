from tkinter import *
from string import *
from random import *
import tkinter as tk
from tkinter import ttk
import sv_ttk
import pywinstyles, sys

window=Tk()
window.title("Exo6")
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
    r=20
    x=randint(r,l-r)
    y=randint(r,h-r)
    Canvas.create_oval(x-r,y-r,x+r,y+r,outline='beige',fill='#fafafa')

def effacer():
    Canvas.delete(ALL)

l=480
h=320
Canvas=Canvas(window,width=l,height=h,bg="black")
Canvas.pack(padx=5,pady=5)

style.configure("button.TButton", font=("Rubik", 16))
go=ttk.Button(window,text="Go",command=cercle,style="button.TButton")
go.pack(side=LEFT,padx=10,pady=10,fill=X)

effacer=ttk.Button(window,text='Effacer',command=effacer)
effacer.pack(side=LEFT,ipadx=15,pady=5)

quitter=ttk.Button(window,text='Quitter',command=quit)
quitter.pack(side=RIGHT,padx=5)

window.mainloop()