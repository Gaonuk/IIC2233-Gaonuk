from abstracts import Vehiculo


class Bicicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, zapatillas, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._zapatillas = zapatillas
        self.categoria = 'bicicleta'

    def __str__(self):
        impresion = 'Vehiculo {}\n'.format(self.nombre)
        impresion += '- Dueño: {}\n'.format(self.dueno)
        impresion += '- Chasis: {}\n'.format(self.chasis)
        impresion += '- Carroceria: {}\n'.format(self.carroceria)
        impresion += '- Ruedas: {}\n'.format(self._ruedas)
        impresion += '- Peso: {}\n'.format(self._peso)
        impresion += '- Zapatillas: {}\n'.format(self._zapatillas)
        return impresion

class Automovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._motor = motor
        self.categoria = 'automóvil'
    
    def __str__(self):
        impresion = 'Vehiculo {}\n'.format(self.nombre)
        impresion += '- Dueño: {}\n'.format(self.dueno)
        impresion += '- Chasis: {}\n'.format(self.chasis)
        impresion += '- Carroceria: {}\n'.format(self.carroceria)
        impresion += '- Ruedas: {}\n'.format(self._ruedas)
        impresion += '- Peso: {}\n'.format(self._peso)
        impresion += '- Motor: {}\n'.format(self._motor)
        return impresion

class Troncomovil(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, zapatillas, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._zapatillas = zapatillas
        self.categoria = 'troncomóvil'

    def __str__(self):
        impresion = 'Vehiculo {}\n'.format(self.nombre)
        impresion += '- Dueño: {}\n'.format(self.dueno)
        impresion += '- Chasis: {}\n'.format(self.chasis)
        impresion += '- Carroceria: {}\n'.format(self.carroceria)
        impresion += '- Ruedas: {}\n'.format(self._ruedas)
        impresion += '- Peso: {}\n'.format(self._peso)
        impresion += '- Zapatillas: {}\n'.format(self._zapatillas)
        return impresion

class Motocicleta(Vehiculo):
    def __init__(self, nombre, dueno, chasis, carroceria, ruedas, motor, peso):
        super().__init__(nombre, dueno, chasis, carroceria, ruedas, peso)
        self._motor = motor
        self.categoria = 'motocicleta'

    def __str__(self):
        impresion = 'Vehiculo {}\n'.format(self.nombre)
        impresion += '- Dueño: {}\n'.format(self.dueno)
        impresion += '- Chasis: {}\n'.format(self.chasis)
        impresion += '- Carroceria: {}\n'.format(self.carroceria)
        impresion += '- Ruedas: {}\n'.format(self._ruedas)
        impresion += '- Peso: {}\n'.format(self._peso)
        impresion += '- Motor: {}\n'.format(self._motor)
        return impresion
