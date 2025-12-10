from tkinter import *
window=Tk()
window.title("Exo6")
window.geometry("500x400")
window.config(background="black")

l=480
h=320
Canvas=Canvas(window,width=l,height=h,bg="black")
Canvas.pack(padx=5,pady=5)

go=Button(window,text="Go",command=cercle)
go.pack(side=LEFT,padx=10,pady=10)

effacer=Button(window,text='Effacer',command=effacer)
effacer.pack(side=LEFT,ipadx=15,pady=5)

quitter=Button(window,text='Quitter',command=quit)
quitter.pack(side=RIGHT,padx=5,pady=20)

window.mainloop()