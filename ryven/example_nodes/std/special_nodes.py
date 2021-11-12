import code
from contextlib import redirect_stdout, redirect_stderr

from ryven.NENV import *
widgets = import_widgets(__file__)


class NodeBase(Node):
    color = '#FFCA00'


class DualNodeBase(NodeBase):
    """For nodes that can be active and passive"""

    def __init__(self, params, active=True):
        super().__init__(params)

        self.active = active
        if active:
            self.actions['make passive'] = {'method': self.make_passive}
        else:
            self.actions['make active'] = {'method': self.make_active}

    def make_passive(self):
        del self.actions['make passive']

        self.delete_input(0)
        self.delete_output(0)
        self.active = False

        self.actions['make active'] = {'method': self.make_active}

    def make_active(self):
        del self.actions['make active']

        self.create_input(type_='exec', insert=0)
        self.create_output(type_='exec', insert=0)
        self.active = True

        self.actions['make passive'] = {'method': self.make_passive}

    def get_state(self) -> dict:
        return {
            'active': self.active
        }

    def set_state(self, data: dict, version):
        self.active = data['active']


# -------------------------------------------


class Checkpoint_Node(NodeBase):
    """Provides a simple checkpoint to reroute your connections"""

    title = 'checkpoint'
    init_inputs = [
        NodeInputBP(type_='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    style = 'small'

    def __init__(self, params):
        super().__init__(params)

        self.display_title = ''

        self.active = False

        # initial actions
        self.actions['add output'] = {
            'method': self.add_output
        }
        self.actions['remove output'] = {
            '0': {'method': self.remove_output, 'data': 0}
        }
        self.actions['make active'] = {
            'method': self.make_active
        }

    """State transitions"""

    def clear_ports(self):
        # remove all outputs
        for i in range(len(self.outputs)):
            self.delete_output(0)

        # remove all inputs
        for i in range(len(self.inputs)):
            self.delete_input(0)

    def make_active(self):
        self.active = True

        # rebuild inputs and outputs
        self.clear_ports()
        self.create_input(type_='exec')
        self.create_output(type_='exec')

        # update actions
        del self.actions['make active']
        self.actions['make passive'] = {
            'method': self.make_passive
        }
        self.actions['remove output'] = {
            '0': {'method': self.remove_output, 'data': 0}
        }

    def make_passive(self):
        self.active = False

        # rebuild inputs and outputs
        self.clear_ports()
        self.create_input(type_='data')
        self.create_output(type_='data')

        # update actions
        del self.actions['make passive']
        self.actions['make active'] = {
            'method': self.make_active
        }
        self.actions['remove output'] = {
            '0': {'method': self.remove_output, 'data': 0}
        }

    """Actions"""

    def add_output(self):
        index = len(self.outputs)

        if self.active:
            self.create_output(type_='exec')
        else:
            self.create_output(type_='data')

        self.actions['remove output'][str(index)] = {
            'method': self.remove_output,
            'data': index,
        }

    def remove_output(self, index):
        self.delete_output(index)

        del self.actions['remove output'][str(len(self.outputs))]

    """Behavior"""

    def update_event(self, inp=-1):
        if self.active and inp == 0:
            for i in range(len(self.outputs)):
                self.exec_output(i)

        elif not self.active:
            data = self.input(0)
            for i in range(len(self.outputs)):
                self.set_output_val(i, data)

    """State Reload"""

    def get_state(self) -> dict:
        return {
            'active': self.active,
            'num outputs': len(self.outputs),
        }

    def set_state(self, data: dict, version):
        self.actions['remove output'] = {
            {'method': self.remove_output, 'data': i}
            for i in range(data['num outputs'])
        }

        if data['active']:
            self.make_active()


class Button_Node(NodeBase):
    title = 'Button'
    main_widget_class = widgets.ButtonNode_MainWidget
    main_widget_pos = 'between ports'
    init_inputs = [

    ]
    init_outputs = [
        NodeOutputBP(type_='exec')
    ]
    color = '#99dd55'

    def update_event(self, inp=-1):
        self.exec_output(0)


class Print_Node(DualNodeBase):
    title = 'Print'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Data(size='m')),
    ]
    init_outputs = [
        NodeOutputBP(type_='exec'),
    ]
    color = '#5d95de'

    def __init__(self, params):
        super().__init__(params, active=True)

    def update_event(self, inp=-1):
        if self.active and inp == 0:
            print(self.input(1))
        elif not self.active:
            print(self.input(0))


