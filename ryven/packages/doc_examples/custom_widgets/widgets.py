from NWENV import *

from qtpy.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


class MyMainWidget(MWB, QWidget):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QLabel('click it!'))
        b = QPushButton('click me')
        b.clicked.connect(self.button_clicked)
        self.layout().addWidget(b)

    def button_clicked(self):
        print('I have been clicked!!')
        self.update_node()


class MyInputWidget(IWB, QLineEdit):
    def __init__(self, params):
        IWB.__init__(self, params)
        QLineEdit.__init__(self)

        self.setPlaceholderText('type something...')
        self.editingFinished.connect(self.update_node)

    # override this from IWB
    def get_val(self):
        return self.text()

    # triggered when the input is connected and it received some data
    def val_update_event(self, val):
        self.setText(str(val))


export_widgets(
    MyMainWidget,
    MyInputWidget,
)
