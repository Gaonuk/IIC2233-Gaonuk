from abstracts import Vehiculo

class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, zapatillas):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas)
        self._zapatillas = zapatillas


class Automovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas)
        self._motor = motor


class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, zapatillas):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas)
        self._zapatillas = zapatillas


class Motocicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas)
        self._motor = motor
    


