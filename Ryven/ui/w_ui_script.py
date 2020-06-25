from PySide2.QtWidgets import QWidget

from ui.ui_script import Ui_script_widget


class WUIScript(QWidget):

    def __init__(self):
        super(WUIScript, self).__init__()
        self.ui = Ui_script_widget()
        self.ui.setupUi(self)