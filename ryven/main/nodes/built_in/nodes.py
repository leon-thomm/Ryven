from ryven.NENV import *
widgets = import_widgets(__file__)


class NodeBase(Node):
    pass


class GetVar_Node(NodeBase):
    """Gets the value of a script variable"""

    version = 'v0.1'

    title = 'get var'
    init_inputs = [
        NodeInputBP(dtype=dtypes.String(size='m')),
    ]
    init_outputs = [
        NodeOutputBP(label='val')
    ]
    color = '#c69a15'

    def __init__(self, params):
        super().__init__(params)

        self.var_name = ''
        self.temp_var_val = None

    def place_event(self):
        self.update()

    def view_place_event(self):
        self.var_name = self.input(0)

    def update_event(self, input_called=-1):
        if self.input(0) != self.var_name:

            if self.var_name != '':  # disconnect old var val update connection
                self.unregister_var_receiver(self.var_name, self.var_val_changed)

            self.var_name = self.input(0)

            # create new var update connection
            self.register_var_receiver(self.var_name, self.var_val_changed)

        self.set_output_val(0, self.get_var_val(self.var_name))

    def var_val_changed(self, name, val):
        self.set_output_val(0, val)


class Result_Node(NodeBase):
    """Simply shows a value converted to str"""

    version = 'v0.1'

    title = 'result'
    init_inputs = [
        NodeInputBP(type_='data'),
    ]
    main_widget_class = widgets.Result_Node_MainWidget
    main_widget_pos = 'between ports'
    color = '#c69a15'

    def __init__(self, params):
        super().__init__(params)
        self.val = None

    def place_event(self):
        self.update()

    def view_place_event(self):
        self.main_widget().show_val(self.val)

    def update_event(self, input_called=-1):
        self.val = self.input(0)
        if self.session.gui:
            self.main_widget().show_val(self.val)


class Val_Node(NodeBase):
    """Evaluates a string from the input field"""

    version = 'v0.1'

    title = 'val'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Data(size='s')),
    ]
    init_outputs = [
        NodeInputBP(type_='data'),
    ]
    style = 'small'
    color = '#c69a15'

    def __init__(self, params):
        super().__init__(params)

        self.display_title = ''
        self.actions['edit val via dialog'] = {'method': self.action_edit_via_dialog}
        self.val = None


    def place_event(self):
        self.update()

    def update_event(self, input_called=-1):
        self.val = self.input(0)
        self.set_output_val(0, self.val)

    def action_edit_via_dialog(self):
        return

        # from ..EditVal_Dialog import EditVal_Dialog
        #
        # val_dialog = EditVal_Dialog(parent=None, init_val=self.val)
        # accepted = val_dialog.exec_()
        # if accepted:
        #     self.main_widget().setText(str(val_dialog.get_val()))
        #     self.update()

    def get_current_var_name(self):
        return self.input(0)

    def get_state(self):
        return {
            'val': self.val  # self.main_widget().get_val()
        }

    def set_state(self, data, version):
        self.val = data['val']

        if version is None:

            self.display_title = ''

            self.create_input_dt(dtype=dtypes.Data(size='s'))

            # the old version didn't use a dtype
            self.inputs[0].dtype.val = self.val
            self.inputs[0].update(self.val)



class SetVar_Node(NodeBase):
    """Sets the value of a script variable"""

    version = 'v0.1'

    title = 'set var'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.String(), label='var'),
        NodeInputBP(dtype=dtypes.Data(size='s'), label='val'),
    ]
    init_outputs = [
        NodeOutputBP(type_='exec'),
        NodeOutputBP(type_='data', label='val'),
    ]
    style = 'normal'
    color = '#c69a15'

    def __init__(self, params):
        super().__init__(params)

        self.actions['make passive'] = {'method': self.action_make_passive}
        self.active = True

        self.var_name = ''
        self.num_vars = 1

    def update_event(self, input_called=-1):

        if self.active and input_called == 0:

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
        del self.actions['make passive']
        self.actions['make active'] = {'method': self.action_make_active}

    def action_make_active(self):
        self.active = True
        self.create_input(type_='exec', pos=0)
        self.create_output(type_='exec', pos=0)
        del self.actions['make active']
        self.actions['make passive'] = {'method': self.action_make_passive}

    def get_state(self):
        return {'active': self.active}

    def set_state(self, data, version):
        self.active = data['active']


class SetVarsPassive_Node(NodeBase):
    """Sets the values of multiple script variables"""

    version = 'v0.1'

    title = 'set vars passive'
    init_inputs = []
    init_outputs = []
    style = 'normal'
    color = '#c69a15'

    def __init__(self, params):
        super().__init__(params)

        self.actions['add var input'] = {'method': self.add_var_input}

        self.num_vars = 0

    def place_event(self):
        if self.num_vars == 0:
            self.add_var_input()

    def add_var_input(self):
        self.create_input_dt(label='var', dtype=dtypes.String(size='l'))
        self.create_input_dt(label='val', dtype=dtypes.Data(size='l'))
        self.num_vars += 1

        self.actions[f'remove var {self.num_vars}'] = {
            'method': self.remove_var_input,
            'data': self.num_vars
        }

    def remove_var_input(self, number):
        self.delete_input((number-1)*2)
        self.delete_input((number-1)*2)
        self.num_vars -= 1
        self.rebuild_remove_actions()

    def rebuild_remove_actions(self):

        remove_keys = []
        for k, v in self.actions.items():
            if k.startswith('remove var'):
                remove_keys.append(k)

        for k in remove_keys:
            del self.actions[k]

        for i in range(self.num_vars):
            self.actions[f'remove var {i+1}'] = {
                'method': self.remove_var_input,
                'data': i+1
            }

    def update_event(self, input_called=-1):

        var_names = [self.input(i) for i in range(0, len(self.inputs), 2)]
        values = [self.input(i) for i in range(1, len(self.inputs), 2)]

        for i in range(len(var_names)):
            self.set_var_val(var_names[i], values[i])

    def get_state(self):
        return {'num vars': self.num_vars}

    def set_state(self, data, version):
        self.num_vars = data['num vars']


export_nodes(
    SetVar_Node,
    GetVar_Node,
    Val_Node,
    Result_Node,
    SetVarsPassive_Node,
)
