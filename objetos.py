from personajes import *

#1. Solicitamos los datos para los objetos
print("")
print("### solicitud Datos Heroe ###")
especieH=input("Escribe la especie del Heroe: ")
nombreH=input("Escribe el nombre del Heroe: ")
alturaH=input("Escribe la altura del Heroe: ")
recargaH=int(input("Ingresa las balas para el Heroe: "))

print("")
print("### solicitud Datos Villano ###")
especieV=input("Escribe la especie del Villano: ")
nombreV=input("Escribe el nombre del Villano: ")
alturaV=float(input("Escribe la altura del Villano: "))
recargaV=int(input("Ingresa las balas para el Villano: "))

#2. Creamos los objetos
Heroe = Personaje(especieH,nombreH,alturaH)
Villano = Personaje(especieV,nombreV,alturaV)

#ejemplo de uso de SET
Heroe.setNombre("Pepe Pecas")

#3. Usamos los atributos del Heroe y Villano
print("")
print("### atributos y metodos del Heroe ###")
print("El personaje se llama " + Heroe.getNombre())
print("pertenece a la especie " + Heroe.getEspecie())
print("y una altura " + str(Heroe.getAltura()))

Heroe.correr(True)
Heroe.lanzarGranadas()
Heroe.recargarArma(recargaH)

print("")
print("### atributos y metodos del Villano ###")
print("El personaje se llama " + Villano.getNombre())
print("pertenece a la especie " + Villano.getEspecie())
print("y una altura " + str(Villano.getNombre()))

Villano.correr(True)
Villano.lanzarGranadas()
Villano.recargarArma(recargaV)
#
#Villano.__pensar()