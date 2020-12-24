import pickle
import base64
import random


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
        if (self.parent_node_instance.is_active() and self.type_ == 'exec') or not self.parent_node_instance.is_active():
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


class GetVar_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(GetVar_NodeInstance, self).__init__(params)
        self.var_name = ''
        self.temp_var_val = None

    def update_event(self, input_called=-1):
        if self.input(0) != self.var_name:
            if self.var_name != '':
                self.unregister_var_receiver(self.var_name)
            self.var_name = self.input(0)
            self.register_var_receiver(self.var_name, M(self.var_val_changed))
            val = self.get_var_val(self.input(0))
            if val is not None:
                self.set_output_val(0, val)
            else:
                self.set_output_val(0, None)
        else:
            self.set_output_val(0, self.get_var_val(self.var_name))

    def var_val_changed(self, name, val):
        self.update()

    def get_current_var_name(self):
        return self.input(0)

    def get_data(self):
        return {}

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class Checkpoint_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Checkpoint_NodeInstance, self).__init__(params)
        self.special_actions['make exec'] = {
            'method': M(self.action_make_exec)}
        self.passive = True
        self.num_exec_outputs = 0

    def action_make_exec(self):
        self.passive = False
        self.delete_input(0)
        self.delete_output(0)
        self.create_new_input('exec', '')
        del self.special_actions['make exec']
        self.special_actions['make data'] = {
            'method': M(self.action_make_data)}
        self.special_actions['add sequence output'] = {
            'method': M(self.action_add_sequence_output)}
        self.action_add_sequence_output()

    def action_add_sequence_output(self):
        self.create_new_output('exec', '')
        self.num_exec_outputs += 1
        self.special_actions['remove output ' + str(self.num_exec_outputs)] = {'method': M(
            self.action_remove_sequence_output), 'data': self.num_exec_outputs - 1}

    def action_remove_sequence_output(self, index):
        self.delete_output(index)
        for i in range(self.num_exec_outputs):
            del self.special_actions['remove output ' + str(i + 1)]
        self.num_exec_outputs -= 1
        for i in range(self.num_exec_outputs):
            self.special_actions['remove output ' + str(i + 1)] = {'method': M(
                self.action_remove_sequence_output), 'data': i}

    def action_make_data(self):
        self.passive = True
        self.delete_input(0)
        for i in range(self.num_exec_outputs):
            self.delete_output(0)
            del self.special_actions['remove output ' + str(i + 1)]
        self.num_exec_outputs = 0
        self.create_new_input('data', '')
        self.create_new_output('data', '')
        del self.special_actions['make data']
        del self.special_actions['add sequence output']
        self.special_actions['make exec'] = {
            'method': M(self.action_make_exec)}

    def update_event(self, input_called=-1):
        if self.passive:
            self.set_output_val(0, self.input(0))
        elif input_called == 0:
            for i in range(self.num_exec_outputs):
                self.exec_output(i)

    def get_data(self):
        data = {'passive': self.passive,
                'num exec outputs': self.num_exec_outputs}
        return data

    def set_data(self, data):
        self.passive = data['passive']
        self.num_exec_outputs = data['num exec outputs']

    def removing(self):
        pass


class Minus_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Minus_NodeInstance, self).__init__(params)
        self.special_actions['add input'] = {
            'method': M(self.action_add_input)}
        self.num_inputs = 2

    def update_event(self, input_called=-1):
        sum_val = self.input(0)
        for i in range(1, len(self.inputs)):
            sum_val -= self.input(i)
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


