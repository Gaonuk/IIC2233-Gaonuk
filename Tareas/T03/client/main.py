from PyQt5.QtWidgets import QApplication
import sys
from ventana import VentanaClub, VentanaPrincipal
from chat import VentanaChat
# from procesos import BackEnd
import socket

def hook(type, value, traceback):
    print(type)
    print(traceback)

sys.__excepthook__ = hook

app = QApplication([])
ventana = VentanaPrincipal()
club = VentanaClub()
chat = VentanaChat(1)
chat2 = VentanaChat(2)
chat3 = VentanaChat(3)
chat4 = VentanaChat(4)

ventana.main_window_signal.connect(club.init_gui)
club.disconnect_signal.connect(ventana.show)
club.connect_sala_signal.connect(chat.init_gui)
ventana.senal_mensaje_chat.connect(chat.mostrar_mensaje)
chat.salir_chat_signal.connect(club.show)
ventana.show()
sys.exit(app.exec_())


