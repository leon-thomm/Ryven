import pickle
import base64
import numpy as np
from numpy import conjugate, matmul
from numpy.linalg import matrix_power

"""All required static components for building the flow in the target source"""


class Flow_AlgorithmMode:
    mode_data_flow = '''+str(self.flow_algorithm_mode.mode_data_flow)+'''


class Node:
    """Base node class with very basic properties"""

    def __init__(self, title, inputs, outputs):
        self.title = title
        self.inputs = inputs
        self.outputs = outputs


class NodePort:
    """Inputs and outputs for nodes"""

    def __init__(self, type_, label):
        self.type_ = type_
        self.label = label


class M:
    """Replaces the retain mechanism from Ryven, which isn't needed in the
    target source, as no source code will be edited live."""

    def __init__(self, method):
        self.method = method  # retain(method)

    def __call__(self, *args, **kwargs):
        self.method(*args, **kwargs)


class PlaceholderClass:
    """Placeholder class, used for widgets here, to automatically block all
    communication to a NodeInstance's main_widget"""

    def __getattr__(self, item):
        def method(*args):
            pass

        return method

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            return
        super(PlaceholderClass, self).__setattr__(key, value)


class VarsManager:
    def __init__(self, config=None):

        self.variables = []
        self.list_widget = PlaceholderClass()
        self.var_receivers = {}

        if config is not None:
            for name in config.keys():
                self.create_new_var(name, val=config[name])
            self.list_widget.recreate_ui()

    def create_new_var_and_update(self, name):
        """Also updates the GUI"""

        self.create_new_var(name)
        self.list_widget.recreate_ui()

    def create_new_var(self, name, val=None):

        if len(name) == 0:
            return

        # search for name issues
        for v in self.variables:
            if v.name == name:
                return

        self.variables.append(Variable(name, val))

    def get_var(self, name):
        for v in self.variables:
            if v.name == name:
                return v
        return None

    def get_var_val(self, name):
        var = self.get_var(name)
        return var.val if var is not None else None

    def set_var(self, name, val):
        var_index = self.get_var_index_from_name(name)
        if var_index is None:
            return False

        self.variables[var_index].val = val

        # update all variable usages by calling all registered object's methods on updated variable with the new val
        for receiver, var_name in self.var_receivers.keys():
            if var_name == name:
                self.var_receivers[receiver, var_name](
                    var_name, val)  # calling the slot method

        return True

    def get_var_index_from_name(self, name):
        var_names_list = [v.name for v in self.variables]
        for i in range(len(var_names_list)):
            if var_names_list[i] == name:
                return i

        return None

    def register_receiver(self, receiver, var_name, method):
        """A registered receiver (method) gets triggered every time the
        value of a variable changes"""

        self.var_receivers[(receiver, var_name)] = method

    def unregister_receiver(self, receiver, var_name):
        try:
            del self.var_receivers[(receiver, var_name)]
        except Exception:
            return


class Variable:
    def __init__(self, name='', val=None):
        super(Variable, self).__init__()

        self.name = name
        self.val = None
        if type(val) != dict:  # backwards compatibility
            try:
                self.val = pickle.loads(base64.b64decode(val))
            except Exception:
                self.val = val

        elif 'serialized' in val.keys():
            self.val = pickle.loads(base64.b64decode(val['serialized']))

    def serialize(self):
        pickled = pickle.dumps(self.val)
        serialized = base64.b64encode(pickled).decode('ascii')
        return serialized


class PortInstance:
    def __init__(self, parent_node_instance, type_, label):
        self.parent_node_instance = parent_node_instance
        self.type_ = type_
        self.label = label
        self.connected_port_instances = []

    def get_val(self):
        pass


class OutputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_, label):
        super(OutputPortInstance, self).__init__(
            parent_node_instance, type_, label)

        self.val = None

    def exec(self):
        for cpi in self.connected_port_instances:
            cpi.update()

    def set_val(self, val):
        self.val = val

        if Flow_AlgorithmMode.mode_data_flow and not self.parent_node_instance.initializing:
            for cpi in self.connected_port_instances:
                cpi.update()

    def get_val(self):
        if not Flow_AlgorithmMode.mode_data_flow:
            self.parent_node_instance.update()
        return self.val


class InputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_: str, label: str, widget_data: str):
        super(InputPortInstance, self).__init__(
            parent_node_instance, type_, label)

        self.val = None
        try:
            self.val = eval(widget_data)
        except Exception as e:
            self.val = widget_data

    def get_val(self):
        if len(self.connected_port_instances) == 0:
            return self.val
        else:
            return self.connected_port_instances[0].get_val()

    def update(self):
        if (
                self.parent_node_instance.is_active() and self.type_ == 'exec') or not self.parent_node_instance.is_active():
            self.parent_node_instance.update(
                self.parent_node_instance.inputs.index(self))


class NodeInstance:
    """NodeInstance base class with functionality required for executing the flow"""

    def __init__(self, params):
        super(NodeInstance, self).__init__()

        self.parent_node, self.flow, config = params
        self.inputs = []
        self.outputs = []
        self.initializing = True
        self.init_config = config
        self.special_actions = {}
        self.main_widget = PlaceholderClass()

    def initialized(self):
        self.setup_ports(
            self.init_config['inputs'], self.init_config['outputs'])
        self.set_data(self.init_config['state data'])
        self.initializing = False
        self.update()

    def setup_ports(self, inputs_config, outputs_config):
        for inp in inputs_config:
            pi = InputPortInstance(
                self, inp['type'], inp['label'], inp['widget data'] if inp['has widget'] else None)
            self.inputs.append(pi)

        for out in outputs_config:
            pi = OutputPortInstance(self, out['type'], out['label'])
            self.outputs.append(pi)

    def update(self, input_called=-1, output_called=-1):
        try:
            self.update_event(input_called)
        except Exception as e:
            print('EXCEPTION in', self.parent_node.title, e)

    def update_event(self, input_called=-1):
        pass

    def input(self, index):
        return self.inputs[index].get_val()

    def exec_output(self, index):
        self.outputs[index].exec()

    def set_output_val(self, index, val):
        self.outputs[index].set_val(val)

    def remove_event(self):
        pass

    def new_log(self, title):
        return PlaceholderClass()

    def log_message(self, message: str, target='global'):
        pass

    def update_shape(self):
        pass

    def get_data(self):
        pass

    def set_data(self, data):
        pass

    def get_vars_manager(self):
        return vars_manager

    def get_var_val(self, name):
        return self.get_vars_manager().get_var_val(name)

    def set_var_val(self, name, val):
        return self.get_vars_manager().set_var(name, val)

    def register_var_receiver(self, name, method):
        self.get_vars_manager().register_receiver(self, name, method)

    def unregister_var_receiver(self, name):
        self.get_vars_manager().unregister_receiver(self, name)

    def is_active(self) -> bool:
        for i in self.inputs:
            if i.type_ == 'exec':
                return True
        for o in self.outputs:
            if o.type_ == 'exec':
                return True
        return False


class Conjugate_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Conjugate_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        conjugated = conjugate(self.input(0))
        self.set_output_val(0, conjugated)
        self.main_widget.update_matrix(conjugated)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass


class MatrixPower_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(MatrixPower_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        matrix = matrix_power(self.input(0), self.input(1))
        self.set_output_val(0, matrix)
        self.main_widget.update_matrix(matrix)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass


class Times_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Times_NodeInstance, self).__init__(params)
        self.special_actions['add input'] = {
            'method': M(self.action_add_input)}
        self.num_inputs = 2

    def update_event(self, input_called=-1):
        sum_val = self.input(0)
        for i in range(1, len(self.inputs)):
            sum_val *= self.input(i)
        self.outputs[0].set_val(sum_val)

    def action_add_input(self):
        self.create_new_input(
            'data', '', widget_name='std line edit s r nb', widget_pos='besides')
        self.num_inputs += 1
        self.special_actions['remove input'] = {
            'method': M(self.action_remove_input)}

    def action_remove_input(self):
        self.delete_input(self.inputs[-1])
        self.num_inputs -= 1
        if self.num_inputs == 2:
            del self.special_actions['remove input']

    def get_data(self):
        data = {'num inputs': self.num_inputs}
        return data

    def set_data(self, data):
        self.num_inputs = data['num inputs']

    def remove_event(self):
        pass


