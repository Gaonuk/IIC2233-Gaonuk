from abstracts import Vehiculo


class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, zapatillas, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._zapatillas = zapatillas
        self.categoria = 'bicicleta'


class Automovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._motor = motor
        self.categoria = 'automóvil'

class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, zapatillas, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._zapatillas = zapatillas
        self.categoria = 'troncomóvil'

class Motocicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._motor = motor
        self.categoria = 'motocicleta'


