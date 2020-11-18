from custom_src.Node import Node, NodePort


class GetVar_Node(Node):
    def __init__(self):
        super(GetVar_Node, self).__init__()

        self.title = 'get var'
        self.type_ = 'get variable node'
        self.package = 'built in'
        self.description = 'gets the value of a variable'

        data_input_port = NodePort()
        data_input_port.type_ = 'data'
        data_input_port.widget_name = 'std line edit'
        data_input_port.widget_pos = 'besides'
        self.inputs.append(data_input_port)

        data_output_port = NodePort()
        data_output_port.type_ = 'data'
        data_output_port.label = 'val'
        self.outputs.append(data_output_port)