from PySide2.QtGui import QColor


class Node:
    def __init__(self):
        # general attributes
        #   static:
        self.title = ''
        self.type = ''  # kind of extends the title with further information, f.ex.: 'function input node'
        self.description = ''
        self.package = None  # 'built in' means built in, everything else that the node came from outside (important)
        self.has_main_widget = False
        self.main_widget_class = None
        self.main_widget_pos = ''
        self.design_style = 'extended'  # default value just for testing
        self.color = QColor(198, 154, 21)  # QColor(59, 156, 217)

        #   dynamic: (get copied and then individually edited in NIs)
        self.code = ''  # only exists in pryScript for source code generation in static nodes (standard)!
        self.inputs = []
        self.outputs = []
        # !!! inputs and outputs may be edited for input-and output nodes in VyFunction !!!



# class GetVariable_Node(Node):
#     def __init__(self, parent_variable):
#         super(GetVariable_Node, self).__init__()
#
#         self.parent_variable = parent_variable
#
#         self.title = parent_variable.vy_name
#         self.type = 'get variable node'
#         self.package = 'built in'
#         self.description = 'returns variable'
#         # TODO code of GetVariableNode
#
#         output_port = NodePort()
#         output_port.type = 'data'
#         self.outputs.append(output_port)
#
#
class SetVariable_Node(Node):
    def __init__(self):
        super(SetVariable_Node, self).__init__()

        self.title = 'set var'
        self.type = 'set variable node'
        self.package = 'built in'
        self.description = 'sets the value of a variable'

        exec_input_port = NodePort()
        exec_input_port.type = 'exec'
        self.inputs.append(exec_input_port)

        var_name_data_input_port = NodePort()
        var_name_data_input_port.type = 'data'
        var_name_data_input_port.label = 'var'
        var_name_data_input_port.widget_pos = 'besides'
        self.inputs.append(var_name_data_input_port)

        val_name_data_input_port = NodePort()
        val_name_data_input_port.type = 'data'
        val_name_data_input_port.label = 'val'
        val_name_data_input_port.widget_pos = 'besides'
        self.inputs.append(val_name_data_input_port)

        exec_output_port = NodePort()
        exec_output_port.type = 'exec'
        self.outputs.append(exec_output_port)

        val_output_port = NodePort()
        val_output_port.type = 'data'
        val_output_port.label = 'val'
        self.outputs.append(val_output_port)

class GetVariable_Node(Node):
    def __init__(self):
        super(GetVariable_Node, self).__init__()

        self.title = 'get var'
        self.type = 'get variable node'
        self.package = 'built in'
        self.description = 'gets the value of a variable'

        data_input_port = NodePort()
        data_input_port.type = 'data'
        data_input_port.widget_type = 'std line edit'
        data_input_port.widget_pos = 'besides'
        self.inputs.append(data_input_port)

        data_output_port = NodePort()
        data_output_port.type = 'data'
        data_output_port.label = 'val'
        self.outputs.append(data_output_port)




class NodePort:
    # type = ''
    # label = ''

    def __init__(self):
        # general attributes
        self.type = ''  # TODO: change type to _type (shadowing!)
        self.label = ''
        self.widget_type = 'std line edit'  # only important for data inputs
        self.widget_name = ''  # only important for data inputs with custom programmed widgets
        self.widget_pos = 'under'  # " same