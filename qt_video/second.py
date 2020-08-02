import sys
from PyQt5.QtWidgets import QDesktopWidget,QMainWindow, QApplication, QAction
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):

    def __init__(self, parent= None):
        super(FirstMainWin,self).__init__(parent)
        self.setWindowTitle('fist windon')
        self.resize(400,300)
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()



        bar = self.menuBar()
        file = bar.addMenu("file")
        file.addAction(QAction('new',self))

        save = QAction("Save", self)
        save.setShortcut("ctrl+s")
        file.addAction(save)

        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction('paste')

        file.triggered[QAction].connect(self.processtrigger)

    def processtrigger(self, q):
        print(q.text()+"is triggers")

if __name__ == "__main__":

    app = QApplication(sys.argv)
    demo = FirstMainWin()
    demo.show()
    sys.exit(app.exec_())


