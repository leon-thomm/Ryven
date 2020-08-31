from custom_src.retain import M

# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import os
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


package_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))


class %NODE_TITLE%_NodeInstance_MainWidget(FigureCanvasQTAgg):
    def __init__(self, parent_node_instance):
        fig = Figure(figsize=(5, 4), dpi=100)
        self.axes = fig.add_subplot(111)
        super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__(fig)

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

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
