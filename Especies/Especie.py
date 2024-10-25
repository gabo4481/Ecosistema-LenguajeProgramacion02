from abc import abstractmethod

class Especie():
    def __init__(self,nombre,poblacion,reproduccion,tipo_especie):
        self.nombre = nombre
        self.poblacion = poblacion
        self.reproduccion = reproduccion
        self.tipo_especie = tipo_especie
        
    @abstractmethod
    def alimentarse(self):
        pass
        
    @abstractmethod
    def reproducirse(self):
        pass
    
    @abstractmethod
    def mortalidad(self):
        pass
    