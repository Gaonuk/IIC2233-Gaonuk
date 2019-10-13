from parametros_precios import (PRECIO_AZADA, PRECIO_ALACACHOFAS,
        PRECIO_CHOCLOS, PRECIO_HACHA, PRECIO_LEÑA, PRECIO_ORO, 
        PRECIO_SEMILLA_ALCACHOFAS, PRECIO_SEMILLA_CHOCLOS)
from parametros_generales import (PATHS, SIZE_TILE, PERSONAJE, 
                                  KEY_EVENT_DICT, DINERO_INICIAL,
                                  FONT, FONT_CHICA)
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)
from PyQt5.Qt import QTest
from PyQt5 import uic
from time import sleep
import sys
from threads import Actualizador
from drags import DraggableLabel, DropLabel

window_name4, base_class4 = uic.loadUiType("tienda.ui")
window_name, base_class = uic.loadUiType("perder.ui")
window_name3, base_class3 = uic.loadUiType("inventario.ui")



class VentanaTienda(window_name4, base_class4):
    senal_venta = pyqtSignal(str)
    senal_compra = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        

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
        self.compra2.clicked.connect(self.compro)
        self.compra3.clicked.connect(self.compro)
        self.compra4.clicked.connect(self.compro)
        self.venta1.clicked.connect(self.venta)
        self.venta1.setEnabled(False)
        self.venta2.clicked.connect(self.venta)
        self.venta2.setEnabled(False)
        self.venta3.clicked.connect(self.venta)
        self.venta3.setEnabled(False)
        self.venta4.clicked.connect(self.venta)
        self.venta4.setEnabled(False)
        self.venta5.clicked.connect(self.venta)
        self.venta6.clicked.connect(self.venta)
        self.venta7.clicked.connect(self.venta)
        self.venta8.clicked.connect(self.venta)
        self.venta5.setEnabled(False)
        self.venta6.setEnabled(False)
        self.venta7.setEnabled(False)
        self.venta8.setEnabled(False)
        
        self.show()

    def compro(self):
        boton = self.sender()
        self.senal_compra.emit(boton.objectName())

    def venta(self):
        boton = self.sender()
        self.senal_venta.emit(boton.objectName())

    def actualizar_botones(self, data):
        if data['nombre'] == 'compra1':
            self.compra1.setEnabled(False)
            self.venta1.setEnabled(True)
        elif data['nombre'] == 'compra2':
            self.compra2.setEnabled(False)
            self.venta2.setEnabled(True)
        elif data['nombre'] == 'compra3':
            if data['cantidad'] > 0:
                self.venta3.setEnabled(True)
        elif data['nombre'] == 'compra4':
            if data['cantidad'] > 0:
                self.venta4.setEnabled(True)
        elif data['nombre'] == 'venta1':
            self.compra1.setEnabled(True)
            self.venta1.setEnabled(False)
        elif data['nombre'] == 'venta2':
            self.compra2.setEnabled(True)
            self.venta2.setEnabled(False)
        elif data['nombre'] == 'venta3':
            if data['cantidad'] == 0:
                self.venta3.setEnabled(False)
            else:
                self.venta3.setEnabled(True)
        elif data['nombre'] == 'venta4':
            if data['cantidad'] == 0:
                self.venta4.setEnabled(False)
            else:
                self.venta4.setEnabled(True)
        elif data['nombre'] == 'venta5':
            if data['cantidad'] == 0:
                self.venta5.setEnabled(False)
            else:
                self.venta5.setEnabled(True)
        elif data['nombre'] == 'venta6':
            if data['cantidad'] == 0:
                self.venta6.setEnabled(False)
            else:
                self.venta6.setEnabled(True)
        elif data['nombre'] == 'venta7':
            if data['cantidad'] == 0:
                self.venta7.setEnabled(False)
            else:
                self.venta7.setEnabled(True)
        elif data['nombre'] == 'venta8':
            if data['cantidad'] == 0:
                self.venta8.setEnabled(False)
            else:
                self.venta8.setEnabled(True)

    def no_hay_dinero(self, data):
        if data == 'precio_azada':
            self.precio_azada.setText('Dinero Insuficiente')
            self.precio_azada.setFont(FONT_CHICA)
            QTest.qWait(770)
            self.precio_azada.setText(f'${PRECIO_AZADA}')
            self.precio_azada.setFont(FONT)
        elif data == 'precio_hacha':
            self.precio_hacha.setText('Dinero Insuficiente')
            self.precio_hacha.setFont(FONT_CHICA)
            QTest.qWait(770)
            self.precio_hacha.setText(f'${PRECIO_HACHA}')
            self.precio_hacha.setFont(FONT)
        elif data == 'precio_choclo1':
            self.precio_choclo1.setText('Dinero Insuficiente')
            self.precio_choclo1.setFont(FONT_CHICA)
            QTest.qWait(770)
            self.precio_choclo1.setText(f'${PRECIO_SEMILLA_CHOCLOS}')
            self.precio_choclo1.setFont(FONT)
        elif data == 'precio_alcachofa1':
            self.precio_alcachofa1.setText('Dinero Insuficiente')
            self.precio_alcachofa1.setFont(FONT_CHICA)
            QTest.qWait(770)
            self.precio_alcachofa1.setText(f'${PRECIO_SEMILLA_ALCACHOFAS}')
            self.precio_alcachofa1.setFont(FONT)

