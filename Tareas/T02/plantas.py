from PyQt5.QtCore import QObject, QTimer

class Planta(QObject):
    senal_update = None
    def __init__(self, tipo, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.tipo = tipo
        self.timer = QTimer()
        self.timer.start(100)
        self.init_gui()

    def init_gui(self):
        while self.timer.remainingTime() > 0:
            print(self.timer.remainingTime())