import logging


class Log_Node(DualNodeBase):
    title = 'Log'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP('msg', type_='data'),
    ]
    init_outputs = [
        NodeOutputBP(type_='exec'),
    ]
    main_widget_class = widgets.LogNode_MainWidget
    main_widget_pos = 'below ports'
    color = '#5d95de'

    def __init__(self, params):
        super().__init__(params, active=True)

        self.logger = self.new_logger('Log Node')

        self.targets = {
            **self.script.logs_manager.default_loggers,
            'own': self.logger,
        }
        self.target = 'global'

    def update_event(self, inp=-1):
        if self.active and inp == 0:
            i = 1
        elif not self.active:
            i = 0
        else:
            return

        msg = self.input(i)

        self.targets[self.target].log(logging.INFO, msg=msg)

    def get_state(self) -> dict:
        return {
            **super().get_state(),
            'target': self.target,
        }

    def set_state(self, data: dict, version):
        super().set_state(data, version)
        self.target = data['target']
        if self.session.gui and self.main_widget():
            self.main_widget().set_target(self.target)


class Clock_Node(NodeBase):
    title = 'clock'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Float(default=0.1), label='delay'),
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 1000)), label='iterations'),
    ]
    init_outputs = [
        NodeOutputBP(type_='exec')
    ]
    color = '#5d95de'
    main_widget_class = widgets.ClockNode_MainWidget
    main_widget_pos = 'below ports'

    def __init__(self, params):
        super().__init__(params)

        self.actions['start'] = {'method': self.start}
        self.actions['stop'] = {'method': self.stop}

        if self.session.gui:

            from qtpy.QtCore import QTimer
            self.timer = QTimer(self)
            self.timer.timeout.connect(self.timeouted)
            self.iteration = 0


    def timeouted(self):
        self.exec_output(0)
        self.iteration += 1
        if -1 < self.input(1) <= self.iteration:
            self.stop()

    def start(self):
        if self.session.gui:
            self.timer.setInterval(self.input(0)*1000)
            self.timer.start()
        else:
            import time
            for i in range(self.input(1)):
                self.exec_output(0)
                time.sleep(self.input(0))

    def stop(self):
        self.iteration = 0
        if self.session.gui:
            self.timer.stop()

    def toggle(self):
        # triggered from main widget
        if self.session.gui:
            if self.timer.isActive():
                self.stop()
            else:
                self.start()

    def update_event(self, inp=-1):
        if self.session.gui:
            self.timer.setInterval(self.input(0)*1000)

    def remove_event(self):
        self.stop()


class Slider_Node(NodeBase):
    title = 'slider'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Integer(default=1), label='scl'),
        NodeInputBP(dtype=dtypes.Boolean(default=False), label='round'),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    main_widget_class = widgets.SliderNode_MainWidget
    main_widget_pos = 'below ports'

    def __init__(self, params):
        super().__init__(params)

        self.val = 0

    def place_event(self):
        self.update()

    def view_place_event(self):
        # when running in gui mode, the value might come from the input widget
        self.update()

    def update_event(self, inp=-1):

        v = self.input(0) * self.val
        if self.input(1):
            v = round(v)

        self.set_output_val(0, v)

    def get_state(self) -> dict:
        return {
            'val': self.val,
        }

    def set_state(self, data: dict, version):
        self.val = data['val']


