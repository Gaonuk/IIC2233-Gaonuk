from threading import Thread, Lock
from utils import reloj
import random

lock_global = Lock()

class Excavador(Thread):
    def __init__(self, nombre, berlin, tunel):
        super().__init__()
        self.nombre = nombre
        self.tunel = tunel
        self.berlin = berlin


    def run(self):
        '''
        Funcionalidad de Excavador que crea x metros de tunel cada 10 min,
        cada iteracion chequea si se cumple que hay problema con la picota (10%)
        '''
        while self.tunel.metros_avanzados < self.tunel.largo:
            metros = random.randint(50, 100)
            self.avanzar(metros)
            problema = random.uniform(0, 1)
            if problema <= 0.1:
                self.problema_picota()

            reloj(10)

    def problema_picota(self):
        '''
        Probabilida de problema con la picota de 10%
        Se llama a berlin para resolverlo
        '''
        print('{0}: Oh no! Tenemos un problema con la picota!'.format(self.nombre))
        
        self.berlin.acquire()
        print('Berlin solucionando problema de {}'.format(self.nombre))
        reloj(5)
        self.berlin.release()


    def avanzar(self, metros):
        '''
        Usar este método para avanzar en la excavación del túnel
        ***Acá debes procurarte de evitar errores de concurrencia***
        :param metros: int
        '''
        
        lock_global.acquire()
        self.tunel.metros_avanzados += metros

        print('{0}: avanzando {1} metros'.format(self.nombre, metros))
        print('LLevamos {0} metros'.format(self.tunel.metros_avanzados))
        lock_global.release()

        if self.tunel.metros_avanzados >= self.tunel.largo:
            self.tunel.tunel_listo.set()
            print('Hemos terminado el Tunel!')
        
        
