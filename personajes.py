class Personaje:
    
    #agregamos el costructor del personaje
    def __init__(self,esp,nom,alt):
        self.especie= esp
        self.nombre= nom
        self.altura= alt
    
    #metodos
    def correr(self, status):
        if(status):
            print("El personaje " + self.nombre + " esta corriendo")
        else:
            print("El personaje " + self.nombre + " se detuvo")
            
    def lanzarGranadas(self):
        print("El personaje " + self.nombre + " se lanzo una granada") 
                
    def  recargarArma(self, municiones):
        cargardor=10
        cargardor = cargardor + municiones
        print("El arma recargada tiene " + str(cargardor) + " balas")