import json
from Especies.tipos_especie.Herbivoros import Herbivoro
from Especies.tipos_especie.Carnivoros import Carnivoro
from Especies.tipos_especie.Plantas import Planta
import random

class Ecosistema():
    def __init__(self):
        self.especies = []
            
    def agregar_especie(self, especie):
        self.especies.append(especie)
        
    def cargar_especies(self,archivo):
        try:
            with open(archivo, 'r') as file:
                especies_dict = json.load(file)
                for especie_data in especies_dict:
                    tipo_especie = especie_data['tipo_especie']
                    if tipo_especie == 'herbivoro':
                        especie = Herbivoro(**especie_data)
                    elif tipo_especie == 'carnivoro':
                        especie = Carnivoro(**especie_data)
                    elif tipo_especie == 'planta':
                        especie = Planta(**especie_data)
                    else:
                        continue
                    self.especies.append(especie)
            print(f"Especies cargado exitosamente desde {archivo}")
        except FileNotFoundError:
            print(f"Archivo {archivo} no encontrado. Iniciando un listado de especies vacío.")
        except Exception as e:
            print(f"Error al cargar las especies: {e}")
    
    def guardar_especies(self, archivo):
        try:
            with open(archivo, "w") as file:
                especies_dict = [especie.__dict__ for especie in self.especies]
                json.dump(especies_dict, file, indent=4)
            print(f"Especies guardadas exitosamente en {archivo}")
        except Exception as e:
            print(f"Error al guardar las especies: {e}")
            
    def guardar_datos_ecosistema(self,archivo,textos):
        try:
            with open(archivo,"w") as file:
                file.writelines(textos)
        except Exception as e:
            print(f"Error al guardar los datos de la simulacion: {e}")
            
    def cargar_datos_ecosistema(self,archivo):
        try:
            with open(archivo,"r") as file:
                lineas = file.readlines()
                for linea in lineas:
                    print(linea.strip())
        except Exception as e:
            print(f"Error al cargar los datos de la simulacion anterior: {e}")