from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout, 
                             QGridLayout, QSizePolicy)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect, QTimer)
from PyQt5.QtGui import (QPixmap, QFont)
from PyQt5 import uic
import sys
import json
from os.path import join
from client import Cliente


#TODO: Create the desginer file for the main windows of the application

window_name, base_class = uic.loadUiType("principal.ui")
window_name2, base_class2 = uic.loadUiType("club.ui")

class VentanaPrincipal(window_name, base_class):
    main_window_signal = pyqtSignal(dict)
    senal_a_backend = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_gui()
        self.senal_mensaje_chat = None
        self.client = None
            
    def init_gui(self):
        self.client = Cliente()
        self.senal_mensaje_chat = self.client.enviar_a_interfaz
        self.senal_a_backend.connect(self.client.enviar_al_servidor)
        with open("parametros.json", 'r') as file:
            lista_cargada = json.load(file)
        
        pixmap = QPixmap(lista_cargada['PATHS']['logo'])
        
        self.label.setPixmap(pixmap)
        self.label.setScaledContents(True)
        self.ingresar.clicked.connect(self.entrar)
        self.show()

    def entrar(self):
        with open("../usuarios.json", 'r') as file:
            lista_usuarios = json.load(file)
        for d in lista_usuarios:
            if d['nombre'] == self.usuario.text():
                if self.client.check_user(d['nombre']):
                    self.main_window_signal.emit(d)
                    self.senal_a_backend.emit(d['nombre'], True)
                    self.error.setText('Acceso Permitido!')
                    self.hide()
                    return
                else:
                    self.error.setText('Nombre de usuario invalido!')
        self.error.setText('Nombre de usuario invalido!')


class VentanaClub(window_name2, base_class2):
    disconnect_signal = pyqtSignal()
    actualizar_salas_signal = pyqtSignal(dict)
    connect_sala_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.init_gui()
        
        self.actualizar_salas_signal.connect(self.actualizar_salas)

    def init_gui(self, usuario):

        # self.backend = BackEnd(usuario)
        # self.backend.profile_signal.connect(self.cargar_amistades)
        self.usuario = usuario
        self.nombre.setText(usuario['nombre'])
        font = QFont('Times', 16)
        self.nombre.setFont(font)
        with open('parametros.json', 'r') as file:
            lista = json.load(file)
        path = f'{lista["PATHS"]["personajes"]}{usuario["personaje"]}/idle.png'
        print(path)
        pixmap = QPixmap(path)
        self.personaje.setPixmap(pixmap)
        self.personaje.setScaledContents(True)
        with open("parametros.json", 'r') as file:
            lista_cargada = json.load(file)
        
        pixmap2 = QPixmap(lista_cargada['PATHS']['logo'])
        
        self.logo.setPixmap(pixmap2)
        self.logo.setScaledContents(True)
        self.cargar_amistades(usuario)
        self.lobby1.clicked.connect(self.entrar_sala)
        self.show()

    def cargar_amistades(self, data):
        with open('../amigos.json', 'r') as file:
            listado = json.load(file)
        amigos = listado[self.usuario['nombre']]
        cantidad = len(amigos)
        lista_amigos = ''
        for amigo in amigos:
            lista_amigos += amigo 
            lista_amigos += '\n'
        print(lista_amigos)
        self.amigos.setText(lista_amigos)
        self.cantidad.setText(str(cantidad))
        font = QFont('Times', 14)
        self.amigos.setFont(font)
        self.cantidad.setFont(font)


    def closeEvent(self, event):
        print(event)
        self.disconnect_signal.emit()


    def actualizar_salas(self, data):
        pass

    def entrar_sala(self):
        self.connect_sala_signal.emit(self.usuario)
        self.hide()

