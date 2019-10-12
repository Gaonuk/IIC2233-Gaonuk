from parametros_precios import (PRECIO_AZADA, PRECIO_ALACACHOFAS,
        PRECIO_CHOCLOS, PRECIO_HACHA, PRECIO_LEÑA, PRECIO_ORO, 
        PRECIO_SEMILLA_ALCACHOFAS, PRECIO_SEMILLA_CHOCLOS)
from parametros_generales import (PATHS, SIZE_TILE, PERSONAJE, 
                                  KEY_EVENT_DICT, DINERO_INICIAL,
                                  FONT)
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
from PyQt5 import uic
from time import sleep
import sys

window_name4, base_class4 = uic.loadUiType("tienda.ui")
window_name, base_class = uic.loadUiType("perder.ui")


class VentanaTienda(window_name4, base_class4):
    senal_venta = pyqtSignal(str)
    senal_compra = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.init_gui()

    def init_signals(self):
        pass

    def init_gui(self):
        sprite = QPixmap(PATHS['fondo'])
        sprite = sprite.scaled(760, 484)
        self.fondo.setPixmap(sprite)
        pixmap = QPixmap(PATHS['azada'])
        self.azada.setPixmap(pixmap)
        self.precio_azada.setText(f"${PRECIO_AZADA}")
        self.precio_azada.setFont(FONT)
        pixmap = QPixmap(PATHS['hacha'])
        self.hacha.setPixmap(pixmap)
        self.precio_hacha.setText(f"${PRECIO_HACHA}")
        self.precio_hacha.setFont(FONT)
        pixmap = QPixmap(PATHS['semilla_c'])
        self.semilla_choclo.setPixmap(pixmap)
        self.precio_choclo1.setText(f"${PRECIO_SEMILLA_CHOCLOS}")
        self.precio_choclo1.setFont(FONT)
        pixmap = QPixmap(PATHS['semilla_a'])
        self.semilla_alcachofa.setPixmap(pixmap)
        self.precio_alcachofa1.setText(f"${PRECIO_SEMILLA_ALCACHOFAS}")
        self.precio_alcachofa1.setFont(FONT)
        pixmap = QPixmap(PATHS['alcachofa'])
        self.alcachofa.setPixmap(pixmap)
        self.precio_alcachofa2.setText(f"${PRECIO_ALACACHOFAS}")
        self.precio_alcachofa2.setFont(FONT)
        pixmap = QPixmap(PATHS['choclo'])
        self.choclo.setPixmap(pixmap)
        self.precio_choclo2.setText(f"${PRECIO_CHOCLOS}")
        self.precio_choclo2.setFont(FONT)
        pixmap = QPixmap(PATHS['madera'])
        self.madera.setPixmap(pixmap)
        self.precio_madera.setText(f"${PRECIO_LEÑA}")
        self.precio_madera.setFont(FONT)
        pixmap = QPixmap(PATHS['oro'])
        self.oro.setPixmap(pixmap)
        self.coste_oro.setText(f"${PRECIO_ORO}")
        self.coste_oro.setFont(FONT)
        self.compra1.clicked.connect(self.compro)
        self.venta1.clicked.connect(self.venta)
        
        self.show()

    def compro(self):
        boton = self.sender()
        print(boton)
        self.senal_compra.emit(boton.objectName())

    def venta(self):
        boton = self.sender()
        print(boton.objectName())
        self.senal_venta.emit(boton.objectName())

    def actualizar_botones(self, boton):
        pass

class VentanaPerder(window_name, base_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def init_gui(self):
        pix = QPixmap(PATHS['fondo'])
        pix = pix.scaled(811, 331)
        self.label_2.setPixmap(pix)
        self.label_2.setScaledContents(True)
        self.show()
        sleep(5)
        sys.exit()