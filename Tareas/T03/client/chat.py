from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QTimer)
from PyQt5.QtGui import (QPixmap, QFont)
from PyQt5 import uic
import sys
import json
from os.path import join

window_name, base_class = uic.loadUiType("chat.ui")

class VentanaChat(window_name, base_class):
    salir_chat_signal = pyqtSignal()
    senal_backend = pyqtSignal()

    def __init__(self, number):
        super().__init__()
        self.number = number
        self.setupUi(self)
        # self.init_gui(number)

    def init_gui(self, usuario):
        with open('parametros.json', 'r') as file:
            lista = json.load(file)
        pixmap = QPixmap(f'{lista["PATHS"]["fondo"]}/{self.number}.png')
        self.fondo.setPixmap(pixmap)
        self.fondo.setScaledContents(True)
        path = f'{lista["PATHS"]["personajes"]}{usuario["personaje"]}/idle.png'
        print(path)
        pixmap = QPixmap(path)
        self.usuario.setPixmap(pixmap)
        self.usuario.setScaledContents(True)
        pixmap = QPixmap(lista["PATHS"]['server_char'])
        self.server.setPixmap(pixmap)
        self.server.setScaledContents(True)
        self.enviar.clicked.connect(self.enviar_mensaje)
        self.show()

    def mostrar_mensaje(self, data):
        pass

    def enviar_mensaje(self):
        mensaje = self.mensaje.text()
        print(mensaje)


    
    def closeEvent(self, event):
        print(event)
        self.salir_chat_signal.emit()
