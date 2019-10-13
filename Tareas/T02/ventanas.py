from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QTimer)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
from PyQt5 import uic
from parametros_generales import (PATHS, SIZE_TILE, PERSONAJE, 
                                  KEY_EVENT_DICT, DINERO_INICIAL,
                                  FONT, DINERO_TRAMPA, DURACION_ORO)
from parametros_acciones import ENERGIA_HERRAMIENTA, ENERGIA_COSECHAR
import sys
from os.path import join
from random import randint
from personaje import Personaje
from drags import DraggableLabel, DropLabel
from threads import Planta, Actualizador
from collections import deque
from ventanas2 import Recurso, ClickLabel, VentanaTienda


window_name, base_class = uic.loadUiType("inicio.ui")
window_name2, base_class2 = uic.loadUiType("juego.ui")


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
    senal_enviar_energia = pyqtSignal(int)
    senal_plantar = pyqtSignal(dict)


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.teclas = set()
        self._frame = 1
        self.update_personaje_signal = None
        self.current_sprite = None
        self.senal_compra = None
        self.senal_venta = None
        self.senal_energia = None
        self.no_compra = None
        

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
                    tile.clicked.connect(self.item_clicked)
                    tile.senal_inventario = self.senal_plantar

               
                    self.grilla.addWidget(tile, y, x)
                else:
                    tile = ClickLabel('tile', self)
                    n = randint(0, 100)
                    if n <= 10:
                        pixeles = QPixmap(PATHS['flores'])
                    else:
                        pixeles = QPixmap(PATHS['tile'])
                    pixeles = pixeles.scaled(SIZE_TILE, SIZE_TILE)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.clicked.connect(self.item_clicked)
                    
                    self.grilla.addWidget(tile, y, x)

        self.grilla.setVerticalSpacing(0)
        self.grilla.setHorizontalSpacing(0)
        self.personaje = Personaje(100, 200, self.widget.geometry().width(), 
            self.geometry().height()- 60, mapa)
        self.tienda = VentanaTienda()
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
        self.senal_compra = self.tienda.senal_compra
        self.senal_venta = self.tienda.senal_venta
        self.personaje.senal_botones.connect(self.tienda.actualizar_botones)
        self.senal_compra.connect(self.personaje.compra)
        self.senal_venta.connect(self.personaje.venta)
        self.personaje.senal_dinero = self.actualizar_dinero
        self.personaje.uptade_window_signal = self.update_window_signal
        self.update_personaje_signal = self.personaje.update_character_signal
        self.personaje.update_front.connect(self.update_mapa)
        self.senal_energia = self.personaje.senal_energia
        self.senal_energia.connect(self.enviar_energia)
        self.senal_roca.connect(self.personaje.obstaculos.add_roca)
        self.personaje.invalid_transaccion.connect(self.tienda.no_hay_dinero)
        self.personaje.senal_inventario = self.inventario_signal_update
        

    @property
    def frame(self):
        return self._frame
    
    @frame.setter 
    def frame(self, value):
        self._frame = value if value < 3 else 1

    def keyPressEvent(self, e):
        self.teclas.add(e.key())
        if e.key() in KEY_EVENT_DICT:
            action = KEY_EVENT_DICT[e.key()]
            self.update_personaje_signal.emit(action)

        if self.teclas == set([73, 80, 75]):
            self.restaurar_energia.emit()

        if self.teclas == set([89, 77, 78]):
            self.personaje.dinero += DINERO_TRAMPA

    def enviar_energia(self, energia):
        self.senal_enviar_energia.emit(energia)

    def keyReleaseEvent(self, e):
        self.teclas.remove(e.key())

    def update_mapa(self, event):
        if event['status'] == 'oro':
            item = Recurso('oro', '', self)
            self.grilla.addWidget(item, *(event['coordenadas']))
        else:
            item = ClickLabel('arbol', self)
            pix = QPixmap(PATHS['arbol'])
            pix = pix.scaled(SIZE_TILE, SIZE_TILE)
            item.setPixmap(pix)
            item.setScaledContents(True)
            item.clicked.connect(self.item_clicked)
            self.grilla.addWidget(item, *(event['coordenadas']))
        # self.inventario_signal_update.emit(event)


    def item_clicked(self):
        label = self.sender()
        if label.text() == 'tile' and self.personaje.azada == True:
            cultivo = DropLabel('', self)
            pixeles = QPixmap(PATHS['cultivo'])
            pixeles = pixeles.scaled(SIZE_TILE, SIZE_TILE)
            cultivo.setPixmap(pixeles)
            cultivo.setScaledContents(True)
            self.grilla.replaceWidget(label, cultivo)
            cultivo.senal_inventario = self.senal_plantar
            label.hide()
            label.deleteLater()
            label.destroy()
            self.personaje.energia -= ENERGIA_HERRAMIENTA
            # grid = QGridLayout()
            # grid.replaceWidget()
            # label = cultivo
            # label.show()
        elif label.text() == 'arbol' and self.personaje.hacha:
            item = Recurso('madera', '', self)
            
            self.grilla.replaceWidget(label, item)
            label.hide()
            label.deleteLater()
            label.destroy()

            self.personaje.energia -= ENERGIA_HERRAMIENTA

        elif label.text() == 'choclo':
            item = Recurso(label.text(), '', self)
            
            y = label.y()
            x = label.x()
            item.setGeometry(x, y, SIZE_TILE, SIZE_TILE)
            item.show()
            label.actualizar_sprite(7, 'semilla_c')
            # self.grilla.addWidget()
            self.personaje.energia -= ENERGIA_COSECHAR
        elif label.text() == 'alcachofa':
            item = Recurso(label.text(), '', self)
            self.grilla.replaceWidget(label, item)
            label.hide()
            label.deleteLater()
            label.destroy()
            self.personaje.energia -= ENERGIA_COSECHAR
        else:
            print('no se puede cosechar')


    def update_window(self, e):
        direction = e['direction']
        position = e['position']
        if position == 'walk':
            self.frame += 1
            self.current_sprite = QPixmap(PERSONAJE[(direction, self.frame)])
            self.current_sprite = self.current_sprite.scaled(14*1.5, 30*1.5)
        self.front_personaje.setPixmap(self.current_sprite)
        self.front_personaje.move(e['x'], e['y'])

    def eliminar_de_inventario(self):
        pass



