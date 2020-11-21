from custom_src.retain import M

# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class %CLASS%(FigureCanvasQTAgg):
    def __init__(self, parent_node_instance):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.axes = fig.add_subplot(111)
        super(%CLASS%, self).__init__(fig)

        

        self.setStyleSheet('''

        ''')

        self.axes.plot([0,1,2,3,4], [10,1,20,3,40])


    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
