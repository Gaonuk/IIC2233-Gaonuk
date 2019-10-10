from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, QGridLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
from PyQt5 import uic
from parametros_generales import PATHS
import sys
from os.path import join

window_name, base_class = uic.loadUiType("inicio.ui")
window_name2, base_class2 = uic.loadUiType("juego.ui")

class VentanaInicio(window_name, base_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.jugar.clicked.connect(self.play)

    def play(self):
        mapa = self.mapa.text()
        if mapa in ['mapa_1.txt', 'mapa_2.txt']:
            print('empezando el juego')
            self.hide()
            ruta = mapa.split('.')[0]
            self.ventanaJuego = VentanaJuego(ruta)
            self.ventanaJuego.show()
        else:
            self.error.setText('Nombre de mapa invalido')


class VentanaJuego(window_name2, base_class2):
    def __init__(self, ruta):
        super().__init__()
        self.ruta = ruta
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        posiciones = [(i, j) for i in range(21) for j in range(14)]
        with open(PATHS[self.ruta], 'r', encoding='utf-8') as file:
            lista = file.readlines()
        n = 0
        mapa = []
        posy = [j for j in range(14)]
        posx = [i for i in range(21)]
        for linea in lista:
            mapa.append(linea.replace(' ',''))

        t = 1
        h = 1
        for linea, y in zip(mapa, posy):
            for c, x in zip(linea, posx):
                if not c in ['O', 'T', 'R', 'H', 'C']:
                    pass
                elif c == 'T' and t == False:
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    pixeles.scaledToHeight(32)
                    pixeles.scaledToWidth(32)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(tile, y, x)

                    
                    t += 1
                elif c == 'H':
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    pixeles.scaledToHeight(32)
                    pixeles.scaledToWidth(32)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(tile, y, x)
                    h += 1
                elif c == 'H' and h == 4:
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    pixeles.scaledToHeight(32)
                    pixeles.scaledToWidth(32)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(tile, y, x)
                    house = QLabel('', self)
                    pix = QPixmap(PATHS['house'])
                    pix.scaledToHeight(32)
                    pix.scaledToWidth(32)
                    house.setPixmap(pix)
                    house.setScaledContents(True)
                    house.resize(house.sizeHint())
                    self.grid.addWidget(house, y-1, x-1, 2, 2)
                elif c == 'T' and t == 4:
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    pixeles.scaledToHeight(32)
                    pixeles.scaledToWidth(32)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(tile, y, x)
                    tienda = QLabel('', self)
                    pix = QPixmap(PATHS['store'])
                    pix.scaledToHeight(32)
                    pix.scaledToWidth(32)
                    tienda.setPixmap(pix)
                    tienda.setScaledContents(True)
                    tienda.resize(tienda.sizeHint())
                    self.grid.addWidget(tienda, y-1, x-1, 2, 2)
                elif c == 'R':
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    pixeles.scaledToHeight(32)
                    pixeles.scaledToWidth(32)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(tile, y, x)
                    roca = QLabel('', self)
                    pix = QPixmap(PATHS['roca'])
                    pix.scaledToHeight(32)
                    pix.scaledToWidth(32)
                    roca.setPixmap(pix)
                    roca.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(roca, y, x)
                elif c == 'C':
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['cultivo'])
                    pixeles.scaledToHeight(32)
                    pixeles.scaledToWidth(32)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(tile, y, x)
                else:
                    tile = QLabel('', self)
                    pixeles = QPixmap(PATHS['tile'])
                    pixeles.scaledToHeight(32)
                    pixeles.scaledToWidth(32)
                    tile.setPixmap(pixeles)
                    tile.setScaledContents(True)
                    tile.resize(tile.sizeHint())
                    self.grid.addWidget(tile, y, x)

        self.grid.setVerticalSpacing(0)
        self.grid.setHorizontalSpacing(0)
        
    


if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaInicio()  
    ventana.show()
    sys.exit(app.exec_())