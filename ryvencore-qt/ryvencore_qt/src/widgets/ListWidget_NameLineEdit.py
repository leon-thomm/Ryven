from qtpy.QtWidgets import QLineEdit


class ListWidget_NameLineEdit(QLineEdit):

    def __init__(self, text, parent):
        super().__init__(text, parent)
