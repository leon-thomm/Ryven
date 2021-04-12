# import sys
# import types
# import inspect
# from optparse import OptionParser
# import random
# import math
# import pickle
# import os
# from pyowm import OWM
# import librosa
# import numpy as np
# np.complex





# from qtconsole.rich_jupyter_widget import RichJupyterWidget
# from qtconsole.inprocess import QtInProcessKernelManager


# class ConsoleWidget(RichJupyterWidget):
#
#
#     def __init__(self, customBanner=None, *args, **kwargs):
#         super(ConsoleWidget, self).__init__(*args, **kwargs)
#
#         if customBanner is not None:
#             self.banner = customBanner
#
#         self.font_size = 6
#         self.kernel_manager = kernel_manager = QtInProcessKernelManager()
#         kernel_manager.start_kernel(show_banner=False)
#         kernel_manager.kernel.gui = 'qt'
#         self.kernel_client = kernel_client = self._kernel_manager.client()
#         kernel_client.start_channels()
#
#         def stop():
#             kernel_client.stop_channels()
#             kernel_manager.shutdown_kernel()
#             guisupport.get_app_qt().exit()
#
#         self.exit_requested.connect(stop)
#
#     def push_vars(self, variableDict):
#         """
#         Given a dictionary containing name / value pairs, push those variables
#         to the Jupyter console widget
#         """
#         self.kernel_manager.kernel.shell.push(variableDict)
#
#     def clear(self):
#         """
#         Clears the terminal
#         """
#         self._control.clear()
#
#         # self.kernel_manager
#
#     def print_text(self, text):
#         """
#         Prints some plain text to the console
#         """
#         self._append_plain_text(text)
#
#     def execute_command(self, command):
#         """
#         Execute a command in the frame of the console widget
#         """
#         self._execute(command, False)






from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QGraphicsView, \
    QGraphicsScene, QGraphicsProxyWidget, QMenu, QGestureRecognizer, QGesture, QLineEdit, \
    QGraphicsItem, QPushButton
from PySide6.QtGui import QFont, QColor, QImage, QPainter, QPen, QBrush, QTouchEvent, QKeySequence, QMouseEvent, QAction, QShortcut
from PySide6.QtCore import Qt, QRectF, QEvent


# Beat tracking example
# import librosa


class PlaceholderAttributeException(Exception):
    pass


class Nope:
    pass


def placeholder_method(*args):
    pass

class PlaceholderWidget:
    # def __getattr__(self, item):
    #     print('getting attribute', item)
    #     if not hasattr(self, item):
    #         raise PlaceholderAttributeException('nope')
    #     else:
    #         return super(PlaceholderWidget, self).__getattr__(item)

    def y(self):
        return 'y!'

    def __getattr__(self, item):
        print('getting attribute:', item)

        def method(*args):
            print('unknown method used:', item)

        return method

    def __setattr__(self, key, value):
        print('setting attr', key, 'to', value)
        print(hasattr(self, key))
        if not hasattr(self, key):
            return
        super(PlaceholderWidget, self).__setattr__(key, value)


class PanGesture(QGesture):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pos = None
        self.press = None
        self.last = None


class PanGestureRecognizer(QGestureRecognizer):
    # def __init__(self):
    #     super(PanGestureRecognizer, self).__init__()

    def create(self, target) -> QGesture:
        return PanGesture()

    def reset(self, state: QGesture) -> None:
        pass

    def recognize(self, state: QGesture, watched, event: QEvent) -> QGestureRecognizer.Result:
        if event.type() == QEvent.TouchBegin:
            touch_event: QTouchEvent = event
            if len(touch_event.touchPoints()) == 1:
                state.press = touch_event.touchPoints()[0]
                state.pos = state.press
                return QGestureRecognizer.MayBeGesture
        elif event.type() == QEvent.TouchUpdate:
            touch_event: QTouchEvent = event
            state.last = state.pos
            state.pos = touch_event.touchPoints()[0]
            return QGestureRecognizer.TriggerGesture
        return QGestureRecognizer.Ignore


