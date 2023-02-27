from tkinter import Tk,Button,Frame

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
botonAzul= Button(seccion1,text="soy el boton azul",fg="blue")
botonAzul.place(x=60,y=60,width=100,height=30)

botonNegro= Button(seccion2,text="soy el boton negro",fg="black")
botonNegro.grid(row=0,column=0)

botonAmarillo= Button(seccion2,text="soy el boton amarillo",fg="yellow")
botonAmarillo.grid(row=1,column=1)

botonVerde= Button(seccion3,text="soy el boton verde",fg="green")
botonVerde.pack()


#Metodo maid para la ejecucion del ventana
ventana.mainloop()
