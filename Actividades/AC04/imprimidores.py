from threading import Thread, Lock
from utils import reloj
import random

lock_global = Lock()

class Imprimidor(Thread):

    def __init__(self, nombre, berlin, bolsa_dinero):
        super().__init__(daemon=True)
        self.nombre = nombre
        self.berlin = berlin
        self.bolsa_dinero = bolsa_dinero

    def run(self):
        '''
        Funcionalidad de iMPRIMIDOR que imprime dinero cada 5 minutos, cada
        iteracion chequea si se cumple que hay problema con el dinero (20%)
        '''
        while True:
            dinero = random.randint(100000, 500000)
            self.imprimir_dinero(dinero)
            problema = random.uniform(0, 1)
            if problema <= 0.2:
                self.problema_papel()
            reloj(5)

    def imprimir_dinero(self, dinero):
        '''
        Llamar a este método para imprimir dinero.
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param dinero:
        :return:
        '''
        lock_global.acquire()
        print('{0}: imprimiendo {1} euros'.format(self.nombre, dinero))
        self.bolsa_dinero.dinero_acumulado += dinero
        print('Llevamos {0} euros'.format(self.bolsa_dinero.dinero_acumulado))
        lock_global.release()

        if self.bolsa_dinero.dinero_acumulado >= self.bolsa_dinero.meta_dinero:
            self.bolsa_dinero.dinero_listo.set()


    def problema_papel(self):
        '''
        Probabilidad de problema con el papel de 20%
        '''
        self.berlin.acquire()
        print('{}: Oh no! Tenemos un problema con el papel!'.format(self.nombre))
        print('Berlin solucionando problema de {}'.format(self.nombre))
        reloj(10)
        self.berlin.release()