class Item(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)

    def boundingRect(self) -> QRectF:
        return QRectF(0,0,50,50)

    def paint(self, painter, option, widget) -> None:
        painter.fillRect(self.boundingRect(), QColor('#555555'))

class View(QGraphicsView):
    def __init__(self):
        super().__init__()

        # self.resize(300, 200)
        scene = QGraphicsScene(self)
        # scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(0, 0, self.width(), self.height())
        self.setScene(scene)

        recognizer = PanGestureRecognizer()
        pan_gesture_id = QGestureRecognizer.registerRecognizer(recognizer)
        self.grabGesture(pan_gesture_id)

        # copy_shortcut = QShortcut(QKeySequence.Copy, self)
        # copy_shortcut.activated.connect(self.copy)

    #     self.setCacheMode(QGraphicsView.CacheBackground)
    #     self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
    #     self.setRenderHint(QPainter.Antialiasing)
    #     self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
    #     self.setDragMode(QGraphicsView.RubberBandDrag)
    #     scene.selectionChanged.connect(self.selection_changed)
    #     self.scene().addItem(Item())
    #
    #
    #
    # def selection_changed(self):
    #     print('selection changed!')
    #     print(self.scene().selectedItems())
    #
    # def mousePressEvent(self, event:QMouseEvent) -> None:
    #     if event.button() == Qt.RightButton:
    #         if self.itemAt(event.pos()):
    #             print(self.scene().selectedItems())
    #             return
    #         i = Item()
    #         self.scene().addItem(i)
    #         i.setPos(event.pos())
    #     return QGraphicsView.mousePressEvent(self, event)

    def copy(self):
        print('copy in view!')


class W(QWidget):
    def __init__(self):
        super().__init__()
        copy_shortcut = QShortcut(QKeySequence.Copy, self)
        copy_shortcut.activated.connect(self.copy)
        select_all_shortcut = QShortcut(QKeySequence.SelectAll, self)
        select_all_shortcut.activated.connect(self.select_all)
        self.setFixedSize(300, 200)
        self.setFocusPolicy(Qt.ClickFocus)

    def copy(self):
        print('copy!')

    def select_all(self):
        print('select all!')


class MyButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)

class ViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(View())



#         self.setLayout(QVBoxLayout())
#
#         l = QVBoxLayout()
#         l.addWidget(W())
#         textedit = QPlainTextEdit('''
# kjasdgfiuzakhdousdhjlsd
#         ''')
#         textedit.setReadOnly(True)
#         # textedit.setProperty('NoFocus', True)
#         textedit.setFocusPolicy(Qt.ClickFocus)
#         l.addWidget(textedit)
#
#         l.addWidget(MyButton('asdf'));
#
#         w = QWidget()
#         w.setLayout(l)
#         self.setCentralWidget(w)
#
#
#         self.setStyleSheet('''
# QPushButton {
#     background-color: blue;
# }
# QPushButton.MyButton {
#     background-color: green;
# }
#         ''')


if __name__ == '__main__':
    app = QApplication()
    widget = ViewWindow()
    widget.show()
    app.exec_()

    # pw = PlaceholderWidget()
    # print('1')
    # pw.x = 10
    # print(pw.x)
    # print('2')
    # print(pw.y())
    # pw.foo(15)
    # print('3')


    # print('asdf')
    # # 1. Get the file path to an included audio example
    # filename = librosa.example('nutcracker')
    # print('asdf')
    #
    # # 2. Load the audio as a waveform `y`
    # #    Store the sampling rate as `sr`
    # y, sr = librosa.load(filename)
    # print('asdf')
    #
    # # 3. Run the default beat tracker
    # tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    #
    # print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
    #
    # # 4. Convert the frame indices of beat events into timestamps
    # beat_times = librosa.frames_to_time(beat_frames, sr=sr)
