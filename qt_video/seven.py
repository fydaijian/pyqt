import sys
from PyQt5.QtWidgets import *from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

def initUI(self):
hbox = QHBoxLayout(self)
left = QFrame(self)
# QFrame 控件添加StyledPanel样式能使QFrame 控件之间的界限更加明显
#left.setFrameShape(QFrame.StyledPanel)
# right = QFrame(self)
#right.setFrameShape(QFrame.StyledPanel)
splitter1 = QSplitter(Qt.Horizontal)
splitter1.addWidget(left)
splitter1.setSizes([20,]) #设置分隔条位置
splitter1.addWidget(right)
hbox.addWidget(splitter1)
self.setLayout(hbox)


# 树
self.tree = QTreeWidget(left)
 31         self.tree.setStyleSheet("background-color:#eeeeee;border:outset;color:#215b63;")
 32         self.tree.setAutoScroll(True)
 33         self.tree.setEditTriggers(QAbstractItemView.DoubleClicked | QAbstractItemView.EditKeyPressed)
 34         self.tree.setTextElideMode(Qt.ElideMiddle)
 35         #self.tree.setIndentation(30)
 36         self.tree.setRootIsDecorated(True)
 37         self.tree.setUniformRowHeights(False)
 38         self.tree.setItemsExpandable(True)
 39         self.tree.setAnimated(False)
 40         self.tree.setHeaderHidden(True)
 41         self.tree.setExpandsOnDoubleClick(True)
 42         self.tree.setObjectName("tree")
 43
 44
 45         # 设置根节点
 46         root = QTreeWidgetItem(self.tree)
 47         root.setText(0, '系统管理')
 48         # 设置树形控件的列的宽度
 49         #self.tree.setColumnWidth(0, 150)
 50         # 设置子节点1
 51         child1 = QTreeWidgetItem()
 52         child1.setText(0, '增加人员信息')
 53         root.addChild(child1)
 54         # 设置子节点2
 55         child2 = QTreeWidgetItem(root)
 56         child2.setText(0, '查询人员信息')
 57         # 加载根节点的所有属性与子控件
 58         self.tree.addTopLevelItem(root)
 59         # 设置stackedWidget
 60         self.stackedWidget = QStackedWidget(right)
 61
 62         # 设置第一个面板
 63         self.form1 = QWidget()
 64         self.formLayout1 = QHBoxLayout(self.form1)
 65         self.label1 = QLabel()
 66         self.label1.setText("增加人员信息面板")
 67         self.label1.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
 68         self.label1.setAlignment(Qt.AlignCenter)
 69         self.label1.setFont(QFont("Roman times", 50, QFont.Bold))
 70         self.formLayout1.addWidget(self.label1)
 71
 72         # 设置第二个面板
 73         self.form2 = QWidget()
 74         self.formLayout2 = QHBoxLayout(self.form2)
 75         self.label2 = QLabel()
 76         self.label2.setText("查询人员信息面板")
 77         self.label2.setSizePolicy(QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding))
 78         self.label2.setAlignment(Qt.AlignCenter)
 79         self.label2.setFont(QFont("Roman times", 50, QFont.Bold))
 80         self.formLayout2.addWidget(self.label2)
 81
 82         # 将两个面板，加入stackedWidget
 83         self.stackedWidget.addWidget(self.form1)
 84         self.stackedWidget.addWidget(self.form2)
 85
 86         # 树节点监听事件
 87         self.tree.clicked.connect(self.onClicked)
 88
 89
 90         # 窗口最大化
 91         self.showMaximized()
 92         self.setWindowTitle('树窗口分隔案列')
 93         self.show()
 94
 95     def onClicked(self,qmodeLindex):
 96         item=self.tree.currentItem()
 97         print('Key=%s,value=%s'%(item.text(0),item.text(1)))
 98         if item.text(0) == '增加人员信息':
 99             self.on_pushButton1_clicked()
100         elif item.text(0) == '查询人员信息':
101             self.on_pushButton2_clicked()
102         else:
103             print('返回主界面')
104
105
106     # 按钮一：打开第一个面板
107     def on_pushButton1_clicked(self):
108         self.stackedWidget.setCurrentIndex(0)
109
110     # 按钮二：打开第二个面板
111     def on_pushButton2_clicked(self):
112         self.stackedWidget.setCurrentIndex(1)
113
114
115 if __name__ == '__main__':
116     app = QApplication(sys.argv)
117     ex = Example()
118     sys.exit(app.exec_())