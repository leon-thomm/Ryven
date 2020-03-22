import sys
import random
import math
import pickle

from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QAction, QMenu
from PySide2.QtGui import QFont, QColor, QImage, QPainter, QPen, QBrush
from PySide2.QtCore import Qt, QRectF


class CodeWidget(QWidget):
    def __init__(self):
        super(CodeWidget, self).__init__()

        # UI
        self.setLayout(QVBoxLayout())

        self.add_new_script()

    def add_new_script(self):
        code_text_edit = QPlainTextEdit('test code')
        code_text_edit.setStyleSheet('background: black; color: grey;')
        print('before: ', self.height())
        self.layout().addWidget(code_text_edit)
        print('after: ', self.height())

    def mousePressEvent(self, event):
        print('mouse pressed! adding new script')
        self.add_new_script()


class MyView(QGraphicsView):
    def __init__(self):
        super(MyView, self).__init__()


        # create UI
        scene = QGraphicsScene(self)
        scene.setSceneRect(0, 0, 500, 500)

        self.setScene(scene)

        self.code_proxy = QGraphicsProxyWidget()
        self.code_widget = CodeWidget()
        self.code_proxy.setWidget(self.code_widget)

        scene.addItem(self.code_proxy)
        self.code_proxy.setPos(50, 50)




class MyAction(QAction):
    def __init__(self, text, menu):
        super(MyAction, self).__init__(text=text, parent=menu)


class MyWidget(QWidget):
    def __init__(self):
        super(MyWidget, self).__init__()

    def contextMenuEvent(self, event):
        menu = QMenu()
        menu.addAction(MyAction('action 1', menu))
        menu.addAction(MyAction('action 2', menu))
        menu.exec_(event.globalPos())


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # w = MyView()
        w = MyWidget()

        self.setCentralWidget(w)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    mw = MainWindow()
    mw.show()

    sys.exit(app.exec_())

    # db = QFontDatabase()
    # print(QFontDatabase.families())