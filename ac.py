from tkinter import *
import webbrowser
window=Tk()
window.title("Mon Application")
window.geometry("800x800")
window.minsize(400,300)
window.config(background="#0050FF")
frame=Frame(window,bg="#0050FF",bd=1,relief=SUNKEN)
frame2=Frame(window,bg="#6E6E6E",bd=1,relief=SUNKEN)
frame.pack(side=TOP)
frame2.pack(expand=YES)
label_titre=Label(frame,text="Première application",font=("Courrier",40),bg="#0050FF",fg="white")
label_titre.pack(side=TOP)
label_sous_titre=Label(frame2,text="Bonjour tout le monde",font=("Courrier",20),bg="#0050FF",fg="white")
label_sous_titre.pack(side=TOP)

def ouvrir_nsi():
    webbrowser.open_new("http://gisele.bareux.free.fr/NSI1.htm")
bouton_nsi=Button(frame2,text="NSI",font=("Courrier",20),bg="#0050FF",fg="white",command=ouvrir_nsi)
bouton_nsi.pack(pady=50,fill=X,padx=50)

window.mainloop()