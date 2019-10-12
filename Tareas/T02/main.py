from ventanas import Inventario, VentanaInicio, VentanaJuego
from PyQt5.QtWidgets import QApplication
import sys
from threads import Calendario, Actualizador
from ventanas2 import VentanaPerder, VentanaTienda

def hook(type, value, traceback):
    print(type)
    print(traceback)

sys.__excepthook__ = hook

app = QApplication([])
juego = VentanaJuego()
ventana = VentanaInicio()
inv = Inventario()
tienda = VentanaTienda()
perder = VentanaPerder()
ventana.show()
ventana.senal_juego.connect(juego.init_gui)
juego.senal_inventario.connect(inv.init_gui)
juego.senal_compra = tienda.senal_compra
juego.senal_venta = tienda.senal_venta
juego.inventario_signal_update.connect(inv.actualizar_inventario)
juego.restaurar_energia.connect(inv.restaurar_energia)
juego.actualizar_dinero.connect(inv.actualizar_dinero)
inv.senal_perder.connect(perder.init_gui)
CALENDARIO = Calendario()
CALENDARIO.senal_tiempo.connect(inv.actualizar_labels)
CALENDARIO.senal_energia.connect(inv.actualizar_energia)
juego.senal_start.connect(CALENDARIO.start)



sys.exit(app.exec_())