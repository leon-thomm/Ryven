# from PySide2.QtWidgets import ...
from PySide2.QtCore import Qt
# from PySide2.QtGui import ...

from PySide2.QtWidgets import QSlider


class %INPUT_WIDGET_TITLE%_PortInstanceWidget(QSlider):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(%INPUT_WIDGET_TITLE%_PortInstanceWidget, self).__init__(Qt.Horizontal)

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        self.log = self.parent_node_instance.new_log('Clock Slider Log')

        self.setStyleSheet('''
            background: transparent;
        ''')
        self.setFixedWidth(70)
        self.setMinimum(0)
        self.setMaximum(100000)
        self.setSingleStep(1)
        self.valueChanged.connect(self.slider_val_changed)


    def slider_val_changed(self):
        self.parent_node_instance.update_timer_interval((self.value()/self.maximum()))
        self.log.log('setting value to:', (self.value()/self.maximum()))

    def get_val(self):
        return (self.value()/self.maximum())

    def get_data(self):
        data = {'val': self.value()}
        return data

    def set_data(self, data):
        self.setValue(data['val'])
