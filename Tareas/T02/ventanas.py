from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
from PyQt5 import uic
from parametros_generales import (PATHS, SIZE_TILE, PERSONAJE, 
                                  KEY_EVENT_DICT, DINERO_INICIAL,
                                  FONT, DINERO_TRAMPA)
import sys
from os.path import join
from random import randint
from personaje import Personaje
from drags import DraggableLabel, DropLabel
from plantas import Planta
from collections import deque

window_name, base_class = uic.loadUiType("inicio.ui")
window_name2, base_class2 = uic.loadUiType("juego.ui")
window_name3, base_class3 = uic.loadUiType("inventario.ui")


class VentanaInicio(window_name, base_class):
    senal_juego = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.jugar.clicked.connect(self.play)

    def init_gui(self):
        pixmap = QPixmap(PATHS['logo'])
        self.label_2.setPixmap(pixmap)

    def play(self):
        mapa = self.mapa.text()
        if mapa in ['mapa_1.txt', 'mapa_2.txt']:
            print('empezando el juego')
            self.hide()
            ruta = mapa.split('.')[0]
            self.senal_juego.emit(ruta)
        else:
            self.error.setText('Nombre de mapa invalido')


class VentanaJuego(window_name2, base_class2):
    senal_start = pyqtSignal()
    update_window_signal = pyqtSignal(dict)
    senal_inventario = pyqtSignal()
    inventario_signal_update = pyqtSignal(dict)
    restaurar_energia = pyqtSignal()
    actualizar_dinero = pyqtSignal(int)
    senal_roca = pyqtSignal(tuple)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.teclas = set()
        self._frame = 1
        self.update_personaje_signal = None
        self.current_sprite = None
        self.senal_compra = None
        self.senal_venta = None
        

    def init_gui(self, ruta):
        sprite = QPixmap(PATHS['fondo'])
        sprite = sprite.scaled(813, 574)
        self.label.setPixmap(sprite)
        
        self.ruta = ruta
        posiciones = [(i, j) for i in range(21) for j in range(14)]
        with open(PATHS[self.ruta], 'r', encoding='utf-8') as file:
            lista = file.readlines()
        n = 0
        mapa = []
        posy = [j for j in range(len(lista))]
        posx = [i for i in range(len(lista[0].replace(' ','')))]
        for linea in lista:
            mapa.append(linea.replace(' ',''))
        for linea, y in zip(mapa, posy):
            for c, x in zip(linea, posx):
                if not c in ['O', 'T', 'R', 'H', 'C']:
                    pass
                elif c == 'T':
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    # pixeles.scaledToHeight(SIZE_TILE)
                    # pixeles.scaledToWidth(SIZE_TILE)
                    pixeles = pixeles.scaled(SIZE_TILE, SIZE_TILE)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    self.grilla.addWidget(tile, y, x)
                elif c == 'H':
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    # pixeles.scaledToHeight(SIZE_TILE)
                    # pixeles.scaledToWidth(SIZE_TILE)
                    pixeles = pixeles.scaled(SIZE_TILE, SIZE_TILE)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    self.grilla.addWidget(tile, y, x)
                elif c == 'R':
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    # pixeles.scaledToHeight(SIZE_TILE)
                    # pixeles.scaledToWidth(SIZE_TILE)
                    pixeles = pixeles.scaled(SIZE_TILE, SIZE_TILE)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    
                    self.grilla.addWidget(tile, y, x)
                    roca = QLabel('', self)
                    pix = QPixmap(PATHS['roca'])

                    # pix.scaledToHeight(SIZE_TILE)
                    # pix.scaledToWidth(SIZE_TILE)
                    pix = pix.scaled(SIZE_TILE, SIZE_TILE)
                    roca.setPixmap(pix)
                    roca.setScaledContents(True)
                    
                    self.grilla.addWidget(roca, y, x)
                elif c == 'C':
                    tile = DropLabel('', self)
                    pixeles = QPixmap(PATHS['cultivo'])
                    # pixeles.scaledToHeight(SIZE_TILE)
                    # pixeles.scaledToWidth(SIZE_TILE)
                    pixeles = pixeles.scaled(SIZE_TILE, SIZE_TILE)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    
                    self.grilla.addWidget(tile, y, x)
                else:
                    tile = QLabel('', self)
                    n = randint(0, 100)
                    if n <= 10:
                        pixeles = QPixmap(PATHS['flores'])
                    else:
                        pixeles = QPixmap(PATHS['tile'])
                    pixeles = pixeles.scaled(SIZE_TILE, SIZE_TILE)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    
                    self.grilla.addWidget(tile, y, x)
        self.grilla.setVerticalSpacing(0)
        self.grilla.setHorizontalSpacing(0)
        self.personaje = Personaje(100, 200, self.widget.geometry().width(), 
            self.geometry().height()- 60)
        self.init_signals()
        t = True
        h = True
        for linea, y in zip(mapa, posy):
            for c, x in zip(linea, posx):
                if c == 'R':
                    self.senal_roca.emit((y, x))
                if c == 'H' and t:
                    house = QLabel('', self)
                    pix = QPixmap(PATHS['house'])
                    pix = pix.scaled(SIZE_TILE*2, SIZE_TILE*2)
                    # house.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
                    house.setPixmap(pix)
                    # house.resize(16,16)
                    
                    house.setScaledContents(True)
                    self.grilla.addWidget(house, y, x, 2, 2)
                    t = False


                if c == 'T' and h:
                    house = QLabel('', self)
                    pix = QPixmap(PATHS['store'])
                    pix = pix.scaled(SIZE_TILE*2, SIZE_TILE*2)
                    house.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)
                    house.setPixmap(pix)
                    house.setScaledContents(True)
                    
                    
                    # house.setScaledContents(True)
                    self.grilla.addWidget(house, y, x, 2, 2)
                    h = False
        
        
        
        self.front_personaje = QLabel('', self)
        self.current_sprite = QPixmap(PERSONAJE[('D', 1)])
        self.current_sprite = self.current_sprite.scaled(14*1.5, 30*1.5)
        self.front_personaje.setPixmap(self.current_sprite)
        self.front_personaje.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.front_personaje.move(100, 200)
        
        
        self.move(150, 200)
        self.show()

        
        self.senal_inventario.emit()
        self.senal_start.emit()

        

    def init_signals(self):
        self.update_window_signal.connect(self.update_window)
        self.senal_compra.connect(self.personaje.compra)
        self.senal_venta.connect(self.personaje.venta)
        self.personaje.senal_dinero = self.actualizar_dinero
        self.personaje.uptade_window_signal = self.update_window_signal
        self.update_personaje_signal = self.personaje.update_character_signal
        self.personaje.update_front.connect(self.update_mapa)
        self.senal_roca.connect(self.personaje.obstaculos.add_roca)
        

    @property
    def frame(self):
        return self._frame
    
    @frame.setter 
    def frame(self, value):
        self._frame = value if value < 3 else 1

    def keyPressEvent(self, e):
        self.teclas.add(e.key())
        print(self.teclas)
        if e.key() in KEY_EVENT_DICT:
            action = KEY_EVENT_DICT[e.key()]
            self.update_personaje_signal.emit(action)

        if self.teclas == set([73, 80, 75]):
            print('wea')
            self.restaurar_energia.emit()

        if self.teclas == set([89, 77, 78]):
            self.personaje.dinero += DINERO_TRAMPA

        

    def keyReleaseEvent(self, e):
        self.teclas.remove(e.key())

    def update_mapa(self, event):
        if event['status'] == 'oro':
            item = QLabel('', self)
            pix = QPixmap(PATHS['oro'])
            pix = pix.scaled(SIZE_TILE, SIZE_TILE)
            item.setPixmap(pix)
            item.setScaledContents(True)
            self.grilla.addWidget(item, *(event['coordenadas']))
        else:
            item = QLabel('', self)
            pix = QPixmap(PATHS['arbol'])
            pix = pix.scaled(SIZE_TILE, SIZE_TILE)
            item.setPixmap(pix)
            item.setScaledContents(True)
            self.grilla.addWidget(item, *(event['coordenadas']))
        # self.inventario_signal_update.emit(event)

    def update_window(self, e):
        direction = e['direction']
        position = e['position']
        if position == 'walk':
            self.frame += 1
            self.current_sprite = QPixmap(PERSONAJE[(direction, self.frame)])
            self.current_sprite = self.current_sprite.scaled(14*1.5, 30*1.5)
        self.front_personaje.setPixmap(self.current_sprite)
        self.front_personaje.move(e['x'], e['y'])



