from NIWENV import *

from PySide2.QtWidgets import QWidget, QVBoxLayout
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import numpy as np

# import matplotlib
# import matplotlib.pyplot as plt
# matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvas#, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from qbstyles import mpl_style


class %CLASS%(QWidget, MWB):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        

        self.setStyleSheet('''
background-color: transparent;
        ''')
        mpl_style(dark=True)
        
        self.setLayout(QVBoxLayout())
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout().addWidget(self.canvas)
        self.setFixedHeight(300)
        self.ax = self.canvas.figure.subplots()

        #fig = Figure(figsize=(5, 4), dpi=100)
        #fig.add_subplot(111).plot([0,1,2,3,4], [10,1,20,3,40])


    def redraw(self, x, functions):
        self.ax.clear()
        for f in functions.keys():
            self.ax.plot(x, functions[f], label=f)
        self.ax.figure.canvas.draw()
        #self.ax.plot.legend(loc='upper left')



        #fig = plt.figure()
        #ax = fig.add_subplot(1, 1, 1)
        #ax.spines['left'].set_position('center')
        #ax.spines['bottom'].set_position('center')
        #ax.spines['right'].set_color('none')
        #ax.spines['top'].set_color('none')
        #ax.xaxis.set_ticks_position('bottom')
        #ax.yaxis.set_ticks_position('left')

        # plot the functions
        #plt.plot(x,y, 'c', label='y=sin(x)')
        #plt.plot(x,z, 'm', label='y=cos(x)')
        
        #plt.legend(loc='upper left')

        # show the plot
        #plt.show()

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
