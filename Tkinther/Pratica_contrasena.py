import os
from tkinter import Entry,Label, Tk,Button,Frame

def login():
    vent=Tk()
    vent.title("Login")
    vent.geometry("500x500")
    Label (vent, text="Introduzca el correo electronico y contrasena").pack()
    
    global verifica_usuario
    global verifica_contra
    
    
    verifica_usuario= str()
    verifica_contra= str()
    
    global entrada_lusuario
    global entrada_lcontra
    
    Label (vent, text="Correo electronico:").pack()
    entrada_lusuario = Entry(vent, textv=verifica_usuario).pack()
    Label (vent, text="").pack()
    Label (vent, text="Conrasena:").pack()
    entrada_lcontra = Entry(vent, textv=verifica_contra).pack()
    Label (vent, text="").pack()
    botonIngresar= Button(seccion2,text="Ingresar",fg="white",bg="#a428c7", command = verifica_login).pack()
    
    seccion1= Frame(vent,bg="#97b7f7")
    seccion1.pack(expand=True,fill='both')

    seccion2= Frame(vent,bg="#97f7a5")
    seccion2.pack(expand=True,fill='both')

def verifica_login():
    usuariol= verifica_usuario.get()
    contra= verifica_contra.get()
    entrada_lusuario.delete(0, 100)
    entrada_lcontra.delete(0, 100)
    
    lista_a = os.lista_d
    if usuariol in lista_a:
        archivol = open(usuariol, "u")
        verifica = archivol.read().splitlines()
        if contra in verifica:
            exito_login()
        else:
            no_contra()
    else:
        no_usuario()        

def no_usuario():
    global ventana_nousuario
    ventana_nousuario.tittle("ERROR")
    ventana_nousuario.geometry("250x250")
    Label(ventana_nousuario, text="Usuario no encontrado").pack()
    Button(ventana_nousuario, text="OK", command=borrar_nousuario).pack()
    
def exito_login():
    global ventana_exito
    ventana_nousuario.tittle("EXITO")
    ventana_nousuario.geometry("250x250")
    Label(ventana_exito, text="Login finalizado con exito").pack()
    Button(ventana_exito, text="OK", command=borrar_exitol).pack()    
    
def no_contra():
    global ventana_nocontra
    ventana_nocontra.tittle("ERROR")
    ventana_nocontra.geometry("250x250")
    Label(ventana_nocontra, text="Contrasena incorrecta").pack()
    Button(ventana_nocontra, text="OK", command=borrar_nocontra).pack()    

def borrar_exitol():
    ventana_exito.destroy()

def borrar_nocontra():
    ventana_nocontra.destroy()
    
def borrar_nousuario():
    ventana_nousuario.destroy()