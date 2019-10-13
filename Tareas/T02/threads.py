from time import time, sleep
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QWidget
from parametros_generales import (SIZE_TILE, PROB_ARBOL, PROB_ORO, 
    CHOCLO, DURACION_ORO, DURACION_LENA)
from parametros_plantas import (FASES_CHOCLOS, FASES_ALCACHOFAS, 
                                TIEMPO_ALCACHOFAS, TIEMPO_CHOCLOS)
from PyQt5.Qt import QTest, QRect
from random import randint

class Calendario(QThread):
    senal_tiempo = pyqtSignal(int,int, int)
    time_start = time()
    senal_energia = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.energia = 100
        self.seconds = 0
        self.minutes = 0
        self.dias = 0

    def run(self):
        while True:
            sleep(0.05)
            self.seconds += 1
            
            if self.seconds >= 60:
                self.minutes += 1
                self.seconds = 0
            if self.minutes == 24:
                self.minutes = 0
                self.seconds = 0
                self.dias += 1

            self.senal_tiempo.emit(self.minutes, self.seconds,
                 self.dias)

            


class Actualizador(QThread):
    senal_destruir = pyqtSignal()
    def __init__(self, tipo, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.tipo = tipo
        self.tiempo = 0
        if self.tipo == 'oro':
            self.duracion = DURACION_ORO
        else:
            self.duracion = DURACION_LENA
        


    def run(self):
        while self.tiempo < self.duracion:
            self.tiempo += 1
            sleep(1)
        self.senal_destruir.emit()


class Planta(QThread):
    senal_actualizar = pyqtSignal(int, str)
    def __init__(self, tipo):
        super().__init__()
        self.sprite = None
        self.frame = 1
        self.tipo = tipo
        self.maxframe = 0
        if self.tipo == 'semilla_c':
            self.maxframe = FASES_CHOCLOS - 1
            self.tiempo = TIEMPO_CHOCLOS/FASES_CHOCLOS
        else:
            self.maxframe = FASES_ALCACHOFAS
            self.tiempo = TIEMPO_ALCACHOFAS/FASES_ALCACHOFAS
        
        

    def run(self):
        while self.frame < self.maxframe + 1:
            self.senal_actualizar.emit(self.frame, self.tipo)
            self.frame += 1
            
            sleep(self.tiempo)

        
class Obstaculos(QThread):
    update_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        row = [''] * 21
        columns = []
        for i in range(14):
            new_row = row[:]
            columns.append(new_row)
        self.columns = columns

    def run(self):
        while True:
            self.add_item()
            QTest.qWait(36000)

    def add_item(self):
        x = randint(0, 20)
        y = randint(0, 13)

        if self.columns[y][x]:
            return
        
        rect = QRect(1 + SIZE_TILE*x, 1 + SIZE_TILE*y, SIZE_TILE, SIZE_TILE)
        
        r = randint(0, 100)
        if r <= PROB_ORO:
            self.columns[y][x] = (rect, 'oro')
            self.update_signal.emit({'status': 'oro', 'coordenadas': (y, x), 
                'location': rect, 'mode': 'crear'})
        elif r <= PROB_ARBOL:
            self.columns[y][x] = (rect, 'arbol')
            self.update_signal.emit({'status': 'arbol', 'coordenadas': (y, x), 
                'location': rect, 'mode': 'crear'})
        
        
    # def add_recurso(self, position, tipo):
    #     y, x = position
    #     rect = QRect(1 + SIZE_TILE*x, 1 + SIZE_TILE*y, SIZE_TILE, SIZE_TILE)
    #     self.columns[y][x] = (rect, tipo)


    def add_roca(self, position):
        y, x = position
        rect = QRect(1 + SIZE_TILE*x, 1 + SIZE_TILE*y, SIZE_TILE, SIZE_TILE)
        self.columns[y][x] = (rect, 'roca')


    def recoger_recurso(self, position):
        pos_x, pos_y = position
        bottom_pos_x = pos_x // 21
        bottom_pox_y = pos_y // 45

        top_pos_x = (pos_x // 21) + 1
        top_pos_y = (pos_y // 45) + 1

        for x in [bottom_pos_x, top_pos_x]:
            for y in [bottom_pox_y, top_pos_y]:
                if x > 20 or y > 13 or x < 0 or y < 0:
                    continue
                    
                if self.columns[y][x]:
                    rect, tipo = self.columns[y][x]
                    if tipo not in ['roca', 'arbol']:
                        self.update_signal.emit({'status': f'{tipo}', 'coordenates': (x, y), 'mode':'recoger'})
                        self.columns[y][x] = None
                    else:
                        pass
            

    
