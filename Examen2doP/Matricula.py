from tkinter import *
import tkinter as tk

ventana= Tk()
ventana.title("Creacion de matriculas")
ventana.geometry("500x250")

seccion1= Frame(ventana,bg="#d8f7ba")
seccion1.pack(expand= True, fill= 'both')

titulo= Label(seccion1, text="Creacion de matriculas")

var1= tk.StringVar()
lbln1= Label(seccion1,text="Ingrese su nombre:  ").pack()
txtn1= Entry(seccion1,textvariable=var1).pack()

var2= tk.StringVar()
lblap= Label(seccion1,text="Ingrese su apellido paterno: ").pack()
txtap= Entry(seccion1,textvariable=var2).pack()
var3= tk.StringVar()
lblam= Label(seccion1,text="Ingrese su apellido materno: ").pack()
txtam= Entry(seccion1,textvariable=var3).pack()

var4= tk.StringVar()
lblan= Label(seccion1,text="Ingrese su año de nacimiento: ").pack()
txtan= Entry(seccion1,textvariable=var4).pack()

var5= tk.StringVar()
lblca= Label(seccion1,text="Ingrese su carrera: ").pack()
txtca= Entry(seccion1,textvariable=var5).pack()


botonComprobar= Button(seccion1,text="Generar")
botonComprobar.pack()

ventana.mainloop()