class VentanaPerder(window_name, base_class):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_gui()

    def init_gui(self):
        pix = QPixmap(PATHS['fondo'])
        pix = pix.scaled(811, 331)
        self.label_2.setPixmap(pix)
        self.label_2.setScaledContents(True)
        self.label.setText('TE HAS QUEDADO SIN ENERGIA!\nPERDISTE!')
        sleep(3)
    
    def perder(self):
        self.show()
        sleep(5)
        sys.exit()


class Recurso(QLabel):
    def __init__(self, tipo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = tipo
        if self.tipo == 'oro':
            pix = QPixmap(PATHS['oro'])
            pix = pix.scaled(SIZE_TILE, SIZE_TILE)
            self.setPixmap(pix)
            # self.setScaledContents(True)
            self.timer = Actualizador('oro')
            self.timer.senal_destruir.connect(self.eliminar_recurso)
            self.timer.start()
        elif self.tipo == 'madera':
            pix = QPixmap(PATHS['madera'])
            pix = pix.scaled(SIZE_TILE, SIZE_TILE)
            self.setPixmap(pix)
            self.setScaledContents(True)
            self.timer = Actualizador('madera')
            self.timer.senal_destruir.connect(self.eliminar_recurso)
            self.timer.start()
        elif self.tipo == 'choclo':
            pix = QPixmap(PATHS['choclo'])
            pix = pix.scaled(SIZE_TILE, SIZE_TILE)
            self.setPixmap(pix)
            self.setScaledContents(True)
        elif self.tipo == 'alcachofa':
            pix = QPixmap(PATHS['alcachofa'])
            pix = pix.scaled(SIZE_TILE, SIZE_TILE)
            self.setPixmap(pix)
            self.setScaledContents(True)
        

    def eliminar_recurso(self):
        # self.setPixmap(None)
        self.hide()
        self.destroy()


class ClickLabel(QLabel):
    clicked = pyqtSignal()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(args[0])
        self._text = None       

    def setPixmap(self, pixmap):
        if pixmap.isNull():
            self._text = None
        else:
            self._text = self.text()
        super().setPixmap(pixmap)

    def text(self):
        if self._text:
            return self._text
        return super().text()

    def mousePressEvent(self, event):
        self.clicked.emit()
        QLabel.mousePressEvent(self, event)
    


class Inventario(window_name3, base_class3):
    senal_perder = pyqtSignal()
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.posx = 0
        self.posy = 0
        self.items = [['' for i in range(12)] for j in range(3)]

    def init_gui(self):
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
                self.items[y][x] = item
                self.inventario.addWidget(item, y, x)
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
    
    def actualizar_energia(self, energia):
        self.pbar.setValue(energia)
        if energia == 0:
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
        # grid = QGridLayout()
        # grid.itemAtPosition().widget()
        if event['modo'] == 'agregar':
            if self.posx < 11:
                item = self.inventario.itemAtPosition(self.posy, self.posx).widget()
                if item.text() != '':
                    self.posx += 1
                    self.actualizar_inventario(event)
                    return
                new_item = DraggableLabel(event['tipo'], self)
                pix = QPixmap(PATHS[event['tipo']])
                pix = pix.scaled(SIZE_TILE, SIZE_TILE)
                new_item.setPixmap(pix)
                self.items[self.posy][self.posy] = new_item
                self.inventario.replaceWidget(item, new_item)
                new_item.senal_inventario.connect(self.eliminar_item)
                item.hide()
                item.deleteLater()
                item.destroy()
                self.posx += 1
            elif self.posy < 3:
                item = self.inventario.itemAtPosition(self.posy, self.posx).widget()
                if item.text() != '':
                    self.posy += 1
                    self.posx = 0
                    self.actualizar_inventario(event)
                    return
                new_item = DraggableLabel(event['tipo'], self)
                pix = QPixmap(PATHS[event['tipo']])
                pix = pix.scaled(SIZE_TILE, SIZE_TILE)
                new_item.setPixmap(pix)
                new_item.senal_inventario.connect(self.eliminar_item)
                self.inventario.replaceWidget(item, new_item)
                item.hide()
                item.deleteLater()
                item.destroy()
                self.items[self.posy][self.posy] = new_item
                self.posy += 1
                self.posx = 0
                
            else:
                print('maximos items en el inventario')
        else:
            for y in range(len(self.items)):
                for x in range(len(self.items[0])):
                    if self.items[y][x].text() == event['tipo']:
                        posx, posy = x, y
            item = self.inventario.itemAtPosition(posy, posx).widget()
            new_item = DraggableLabel('', self)
            self.inventario.replaceWidget(item, new_item)
            item.hide()
            item.deleteLater()
            item.destroy()
            self.posy, self.posx = posy, posx
    def eliminar_item(self, data):
        item = data['object']
        new_item = DraggableLabel('', self)
        self.inventario.replaceWidget(item, new_item)
        item.hide()
        item.deleteLater()
        item.destroy()
        for y in range(len(self.items)):
            for x in range(len(self.items[0])):
                if self.items[y][x].text() == item.text():
                    posx, posy = x, y
                    break
        self.posx = posx
        self.posy = posy