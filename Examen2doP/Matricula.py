from tkinter import *
import tkinter as tk
from tkinter import messagebox

def mostrarMatricula():
    messagebox.showinfo("Creacion de matricula","Tu matricula es: ")
    

ventana= Tk()
ventana.title("Creacion de matriculas")
ventana.geometry("500x500")

seccion1= Frame(ventana,bg="#d8f7ba")
seccion1.pack(expand= True, fill= 'both')

titulo= Label(seccion1, text="Creacion de matriculas")

var1= tk.StringVar()
lblno= Label(seccion1,text="Ingrese su nombre:  ").pack()
txtno= Entry(seccion1,textvariable=var1).pack()

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

var6= tk.StringVar()
lblaa= Label(seccion1,text="Ingrese el año actual: ").pack()
txtaa= Entry(seccion1,textvariable=var6).pack()

var7= tk.StringVar()
lbldg= Label(seccion1, text="Ingresa solo 3 numero: ").pack()
txtdg= Entry(seccion1, textvariable=var7).pack()

botonComprobar= Button(seccion1,text="Generar",command=mostrarMatricula)
botonComprobar.pack()

def getanioactual(self):
    return self.__aa
def setanioactual(self, aa):
    self.__aa= aa
    
def getanionaci(self):
    return self.__an
def setanionaci(self, an):
    self.__an= an

def getnombre(self):
    return self.__no
def setnombre(self,no):
    self.__no= no
    
def getapellidop(self):
    return self.__ap
def setapellidop(self,ap):
    self.__ap= ap  
 
def getapellidom(self):
    return self.__am
def setapellidom(self,am):
    self.__am= am

def getdigito(self):
    return self.__dg
def setdigito(self,dg):
    self.__dg= dg
    
def getcarrera(self):
    return self.__dg
def setcarrera(self,ca):
    self.__ca= ca


ventana.mainloop()