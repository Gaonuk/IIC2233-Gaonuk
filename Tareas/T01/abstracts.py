from abc import ABC, abstractmethod
from parametros import PATHS
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

    @abstractmethod
    def menu(self):
        pass


    def verificar_piloto(self, nom_usuario):
        nombre = nom_usuario.replace(' ', '')
        valido = 0
        if not nombre.isalnum():
            valido = 1
            return valido

        
        else:
            existe = 0
            with open(PATHS['PILOTOS'], 'r', encoding='utf-8') as archivo:
                # Se genera un molde para buscar en que posicion 
                # se encuentra le nombre de los pilotos
                molde = archivo.readline()
                molde = molde.strip().split(',')
                for m in molde:
                    if m == 'Nombre':
                        nom = molde.index(m)
                for l in archivo:
                    piloto = l.strip().split(',')
                    if piloto[nom] == nom_usuario:
                        existe = 1
            return existe

    def verificar_vehiculo(self, nom_vehiculo):
        nombre = nom_vehiculo.replace(' ', '')
        valido = 0
        if not nombre.isalnum():
            valido = 1
            return valido
        
        else:
            existe = 0
            with open(PATHS['VEHICULOS'], 'r', encoding='utf-8') as archivo:
                # Se genera un molde para buscar en que posicion 
                # se encuentra le nombre de los pilotos
                molde = archivo.readline()
                molde = molde.strip().split(',')
                for m in molde:
                    if m == 'Nombre':
                        nom = molde.index(m)
                for l in archivo:
                    vehiculo = l.strip().split(',')
                    if vehiculo[nom] == nom_vehiculo:
                        existe = 1
            return existe

class Vehiculo(ABC):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, peso):
        self._nombre = nombre
        self._dueno = dueno
        self._chasis = chasis
        self._carroceria = carroceria
        self._ruedas = ruedas
        self._peso = peso

    @property
    def nombre(self):
        return self._nombre

    @property
    def dueno(self):
        return self._dueno

    @property
    def chasis(self):
        return self._chasis

    @chasis.setter 
    def set_chasis(self, chasis):
        if chasis < 0:
            self._chasis = 0
        else:
            self._chasis = chasis

    @property
    def carroceria(self):
        return self._carroceria

    @carroceria.setter 
    def carroceria(self, carroceria):
        if carroceria < 0:
            self._carroceria = 0
        else:
            self._carroceria = carroceria

    @abstractmethod
    def __str__(self):
        pass

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


    @property
    def nombre(self):
        return self._nombre

    @property
    def personalidad(self):
        return self._personalidad

    @property
    def experiencia(self):
        return self._experiencia

    @experiencia.setter
    def experiencia(self, exp):
        self._experiencia = exp

    @property
    def contextura(self):
        return self._contextura
    
    @contextura.setter
    def contextura(self, cont):
        self._contextura = cont

    @property
    def equilibrio(self):
        return self._equilibrio

    @equilibrio.setter
    def equilibrio(self, equi):
        self._equilibrio = equi

    @abstractmethod
    def __str__(self):
        pass

    def get_vehiculo(self, vehiculo):
        for v in self.vehiculos:
            if v.nombre == vehiculo.nombre:
                return v

class Pista(ABC):
    def __init__(self, nombre, dificultad, 
        vueltas, contrincantes, largo):
        self._nombre = nombre
        self._dificultad = dificultad
        self._vueltas = vueltas
        self._contrincantes = contrincantes
        self._largo = largo

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def dificultad(self):
        return self._dificultad

    @property
    def vueltas(self):
        return self._vueltas

    @property
    def contrincantes(self):
        return self._contrincantes


    @abstractmethod
    def get_tipo(self):
        pass