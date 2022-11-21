import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.func)

    def func(self):
        self.x, self.y = self.get_coords()
        self.r = randint(3, 100)
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setBrush(QColor(200, 150, 0))
        if self.draw:
            p.drawEllipse(self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r)
        p.end()
        self.draw = False

    def get_coords(self):
        x, y = randint(0, self.width()), randint(0, self.height())
        return x, y


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

