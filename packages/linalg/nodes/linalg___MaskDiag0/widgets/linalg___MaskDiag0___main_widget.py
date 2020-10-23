from NIWENV import *

# from PySide2.QtWidgets import ...
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...

import os
import importlib.util


package_path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))
spec = importlib.util.spec_from_file_location('matrix_widget.MatrixWidget', package_path+'/matrix_widget.py')
matrix_widget = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix_widget)


class MaskDiag_NodeInstance_MainWidget(matrix_widget.MatrixWidget):
    def __init__(self, parent_node_instance):
        super(MaskDiag_NodeInstance_MainWidget, self).__init__(parent_node_instance)
