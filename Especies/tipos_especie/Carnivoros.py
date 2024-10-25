from Especies.Especie import Especie


class Carnivoro(Especie):
    def __init__(self,nombre, poblacion, reproduccion, tipo_especie, capacidad_busqueda,velocidad_digestion, tasa_efectividad_caza,tasa_mortalidad_adicional,especie_alimento,alimentar_prioridad):
        super().__init__(nombre, poblacion, reproduccion, tipo_especie)
        self.capacidad_busqueda = capacidad_busqueda
        self.velocidad_digestion = velocidad_digestion
        self.tasa_efectividad_caza = tasa_efectividad_caza
        self.tasa_mortalidad_adicional = tasa_mortalidad_adicional
        self.especie_alimento = especie_alimento
        self.alimentar_prioridad = alimentar_prioridad
        
        
    def __lt__(self,otro):
        return self.alimentar_prioridad < otro.alimentar_prioridad
    
    def reproducirse(self,textos):
        self.poblacion = self.poblacion + (self.poblacion * self.reproduccion)
        textos.append(f"El carnivoro {self.nombre} se ha reproducido, nueva poblacion: {int(self.poblacion)}" + "\n")
        
    def alimentarse(self, herbivoros, textos):
        for herbivoro in herbivoros:
            if herbivoro.nombre.lower() == self.especie_alimento.lower():
                # Cálculo del alimento consumido
                total_alimento_consumido = int(herbivoro.poblacion * self.capacidad_busqueda * self.velocidad_digestion * self.tasa_efectividad_caza)
                
                if total_alimento_consumido > 0 and total_alimento_consumido <= herbivoro.poblacion:
                    herbivoro.poblacion -= total_alimento_consumido
                    textos.append(f"El carnivoro {self.nombre}, se ha alimentado del herbivoro {herbivoro.nombre} redujo la poblacion en {herbivoro.poblacion}." + "\n")
                    self.reproducirse(textos)  # Solo se reproduce si ha comido algo
                else:
                    textos.append(f"El carnivoro {self.nombre} no ha encontrado suficiente alimento." + "\n")
                    self.mortalidad(textos)

                    
    def mortalidad(self,textos):
        self.poblacion = self.poblacion - (self.poblacion * (self.tasa_mortalidad_adicional + 0.1))
        textos.append(f"El carnivoro {self.nombre} tuvo mortalidad, nueva poblacion: {int(self.poblacion)}" + "\n")
        
        
    