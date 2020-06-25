from PySide2.QtGui import QColor


class Node:
    def __init__(self):
        # GENERAL ATTRIBUTES
        #   static:
        self.title = ''
        self.type_ = ''  # just for clarity - grouping nodes (f.ex. 'http')
        self.description = ''
        self.package = None  # everything else than 'built in' means that the node came from outside (important)
        self.has_main_widget = False
        self.main_widget_class = None
        self.main_widget_pos = ''
        self.design_style = 'extended'  # default value just for testing
        self.color = QColor(198, 154, 21)  # default value just for testing

        #   dynamic: (get copied and can be individually edited in NIs)
        self.inputs = []
        self.outputs = []


class SetVariable_Node(Node):
    def __init__(self):
        super(SetVariable_Node, self).__init__()

        self.title = 'set var'
        self.type_ = 'set variable node'
        self.package = 'built in'
        self.description = 'sets the value of a variable'

        exec_input_port = NodePort()
        exec_input_port.type_ = 'exec'
        self.inputs.append(exec_input_port)

        var_name_data_input_port = NodePort()
        var_name_data_input_port.type_ = 'data'
        var_name_data_input_port.label = 'var'
        var_name_data_input_port.widget_pos = 'besides'
        self.inputs.append(var_name_data_input_port)

        val_name_data_input_port = NodePort()
        val_name_data_input_port.type_ = 'data'
        val_name_data_input_port.label = 'val'
        val_name_data_input_port.widget_pos = 'besides'
        self.inputs.append(val_name_data_input_port)

        exec_output_port = NodePort()
        exec_output_port.type_ = 'exec'
        self.outputs.append(exec_output_port)

        val_output_port = NodePort()
        val_output_port.type_ = 'data'
        val_output_port.label = 'val'
        self.outputs.append(val_output_port)

class GetVariable_Node(Node):
    def __init__(self):
        super(GetVariable_Node, self).__init__()

        self.title = 'get var'
        self.type_ = 'get variable node'
        self.package = 'built in'
        self.description = 'gets the value of a variable'

        data_input_port = NodePort()
        data_input_port.type_ = 'data'
        data_input_port.widget_type = 'std line edit'
        data_input_port.widget_pos = 'besides'
        self.inputs.append(data_input_port)

        data_output_port = NodePort()
        data_output_port.type_ = 'data'
        data_output_port.label = 'val'
        self.outputs.append(data_output_port)




class NodePort:
    def __init__(self):
        # general attributes
        self.type_ = ''
        self.label = ''
        self.widget_type = 'std line edit'  # only important for data inputs
        self.widget_name = ''  # only important for data inputs with custom programmed widgets
        self.widget_pos = 'under'  # same as above