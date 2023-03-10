from tkinter import *
import tkinter as tk

def conprobarContra(contra):
    largo = False
    mayus = False
    numer = False
    if len(contra) > 8:
        

ventana= Tk()
ventana.title("Verificacion de contraseñas")
ventana.geometry("500x250")

seccion1= Frame(ventana)
seccion1.pack(expand= True, fill= 'both', bg="#d8f7ba")

titulo= Label(seccion1, text="Verificacion de contraseñas")

var1= tk.StringVar()
lblContra= Label(seccion1,text="Contraseña: ").pack()
txtContra= Entry(seccion1, show="*",textvariable=var1).pack()

botonComprobar= Button(seccion1,text="Comprobar")
botonComprobar.pack()

ventana.mainloop()