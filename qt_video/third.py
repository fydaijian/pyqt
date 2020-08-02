import sys
from PyQt5.QtWidgets import QPushButton,QWidget,QHBoxLayout, QMainWindow,QApplication,QWidget

class QuitApplication(QWidget):
    def __init__(self):
        super(QuitApplication,self).__init__()
        self.resize(300,120)
        self.setWindowTitle("qwidget")

        self.button1 = QPushButton("application")
        self.button1.clicked.connect(self.onClick_BUtton)

        layout = QHBoxLayout(self)
        layout.addWidget(self.button1)

        # mainFrame = QWidget()
        # mainFrame.setLayout(layout)
        # self.setCentralWidget(mainFrame)



    def onClick_BUtton(self):
        sender = self.sender()
        print(sender.text() + "按键按下")
        app = QApplication.instance()
        app.quit()


if __name__ == "__main__":

    app = QApplication(sys.argv)
    demo = QuitApplication()
    demo.show()
    sys.exit(app.exec_())