class _DynamicPorts_Node(NodeBase):
    init_inputs = []
    init_outputs = []

    def __init__(self, params):
        super().__init__(params)

        self.actions['add input'] = {'method': self.add_inp}
        self.actions['add output'] = {'method': self.add_out}

        self.num_inputs = 0
        self.num_outputs = 0

    def add_inp(self):
        self.create_input()

        index = self.num_inputs
        self.actions[f'remove input {index}'] = {
            'method': self.remove_inp,
            'data': index
        }

        self.num_inputs += 1

    def remove_inp(self, index):
        self.delete_input(index)
        self.num_inputs -= 1
        del self.actions[f'remove input {self.num_inputs}']

    def add_out(self):
        self.create_output()

        index = self.num_outputs
        self.actions[f'remove output {index}'] = {
            'method': self.remove_out,
            'data': index
        }

        self.num_outputs += 1

    def remove_out(self, index):
        self.delete_output(index)
        self.num_outputs -= 1
        del self.actions[f'remove output {self.num_outputs}']

    def get_state(self) -> dict:
        return {
            'num inputs': self.num_inputs,
            'num outputs': self.num_outputs,
        }

    def set_state(self, data: dict):
        self.num_inputs = data['num inputs']
        self.num_outputs = data['num outputs']


# class Node_Node(_DynamicPorts_Node):
#     """EXPERIMENTAL"""
#     title = 'node'
#     init_inputs = []
#     init_outputs = []
#     main_widget_class = widgets.CodeNode_MainWidget
#     main_widget_pos = 'between ports'
#
#     def __init__(self, params):
#         super().__init__(params)
#
#         self.code = \
# """from ryven.NENV import *
#
# class CustomNode(Node):
#     title = ''
#     init_inputs = []
#     init_outputs = []
#
#     def __init__(self, params):
#         super().__init__(params)
#
#     def update_event(self, inp=-1):
#         ...
# """
#         self.CustomNodeCls = None
#         self.custom_node = None
#         self.actions['build node'] = {'method': self.build_node}
#
#     def view_place_event(self):
#         self.main_widget().setText(self.code)
#
#     def build_node(self):
#         d = globals()
#         if 'CustomNode' in d:
#             del d['CustomNode']
#         try:
#             exec(self.code, d)
#             self.CustomNodeCls = d['CustomNode']
#             self.custom_node = self.CustomNodeCls(self.flow, self.session, {})
#
#             # sync ports
#             for i, inp in enumerate(self.custom_node.inputs):
#                 if len(self.inputs) > i:
#                     if self.inputs[i].type_ == inp.type_ and self.inputs[i].label == inp.label:
#                         continue
#                     else:
#                         self.delete_input(i)
#                         self.create_input(inp.label, inp.type_,)
#
#         except Exception:
#             pass
#
#     def update_event(self, inp=-1):
#         self.custom_node.update_event(inp)
#
#     def get_state(self) -> dict:
#         cn_config = {}
#         if self.custom_node:
#             cn_config = self.custom_node.get_state()
#
#         return {
#             'custom node config': cn_config,
#             'code': self.code,
#         }
#
#     def set_state(self, data: dict):
#         self.code = data['code']
#         self.build_node()
#         if self.custom_node:
#             self.custom_node.set_state(data['custom node config'])


class Exec_Node(_DynamicPorts_Node):
    title = 'exec'
    main_widget_class = widgets.CodeNode_MainWidget
    main_widget_pos = 'between ports'

    def __init__(self, params):
        super().__init__(params)

        self.code = None

    def place_event(self):
        pass

    def update_event(self, inp=-1):
        exec(self.code)

    def get_state(self) -> dict:
        return {
            **super().get_state(),
            'code': self.code,
        }

    def set_state(self, data: dict, version):
        super().set_state(data, version)
        self.code = data['code']


