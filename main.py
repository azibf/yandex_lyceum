from random import randint
import sys
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic


class Main(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.z = 0
        self.x = 0
        self.y = 0
        self.color = QColor('yellow')
        self.initUI()

    def initUI(self):
        self.show()
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.z = randint(10, 100)
        self.x = randint(0, 500)
        self.y = randint(0, 500)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawc(qp)
        qp.end()

    def drawc(self, qp):
        qp.setBrush(self.color)
        qp.drawEllipse(self.x, self.y, self.z, self.z)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    sys.exit(app.exec_())
