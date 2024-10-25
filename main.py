from Especies.tipos_especie.Herbivoros import Herbivoro
from Especies.tipos_especie.Carnivoros import Carnivoro
from Especies.tipos_especie.Plantas import Planta
from Ecosistemas.Ecosistema import Ecosistema


ecosistema = Ecosistema()

def agregar_especie():
    nombre = input("Ingresa el nombre de la especie: ")
    poblacion = int(input("Ingresa la poblacion de la especie: "))
    reproduccion = float(input("Ingresa la capacidad de reproduccion de la especie, valor entre (0 - 1): "))
    tipo_especie = input("La especie es planta/carnivoro/herbivoro: ")

    if tipo_especie.lower() == "herbivoro":
        capacidad_busqueda = float(input("Ingresa la capacidad de busqueda de la especie, valor entre (0 - 1): "))
        velocidad_digestion = float(input("Ingresa la velocidad de digestion de la especie, valor entre (0 - 1): "))
        alimento_especie = input("Ingrese la especie de la que se alimentara el herbivoro: ")
        especie = Herbivoro(nombre.capitalize(), poblacion, reproduccion, tipo_especie, capacidad_busqueda, velocidad_digestion,alimento_especie)
    
    elif tipo_especie.lower() == "carnivoro":
        capacidad_busqueda = float(input("Ingresa la capacidad de busqueda de la especie, valor entre (0 - 1): "))
        velocidad_digestion = float(input("Ingresa la velocidad de digestion de la especie, valor entre (0 - 1): "))
        tasa_efectividad_caza = float(input("Ingresa la tasa de efectividad de caza de la especie, valor entre (0 - 1): "))
        carnivoro_pelea = int(input("El carnivoro tiende a peliar mucho ? 1.si 2.no"))
        if carnivoro_pelea == 1:
            tasa_mortalidad_adicional = float(input("Ingresa la tasa de mortalidad adicional por peleas o vejez, valor entre (0 - 1): "))
        else:
            tasa_mortalidad_adicional = 0.02
        alimento_especie = input("Ingrese la especie de la que se alimentara el carnivoro: ")
        prioridad_alimento = capacidad_busqueda * tasa_efectividad_caza
        
        especie = Carnivoro(nombre.capitalize(), poblacion, reproduccion, tipo_especie, capacidad_busqueda,velocidad_digestion, tasa_efectividad_caza,tasa_mortalidad_adicional,alimento_especie.capitalize(),prioridad_alimento)
    
    elif tipo_especie.lower() == "planta":
        especie = Planta(nombre.capitalize(), poblacion, reproduccion, tipo_especie)
    
    else:
        print(f"Error, opcion de especie {tipo_especie} invalida")
        pass

    print(f"Se ha agregado {especie.nombre}")
    ecosistema.agregar_especie(especie) 
    ecosistema.guardar_especies("archivos/especies.txt")

def simulador_dia(dias):
    plantas = []
    carnivoros = []
    herbivoros = []

    # Cargar especies desde el ecosistema
    especies = ecosistema.especies

    for especie in especies:
        if especie.tipo_especie == "planta":
            plantas.append(especie)
        elif especie.tipo_especie == "carnivoro":
            carnivoros.append(especie)
        elif especie.tipo_especie == "herbivoro":
            herbivoros.append(especie)
    
    carnivoros.sort(reverse=True)
    herbivoros.sort(reverse=True)
        
    textos = []
    for dia in range(dias):
        print(f"--- Dia {dia + 1} ---")
        textos.append(f"--- Dia {dia + 1} ---" + "\n")

        # Reproducción de las plantas
        for planta in plantas:
            planta.reproducirse(textos)
            

        # Los herbívoros se alimentan de las plantas
        for herbivoro in herbivoros:
            herbivoro.alimentarse(plantas,textos) 

        # Los carnívoros se alimentan de los herbívoros
        for carnivoro in carnivoros:
            carnivoro.alimentarse(herbivoros,textos)
            
        ecosistema.guardar_datos_ecosistema("archivos/datos.txt",textos)


def mostrar_estadisticas():
    ecosistema.cargar_datos_ecosistema("archivos/datos.txt")


condicion = True
ecosistema.cargar_especies("archivos/especies.txt")  

while condicion:
    print("--- Menu del simulador de Ecosistemas ---")
    print("1. Agregar Especie")
    print("2. Simulador Dia")
    print("3. Mostrar Estadisticas")
    print("4. Salir")

    try:
        eleccion = int(input("Ingresa tu eleccion: "))

        if eleccion == 1:
            agregar_especie()
        elif eleccion == 2:
            dias = int(input("Ingresa la cantidad de dias de la simulacion: "))
            simulador_dia(dias)
        elif eleccion == 3:
            mostrar_estadisticas()
        elif eleccion == 4:
            condicion = False
            print("Terminando Programa...")
        else:
            print("Opcion invalida...")
    except ValueError:
        print("---- Error, vuelve a intentarlo ----")
