from PyQt5.QtWidgets import QApplication
from Ventanas import VentanaJuego, VentanaPalabra, VentanaGif
from DCColgado import DCColgado
import sys


def hook(type, value, traceback):
    print(type)
    print(traceback)
sys.__excepthook__ = hook

# Se instancia la app
app = QApplication(sys.argv)

# Se crea el Front-end
ventana2 = VentanaPalabra()

ventana = VentanaJuego(ventana2)
ventana.show()

ventanagif = VentanaGif()
# Se crea el Back-end
DCC_51 = DCColgado()

# Se conectan las señales de front-end con el back-end.
ventana.enviar_letra_signal.connect(DCC_51.check_info)
ventana.reiniciar_signal.connect(DCC_51.nueva_palabra)
ventana2.enviar_palabra_signal.connect(DCC_51.check_info)



# ===== Debes conectar esta señal con el metodo respectivo del front-end ======
DCC_51.respuesta_signal.connect(ventana.actualizar_interfaz)
DCC_51.end_signal.connect(ventanagif.abrir_gif)


# Se inicia una partida.
ventana.reiniciar_signal.emit()
sys.exit(app.exec())