class Print_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Print_NodeInstance, self).__init__(params)
        self.special_actions['print something 1'] = {
            'method': M(self.print_something), 'data': 'hello!!'}
        self.special_actions['print something 2'] = {
            'method': M(self.print_something), 'data': 'HELLOO!?!?!?'}

    def update_event(self, input_called=-1):
        if input_called == 0:
            print(self.input(1))
            self.exec_output(0)

    def print_something(self, data):
        print(data)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class SetVar_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(SetVar_NodeInstance, self).__init__(params)
        self.special_actions['make passive'] = {
            'method': M(self.action_make_passive)}
        self.active = True
        self.var_name = ''

    def update_event(self, input_called=-1):
        if self.active and input_called == 0:
            self.var_name = self.input(1)
            if self.set_var_val(self.input(1), self.input(2)):
                self.set_output_val(1, self.input(2))
            self.exec_output(0)
        elif not self.active:
            self.var_name = self.input(0)
            if self.set_var_val(self.input(0), self.input(1)):
                self.set_output_val(0, self.get_var_val(self.var_name))

    def action_make_passive(self):
        self.active = False
        self.delete_input(0)
        self.delete_output(0)
        del self.special_actions['make passive']
        self.special_actions['make active'] = {
            'method': M(self.action_make_active)}

    def action_make_active(self):
        self.active = True
        self.create_new_input('exec', '', pos=0)
        self.create_new_output('exec', '', pos=0)
        del self.special_actions['make active']
        self.special_actions['make passive'] = {
            'method': M(self.action_make_passive)}

    def get_data(self):
        return {'active': self.active}

    def set_data(self, data):
        self.active = data['active']

    def remove_event(self):
        pass


class ArrGet_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(ArrGet_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        arr = self.input(0)
        index = self.input(1)
        self.outputs[0].set_val(arr[index])

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class While_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(While_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        if input_called == 0:
            while self.input(1):
                self.exec_output(0)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class SwapArrElements_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(SwapArrElements_NodeInstance, self).__init__(params)

    def update_event(self, input_called=-1):
        if input_called == 0:
            arr = self.input(1)
            temp = arr[self.input(2)]
            arr[self.input(2)] = arr[self.input(3)]
            arr[self.input(3)] = temp
            self.set_output_val(1, arr)
            self.exec_output(0)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def removing(self):
        pass


class Plus_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Plus_NodeInstance, self).__init__(params)
        self.special_actions['add input'] = {
            'method': M(self.action_add_input)}
        self.num_inputs = 2

    def update_event(self, input_called=-1):
        try:
            sum_val = sum([self.input(i) for i in range(len(self.inputs))])
            self.outputs[0].set_val(sum_val)
        except Exception as e:
            sum_val = ''
            for i in range(len(self.inputs)):
                val = self.input(i)
                if val is None:
                    self.set_output_val(0, None)
                    return
                sum_val += str(self.input(i))
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


class ForNDim_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(ForNDim_NodeInstance, self).__init__(params)
        self.special_actions['add dimension'] = {
            'method': M(self.action_add_dimension)}
        self.dimensions = 1

    def update_event(self, input_called=-1):
        if input_called == 0:
            self.iterate(1)

    def iterate(self, current_dim):
        from_input_index = 1 + 2 * (current_dim - 1)
        to_input_index = from_input_index + 1
        exec_output_index = 2 * (current_dim - 1)
        counter_output_index = exec_output_index + 1
        for i in range(self.input(from_input_index), self.input(to_input_index)):
            self.outputs[counter_output_index].set_val(i)
            self.exec_output(exec_output_index)
            if current_dim < self.dimensions:
                self.iterate(current_dim + 1)

    def action_add_dimension(self):
        new_dim = self.dimensions + 1
        self.create_new_input('data', 'i' + str(new_dim) + ' from',
                              widget_name='std spin box', widget_pos='besides')
        self.create_new_input('data', 'i' + str(new_dim) + ' to',
                              widget_name='std spin box', widget_pos='besides')
        self.create_new_output('exec', 'i' + str(new_dim) + ' loop')
        self.create_new_output('data', 'i' + str(new_dim))
        self.dimensions += 1
        self.special_actions['remove dimension'] = {
            'method': M(self.action_remove_dimension)}

    def action_remove_dimension(self):
        self.delete_input(-1)
        self.delete_input(-1)
        self.delete_output(-1)
        self.delete_output(-1)
        self.dimensions -= 1
        if self.dimensions == 1:
            del self.special_actions['remove dimension']

    def get_data(self):
        data = {'num dimensions': self.dimensions}
        return data

    def set_data(self, data):
        self.dimensions = data['num dimensions']

    def remove_event(self):
        pass


class Button_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Button_NodeInstance, self).__init__(params)

    def button_clicked(self):
        self.update()

    def update_event(self, input_called=-1):
        self.exec_output(0)

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class If_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(If_NodeInstance, self).__init__(params)
        self.special_actions['add else if'] = {
            'method': M(self.action_add_else_if)}
        self.else_if_enlargement_state = 0

    def action_add_else_if(self):
        self.create_new_input('data', 'condition ' + str(self.else_if_enlargement_state + 1),
                              widget_name='std line edit m', widget_pos='under')
        self.create_new_output(
            'exec', 'elif ' + str(self.else_if_enlargement_state + 1), pos=len(self.outputs) - 1)
        self.else_if_enlargement_state += 1
        self.special_actions['remove else if'] = {
            'method': M(self.action_remove_else_if)}

    def action_remove_else_if(self):
        self.delete_input(self.inputs[-1])
        self.delete_output(self.outputs[-2])
        self.else_if_enlargement_state -= 1
        if self.else_if_enlargement_state == 0:
            del self.special_actions['remove else if']

    def update_event(self, input_called=-1):
        if input_called == 0:
            self.do_if(0, self.else_if_enlargement_state)

    def do_if(self, if_cnt, current_enlarment_state):
        if self.input(1 + if_cnt):
            self.exec_output(if_cnt)
        elif if_cnt < current_enlarment_state:
            self.do_if(if_cnt + 1, current_enlarment_state)
        else:
            self.exec_output(len(self.outputs) - 1)

    def get_data(self):
        data = {'else if enlargment state': self.else_if_enlargement_state}
        return data

    def set_data(self, data):
        self.else_if_enlargement_state = data['else if enlargment state']

    def remove_event(self):
        pass


