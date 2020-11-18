from custom_src.Node import Node, NodePort


class SetVar_Node(Node):
    def __init__(self):
        super(SetVar_Node, self).__init__()

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
        var_name_data_input_port.widget_name = 'std line edit m'
        var_name_data_input_port.widget_pos = 'besides'
        self.inputs.append(var_name_data_input_port)

        val_name_data_input_port = NodePort()
        val_name_data_input_port.type_ = 'data'
        val_name_data_input_port.label = 'val'
        val_name_data_input_port.widget_name = 'std line edit m'
        val_name_data_input_port.widget_pos = 'besides'
        self.inputs.append(val_name_data_input_port)

        exec_output_port = NodePort()
        exec_output_port.type_ = 'exec'
        self.outputs.append(exec_output_port)

        val_output_port = NodePort()
        val_output_port.type_ = 'data'
        val_output_port.label = 'val'
        self.outputs.append(val_output_port)