class MatrixMult_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(MatrixMult_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        matrix = matmul(self.input(0), self.input(1))
        self.set_output_val(0, matrix)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass


class ShowMatrix_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(ShowMatrix_NodeInstance, self).__init__(params)
        self.special_actions['hide preview'] = {
            'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False
        self.accessed_columns = []
        self.accessed_rows = []

    def update_event(self, input_called=-1):
        matrix = self.input(0)
        self.main_widget.update_matrix(matrix)
        self.set_output_val(0, matrix)
        i = 1
        for r in sorted(self.accessed_rows):
            self.set_output_val(i, matrix[r])
            i += 1
        for c in sorted(self.accessed_columns):
            self.set_output_val(i, np.transpose(matrix[:, c][np.newaxis]))
            i += 1
        if len(matrix) > 0:
            rows_access = {}
            context_rows = set(
                [j for j in range(matrix.shape[0])]) - set(self.accessed_rows)
            for i in context_rows:
                rows_access['access row ' +
                            str(i)] = {'method': M(self.add_row_access), 'data': i}
            self.special_actions['add row access'] = rows_access
        elif self.special_actions.__contains__('add row access'):
            del self.special_actions['add row access']
        if len(matrix.shape) > 1:
            columns_access = {}
            context_columns = set(
                [j for j in range(matrix.shape[1])]) - set(self.accessed_columns)
            for i in context_columns:
                columns_access['access column ' +
                               str(i)] = {'method': M(self.add_column_access), 'data': i}
            self.special_actions['add col access'] = columns_access
        elif self.special_actions.__contains__('add col access'):
            del self.special_actions['add col access']

    def add_row_access(self, data):
        row_index = data
        self.accessed_rows.append(row_index)
        self.create_new_output('data', 'row ' + str(row_index),
                               pos=sorted(self.accessed_rows).index(row_index) + 1)
        remove_actions = self.special_actions['remove output'] if self.special_actions.__contains__(
            'remove output') else {}
        remove_actions['row ' + str(row_index)] = {'method': M(
            self.remove_row_access), 'data': row_index}
        self.special_actions['remove output'] = remove_actions

    def add_column_access(self, data):
        col_index = data
        self.accessed_columns.append(col_index)
        self.create_new_output('data', 'col ' + str(col_index), pos=1 + len(
            self.accessed_rows) + sorted(self.accessed_columns).index(col_index))
        remove_actions = self.special_actions['remove output'] if self.special_actions.__contains__(
            'remove output') else {}
        remove_actions['col ' + str(col_index)] = {'method': M(
            self.remove_col_access), 'data': col_index}
        self.special_actions['remove output'] = remove_actions

    def remove_row_access(self, data):
        row_index = data
        self.delete_output(1 + sorted(self.accessed_rows).index(row_index))
        self.accessed_rows.remove(row_index)
        del self.special_actions['remove output']['row ' + str(row_index)]

    def remove_col_access(self, data):
        col_index = data
        self.delete_output(1 + len(self.accessed_rows) +
                           sorted(self.accessed_columns).index(col_index))
        self.accessed_columns.remove(col_index)
        del self.special_actions['remove output']['col ' + str(col_index)]

    def action_hide_mw(self):
        self.main_widget.hide()
        del self.special_actions['hide preview']
        self.special_actions['show preview'] = {
            'method': M(self.action_show_mw)}
        self.main_widget_hidden = True
        self.update_shape()

    def action_show_mw(self):
        self.main_widget.show()
        del self.special_actions['show preview']
        self.special_actions['hide preview'] = {
            'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False
        self.update_shape()

    def get_data(self):
        data = {'main widget hidden': self.main_widget_hidden,
                'accessed rows': self.accessed_rows, 'accessed columns': self.accessed_columns}
        return data

    def set_data(self, data):
        self.main_widget_hidden = data['main widget hidden']
        self.accessed_rows = data['accessed rows']
        self.accessed_columns = data['accessed columns']

    def removing(self):
        pass


class Matrix_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Matrix_NodeInstance, self).__init__(params)
        self.special_actions['hide preview'] = {
            'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False
        self.expression_matrix = None
        self.evaluated_matrix = None
        self.used_variable_names = []

    def update_event(self, input_called=-1):
        self.set_output_val(0, self.evaluated_matrix)

    def parse_matrix(self, s):
        lines = s.splitlines()
        try:
            self.expression_matrix = np.array(
                [[exp for exp in list(filter(lambda s: s != '', l.split(' ')))] for l in lines])
            self.eval_expression_matrix()
            self.update()
        except ValueError:
            return

    def eval_expression_matrix(self):
        if not self.register_vars(self.expression_matrix):
            return
        self.evaluated_matrix = self.eval_matrix(self.expression_matrix)
        if self.evaluated_matrix is None:
            return
        try:
            self.evaluated_matrix = np.array(self.evaluated_matrix)
        except Exception:
            return

    def eval_matrix(self, lines):
        v = self.get_var_val
        evaled_exp_array = []
        for l in lines:
            evaled_exp_array.append([])
            for exp in l:
                evaled_exp_array[-1].append(eval(exp))
        float_exp_array = [[float(exp) if type(
            exp) == int else exp for exp in l] for l in evaled_exp_array]
        return np.array(float_exp_array)

    def register_vars(self, lines):
        try:
            for name in self.used_variable_names:
                self.unregister_var_receiver(name)
            self.used_variable_names.clear()
            v = self.register_variable
            for l in lines:
                for exp in l:
                    eval(exp)
            return True
        except Exception:
            return False

    def register_variable(self, name):
        self.register_var_receiver(name, M(self.var_val_updated))
        self.used_variable_names.append(name)

    def var_val_updated(self, name, val):
        self.evaluated_matrix = self.eval_matrix(self.expression_matrix)
        self.update()

    def action_hide_mw(self):
        self.main_widget.hide()
        del self.special_actions['hide preview']
        self.special_actions['show preview'] = {
            'method': M(self.action_show_mw)}
        self.main_widget_hidden = True
        self.update_shape()

    def action_show_mw(self):
        self.main_widget.show()
        del self.special_actions['show preview']
        self.special_actions['hide preview'] = {
            'method': M(self.action_hide_mw)}
        self.main_widget_hidden = False
        self.update_shape()

    def get_data(self):
        expression_matrix_list = self.expression_matrix
        if expression_matrix_list is not None:
            expression_matrix_list = expression_matrix_list.tolist()
        data = {'main widget hidden': self.main_widget_hidden,
                'expression matrix': expression_matrix_list}
        return data

    def set_data(self, data):
        self.main_widget_hidden = data['main widget hidden']
        if self.main_widget_hidden:
            self.action_hide_mw()
        self.expression_matrix = np.array(data['expression matrix'])
        self.eval_expression_matrix()

    def removing(self):
        pass


class Divided_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Divided_NodeInstance, self).__init__(params)
        self.special_actions['add input'] = {
            'method': M(self.action_add_input)}
        self.num_inputs = 2

    def update_event(self, input_called=-1):
        sum_val = self.input(0)
        for i in range(1, len(self.inputs)):
            sum_val /= self.input(i)
        self.outputs[0].set_val(sum_val)

    def action_add_input(self):
        self.create_new_input(
            'data', '', widget_name='std line edit s r nb', widget_pos='besides')
        self.num_inputs += 1
        self.special_actions['remove input'] = {
            'method': M(self.action_remove_input)}

    def action_remove_input(self):
        self.delete_input(self.inputs[-1])
        self.num_inputs -= 1
        if self.num_inputs == 2:
            del self.special_actions['remove input']

    def get_data(self):
        data = {'num inputs': self.num_inputs}
        return data

    def set_data(self, data):
        self.num_inputs = data['num inputs']

    def remove_event(self):
        pass


class ExtractProperty_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(ExtractProperty_NodeInstance, self).__init__(params)
        self.special_actions['add param input'] = {
            'method': M(self.action_add_param_input)}
        self.param_counter = 0
        self.text = ''

    def action_add_param_input(self):
        self.param_counter += 1
        self.create_new_input('data', 'param', widget_name=None, pos=-1)
        self.special_actions['remove param ' + str(self.param_counter)] = {'method': M(
            self.action_remove_param_input), 'data': self.param_counter}

    def action_remove_param_input(self, data):
        self.delete_input(data)
        del self.special_actions['remove param ' + str(self.param_counter)]
        for i in range(1, self.param_counter):
            self.special_actions['remove param ' +
                                 str(i)] = {'method': M(self.action_remove_param_input), 'data': i}
        self.param_counter -= 1

    def update_event(self, input_called=-1):
        obj = self.input(0)
        params = [self.input(i) for i in range(1, self.param_counter + 1)]
        res = eval(self.text)
        self.set_output_val(0, res)

    def get_data(self):
        data = {'param counter': self.param_counter, 'text': self.text}
        return data

    def set_data(self, data):
        self.param_counter = data['param counter']
        self.text = data['text']

    def removing(self):
        pass


def create_nodes():
    nodes = [
        Node(title='conjugate', inputs=[NodePort(type_='data', label='')], outputs=[NodePort(type_='data', label='')]),
        Node(title='matrix power', inputs=[NodePort(type_='data', label=''), NodePort(type_='data', label='n')],
             outputs=[NodePort(type_='data', label='')]),
        Node(title='*', inputs=[NodePort(type_='data', label=''), NodePort(type_='data', label='')],
             outputs=[NodePort(type_='data', label='')]),
        Node(title='×', inputs=[NodePort(type_='data', label=''), NodePort(type_='data', label='')], outputs=[
            NodePort(type_='data', label='')]), Node(title='show matrix', inputs=[NodePort(type_='data', label='')],
                                                     outputs=[NodePort(type_='data', label='')]),
        Node(title='matrix', inputs=[], outputs=[NodePort(type_='data', label='')]),
        Node(title='/', inputs=[NodePort(type_='data', label=''), NodePort(type_='data', label='')],
             outputs=[NodePort(type_='data', label='')]),
        Node(title='Extract Property', inputs=[NodePort(type_='data', label='obj')],
             outputs=[NodePort(type_='data', label='')])
    ]
    return nodes


def create_node_instances():
    node_instances = [
        Conjugate_NodeInstance((nodes[0], None, {'parent node title': 'conjugate', 'parent node type': '',
                                                 'parent node package': 'linalg',
                                                 'parent node description': 'Conjugates an array which means inverting all imaginary parts.',
                                                 'position x': 894.0, 'position y': 295.0, 'main widget data': {
                'text': ' 30.0  56.0  42.0\n106.0 281.0 156.0\n102.0 206.0 150.0', 'shown': True}, 'state data': {},
                                                 'special actions': {},
                                                 'inputs': [{'type': 'data', 'label': '', 'has widget': False}],
                                                 'outputs': [{'type': 'data', 'label': ''}]})),
        MatrixPower_NodeInstance((nodes[1], None, {'parent node title': 'matrix power', 'parent node type': '',
                                                   'parent node package': 'linalg',
                                                   'parent node description': 'Raises a square matrix to power n',
                                                   'position x': 483.0, 'position y': 505.0, 'main widget data': {
                'text': ' 3000.0  5600.0  4200.0\n10600.0 28100.0 15600.0\n10200.0 20600.0 15000.0', 'shown': True},
                                                   'state data': {}, 'special actions': {},
                                                   'inputs': [{'type': 'data', 'label': '', 'has widget': False},
                                                              {'type': 'data', 'label': 'n', 'has widget': True,
                                                               'widget name': 'std line edit s r', 'widget data': '2',
                                                               'widget position': 'besides'}],
                                                   'outputs': [{'type': 'data', 'label': ''}]})),
        Times_NodeInstance((nodes[
                                2],
                            None,
                            {
                                'parent node title': '*',
                                'parent node type': '',
                                'parent node package': 'std',
                                'parent node description': '',
                                'position x': 325.0,
                                'position y': 302.0,
                                'state data': {
                                    'num inputs': 2},
                                'special actions': {
                                    'add input': {
                                        'method': 'action_add_input'}},
                                'inputs': [
                                    {
                                        'type': 'data',
                                        'label': '',
                                        'has widget': True,
                                        'widget name': 'std line edit s r nb',
                                        'widget data': '',
                                        'widget position': 'besides'},
                                    {
                                        'type': 'data',
                                        'label': '',
                                        'has widget': True,
                                        'widget name': 'std line edit s r nb',
                                        'widget data': '10',
                                        'widget position': 'besides'}],
                                'outputs': [
                                    {
                                        'type': 'data',
                                        'label': ''}]})),
        MatrixMult_NodeInstance((nodes[3], None,
                                 {'parent node title': '×', 'parent node type': '', 'parent node package': 'linalg',
                                  'parent node description': 'Performs a matrix multiplication, if defined on the provided matrices.',
                                  'position x': 484.0, 'position y': 300.0, 'state data': {}, 'special actions': {},
                                  'inputs': [{'type': 'data', 'label': '', 'has widget': False},
                                             {'type': 'data', 'label': '', 'has widget': False}],
                                  'outputs': [{'type': 'data', 'label': ''}]})),
        ShowMatrix_NodeInstance((nodes[4], None,
                                 {
                                     'parent node title': 'show matrix',
                                     'parent node type': '',
                                     'parent node package': 'linalg',
                                     'parent node description': 'Displays a matrix or any array.',
                                     'position x': 870.0,
                                     'position y': 504.0,
                                     'main widget data': {
                                         'text': ' 3000.0  5600.0  4200.0\n10600.0 28100.0 15600.0\n10200.0 20600.0 15000.0',
                                         'shown': True},
                                     'state data': {
                                         'main widget hidden': False,
                                         'accessed rows': [],
                                         'accessed columns': [
                                         ]},
                                     'special actions': {
                                         'hide preview': {
                                             'method': 'action_hide_mw'},
                                         'add row access': {
                                             'access row 0': {
                                                 'method': 'add_row_access',
                                                 'data': 0},
                                             'access row 1': {
                                                 'method': 'add_row_access',
                                                 'data': 1},
                                             'access row 2': {
                                                 'method': 'add_row_access',
                                                 'data': 2}},
                                         'add col access': {
                                             'access column 0': {
                                                 'method': 'add_column_access',
                                                 'data': 0},
                                             'access column 1': {
                                                 'method': 'add_column_access',
                                                 'data': 1},
                                             'access column 2': {
                                                 'method': 'add_column_access',
                                                 'data': 2}}},
                                     'inputs': [
                                         {
                                             'type': 'data',
                                             'label': '',
                                             'has widget': False}],
                                     'outputs': [
                                         {
                                             'type': 'data',
                                             'label': ''}]})),
        Matrix_NodeInstance((nodes[5], None,
                             {'parent node title': 'matrix', 'parent node type': '', 'parent node package': 'linalg',
                              'parent node description': "Create a custom matrix. You can use <number>j to create complex numbers, which will convert the whole matrix to complex type, and you can use variables using v('<varname>').",
                              'position x': 374.0, 'position y': 91.0, 'main widget data': {
                                 'text': "     1      2      3\n     4 v('a')      6\n     7      8      9",
                                 'shown': True}, 'state data': {'main widget hidden': False,
                                                                'expression matrix': [['1', '2', '3'],
                                                                                      ['4', "v('a')", '6'],
                                                                                      ['7', '8', '9']]},
                              'special actions': {'hide preview': {'method': 'action_hide_mw'}}, 'inputs': [],
                              'outputs': [{'type': 'data', 'label': ''}]})),
        Divided_NodeInstance((nodes[6], None, {
            'parent node title': '/', 'parent node type': '', 'parent node package': 'std',
            'parent node description': '', 'position x': 649.0, 'position y': 302.0, 'state data': {'num inputs': 2},
            'special actions': {'add input': {'method': 'action_add_input'}}, 'inputs': [
                {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb',
                 'widget data': '', 'widget position': 'besides'},
                {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb',
                 'widget data': '100', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})),
        ExtractProperty_NodeInstance((nodes[7], None, {'parent node title': 'Extract Property', 'parent node type': '',
                                                       'parent node package': 'std',
                                                       'parent node description': 'Extracts any property of an object by parsing what you type into the input field.\nYou can also use this for much more than just accessing properties.\nFurthermore, you can add parameters for dynamic evaluations which you can access though the params list.',
                                                       'position x': 798.0, 'position y': 82.0,
                                                       'main widget data': {'text': 'obj.copy()'},
                                                       'state data': {'param counter': 0, 'text': 'obj.copy()'},
                                                       'special actions': {
                                                           'add param input': {'method': 'action_add_param_input'}},
                                                       'inputs': [
                                                           {'type': 'data', 'label': 'obj', 'has widget': False}],
                                                       'outputs': [{'type': 'data', 'label': ''}]}))

    ]
    for ni in node_instances:
        ni.initialized()
    return node_instances


def connect_node_instances():
    node_instances[0].outputs[0].connected_port_instances = []
    node_instances[0].inputs[0].connected_port_instances = [
        node_instances[6].outputs[0]]
    node_instances[1].outputs[0].connected_port_instances = []
    node_instances[1].inputs[0].connected_port_instances = [
        node_instances[2].outputs[0]]
    node_instances[1].inputs[1].connected_port_instances = []
    node_instances[2].outputs[0].connected_port_instances = [
        node_instances[1].inputs[0], node_instances[3].inputs[0], node_instances[3].inputs[1]]
    node_instances[2].inputs[0].connected_port_instances = [
        node_instances[7].outputs[0]]
    node_instances[2].inputs[1].connected_port_instances = []
    node_instances[3].outputs[0].connected_port_instances = [
        node_instances[4].inputs[0], node_instances[6].inputs[0]]
    node_instances[3].inputs[0].connected_port_instances = [
        node_instances[2].outputs[0]]
    node_instances[3].inputs[1].connected_port_instances = [
        node_instances[2].outputs[0]]
    node_instances[4].outputs[0].connected_port_instances = []
    node_instances[4].inputs[0].connected_port_instances = [
        node_instances[3].outputs[0]]
    node_instances[5].outputs[0].connected_port_instances = [
        node_instances[7].inputs[0]]
    node_instances[6].outputs[0].connected_port_instances = [
        node_instances[0].inputs[0]]
    node_instances[6].inputs[0].connected_port_instances = [
        node_instances[3].outputs[0]]
    node_instances[6].inputs[1].connected_port_instances = []
    node_instances[7].outputs[0].connected_port_instances = [
        node_instances[2].inputs[0]]
    node_instances[7].inputs[0].connected_port_instances = [
        node_instances[5].outputs[0]]


def init_vars():
    manager = VarsManager(config={'a': {'serialized': 'gARLDy4='}})
    return manager


if __name__ == '__main__':
    vars_manager = init_vars()
    nodes = create_nodes()
    node_instances = create_node_instances()
    connect_node_instances()
    for ni in node_instances:
        ni.update()

    # ...
