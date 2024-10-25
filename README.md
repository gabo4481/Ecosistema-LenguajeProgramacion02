# Simulador de Ecosistemas

Este proyecto es un simulador de ecosistemas que permite agregar diferentes especies, simular interacciones entre ellas y almacenar datos sobre la población a lo largo del tiempo. Se basa en una jerarquía de clases que representa especies de plantas, herbívoros y carnívoros.


## Clases Principales

### 1. **Especie**
- **Descripción**: Clase base para todas las especies.
- **Métodos**:
  - `alimentarse()`: Método abstracto para definir cómo se alimenta la especie.
  - `reproducirse()`: Método abstracto para definir cómo se reproduce la especie.
  - `mortalidad()`: Método abstracto para definir la mortalidad de la especie.

### 2. **Planta**
- **Descripción**: Representa una planta en el ecosistema.
- **Métodos**:
  - `reproducirse(textos)`: Aumenta la población de la planta en base a su tasa de reproducción.

### 3. **Herbivoro**
- **Descripción**: Representa un herbívoro en el ecosistema.
- **Métodos**:
  - `alimentarse(plantas, textos)`: Se alimenta de plantas específicas, reduce su población y puede reproducirse.
  - `reproducirse(textos)`: Aumenta la población del herbívoro.
  - `mortalidad(textos)`: Aplica una tasa de mortalidad al herbívoro.

### 4. **Carnivoro**
- **Descripción**: Representa un carnívoro en el ecosistema.
- **Métodos**:
  - `alimentarse(herbivoros, textos)`: Se alimenta de herbívoros específicos, reduce su población y puede reproducirse.
  - `reproducirse(textos)`: Aumenta la población del carnívoro.
  - `mortalidad(textos)`: Aplica una tasa de mortalidad al carnívoro.

### 5. **Ecosistema**
- **Descripción**: Gestiona el conjunto de especies y sus interacciones.
- **Métodos**:
  - `agregar_especie(especie)`: Agrega una especie al ecosistema.
  - `cargar_especies(archivo)`: Carga especies desde un archivo JSON.
  - `guardar_especies(archivo)`: Guarda las especies en un archivo JSON.
  - `guardar_datos_ecosistema(archivo, textos)`: Guarda los datos de la simulación en un archivo.
  - `cargar_datos_ecosistema(archivo)`: Carga los datos de una simulación anterior y los imprime.

## Ejecución

Para ejecutar el simulador, simplemente corre el archivo `main.py`. El usuario podrá interactuar con el simulador a través de un menú en la consola, donde podrá:

1. Agregar especies.
2. Simular días en el ecosistema.
3. Mostrar estadísticas de la simulación.
4. Salir del programa.

## Ejemplo de Salida

A continuación se muestra un ejemplo de cómo se vería la salida del simulador en la consola durante un día de simulación:

```python
--- Dia 1 ---
- La planta Monte se ha reproducido, nueva poblacion: 8
- El herbivoro Pato, se ha alimentado de la planta Monte redujo la poblacion en 6.
- El herbivoro Pato se ha reproducido, nueva poblacion: 20.
- El herbivoro Jirafa no ha encontrado suficiente alimento.
- El herbivoro Pato, se ha alimentado de la planta Monte redujo la poblacion en 6.
- El herbivoro Pato se ha reproducido, nueva poblacion: 20.
- El herbivoro Jirafa no ha encontrado suficiente alimento.
- El herbivoro Jirafa tuvo mortalidad, nueva poblacion: 81.
- El carnivoro Leon no ha encontrado suficiente alimento.
- El carnivoro Leon tuvo mortalidad, nueva poblacion: 24
```

## Requisitos

Asegúrate de tener Python instalado en tu máquina. Este proyecto ha sido desarrollado con Python 3.