class RandInts_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(RandInts_NodeInstance, self).__init__(params)
        self.special_actions['make executable'] = {
            'method': M(self.action_make_executable)}
        self.active = False

    def action_make_executable(self):
        del self.special_actions['make executable']
        self.special_actions['make passve'] = {
            'method': M(self.action_make_passive)}
        self.create_new_input('exec', '', pos=0)
        self.create_new_output('exec', '', pos=0)
        self.active = True

    def action_make_passive(self):
        del self.special_actions['make passve']
        self.special_actions['make executable'] = {
            'method': M(self.action_make_executable)}
        self.delete_input(0)
        self.delete_output(0)
        self.active = False

    def update_event(self, input_called=-1):
        if self.active and input_called == 0:
            self.set_output_val(1, [random.randint(self.input(
                2), self.input(3)) for i in range(self.input(1))])
            self.exec_output(0)
        else:
            self.set_output_val(0, [random.randint(self.input(
                1), self.input(2)) for i in range(self.input(0))])

    def get_data(self):
        data = {'active': self.active}
        return data

    def set_data(self, data):
        self.active = data['active']

    def removing(self):
        pass


class Greater_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Greater_NodeInstance, self).__init__(params)
        self.special_actions['add input'] = {
            'method': M(self.action_add_input)}
        self.enlargement_state = 0

    def action_add_input(self):
        self.create_new_input(
            'data', '', widget_name='std line edit s r nb', widget_pos='besides')
        self.enlargement_state += 1
        self.special_actions['remove input'] = {
            'method': M(self.action_remove_input)}

    def action_remove_input(self):
        self.delete_input(self.inputs[-1])
        self.enlargement_state -= 1
        if self.enlargement_state == 0:
            del self.special_actions['remove input']

    def update_event(self, input_called=-1):
        result = True
        for i in range(1 + self.enlargement_state):
            result = result and self.input(i) > self.input(i + 1)
        self.outputs[0].set_val(result)

    def get_data(self):
        data = {'enlargement state': self.enlargement_state}
        return data

    def set_data(self, data):
        self.enlargement_state = data['enlargement state']

    def remove_event(self):
        pass