class Inventario(window_name3, base_class3):
    senal_perder = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.energia = 100
        self.posx = 0
        self.posy = 0
        # self.init_gui()

    def init_gui(self):
        print('hola')
        sprite = QPixmap(PATHS['fondo'])
        sprite = sprite.scaled(800, 428)
        self.label_2.setPixmap(sprite)
        pixmap = QPixmap(PATHS['inventario'])
        self.label.setPixmap(pixmap)
        self.label_4.setText('Dinero: {0}'.format(DINERO_INICIAL))
        self.label_4.setFont(FONT)
        pos_x = [i for i in range(12)]
        pos_y = [j for j in range(3)]
        for y in pos_y:
            for x in pos_x:
                item = DraggableLabel('', self)
                self.inventario.addWidget(item, y, x)
        # self.posx += 1
        self.salir.clicked.connect(self.exit)
        self.move(950, 200)
        self.show()
    
    

    def exit(self):
        self.hide()
        sys.exit()
        
    def actualizar_labels(self, horas, minutos, dias):
        
        if horas < 10:
            horas = '0{0}'.format(horas)
        if minutos < 10:
            minutos = '0{0}'.format(minutos)
            
        self.hora.setText(f"Hora: {horas}:{minutos}")
        self.hora.setFont(FONT)
        self.dia.setText(f"Dia: {dias}")
        self.dia.setFont(FONT)
    
    def actualizar_energia(self):
        self.energia -= 1
        self.pbar.setValue(self.energia)
        if self.energia == 0:
            self.game_over()

    def restaurar_energia(self):
        self.energia = 100
        self.pbar.setValue(self.energia)

    def game_over(self):
        self.senal_perder.emit()

    def actualizar_dinero(self, dinero):
        self.label_4.setText('Dinero: {0}'.format(dinero))
        self.label_4.setFont(FONT)

    def actualizar_inventario(self, event):
        if event['status'] == 'oro':
            grid = QGridLayout()
            grid.replaceWidget()
            self.inventario.itemAtPosition(self.posy, self.posx).setPixmap(QPixmap(PATHS['oro']))
            if self.posx < 11:
                self.posx += 1
            elif self.posy < 3:
                self.posy += 1
                self.posx = 0
            else:
                print('maximos items en el inventario')

