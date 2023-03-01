from tkinter import Tk,Button,Frame,messagebox

#5. Agregar funcion de mensaje
def mostrarmensaje():
    messagebox.showinfo("Informacion","Te informo que todo fallo con exito")
    messagebox.showerror("Error","Perdon te falle!!")
    print(messagebox.askokcancel("Pregunta","Seguro que quieres a guardar algo"))
    print(messagebox.askyesnocancel("Pregunta2","Seguro que quieres a guardar algo"))
    print(messagebox.askquestion("Pregunta2","Seguro que quieres a guardar algo"))
    
#6.funcion agregar botones
def agregarboton():
    botonVerde.config(text="+",bg="green",fg="white")
    botonNuevo= Button(seccion3,text="Boton Nuevo")
    botonNuevo.pack()


#1. Generar una ventana 
ventana=Tk()
ventana.title("Ejemplo de 3 Frames")
ventana.geometry("600x400")

#2. agregar frame y colocar el color
seccion1= Frame(ventana,bg="red")
seccion1.pack(expand=True,fill='both')

seccion2= Frame(ventana,bg="gray")
seccion2.pack(expand=True,fill='both')

seccion3= Frame(ventana,bg="purple")
seccion3.pack(expand=True,fill='both')

#3. agregamos botones
botonAzul= Button(seccion1,text="soy el boton azul",fg="blue",bg="#f5775b",command=mostrarmensaje)

#4. revisar sus posiciones
botonAzul.place(x=60,y=60,width=100,height=30)

botonNegro= Button(seccion2,text="soy el boton negro",fg="black",bg="#a428c7")
botonNegro.grid(row=0,column=0)

botonAmarillo= Button(seccion2,text="soy el boton amarillo",fg="#fcf403",bg="#5b73a8")
botonAmarillo.grid(row=1,column=1)

botonVerde= Button(seccion3,text="soy el boton verde",fg="green",bg="#f797bd",command=agregarboton)
botonVerde.pack()



#Metodo maid para la ejecucion del ventana
ventana.mainloop()