class Eval_Node(NodeBase):
    title = 'eval'
    init_inputs = [
        # NodeInputBP(),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    main_widget_class = widgets.EvalNode_MainWidget
    main_widget_pos = 'between ports'

    def __init__(self, params):
        super().__init__(params)

        self.actions['add input'] = {'method': self.add_param_input}

        self.number_param_inputs = 0
        self.expression_code = None

    def place_event(self):
        if self.number_param_inputs == 0:
            self.add_param_input()

    def add_param_input(self):
        self.create_input()

        index = self.number_param_inputs
        self.actions[f'remove input {index}'] = {
            'method': self.remove_param_input,
            'data': index
        }

        self.number_param_inputs += 1

    def remove_param_input(self, index):
        self.delete_input(index)
        self.number_param_inputs -= 1
        del self.actions[f'remove input {self.number_param_inputs}']

    def update_event(self, inp=-1):
        inp = [self.input(i) for i in range(self.number_param_inputs)]
        self.set_output_val(0, eval(self.expression_code))

    def get_state(self) -> dict:
        return {
            'num param inputs': self.number_param_inputs,
            'expression code': self.expression_code,
        }

    def set_state(self, data: dict, version):
        self.number_param_inputs = data['num param inputs']
        self.expression_code = data['expression code']


class Interpreter_Node(NodeBase):
    """Provides a python interpreter via a basic console with access to the
    node's properties."""
    title = 'interpreter'
    init_inputs = []
    init_outputs = []
    main_widget_class = widgets.InterpreterConsole

    # DEFAULT COMMANDS

    def clear(self):
        self.hist.clear()
        self._hist_updated()

    def reset(self):
        self.interp = code.InteractiveInterpreter(locals=locals())

    COMMANDS = {
        'clear': clear,
        'reset': reset,
    }

    def __init__(self, params):
        super().__init__(params)

        self.interp = None
        self.hist: [str] = []
        self.buffer: [str] = []

        self.reset()

    def _hist_updated(self):
        if self.session.gui:
            self.main_widget().interp_updated()

    def process_input(self, cmds: str):
        if m := self.COMMANDS.get(cmds):
            m()
        else:
            for l in cmds.splitlines():
                self.write(l)  # print input
                self.buffer.append(l)
            src = '\n'.join(self.buffer)

            def run_src():
                more_inp_required = self.interp.runsource(src, '<console>')
                if not more_inp_required:
                    self.buffer.clear()

            if self.session.gui:
                with redirect_stdout(self), redirect_stderr(self):
                    run_src()
            else:
                run_src()

    def write(self, line: str):
        self.hist.append(line)
        self._hist_updated()


class Storage_Node(NodeBase):
    """Sequentially stores all the data provided at the input in an array.
    A COPY of the storage array is provided at the output"""

    title = 'store'
    init_inputs = [
        NodeInputBP(),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    color = '#aadd55'

    def __init__(self, params):
        super().__init__(params)

        self.storage = []

        self.actions['clear'] = {'method': self.clear}

    def clear(self):
        self.storage.clear()
        self.set_output_val(0, [])

    def update_event(self, inp=-1):
        self.storage.append(self.input(0))
        self.set_output_val(0, self.storage.copy())

    def get_state(self) -> dict:
        return {
            'data': self.storage,
        }

    def set_state(self, data: dict, version):
        self.storage = data['data']


import uuid


class LinkIN_Node(NodeBase):
    """You can use link OUT nodes to link them up to this node.
    Whenever a link IN node receives data (or an execution signal),
    if there is a linked OUT node, it will receive the data
    and propagate it further."""

    title = 'link IN'
    init_inputs = [
        NodeInputBP(),
    ]
    init_outputs = []  # no outputs

    # instances registration
    INSTANCES = {}  # {UUID: node}

    def __init__(self, params):
        super().__init__(params)
        self.display_title = 'link'

        # register
        self.ID: uuid.UUID = uuid.uuid4()
        self.INSTANCES[str(self.ID)] = self

        self.actions['add input'] = {
            'method': self.add_inp
        }
        self.actions['remove inp'] = {}
        self.actions['copy ID'] = {
            'method': self.copy_ID
        }

        self.linked_node: LinkOUT_Node = None

    def copy_ID(self):
        from qtpy.QtWidgets import QApplication
        QApplication.clipboard().setText(str(self.ID))

    def add_inp(self):
        index = len(self.inputs)

        self.create_input()

        self.actions['remove inp'][str(index)] = {
            'method': self.rem_inp,
            'data': index,
        }
        if self.linked_node is not None:
            self.linked_node.add_out()

    def rem_inp(self, index):
        self.delete_input(index)
        del self.actions['remove inp'][str(len(self.inputs))]
        if self.linked_node is not None:
            self.linked_node.rem_out(index)

    def update_event(self, inp=-1):
        if self.linked_node is not None:
            self.linked_node.set_output_val(inp, self.input(inp))

    def get_state(self) -> dict:
        return {
            'ID': str(self.ID),
        }

    def set_state(self, data: dict, version):
        if data['ID'] in self.INSTANCES:
            # this happens when some existing node has been copied and pasted.
            # we only want to rebuild links when loading a project, considering
            # new links when copying nodes might get quite complex
            pass
        else:
            del self.INSTANCES[str(self.ID)]     # remove old ref
            self.ID = uuid.UUID(data['ID'])      # use original ID
            self.INSTANCES[str(self.ID)] = self  # set new ref

            # resolve possible pending link builds from OUT nodes that happened
            # to get initialized earlier
            LinkOUT_Node.new_link_in_loaded(self)

    def remove_event(self):
        # break existent link
        if self.linked_node:
            self.linked_node.linked_node = None
            self.linked_node = None


class LinkOUT_Node(NodeBase):
    """The complement to the link IN node"""

    title = 'link OUT'
    init_inputs = []  # no inputs
    init_outputs = []  # will be synchronized with linked IN node

    INSTANCES = []
    PENDING_LINK_BUILDS = {}
    # because a link OUT node might get initialized BEFORE it's corresponding
    # link IN, it then stores itself together with the ID of the link IN it's
    # waiting for in PENDING_LINK_BUILDS

    @classmethod
    def new_link_in_loaded(cls, n: LinkIN_Node):
        for out_node, in_ID in cls.PENDING_LINK_BUILDS.items():
            if in_ID == str(n.ID):
                out_node.link_to(n)

    def __init__(self, params):
        super().__init__(params)
        self.display_title = 'link'

        self.INSTANCES.append(self)
        self.linked_node: LinkIN_Node = None

        self.actions['link to ID'] = {
            'method': self.choose_link_ID
        }

    def choose_link_ID(self):
        """opens a small input dialog for providing a copied link IN ID"""

        from qtpy.QtWidgets import QDialog, QMessageBox, QVBoxLayout, QLineEdit

        class IDInpDialog(QDialog):
            def __init__(self):
                super().__init__()
                self.id_str = None
                self.setLayout(QVBoxLayout())
                self.line_edit = QLineEdit()
                self.layout().addWidget(self.line_edit)
                self.line_edit.returnPressed.connect(self.return_pressed)

            def return_pressed(self):
                self.id_str = self.line_edit.text()
                self.accept()

        d = IDInpDialog()
        d.exec_()

        if d.id_str is not None:
            n = LinkIN_Node.INSTANCES.get(d.id_str)
            if n is None:
                QMessageBox.warning(title='link failed', text='couldn\'t find a valid link in node')
            else:
                self.link_to(n)

    def link_to(self, n: LinkIN_Node):
        self.linked_node = n
        n.linked_node = self

        o = len(self.outputs)
        i = len(self.linked_node.inputs)

        # remove outputs if there are too many
        for j in range(i, o):
            self.delete_output(0)

        # add outputs if there are too few
        for j in range(o, i):
            self.create_output()

        self.update()

    def add_out(self):
        # triggered by linked_node
        self.create_output()

    def rem_out(self, index):
        # triggered by linked_node
        self.delete_output(index)

    def update_event(self, inp=-1):
        if self.linked_node is None:
            return

        # update ALL ports
        for i in range(len(self.outputs)):
            self.set_output_val(i, self.linked_node.input(i))

    def get_state(self) -> dict:
        if self.linked_node is None:
            return {}
        else:
            return {
                'linked ID': str(self.linked_node.ID),
            }

    def set_state(self, data: dict, version):
        if len(data) > 0:
            n: LinkIN_Node = LinkIN_Node.INSTANCES.get(data['linked ID'])
            if n is None:
                # means that the OUT node gets initialized before it's link IN
                self.PENDING_LINK_BUILDS[self] = data['linked ID']
            elif n.linked_node is None:
                # pair up
                n.linked_node = self
                self.linked_node = n

    def remove_event(self):
        # break existent link
        if self.linked_node:
            self.linked_node.linked_node = None
            self.linked_node = None


# -------------------------------------------


nodes = [
    Checkpoint_Node,
    Button_Node,
    Print_Node,
    Log_Node,
    Clock_Node,
    Slider_Node,
    Exec_Node,
    Eval_Node,
    Storage_Node,
    LinkIN_Node,
    LinkOUT_Node,
    Interpreter_Node,
]
