from time import time, sleep
from PyQt5.QtCore import QThread, pyqtSignal, QObject, QTimer
from PyQt5.QtWidgets import QWidget
from parametros_generales import SIZE_TILE
from PyQt5.Qt import QTest, QRect
from random import randint

class Calendario(QThread):
    senal_tiempo = pyqtSignal(int,int, int)
    time_start = time()
    senal_energia = pyqtSignal()
    seconds = 0
    minutes = 0
    dias = 0
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.energia = 100

    def run(self):
        while self.energia > 0:
            sleep(0.2)
            self.seconds = int(time() - self.time_start) \
                - self.minutes * 60
            
            if self.seconds >= 60:
                self.minutes += 1
                self.seconds = 0
                self.senal_energia.emit()
            if self.minutes == 24:
                self.minutes = 0
                self.seconds = 0

            self.senal_tiempo.emit(self.minutes, self.seconds,
                 self.dias)

            


class Actualizador(QThread):

    def __init__(self, ventana, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        self.ventana.show()


class TimerPlanta(QThread):
    senal_actualizar = pyqtSignal(int)
    def __init__(self):
        super().__init__()
        self.sprite = None
        self.frame = 0
        self.timer = QTimer()

    def run(self):
        self.timer.start(1000)
        while frame != 6:
            
            frame += 1
            sleep(10)


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
            QTest.qWait(37000)

    def add_item(self):
        x = randint(0, 20)
        y = randint(0, 13)

        if self.columns[y][x]:
            return
        
        rect = QRect(1 + SIZE_TILE*x, 1 + SIZE_TILE*y, SIZE_TILE, SIZE_TILE)
        
        r = randint(0, 100)
        if r <= 70:
            self.columns[y][x] = (rect, 'oro')
            self.update_signal.emit({'status': 'oro', 'coordenadas': (y, x), 
                'location': rect})
        else:
            self.columns[y][x] = (rect, 'arbol')
            self.update_signal.emit({'status': 'arbol', 'coordenadas': (y, x), 
                'location': rect})


    def add_roca(self, position):
        y, x = position
        rect = QRect(1 + SIZE_TILE*x, 1 + SIZE_TILE*y, SIZE_TILE, SIZE_TILE)
        self.columns[y][x] = (rect, 'roca')

    
