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
    senal_botones = pyqtSignal(dict)
    invalid_transaccion = pyqtSignal(str)
    senal_energia = pyqtSignal(int)
    

    def __init__(self, x, y, sizex, sizey, mapa):
        super().__init__()
        self.direction = 'R'
        self._x = x
        self._y = y
        self.initial_y = y
        self.sizex = sizex
        self.sizey = sizey
        self._dinero = DINERO_INICIAL
        self.semillas_c = 0
        self.semillas_a = 0
        self.choclos = 0
        self.alcachofas = 0
        self._energia = 100 
        self.oro = 0
        self.lena = 0
        self.mapa = mapa
        self.azada = False
        self.hacha = False
        self.inventario = [['' for i in range(12)] for j in range(3)]
        self.uptade_window_signal = None
        self.senal_dinero = None
        self.senal_inventario = None
        self.obstaculos = Obstaculos()
        self.obstaculos.start()
        self.obstaculos.update_signal.connect(self.recibe_obstaculo)
        # self.update_collision.connect(self.obstaculos.check_personaje)
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
    def energia(self):
        return self._energia
    
    @energia.setter
    def energia(self, energia):
        if energia < 0:
            self._energia = 0
        else:
            self._energia = energia
            self.senal_energia.emit(self.energia)

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
            # if self.verificar_obstaculo('R'):
            #     pass
            self.x += 10
        elif event == 'L':
            self.direction = 'L'
            # if self.verificar_obstaculo('L'):
            #     pass
            self.x -= 10
        elif event == 'U':
            self.direction = 'U'
            # if self.verificar_obstaculo('U'):
            #     pass
            
            self.y -= 10
        elif event == 'D':
            self.direction = 'D'
            # if self.verificar_obstaculo('D'):
            #     pass
            
            self.y += 10
        

    def compra(self, data):
        if data == 'compra1':
            if self.dinero >= PRECIO_AZADA and self.azada == False:
                self.dinero -= PRECIO_AZADA
                self.azada = True
                self.senal_botones.emit({'nombre': data})
                self.senal_inventario.emit({'tipo': 'azada', 'modo': 'agregar'})
            else:
                print('no hay dinero')
                self.invalid_transaccion.emit('precio_azada')
        elif data == 'compra2':
            if self.dinero >= PRECIO_HACHA and self.hacha == False:
                self.dinero -= PRECIO_HACHA
                self.hacha = True
                self.senal_botones.emit({'nombre': data})
                self.senal_inventario.emit({'tipo': 'hacha', 'modo': 'agregar'})
                
            else:
                self.invalid_transaccion.emit('precio_hacha')
        elif data == 'compra3':
            if self.dinero >= PRECIO_SEMILLA_CHOCLOS:
                self.dinero -= PRECIO_SEMILLA_CHOCLOS
                self.semillas_c += 1
                self.senal_botones.emit({'nombre': data, 'cantidad':self.semillas_c})
                self.senal_inventario.emit({'tipo': 'semilla_c', 'modo': 'agregar'})
            else:
                self.invalid_transaccion.emit('precio_choclo1')
        elif data == 'compra4':
            if self.dinero >= PRECIO_SEMILLA_ALCACHOFAS:
                self.dinero -= PRECIO_SEMILLA_ALCACHOFAS
                self.semillas_a += 1
                self.senal_botones.emit({'nombre': data, 'cantidad': self.semillas_a})
                self.senal_inventario.emit({'tipo': 'semilla_a', 'modo': 'agregar'})
            else:
                self.invalid_transaccion.emit('precio_alcachofa1')

        
    def venta(self, data):
            if data == 'venta1':
                self.dinero += PRECIO_AZADA
                self.azada = False
                self.senal_botones.emit({'nombre': data})
                self.senal_inventario.emit({'tipo': 'azada', 'modo': 'quitar'})
            elif data == 'venta2':
                self.dinero += PRECIO_HACHA
                self.hacha = False
                self.senal_botones.emit({'nombre': data})
                self.senal_inventario.emit({'tipo': 'hacha', 'modo': 'quitar'})
            elif data == 'venta3':
                self.dinero += PRECIO_SEMILLA_CHOCLOS
                self.semillas_c -= 1
                self.senal_botones.emit({'nombre': data, 'cantidad': self.semillas_c})
                self.senal_inventario.emit({'tipo': 'semillas_a', 'modo': 'quitar'})
            elif data == 'venta4':
                self.dinero += PRECIO_SEMILLA_ALCACHOFAS
                self.semillas_a -= 1
                self.senal_botones.emit({'nombre': data, 'cantidad': self.semillas_a})
                self.senal_inventario.emit({'tipo': 'semillas_a', 'modo': 'quitar'})
            elif data == 'venta5':
                self.dinero += PRECIO_ALACACHOFAS
                self.alcachofas -= 1
                self.senal_botones.emit({'nombre': data, 'cantidad': self.alcachofas})
                self.senal_inventario.emit({'tipo': 'alcachofas', 'modo': 'quitar'})
            elif data == 'venta6':
                self.dinero += PRECIO_CHOCLOS
                self.choclos -= 1
                self.senal_botones.emit({'nombre': data, 'cantidad': self.choclos})
                self.senal_inventario.emit({'tipo': 'choclos', 'modo': 'quitar'})
            elif data == 'venta7':
                self.dinero += PRECIO_LEÑA
                self.lena -= 1
                self.senal_botones.emit({'nombre': data, 'cantidad': self.lena})
                self.senal_inventario.emit({'tipo': 'madera', 'modo': 'quitar'})
            elif data == 'venta8':
                self.dinero += PRECIO_ORO
                self.oro -= 1
                self.senal_botones.emit({'nombre': data, 'cantidad': self.oro})
                self.senal_inventario.emit({'tipo': 'oro', 'modo': 'quitar'})

    def update_dinero(self):
        if self.senal_dinero:
            self.senal_dinero.emit(self.dinero)

    def verificar_obstaculo(self, direction):
        pos_x, pos_y = self.x, self.y
        if direction == 'U':
            pos_y += 10
            bottom_pos_x = pos_x // (2*SIZE_TILE)
            
            top_pos_y = (pos_y // (2*SIZE_TILE)) + 1
            if self.columns[top_pos_y][bottom_pos_x]:
                rect, tipo = self.columns[top_pos_y][bottom_pos_x]
                if tipo == 'roca':
                    return True
                else:
                    return False
            else:
                return False
        elif direction == 'D':
            pos_y -= 10
            bottom_pos_x = pos_x //(2*SIZE_TILE)
            bottom_pos_y = (pos_y //(2*SIZE_TILE)) - 1
            if self.columns[bottom_pos_y][bottom_pos_x]:
                rect, tipo = self.columns[bottom_pos_y][bottom_pos_x]
                if tipo == 'roca':
                    return True
                else:
                    return False
            else:
                return False
        elif direction == 'L':
            pos_x -= 10
            bottom_pos_x = (pos_x//(2*SIZE_TILE)) - 1
            bottom_pos_y = pos_y//(2*SIZE_TILE)
            if self.columns[bottom_pos_y][bottom_pos_x]:
                rect, tipo = self.columns[bottom_pos_y][bottom_pos_x]
                if tipo == 'roca':
                    return True
                else:
                    return False
            else:
                return False
        else:
            pos_x += 10
            top_pos_x = (pos_x//SIZE_TILE) + 1
            bottom_pos_y = (pos_y//SIZE_TILE)
            if self.columns[bottom_pos_y][top_pos_x]:
                rect, tipo = self.columns[bottom_pos_y][top_pos_x]
                if tipo == 'roca':
                    return True
                else:
                    return False
            else:
                return False

        
        

    def recibe_obstaculo(self, event):
        if event['mode'] == 'crear':
            self.update_front.emit(event)
        else:
            pass
        
