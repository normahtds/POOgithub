class Personaje:
    
    #agregamos el costructor del personaje
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #metodos
    def correr(self, status):
        if(status):
            print("El personaje " + self.__nombre + " esta corriendo")
        else:
            print("El personaje " + self.__nombre + " se detuvo")
            
    def lanzarGranadas(self):
        print("El personaje " + self.__nombre + " se lanzo una granada") 
                
    def  recargarArma(self, municiones):
        cargardor=10
        cargardor = cargardor + municiones
        print("El arma recargada tiene " + str(cargardor) + " balas")

    #def __pensar(self):
        #print("toy pensando.............")    
        
    #get y set para un correcto encapsulado
    def getEspecie(self):
        return self.__especie
    
    def setEspecie(self,esp):
        self.__especie= esp
        
    def getNombre(self):
        return self.__nombre 
    
    def setNombre(self,nom):
        self.__nombre= nom  
        
    def getAltura(self):
        return self.__nombre 
    
    def setAltura(self,alt):
        self.__altura= alt   