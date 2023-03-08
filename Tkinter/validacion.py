from validacion import *
from tkinter import Tk,Button,Frame,Label,Entry,messagebox

def ingresar():
    messagebox.showinfo("Informacion","Te informo que todo fallo con exito")
    messagebox.showerror("Error","Perdon te falle!!")
    print(messagebox.askokcancel("Pregunta","Seguro que quieres a guardar algo"))
    print(messagebox.askyesnocancel("Pregunta2","Seguro que quieres a guardar algo"))
    print(messagebox.askquestion("Pregunta2","Seguro que quieres a guardar algo"))