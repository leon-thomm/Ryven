from PySide2.QtWidgets import QLineEdit
import os

from custom_src.Node import Node, NodePort


class ValNode_Instance_MainWidget(QLineEdit):
    def __init__(self, parent_node_instance):
        super(ValNode_Instance_MainWidget, self).__init__()

        # leave these lines ------------------------------
        self.parent_node_instance = parent_node_instance
        self.package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
        # ------------------------------------------------

        self.setStyleSheet('''
            QLineEdit{
                border-radius: 10px;
                background-color: transparent;
                border: 1px solid #404040;
                color: #aaaaaa;
                padding: 3px;
            }
        ''')

        self.setFixedWidth(80)
        self.editingFinished.connect(self.editing_finished)

    def editing_finished(self):
        self.parent_node_instance.update()

    def get_val(self):
        val = None
        try:
            val = eval(self.text())
        except Exception as e:
            val = self.text()
        return val

    def get_data(self):
        data = {'text': self.text()}
        return data

    def set_data(self, data):
        self.setText(data['text'])

    def remove_event(self):
        pass


class Val_Node(Node):
    def __init__(self):
        super(Val_Node, self).__init__()

        self.title = 'val'
        self.type = 'val'
        self.package = 'built in'
        self.description = 'returns the evaluated value that is typed into the widget'
        self.has_main_widget = True
        self.main_widget_class = ValNode_Instance_MainWidget
        self.main_widget_pos = 'between ports'
        self.design_style = 'extended'

        data_output_port = NodePort()
        data_output_port.type_ = 'data'
        data_output_port.label = ''
        self.outputs.append(data_output_port)