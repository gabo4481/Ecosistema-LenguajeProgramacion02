from Especies.Especie import Especie

class Planta(Especie):
    def __init__(self, nombre, poblacion, reproduccion, tipo_especie):
        super().__init__(nombre, poblacion, reproduccion, tipo_especie)
        
    def reproducirse(self,textos):
        self.poblacion = self.poblacion + (self.poblacion * self.reproduccion)
        textos.append( f"La planta {self.nombre} se ha reproducido, nueva poblacion: {int(self.poblacion)}" + "\n")