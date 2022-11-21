import sys

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 500, 500)
        self.pb = QPushButton('.', self)
        self.pb.move(320, 450)
        self.draw = False
        self.c = (0, 0, 0)
        self.pb.clicked.connect(self.func)

    def func(self):
        self.x, self.y = self.get_coords()
        self.r = randint(3, 100)
        self.c = self.get_color()
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        p = QPainter()
        p.begin(self)
        p.setBrush(QColor(*self.c))
        if self.draw:
            p.drawEllipse(self.x - self.r, self.y - self.r, 2 * self.r, 2 * self.r)
        p.end()
        self.draw = False

    def get_coords(self):
        x, y = randint(0, self.width()), randint(0, self.height())
        return x, y

    def get_color(self):
        return randint(0, 255), randint(0, 255), randint(0, 255)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())

