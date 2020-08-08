import sys
import types
import inspect
from optparse import OptionParser
import random
import math
import pickle
import os
from pyowm import OWM
import librosa

from PySide2.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QPlainTextEdit, QGraphicsView, QGraphicsScene, QGraphicsProxyWidget, QAction, QMenu
from PySide2.QtGui import QFont, QColor, QImage, QPainter, QPen, QBrush
from PySide2.QtCore import Qt, QRectF

# Beat tracking example
import librosa


if __name__ == '__main__':
    print('asdf')
    # 1. Get the file path to an included audio example
    filename = librosa.example('nutcracker')
    print('asdf')

    # 2. Load the audio as a waveform `y`
    #    Store the sampling rate as `sr`
    y, sr = librosa.load(filename)
    print('asdf')

    # 3. Run the default beat tracker
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

    print('Estimated tempo: {:.2f} beats per minute'.format(tempo))

    # 4. Convert the frame indices of beat events into timestamps
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)