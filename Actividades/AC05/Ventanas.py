from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QApplication, QHBoxLayout, QVBoxLayout)
from PyQt5.QtCore import (pyqtSignal, Qt, QRect)
from PyQt5.QtGui import (QPixmap, QFont, QMovie)


"""
Debes completar la clase VentanaJuego con los elementos que
estimes necesarios.

Eres libre de agregar otras clases si lo crees conveniente.
"""

class VentanaJuego(QWidget):
    """
    Señales para enviar información (letras o palabras)
    y crear una partida, respectivamente.

    Recuerda que eviar_letra_signal debe llevar un diccionario de la forma:
        {
            'letra': <string>,
            'palabra': <string>  -> Este solo en caso de que 
                                    implementes el bonus
        }
    Es importante que SOLO UNO DE LOS ELEMENTOS lleve contenido, es decir,
    o se envía una letra o se envía una palabra, el otro DEBE 
    ir como string vacío ("").
    """
    enviar_letra_signal = pyqtSignal(dict)
    reiniciar_signal = pyqtSignal()
    recibir_palabra = pyqtSignal(str)

    def __init__(self, ventana=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_gui()
        self.diccionario = {
            'letra': '',
            'palabra': ''
        }
        self.ventana = ventana

    def init_gui(self):
        self.setGeometry(200,200,1000,600)
        self.setWindowTitle('DCColgado51')

        self.label1 = QLabel('Palabra: ', self)
        self.label1.move(10,15)
        self.label1.resize(self.label1.sizeHint())

        self.label = QLabel('', self)
        self.label.move(10, 60)
        self.label.resize(self.label.sizeHint())

        self.letra = QLabel('', self)
        self.letra.move(10, 90)
        self.letra.resize(self.letra.sizeHint())

        self.label2 = QLabel('USADAS: ', self)
        self.label2.move(360, 500)
        self.label2.resize(self.label2.sizeHint())

        self.label3 = QLabel('DISPONIBLES: ', self)
        self.label3.move(360, 530)
        self.label3.resize(self.label3.sizeHint())


        self.boton1 = QPushButton('Seleccionar Letra', self)
        self.boton1.move(10, 500)
        self.boton1.resize(self.boton1.sizeHint())
        self.boton1.clicked.connect(self.enviar_intento)

        self.boton2 = QPushButton('Ingresar Palabra Completa', self)
        self.boton2.move(10, 530)
        self.boton2.resize(self.boton2.sizeHint())
        self.boton2.clicked.connect(self.intentar_palabra)

        self.boton3 = QPushButton('Nuevo Juego', self)
        self.boton3.move(10, 560)
        self.boton3.resize(self.boton3.sizeHint())
        self.boton3.clicked.connect(self.boton_clickeado)

        self.labelimg1 = QLabel(self)
        self.labelimg1.move(400, 50)
        

    def actualizar_interfaz(self, data):
        usadas = 'USADAS: '
        usadas += data["usadas"]
        disp = 'DISPONIBLES: '
        disp += data['disponibles']
        self.label1.setText(data['palabra'])
        self.label1.resize(self.label1.sizeHint())
        self.label2.setText(usadas)
        self.label2.resize(self.label2.sizeHint())
        self.label3.setText(disp)
        self.label3.resize(self.label3.sizeHint())
        ruta_imagen = data['imagen']
        pixeles = QPixmap(ruta_imagen)
        self.labelimg1.setPixmap(pixeles)
        self.labelimg1.setScaledContents(True)
        self.labelimg1.resize(self.labelimg1.sizeHint())
        self.label.setText(data['msg'])
        self.label.resize(self.label.sizeHint())

    def keyPressEvent(self, e):
        self.letra.setText(e.text())
        self.letra.resize(self.letra.sizeHint())
        self.diccionario['letra'] = e.text()
        
    def boton_clickeado(self):
        self.reiniciar_signal.emit()
        self.ventana.hide()

    def enviar_intento(self):
        self.enviar_letra_signal.emit(self.diccionario) 

    def intentar_palabra(self):
        if self.ventana:
            self.ventana.show()


class VentanaPalabra(QWidget):

    enviar_palabra_signal = pyqtSignal(dict)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.init_gui()
        self.data = {
            'letra': '',
            'palabra': ''
        }

    def init_gui(self):
        self.setGeometry(300,300, 450,200)
        self.setWindowTitle('Completar Palabra')

        self.palabra = QLineEdit('', self)
        self.palabra.setGeometry(10,50, 300, 100)

        self.boton = QPushButton('Completar', self)
        self.boton.move(350, 100)

        self.boton.clicked.connect(self.enviar_palabra)

    def enviar_palabra(self):
        self.data['palabra'] = self.palabra.text()
        self.enviar_palabra_signal.emit(self.data)
        
class VentanaGif(QWidget):
    def __init__(self):
        super().__init__()
        self.init_gui()
        

    def init_gui(self):
        self.setGeometry(300,300, 450,500)

        self.gif = QLabel('', self)
        self.gif.resize(self.gif.sizeHint())

    def abrir_gif(self, data):
        print('hi')
        pixeles = QPixmap(data['gif'])
        self.gif.setPixmap(pixeles)
        self.gif.setScaledContents(True)
        self.gif.resize(self.gif.sizeHint())
        self.show()

