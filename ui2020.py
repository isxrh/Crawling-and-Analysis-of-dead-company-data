# 次界面：2020年的数据分析UI显示
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import qdarkstyle


class ui2020(QWidget):
    def __init__(self):
        super(ui2020, self).__init__()
        self.setUpUI()
        self.setWindowTitle("2020年死亡公司数据分析")

    def setUpUI(self):
        # 设置字体大小和样式
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.setFont(font)

        # 背景
        # self.setStyleSheet("background-color:white")

        # Grid布局
        self.layout = QGridLayout()
        self.setLayout(self.layout)

        # Label控件
        self.titlelabel = QLabel("  ---2020年死亡公司数据分析---  ")
        fontTitle = QFont()
        fontTitle.setPointSize(20)
        self.titlelabel.setFont(fontTitle)
        self.titlelabel.setFixedHeight(80)

        self.livetimeLabel = QLabel("存活时间")
        # self.timegraph = QLabel();
        self.timewebengine = QWebEngineView(self)
        # 在QWebEngineView中加载网址
        self.timewebengine.load(QUrl(r"file:///D:/Courses/2020秋-Python/spider/html/liveTimeHistogram_20.html"))

        self.areaLabel = QLabel("地区分布")
        # self.areagraph = QLabel();
        self.areawebengine = QWebEngineView(self)
        # self.qwebengine.setGeometry(1000, 100, 600, 600)
        # 在QWebEngineView中加载网址
        self.areawebengine.load(QUrl(r"file:///D:/Courses/2020秋-Python/spider/html/chinaMap_2020.html"))

        self.statusLabel = QLabel("融资状态")
        self.statuswebengine = QWebEngineView(self)
        # 在QWebEngineView中加载网址
        self.statuswebengine.load(QUrl(r"file:///D:/Courses/2020秋-Python/spider/html/statusPieChart_20.html"))

        self.typeLabel = QLabel("公司类型")
        self.typewebengine = QWebEngineView(self)
        self.typewebengine.load(QUrl(r"file:///D:/Courses/2020秋-Python/spider/html/companyType_20.html"))

        # 控件添加到布局中
        self.layout.addWidget(self.titlelabel, 0, 0, 1, 2, Qt.AlignCenter)
        self.layout.addWidget(self.livetimeLabel, 1, 0, Qt.AlignCenter)
        self.layout.addWidget(self.timewebengine, 2, 0, Qt.AlignCenter)
        self.layout.addWidget(self.areaLabel, 1, 1, Qt.AlignCenter)
        self.layout.addWidget(self.areawebengine, 2, 1, Qt.AlignCenter)
        self.layout.addWidget(self.statusLabel, 3, 0, Qt.AlignCenter)
        self.layout.addWidget(self.statuswebengine, 4, 0, Qt.AlignCenter)
        self.layout.addWidget(self.typeLabel, 3, 1, Qt.AlignCenter)
        self.layout.addWidget(self.typewebengine, 4, 1, Qt.AlignCenter)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./images/dead_icon.png"))     # 图标
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())    # 深色背景（似乎不太好看）
    window = ui2020()
    window.showMaximized()
    sys.exit(app.exec_())