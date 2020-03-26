from PySide2.QtWidgets import QCheckBox
# from PySide2.QtCore import ...
# from PySide2.QtGui import ...


class %INPUT_WIDGET_TITLE%_PortInstanceWidget(QCheckBox):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(%INPUT_WIDGET_TITLE%_PortInstanceWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        # ------------------------------------------------

        # self.setStyleSheet('''
        #
        # ''')


    def get_val(self):
        # QCheckBox.isChecked() is a method of the QCheckBox class, see Qt documentation
        return self.isChecked()


    def get_data(self):
        data = {'checked': self.isChecked()}
        return data

    def set_data(self, data):
        # QCheckBox.setChecked() is a method of the QCheckBox class, see Qt documentation
        self.setChecked(data['checked'])


    # remove logs and stop threads and timers here
    def removing(self):
        pass
