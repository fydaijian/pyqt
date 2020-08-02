from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import  QHBoxLayout,QMainWindow,QApplication,QLabel, QWidget
from PyQt5.QtGui import QPalette
import sys

class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)

        label1.setText("hello")
        label1.setAlignment(Qt.AlignCenter)
        self.setWindowTitle('label ')


if __name__ == "__main__":

    app = QApplication(sys.argv)
    main = QLabelDemo()
    main.show()
    sys.exit(app.exec_())




