from NIWENV import *

from PySide2.QtWidgets import QWidget, QVBoxLayout
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import numpy as np
from random import random as random

import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT as NavigationToolbar
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
        self.setFixedWidth(550)
        self.setFixedHeight(500)
        self.ax = self.canvas.figure.subplots()


    def redraw_by_func(self, f_str, noise_range, m, degree_min, degree_max, space_min, space_max):

        x = np.linspace(space_min, space_max, m)

        # some noise to add
        noise = np.array([10*random()-5 for i in range(m)])
        f = eval('lambda x: '+f_str+'+random()*'+str(noise_range)+'-'+str(noise_range/2))
        # vectorizing f doesn't seem to work with random()
        y = np.array([f(i) for i in x])

        data = np.array([[x[i], y[i]] for i in range(len(x))])
        self.redraw_by_data(data, degree_min, degree_max, space_min, space_max)


    def redraw_by_data(self, data, degree_min, degree_max, space_min, space_max):
        data = np.array(data)
        x = data[:,0]
        y = data[:,1]

        self.ax.clear()
        self.ax.plot(x, y, 'ro')    # our data

        for d in range(degree_min, degree_max+1):   # for all degrees
            # compute vandermonde-matrix
            U = np.zeros((len(data), d+1))
            for i in range(d+1):
                # column i = x^i
                U[:,i] = np.power(x, i)

            # compute out approximation coefficients
            # UH U a = UH y ====> a = (UH U)^-1 UH y
            UH = U.conjugate().transpose()
            a = \
            np.matmul(
                np.matmul(
                    np.linalg.inv(
                        np.matmul(UH, U)
                    ),
                    UH
                ),
                y
            )   # very beautiful^^

            # creating a detailed space for the polynom
            space = np.linspace(space_min, space_max, 300)

            # plotting
            self.ax.plot(space, sum([np.power(space, i)*a[i] for i in range(a.size)]),
                     label= '$'+''.join([
                         '{:.1f}x^{}'.format(a[i], i) if a[i]<0 or i==0
                         else '+{:.1f}x^{}'.format(a[i], i)
                         for i in range(d+1)])+'$'
            )   # our points

        self.ax.legend()    # legend.
        # plt.show()

        self.ax.figure.canvas.draw()



    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
