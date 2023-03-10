from tkinter import *
from tkinter import messagebox
import tkinter as tk

def consultarSaldo():
    saldoActual=saldoIncial
    messagebox.showinfo("Consulta de saldo","Tu saldo es: ", + saldoActual)
    
def ingresarSaldo():
    saldoIncial=saldoIncial+ingresar
    messagebox.showinfo("Ingresar saldo","Tu saldo es: ", + saldoIncial)
    
def retirarSaldo():
    saldoIncial=saldoIncial-retiro
    messagebox.showinfo("Retirar saldo","Tu retiro de saldo es: ", + saldoActual)    
        
def depositarSaldo():
    saldoActual=saldoIncial+ingresar
    messagebox.showinfo("Consulta de saldo","Tu deposito de saldo es: ", + saldoActual)
           
saldoIncial=0
saldoActual=0
ingresar=0
retiro=0


ventana= Tk()
ventana.title("Caja Popular")
ventana.geometry("500x250")

seccion1= Frame(ventana, bg="#d8f7ba")
seccion1.pack(expand= True, fill= 'both')

titulo= Label(seccion1, text="Caja Popular")

var1= tk.StringVar()
lblCaja= Label(seccion1,text="Caja Popular").pack()
Label (ventana, text='\n').pack()
Label (ventana, text='\n').pack()


botonConsultar= Button(seccion1,text="consultar saldo",bg="#f2a668", command=consultarSaldo)
botonConsultar.pack()
botonConsultar= Button(seccion1,text="Ingresar saldo",bg="#cc9df5",command=ingresarSaldo)
botonConsultar.pack()
botonConsultar= Button(seccion1,text="Retirar saldo",bg="#9dbdf5",command=retirarSaldo)
botonConsultar.pack()
botonConsultar= Button(seccion1,text="deposiltar saldo",bg="#aff59d",command=depositarSaldo)
botonConsultar.pack()

ventana.mainloop()