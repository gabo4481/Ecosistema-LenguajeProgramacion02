from Especies.Especie import Especie

class Herbivoro(Especie):
    def __init__(self, nombre, poblacion, reproduccion, tipo_especie,capacidad_busqueda,velocidad_digestion,especie_alimento):
        super().__init__(nombre, poblacion, reproduccion, tipo_especie)
        self.capacidad_busqueda = capacidad_busqueda
        self.velocidad_digestion = velocidad_digestion
        self.especie_alimento = especie_alimento
        
    def alimentarse(self, plantas, textos):
        for planta in plantas:
            if planta.nombre.lower() == self.especie_alimento.lower():
                total_alimento_consumido = int(planta.poblacion * self.capacidad_busqueda * self.velocidad_digestion)
                
                
                
                if total_alimento_consumido > 0 and total_alimento_consumido <= planta.poblacion:
                    planta.poblacion -= total_alimento_consumido
                    textos.append(f"El herbivoro {self.nombre}, se ha alimentado de la planta {planta.nombre} redujo la poblacion en {planta.poblacion}." + "\n")
                    self.reproducirse(textos)  # Solo se reproduce si ha comido algo
                else:
                    textos.append(f"El herbivoro {self.nombre} no ha encontrado suficiente alimento." + "\n")
                    self.mortalidad(textos)

    def __lt__(self,otro):
        return self.capacidad_busqueda < otro.capacidad_busqueda
        
    def reproducirse(self,textos):
        self.poblacion = self.poblacion + (self.poblacion * self.reproduccion)
        textos.append(f"El herbivoro {self.nombre} se ha reproducido, nueva poblacion: {int(self.poblacion)}." + "\n")
        
    def mortalidad(self,textos):
        self.poblacion = self.poblacion - (self.poblacion * 0.1) 
        textos.append(f"El herbivoro {self.nombre} tuvo mortalidad, nueva poblacion: {int(self.poblacion)}." + "\n")