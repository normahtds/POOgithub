from tkinter import Tk,Button,Frame,Label,Entry,messagebox
class ventana:
    ventanaL=Tk()
    ventanaL.title("Login")
    ventanaL.geometry("500x250")
    
    Label (ventanaL, text="Correo electronico:").pack()
    entrada_lusuario = Entry().pack()
    Label (ventanaL, text="").pack()
    Label (ventanaL, text="Conraseña:").pack()
    entrada_lcontra = Entry(show="*").pack()
    Label (ventanaL, text="").pack()
    
    botonIngresar= Button(text="Ingresar",fg="white",bg="#a428c7").pack()
    def ingresar():
        messagebox.showinfo("Informacion","Te informo que todo fallo con exito")
        messagebox.showerror("Error","Perdon te falle!!")
        print(messagebox.askokcancel("Pregunta","Seguro que quieres a guardar algo"))
        print(messagebox.askyesnocancel("Pregunta2","Seguro que quieres a guardar algo"))
        print(messagebox.askquestion("Pregunta2","Seguro que quieres a guardar algo"))
    ventanaL.mainloop()