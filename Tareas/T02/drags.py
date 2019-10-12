import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import QMimeData, Qt, pyqtSignal
from parametros_generales import PATHS
from plantas import Planta


class DraggableLabel(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setText(args[0])
        self._text = None
        self.setAcceptDrops(True)
        print("my text in init ", self.text())


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
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        mimedata.setImageData(self.pixmap().toImage())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        # pixmap = QPixmap(PATHS['alcachofa'])
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(Qt.CopyAction | Qt.MoveAction)

    # def setPixmap(self, QPixmap):
    #     super().setPixmap(self, QPixmap)


class DropLabel(QLabel):
    senal_actualizar = pyqtSignal(str)
    def __init__(self, *args, **kwargs):
        QLabel.__init__(self, *args, **kwargs)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasImage():
            print("event accepted")
            event.acceptProposedAction()
        else:
            print('event rejected')
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().text() in ['semilla_a', 'semilla_c']:
            pos = event.pos()
            text = event.mimeData().text()
            # self.setPixmap(QPixmap(event.mimeData().imageData()))
            print('mimetext', text)
            planta = Planta(text)
            
            event.acceptProposedAction()
        else:
            print('invalid operation')

class Widget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.label = DropLabel("muh",self)
        self.label.setGeometry(190, 65, 100,100)

        self.label_to_drag = DraggableLabel("mist",self)  
        pixmap = QPixmap(PATHS['alcachofa'])
        self.label_to_drag.setPixmap(pixmap)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())