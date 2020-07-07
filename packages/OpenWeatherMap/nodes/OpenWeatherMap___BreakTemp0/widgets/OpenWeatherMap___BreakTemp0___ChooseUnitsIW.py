from custom_src.retain import m

from PySide2.QtWidgets import QWidget, QRadioButton, QVBoxLayout
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...


class ChooseUnitsIW_PortInstanceWidget(QWidget):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(ChooseUnitsIW_PortInstanceWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.setStyleSheet('''
        QWidget {
            background: transparent;
        }
        ''')

        self.units = 'kelvin'
        
        layout = QVBoxLayout()
        self.units_kelvin = QRadioButton('Kelvin')
        self.units_kelvin.setChecked(True)
        layout.addWidget(self.units_kelvin)
        self.units_celsius = QRadioButton('Celsius')
        layout.addWidget(self.units_celsius)
        self.units_kelvin.toggled.connect(m(self.units_kelvin_toggled))
        self.setLayout(layout)


    def units_kelvin_toggled(self):
        if self.units == 'kelvin':
            self.units = 'celsius'
        elif self.units == 'celsius':
            self.units = 'kelvin'

    def get_val(self):
        return self.units


    def get_data(self):
        data = {'units': self.units}
        return data

    def set_data(self, data):
        if data['units'] == 'kelvin':
            self.units_kelvin.setChecked(True)
            self.units_celsius.setChecked(False)
        elif data['units'] == 'celsius':
            self.units_kelvin.setChecked(False)
            self.units_celsius.setChecked(True)
        self.units = data['units']


    # remove logs and stop threads and timers here
    def removing(self):
        pass # ...