class Log_NodeInstance(NodeInstance):

    def __init__(self, params):
        super(Log_NodeInstance, self).__init__(params)
        self.special_actions['add target option'] = {
            'method': M(self.action_add_target_option)}
        self.log = self.new_log('Log Node Log')
        self.default_target = 'personal'
        self.showing_target_option = False
        self.target = self.default_target

    def action_add_target_option(self):
        del self.special_actions['add target option']
        self.add_target_option()

    def add_target_option(self):
        self.special_actions['remove target option'] = {
            'method': M(self.action_remove_target_option)}
        self.create_new_input(
            'data', 'target', widget_name='LogTargetComboBox', widget_pos='besides')
        self.showing_target_option = True

    def action_remove_target_option(self):
        del self.special_actions['remove target option']
        self.remove_target_option()

    def remove_target_option(self):
        self.special_actions['add target option'] = {
            'method': M(self.action_add_target_option)}
        self.delete_input(-1)
        self.target = self.default_target
        self.showing_target_option = False

    def update_event(self, input_called=-1):
        if input_called == 0:
            if self.target == 'personal':
                self.log.write(self.input(1))
            else:
                self.log_message(self.input(1), target=self.target)
            self.exec_output(0)

    def get_data(self):
        data = {'target': self.target,
                'showing target': self.showing_target_option}
        return data

    def set_data(self, data):
        self.target = data['target']
        self.showing_target_option = data['showing target']

    def remove_event(self):
        pass


def create_nodes():
    nodes = [
        Node(title='get var', inputs=[NodePort(type_='data', label='')], outputs=[NodePort(type_='data', label='val')]), Node(title=' ', inputs=[NodePort(type_='data', label='')], outputs=[NodePort(type_='data', label='')]), Node(title='-', inputs=[NodePort(type_='data', label=''), NodePort(type_='data', label='')], outputs=[NodePort(type_='data', label='')]), Node(title='Print', inputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='')], outputs=[NodePort(type_='exec', label='')]), Node(title='set var', inputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='var'), NodePort(type_='data', label='val')], outputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='val')]), Node(title='arr get', inputs=[NodePort(type_='data', label='arr'), NodePort(type_='data', label='index')], outputs=[NodePort(type_='data', label='')]), Node(title='While', inputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='condition')], outputs=[NodePort(type_='exec', label='loop')]), Node(title='Swap Arr Elements', inputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='arr'), NodePort(type_='data', label='index 1'), NodePort(
            type_='data', label='index 2')], outputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='arr')]), Node(title='+', inputs=[NodePort(type_='data', label=''), NodePort(type_='data', label='')], outputs=[NodePort(type_='data', label='')]), Node(title='For n Dim', inputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='i1 from'), NodePort(type_='data', label='i1 to')], outputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='i1')]), Node(title='button', inputs=[], outputs=[NodePort(type_='exec', label='')]), Node(title='If', inputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='condition')], outputs=[NodePort(type_='exec', label='true'), NodePort(type_='exec', label='false')]), Node(title='rand ints', inputs=[NodePort(type_='data', label='cnt'), NodePort(type_='data', label='a'), NodePort(type_='data', label='b')], outputs=[NodePort(type_='data', label='')]), Node(title='>', inputs=[NodePort(type_='data', label=''), NodePort(type_='data', label='')], outputs=[NodePort(type_='data', label='')]), Node(title='Log', inputs=[NodePort(type_='exec', label=''), NodePort(type_='data', label='')], outputs=[NodePort(type_='exec', label='')])
    ]
    return nodes


