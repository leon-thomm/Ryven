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





from qtconsole.rich_jupyter_widget import RichJupyterWidget
from qtconsole.inprocess import QtInProcessKernelManager


class ConsoleWidget(RichJupyterWidget):


    def __init__(self, customBanner=None, *args, **kwargs):
        super(ConsoleWidget, self).__init__(*args, **kwargs)

        if customBanner is not None:
            self.banner = customBanner

        self.font_size = 6
        self.kernel_manager = kernel_manager = QtInProcessKernelManager()
        kernel_manager.start_kernel(show_banner=False)
        kernel_manager.kernel.gui = 'qt'
        self.kernel_client = kernel_client = self._kernel_manager.client()
        kernel_client.start_channels()

        def stop():
            kernel_client.stop_channels()
            kernel_manager.shutdown_kernel()
            guisupport.get_app_qt().exit()

        self.exit_requested.connect(stop)

    def push_vars(self, variableDict):
        """
        Given a dictionary containing name / value pairs, push those variables
        to the Jupyter console widget
        """
        self.kernel_manager.kernel.shell.push(variableDict)

    def clear(self):
        """
        Clears the terminal
        """
        self._control.clear()

        # self.kernel_manager

    def print_text(self, text):
        """
        Prints some plain text to the console
        """
        self._append_plain_text(text)

    def execute_command(self, command):
        """
        Execute a command in the frame of the console widget
        """
        self._execute(command, False)






from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QAction, QMenu
from PySide2.QtGui import QFont, QColor, QImage, QPainter, QPen, QBrush
from PySide2.QtCore import Qt, QRectF

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


if __name__ == '__main__':
    # pw = PlaceholderWidget()
    # print('1')
    # pw.x = 10
    # print(pw.x)
    # print('2')
    # print(pw.y())
    # pw.foo(15)
    # print('3')


    app = QApplication()
    widget = ConsoleWidget()
    widget.show()
    app.exec_()


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