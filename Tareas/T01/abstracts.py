from abc import ABC
#Este archivo contiene todas las clases abstractas

class Menu(ABC):
    def __init__(self):
        self._menu =    "    ____            _            _             __           ____  \n" + \
                        "   /  _/   ____    (_)  _____   (_)  ____ _   / /          / __ \ \n" + \
                        "   / /    / __ \  / /  / ___/  / /  / __ `/  / /          / /_/ / \n" + \
                        " _/ /    / / / / / /  / /__   / /  / /_/ /  / /          / ____/  \n" + \
                        "/___/   /_/ /_/ /_/   \___/  /_/   \__,_/  /_/          /_/       \n"

    #Este es un metodo comun para que todos los menus puedan 
    #recibir inputs 
    def recibir_input(self):
        inpt = input('Por favor, indique su respuesta: (0 para salir) ')
        return inpt



class Vehiculo(ABC):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, peso):
        self._nombre = nombre
        self._dueno = dueno
        self._chasis = chasis
        self._carroceria = carroceria
        self._ruedas = ruedas
        self._peso = peso



class Persona(ABC):
    def __init__(self, nombre, personalidad, contextura ,
         equilibrio, experiencia, equipo):
        self._nombre = nombre
        self._personalidad = personalidad
        self._experiencia = experiencia
        self._contextura = contextura
        self._equilibrio = equilibrio
        self._equipo = equipo
        self.vehiculos = []