def create_node_instances():
    node_instances = [
        GetVar_NodeInstance((nodes[0], None, {'parent node title': 'get var', 'parent node type': '', 'parent node description': 'get the value of a script variable', 'position x': 2627.0, 'position y': 1112.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit', 'widget data': 'values', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': 'val'}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 2609.0, 'position y': 1278.0, 'state data': {'passive': True, 'num exec outputs': 0}, 'special actions': {'make exec': {'method': 'action_make_exec'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': False}], 'outputs': [{'type': 'data', 'label': ''}]})), Minus_NodeInstance((nodes[2], None, {'parent node title': '-', 'parent node type': '', 'parent node description': '', 'position x': 2133.0, 'position y': 1135.0, 'state data': {'num inputs': 2}, 'special actions': {'add input': {'method': 'action_add_input'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '1', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})), GetVar_NodeInstance((nodes[0], None, {'parent node title': 'get var', 'parent node type': '', 'parent node description': 'get the value of a script variable', 'position x': 1435.0, 'position y': 1398.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit', 'widget data': 'values', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': 'val'}]})), Print_NodeInstance((nodes[3], None, {'parent node title': 'Print', 'parent node type': '', 'parent node description': '', 'position x': 1615.0, 'position y': 865.0, 'state data': {}, 'special actions': {'print something 1': {'method': 'print_something', 'data': 'hello!!'}, 'print something 2': {'method': 'print_something', 'data': 'HELLOO!?!?!?'}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit m r', 'widget data': '', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}]})), SetVar_NodeInstance((nodes[4], None, {'parent node title': 'set var', 'parent node type': '', 'parent node description': 'sets the value of a script variable', 'position x': 3397.0, 'position y': 989.0, 'state data': {'active': True}, 'special actions': {}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'var', 'has widget': True, 'widget name': 'std line edit m', 'widget data': 'found_pair', 'widget position': 'besides'}, {'type': 'data', 'label': 'val', 'has widget': True, 'widget name': 'std line edit m', 'widget data': 'True', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'data', 'label': 'val'}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 2769.0, 'position y': 1388.0, 'state data': {'passive': True, 'num exec outputs': 0}, 'special actions': {'make exec': {'method': 'action_make_exec'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': False}], 'outputs': [{'type': 'data', 'label': ''}]})), ArrGet_NodeInstance((nodes[5], None, {'parent node title': 'arr get', 'parent node type': '', 'parent node description': '', 'position x': 2975.0, 'position y': 1199.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': 'arr', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': 'index', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})), GetVar_NodeInstance((nodes[0], None, {'parent node title': 'get var', 'parent node type': '', 'parent node description': 'get the value of a script variable', 'position x': 1098.0, 'position y': 1130.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit', 'widget data': 'found_pair', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': 'val'}]})), While_NodeInstance((nodes[6], None, {'parent node title': 'While', 'parent node type': 'control structure', 'parent node description': '', 'position x': 1481.0, 'position y': 1027.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'condition', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'below'}], 'outputs': [{'type': 'exec', 'label': 'loop'}]})), SwapArrElements_NodeInstance((nodes[7], None, {'parent node title': 'Swap Arr Elements', 'parent node type': '', 'parent node description': 'Swaps two elements in an array by the indices.', 'position x': 3749.0, 'position y': 1247.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'arr', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': 'index 1', 'has widget': True, 'widget name': 'std spin box', 'widget data': 0, 'widget position': 'besides'}, {'type': 'data', 'label': 'index 2', 'has widget': True, 'widget name': 'std spin box', 'widget data': 0, 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'data', 'label': 'arr'}]})), Plus_NodeInstance((nodes[8], None, {'parent node title': '+', 'parent node type': '', 'parent node description': '', 'position x': 3475.0, 'position y': 1398.0, 'state data': {'num inputs': 2}, 'special actions': {'add input': {'method': 'action_add_input'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '1', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})), SetVar_NodeInstance((nodes[4], None, {'parent node title': 'set var', 'parent node type': '', 'parent node description': 'sets the value of a script variable', 'position x': 1732.0, 'position y': 1060.0, 'state data': {'active': True}, 'special actions': {}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'var', 'has widget': True, 'widget name': 'std line edit m', 'widget data': 'found_pair', 'widget position': 'besides'}, {'type': 'data', 'label': 'val', 'has widget': True, 'widget name': 'std line edit m', 'widget data': 'False', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'data', 'label': 'val'}]})), Plus_NodeInstance((nodes[8], None, {'parent node title': '+', 'parent node type': '', 'parent node description': '', 'position x': 2793.0, 'position y': 1288.0, 'state data': {'num inputs': 2}, 'special actions': {'add input': {'method': 'action_add_input'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '1', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})), GetVar_NodeInstance((nodes[0], None, {'parent node title': 'get var', 'parent node type': '', 'parent node description': 'get the value of a script variable', 'position x': 1939.0, 'position y': 1132.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit', 'widget data': 'number_elements', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': 'val'}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 728.0, 'position y': 796.0, 'state data': {'passive': False, 'num exec outputs': 3}, 'special actions': {'make data': {'method': 'action_make_data'}, 'add sequence output': {'method': 'action_add_sequence_output'}, 'remove output 1': {'method': 'action_remove_sequence_output', 'data': 0}, 'remove output 2': {'method': 'action_remove_sequence_output', 'data': 1}, 'remove output 3': {'method': 'action_remove_sequence_output', 'data': 2}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'exec', 'label': ''}, {'type': 'exec', 'label': ''}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 996.0, 'position y': 499.0, 'state data': {'passive': False, 'num exec outputs': 1}, 'special actions': {'remove output 1': {'method': 'action_remove_sequence_output', 'data': 0}, 'make data': {'method': 'action_make_data'}, 'add sequence output': {'method': 'action_add_sequence_output'}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}], 'outputs': [{'type': 'exec', 'label': ''}]})), ForNDim_NodeInstance((nodes[9], None, {'parent node title': 'For n Dim', 'parent node type': 'control structure', 'parent node description': '', 'position x': 2320.0, 'position y': 1074.0, 'state data': {'num dimensions': 1}, 'special actions': {'add dimension': {'method': 'action_add_dimension'}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'i1 from', 'has widget': True, 'widget name': 'std spin box', 'widget data': 0, 'widget position': 'besides'}, {'type': 'data', 'label': 'i1 to', 'has widget': True, 'widget name': 'std spin box', 'widget data': 0, 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'data', 'label': 'i1'}]})), Button_NodeInstance((nodes[10], None, {'parent node title': 'button', 'parent node type': '',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           'parent node description': '', 'position x': 540.0, 'position y': 796.0, 'main widget data': {}, 'state data': {}, 'special actions': {}, 'inputs': [], 'outputs': [{'type': 'exec', 'label': ''}]})), SetVar_NodeInstance((nodes[4], None, {'parent node title': 'set var', 'parent node type': '', 'parent node description': 'sets the value of a script variable', 'position x': 1095.0, 'position y': 1003.0, 'state data': {'active': True}, 'special actions': {}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'var', 'has widget': True, 'widget name': 'std line edit m', 'widget data': 'found_pair', 'widget position': 'besides'}, {'type': 'data', 'label': 'val', 'has widget': True, 'widget name': 'std line edit m', 'widget data': 'True', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'data', 'label': 'val'}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 3150.0, 'position y': 1390.0, 'state data': {'passive': True, 'num exec outputs': 0}, 'special actions': {'make exec': {'method': 'action_make_exec'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': False}], 'outputs': [{'type': 'data', 'label': ''}]})), GetVar_NodeInstance((nodes[0], None, {'parent node title': 'get var', 'parent node type': '', 'parent node description': 'get the value of a script variable', 'position x': 1380.0, 'position y': 886.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit', 'widget data': 'values', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': 'val'}]})), Print_NodeInstance((nodes[3], None, {'parent node title': 'Print', 'parent node type': '', 'parent node description': '', 'position x': 1654.0, 'position y': 1345.0, 'state data': {}, 'special actions': {'print something 1': {'method': 'print_something', 'data': 'hello!!'}, 'print something 2': {'method': 'print_something', 'data': 'HELLOO!?!?!?'}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit m r', 'widget data': '', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}]})), GetVar_NodeInstance((nodes[0], None, {'parent node title': 'get var', 'parent node type': '', 'parent node description': 'get the value of a script variable', 'position x': 1161.0, 'position y': 565.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit', 'widget data': 'number_elements', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': 'val'}]})), If_NodeInstance((nodes[11], None, {'parent node title': 'If', 'parent node type': 'control structure', 'parent node description': '', 'position x': 3143.0, 'position y': 990.0, 'state data': {'else if enlargment state': 0}, 'special actions': {'add else if': {'method': 'action_add_else_if'}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'condition', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'below'}], 'outputs': [{'type': 'exec', 'label': 'true'}, {'type': 'exec', 'label': 'false'}]})), SetVar_NodeInstance((nodes[4], None, {'parent node title': 'set var', 'parent node type': '', 'parent node description': 'sets the value of a script variable', 'position x': 1650.0, 'position y': 511.0, 'state data': {'active': True}, 'special actions': {}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': 'var', 'has widget': True, 'widget name': 'std line edit m', 'widget data': 'values', 'widget position': 'besides'}, {'type': 'data', 'label': 'val', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '[]', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'data', 'label': 'val'}]})), RandInts_NodeInstance((nodes[12], None, {'parent node title': 'rand ints', 'parent node type': '', 'parent node description': 'Generates a number of random integers N in a range a <= N <= b.', 'position x': 1375.0, 'position y': 592.0, 'state data': {'active': False}, 'special actions': {'make executable': {'method': 'action_make_executable'}}, 'inputs': [{'type': 'data', 'label': 'cnt', 'has widget': True, 'widget name': 'std line edit m r nb', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': 'a', 'has widget': True, 'widget name': 'std line edit m r nb', 'widget data': '0', 'widget position': 'besides'}, {'type': 'data', 'label': 'b', 'has widget': True, 'widget name': 'std line edit m r nb', 'widget data': '1000', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 1277.0, 'position y': 1067.0, 'state data': {'passive': False, 'num exec outputs': 2}, 'special actions': {'make data': {'method': 'action_make_data'}, 'add sequence output': {'method': 'action_add_sequence_output'}, 'remove output 1': {'method': 'action_remove_sequence_output', 'data': 0}, 'remove output 2': {'method': 'action_remove_sequence_output', 'data': 1}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'exec', 'label': ''}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 2785.0, 'position y': 1130.0, 'state data': {'passive': True, 'num exec outputs': 0}, 'special actions': {'make exec': {'method': 'action_make_exec'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': False}], 'outputs': [{'type': 'data', 'label': ''}]})), Greater_NodeInstance((nodes[13], None, {'parent node title': '>', 'parent node type': '', 'parent node description': '', 'position x': 3184.0, 'position y': 1240.0, 'state data': {'enlargement state': 0}, 'special actions': {'add input': {'method': 'action_add_input'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit s r nb', 'widget data': '', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})), ArrGet_NodeInstance((nodes[5], None, {'parent node title': 'arr get', 'parent node type': '', 'parent node description': '', 'position x': 2974.0, 'position y': 1287.0, 'state data': {}, 'special actions': {}, 'inputs': [{'type': 'data', 'label': 'arr', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'besides'}, {'type': 'data', 'label': 'index', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'besides'}], 'outputs': [{'type': 'data', 'label': ''}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 3352.0, 'position y': 1130.0, 'state data': {'passive': True, 'num exec outputs': 0}, 'special actions': {'make exec': {'method': 'action_make_exec'}}, 'inputs': [{'type': 'data', 'label': '', 'has widget': False}], 'outputs': [{'type': 'data', 'label': ''}]})), Log_NodeInstance((nodes[14], None, {'parent node title': 'Log', 'parent node type': '', 'parent node description': "Very useful. Logs data either to one of the script's std logs or to a custom log. By right clicking you can add the option to choose a specific log. Default is the custom ('personal') log.", 'position x': 1571.0, 'position y': 738.0, 'state data': {'target': 'personal', 'showing target': False}, 'special actions': {'add target option': {'method': 'action_add_target_option'}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 1421.0, 'position y': 800.0, 'state data': {'passive': False, 'num exec outputs': 2}, 'special actions': {'make data': {'method': 'action_make_data'}, 'add sequence output': {'method': 'action_add_sequence_output'}, 'remove output 1': {'method': 'action_remove_sequence_output', 'data': 0}, 'remove output 2': {'method': 'action_remove_sequence_output', 'data': 1}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'exec', 'label': ''}]})), Checkpoint_NodeInstance((nodes[1], None, {'parent node title': ' ', 'parent node type': '', 'parent node description': 'serves as a checkpoint for connections', 'position x': 1505.0, 'position y': 1286.0, 'state data': {'passive': False, 'num exec outputs': 2}, 'special actions': {'make data': {'method': 'action_make_data'}, 'add sequence output': {'method': 'action_add_sequence_output'}, 'remove output 1': {'method': 'action_remove_sequence_output', 'data': 0}, 'remove output 2': {'method': 'action_remove_sequence_output', 'data': 1}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}], 'outputs': [{'type': 'exec', 'label': ''}, {'type': 'exec', 'label': ''}]})), Log_NodeInstance((nodes[14], None, {'parent node title': 'Log', 'parent node type': '', 'parent node description': "Very useful. Logs data either to one of the script's std logs or to a custom log. By right clicking you can add the option to choose a specific log. Default is the custom ('personal') log.", 'position x': 1655.0, 'position y': 1224.0, 'state data': {'target': 'personal', 'showing target': False}, 'special actions': {'add target option': {'method': 'action_add_target_option'}}, 'inputs': [{'type': 'exec', 'label': '', 'has widget': False}, {'type': 'data', 'label': '', 'has widget': True, 'widget name': 'std line edit m', 'widget data': '', 'widget position': 'besides'}], 'outputs': [{'type': 'exec', 'label': ''}]}))

    ]
    for ni in node_instances:
        ni.initialized()
    return node_instances


def connect_node_instances():
    def c(i1, o, i2, i):
        ni1 = node_instances[i1]
        ni2 = node_instances[i2]
        out = ni1.outputs[o]
        inp = ni2.inputs[i]
        out.connected_port_instances.append(inp)
        inp.connected_port_instances.append(out)

    c(0, 0, 28, 0)
    c(1, 0, 7, 1)
    c(1, 0, 13, 0)
    c(1, 0, 6, 0)
    c(2, 0, 17, 2)
    c(3, 0, 22, 1)
    c(3, 0, 35, 1)
    c(5, 0, 10, 0)
    c(6, 0, 20, 0)
    c(7, 0, 29, 0)
    c(8, 0, 9, 1)
    c(9, 0, 12, 0)
    c(11, 0, 10, 3)
    c(12, 0, 17, 0)
    c(13, 0, 30, 1)
    c(14, 0, 2, 0)
    c(15, 0, 16, 0)
    c(15, 1, 33, 0)
    c(15, 2, 19, 0)
    c(16, 0, 25, 0)
    c(17, 0, 24, 0)
    c(17, 1, 1, 0)
    c(18, 0, 15, 0)
    c(19, 0, 27, 0)
    c(20, 0, 11, 0)
    c(20, 0, 10, 2)
    c(21, 0, 4, 1)
    c(21, 0, 32, 1)
    c(23, 0, 26, 0)
    c(24, 0, 5, 0)
    c(26, 0, 25, 2)
    c(27, 0, 9, 0)
    c(27, 1, 34, 0)
    c(28, 0, 7, 0)
    c(28, 0, 30, 0)
    c(28, 0, 31, 0)
    c(29, 0, 24, 1)
    c(30, 0, 29, 1)
    c(31, 0, 10, 1)
    c(33, 0, 32, 0)
    c(33, 1, 4, 0)
    c(34, 0, 35, 0)
    c(34, 1, 22, 0)


def init_vars():
    manager = VarsManager(config={'values': {'serialized': 'gASVGQEAAAAAAABdlChLCksMSyJLJUsxSzVLOks+S1RLW0t6S4dLkEuTS6BLoUuhS65Lu0vgS+tL7kv3S/5NAQFNBAFNEAFNEwFNFQFNGwFNIQFNIgFNJgFNQgFNYQFNbQFNeAFNhwFNiwFNjAFNjAFNkgFNlwFNlwFNmQFNqQFNwwFNygFN1QFN2gFN2wFN4wFN6AFN7QFN9AFNAQJNHwJNIAJNLwJNNAJNTQJNUQJNVwJNZQJNZgJNhAJNrwJNrwJNswJNtgJNvwJNvwJNwwJNzgJN2gJN6gJN8QJN8QJN9AJN+wJNAANNAwNNDQNNFwNNGwNNHgNNJANNOgNNQANNWQNNWwNNYwNNbANNdANNjwNNjwNNzwNN0QNN1ANN4wNlLg=='}, 'number_elements': {'serialized': 'gARLZC4='}, 'found_pair': {'serialized': 'gASJLg=='}})
    return manager


if __name__ == '__main__':
    vars_manager = init_vars()
    nodes = create_nodes()
    node_instances = create_node_instances()
    connect_node_instances()
    for ni in node_instances:
        ni.update()

    # ...


    button_ni = node_instances[18]
    print(vars_manager.get_var_val('values'))
    button_ni.update()
