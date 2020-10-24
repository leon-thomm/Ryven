from NIWENV import *
from PySide2.QtWidgets import QTextEdit
import importlib.util
package_path = widget_pp(__file__)
spec = importlib.util.spec_from_file_location('matrix_widget.MatrixWidget', package_path+'/matrix_widget.py')
matrix_widget = importlib.util.module_from_spec(spec)
spec.loader.exec_module(matrix_widget)


class %CLASS%(matrix_widget.MatrixWidget):
    def __init__(self, parent_node_instance):
        super(%CLASS%, self).__init__(parent_node_instance, 100, 80)

        self.setReadOnly(False)

        self.textChanged.connect(M(self.text_changed))


    def text_changed(self):
        self.parent_node_instance.parse_matrix(self.toPlainText())
        self.resize_to_content(lines=self.toPlainText().splitlines())

    def focusOutEvent(self, e):
        self.update_matrix(self.parent_node_instance.expression_matrix)
        QTextEdit.focusOutEvent(self, e)
