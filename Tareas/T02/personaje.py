from PyQt5.QtCore import QObject, pyqtSignal
from parametros_generales import DINERO_INICIAL, SIZE_TILE
from parametros_precios import *
from PyQt5.Qt import QTest
from threading import Lock
from threads import Obstaculos

class Personaje(QObject):

    update_character_signal = pyqtSignal(str)
    update_front = pyqtSignal(dict)
    update_collision = pyqtSignal(tuple)
    collect_lock = Lock()

    def __init__(self, x, y, sizex, sizey):
        super().__init__()
        self.direction = 'R'
        self._x = x
        self._y = y
        self.initial_y = y
        self.sizex = sizex
        self.sizey = sizey
        self._dinero = DINERO_INICIAL
        self.inventario = []
        self.azada = False
        self.hacha = False
        self.uptade_window_signal = None
        self.senal_dinero = None
        self.obstaculos = Obstaculos()
        self.obstaculos.start()
        self.obstaculos.update_signal.connect(self.recibe_obstaculo)
        self.update_collision.connect(self.obstaculos.check_personaje)
        self.update_character_signal.connect(self.move)
        
        self.columns = self.obstaculos.columns

    def update_window_character(self, position):
        if self.uptade_window_signal:
            self.uptade_window_signal.emit({
                'x': self.x,
                'y': self.y,
                'direction': self.direction,
                'position': position
            })

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if 0 < value < self.sizey:
            self._y = value
            self.update_window_character('walk')
        
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if 0 < value < self.sizex:
            self._x = value
            self.update_window_character('walk')

    @property
    def dinero(self):
        return self._dinero

    @dinero.setter
    def dinero(self, value):
        if value < 0:
            self._dinero = 0
        else:
            self._dinero = value
            self.update_dinero()


    def move(self, event):
        if event == 'R':
            self.direction = 'R'
            if self.verificar_obstaculo('R'):
                pass
            else:
                self.x += 10
        elif event == 'L':
            self.direction = 'L'
            if self.verificar_obstaculo('L'):
                pass
            else:
                self.x -= 10
        elif event == 'U':
            self.direction = 'U'
            if self.verificar_obstaculo('U'):
                pass
            else:
                self.y -= 10
        elif event == 'D':
            self.direction = 'D'
            if self.verificar_obstaculo('D'):
                pass
            else:
                self.y += 10
        

    def compra(self, data):
        if data == 'compra1':
            if self.dinero >= PRECIO_AZADA and self.azada == False:
                self.dinero -= PRECIO_AZADA
                self.azada = True
                self.senal_comprar.emit('azada')
        
    def venta(self, data):
        pass

    def update_dinero(self):
        if self.senal_dinero:
            self.senal_dinero.emit(self.dinero)

    def verificar_obstaculo(self, direction):
        pos_x, pos_y = self.x, self.y
        if direction == 'U':
            pos_y += 10
        elif direction == 'D':
            pos_y -= 10
        elif direction == 'L':
            pos_x -= 10
        else:
            pos_x += 10
        bottom_pos_x = pos_x //(2*SIZE_TILE)
        top_pos_x = (pos_x//(2*SIZE_TILE)) + 1
        bottom_pos_y = pos_y //(2*SIZE_TILE)
        top_pos_y = (pos_y //(2*SIZE_TILE)) + 1
        

    def recibe_obstaculo(self, event):

        self.update_front.emit(event)
        
