from ryvencore_qt.src.ryvencore import dtypes

from NENV import *
widgets = import_widgets(__file__)


# Result_Node_MainWidget, \
# ValNode_MainWidget, \
#  = load_from_file(file='widgets.py', caller_file=__file__, components_list=[
#     'Result_Node_MainWidget', 'ValNode_MainWidget',
# ], gui=True)


class GetVar_Node(Node):

    title = 'get var'
    description = 'get the value of a script variable'
    init_inputs = [
        NodeInputBP(add_config={'widget name': 'std line edit', 'widget pos': 'besides'}),
    ]
    init_outputs = [
        NodeOutputBP(label='val')
    ]
    color = '#c69a15'

    def __init__(self, params):
        super(GetVar_Node, self).__init__(params)

        self.var_name = ''
        self.temp_var_val = None

    def place_event(self):
        # self.set_output_val(0, self.get_var_val(self.var_name))
        self.update()

    def update_event(self, input_called=-1):
        if self.input(0) != self.var_name:
            if self.var_name != '':  # disconnect old var val update connection
                self.unregister_var_receiver(self.var_name)

            self.var_name = self.input(0)

            # create new var update connection
            self.register_var_receiver(self.var_name, self.var_val_changed)

        self.set_output_val(0, self.get_var_val(self.var_name))

    def var_val_changed(self, name, val):
        self.set_output_val(0, val)

    # def get_data(self) -> dict:
    #     return {'var name': self.var_name}
    #
    # def set_data(self, data: dict):
    #     self.var_name = data['var name']


class Result_Node(Node):

    title = 'result'
    description = 'displays a value converted to string'
    init_inputs = [
        NodeInputBP(type_='data')
    ]
    main_widget_class = widgets.Result_Node_MainWidget
    main_widget_pos = 'between ports'
    color = '#c69a15'

    def __init__(self, params):
        super(Result_Node, self).__init__(params)
        self.val = None

    def place_event(self):
        self.update()

    def view_place_event(self):
        self.main_widget().show_val(self.val)

    def update_event(self, input_called=-1):
        self.val = self.input(0)
        if self.session.gui:
            self.main_widget().show_val(self.val)


class Val_Node(Node):

    title = 'val'
    description = 'returns the evaluated value that is typed into the input field'
    init_outputs = [
        NodeInputBP(type_='data')
    ]
    main_widget_class = widgets.ValNode_MainWidget
    main_widget_pos = 'between ports'
    style = 'extended'
    color = '#c69a15'

    def __init__(self, params):
        super(Val_Node, self).__init__(params)

        self.special_actions['edit val via dialog'] = {'method': self.action_edit_via_dialog}
        self.val = None


    def place_event(self):
        self.update()

    def view_place_event(self):
        self.main_widget().value_changed.connect(self.main_widget_val_changed)

    def main_widget_val_changed(self, val):
        self.val = val
        self.update()

    def update_event(self, input_called=-1):
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

    def get_data(self):
        return {
            'val': self.val  # self.main_widget().get_val()
        }

    def set_data(self, data):
        self.val = data['val']


class SetVar_Node(Node):

    title = 'set var'
    description = 'sets the value of a script variable'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.String(), label='var'),
        NodeInputBP(dtype=dtypes.Data(size='s'), label='val'),
        # NodeInputBP(type_='data', label='var', add_config={'widget name': 'std line edit', 'widget pos': 'besides'}),
        # NodeInputBP(type_='data', label='val', add_config={'widget name': 'std line edit', 'widget pos': 'besides'}),
    ]
    init_outputs = [
        NodeOutputBP(type_='exec'),
        NodeOutputBP(type_='data', label='val')
    ]
    style = 'extended'
    color = '#c69a15'

    def __init__(self, params):
        super(SetVar_Node, self).__init__(params)

        self.special_actions['make passive'] = {'method': self.action_make_passive}
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
        self.special_actions['make active'] = {'method': self.action_make_active}

    def action_make_active(self):
        self.active = True
        self.create_input('exec', '', pos=0)
        self.create_output('exec', '', pos=0)
        del self.special_actions['make active']
        self.special_actions['make passive'] = {'method': self.action_make_passive}

    def get_data(self):
        return {'active': self.active}

    def set_data(self, data):
        self.active = data['active']




export_nodes(
    SetVar_Node,
    GetVar_Node,
    Val_Node,
    Result_Node,
)
