# -*- coding:utf-8 -*-
# 主界面

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ui2020 import ui2020
from ui2019 import ui2019
from ui2018 import ui2018
from ui2017 import ui2017
from PyQt5.QtWebEngineWidgets import *
import qdarkstyle


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setUpUI()
        self.setWindowTitle("主界面")

    def setUpUI(self):
        # 布局
        self.layout = QGridLayout()

        # 背景色
        # self.setStyleSheet("background-color:white")

        # 字体
        font = QFont()
        font.setPointSize(12)
        self.setFont(font)
        font.setFamily("微软雅黑")
        fontTitle = QFont()
        font.setFamily("微软雅黑")
        fontTitle.setPointSize(20)

        # 标题
        self.titlelabel = QLabel("死亡公司库")
        self.titlelabel.setFont(fontTitle)
        self.titlelabel.setFixedHeight(40)

        # 折线图
        self.graphLabel = QLabel("存活时间")
        self.graphwebengine = QWebEngineView(self)
        # 在QWebEngineView中加载网址
        self.graphwebengine.load(QUrl(r"file:///D:/Courses/2020秋-Python/spider/html/numLineChart.html"))

        # 按钮
        self.btn20 = QPushButton("2020")
        self.btn20.setFont(font)
        # self.btn20.setEnabled(True)
        # self.btn20.setIcon(QIcon(QPixmap("./images/.png")))
        self.btn20.clicked.connect(self.btn20click)

        self.btn19 = QPushButton("2019")
        self.btn19.setFont(font)
        # self.btn19.setEnabled(False)
        self.btn19.clicked.connect(self.btn19click)

        self.btn18 = QPushButton("2018")
        self.btn18.setFont(font)
        self.btn18.clicked.connect(self.btn18click)

        self.btn17 = QPushButton("2017")
        self.btn17.setFont(font)
        self.btn17.clicked.connect(self.btn17click)

        # 控件添加到布局
        self.layout.addWidget(self.titlelabel, 0, 0, 2, 4, Qt.AlignCenter)
        self.layout.addWidget(self.graphwebengine, 2, 0, 1, 4, Qt.AlignCenter)
        self.layout.addWidget(self.btn20, 3, 0)
        self.layout.addWidget(self.btn19, 3, 1)
        self.layout.addWidget(self.btn18, 3, 2)
        self.layout.addWidget(self.btn17, 3, 3)
        self.setLayout(self.layout)

    # '2020'按钮的槽函数
    def btn20click(self):
        # self.hide()
        self.ui = ui2020()
        self.ui.showMaximized()

    # 19的槽函数
    def btn19click(self):
        # self.hide()
        self.ui = ui2019()
        self.ui.showMaximized()

    # 18的槽函数
    def btn18click(self):
        # self.hide()
        self.ui = ui2018()
        print("2018")
        self.ui.showMaximized()

    # 17的槽函数
    def btn17click(self):
        # self.hide()
        self.ui = ui2017()
        print("2017")
        self.ui.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/dead_icon.png"))     # 图标
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())     # 深色背景
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
