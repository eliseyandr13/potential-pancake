import PyQt5.QtWidgets as qtw
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
import sys
from random import randint


class MyWidget(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 600, 600)
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_flag(self, qp):
        qp.setPen(QPen(Qt.yellow,  8, Qt.SolidLine))
        n = randint(1, 400)
        qp.drawEllipse(randint(1, 600), randint(1, 600), n, n)



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())