from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana= Tk()
ventana.title("CRUD de usaurios")
ventana.geometry("500x300")

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)
pestana4= ttk.Frame(panel)

#pestaña1: Formulario de registro
titulo= Label(pestana1, text="Registro usuarios",fg="blue",font=("Modern",18)).pack()

varNom= tk.StringVar()
lblNom= Label(pestana1,text="Nombre: ").pack()
txtNom= Entry(pestana1,textvariable=varNom).pack()

varCor= tk.StringVar()
lblCor= Label(pestana1,text="Correo: ").pack()
txtCor= Entry(pestana1,textvariable=varCor).pack()

varCon= tk.StringVar()
lblCon= Label(pestana1,text="Contraseña: ").pack()
txtCon= Entry(pestana1,textvariable=varCon).pack()

btnGuardar= Button(pestana1, text='Guardar usuario').pack()

panel.add(pestana1, text="Formulario Usuario")
panel.add(pestana2, text="Buscar Usuario")
panel.add(pestana3, text="consultar Usuarios")
panel.add(pestana4, text="Actualizar Usuarios")

ventana.mainloop()