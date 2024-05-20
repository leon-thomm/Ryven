from typing import Dict, Set
import code
from contextlib import redirect_stdout, redirect_stderr
from packaging.version import Version

from ryvencore.addons.Logging import LoggingAddon
from ryven.node_env import *


class NodeBase(Node):
    version = 'v0.3'

    def have_gui(self):
        return hasattr(self, 'gui')


class DualNodeBase(NodeBase):
    """For nodes that can be active and passive"""

    def __init__(self, params, active=True):
        super().__init__(params)

        self.active = active

    def make_passive(self):
        self.delete_input(0)
        self.delete_output(0)
        self.active = False

    def make_active(self):
        self.create_input(type_='exec', insert=0)
        self.create_output(type_='exec', insert=0)
        self.active = True

    def get_state(self) -> dict:
        return {
            'active': self.active
        }

    def set_state(self, data: dict, version):
        self.active = data['active']


class Checkpoint_Node(DualNodeBase):
    """Provides a simple checkpoint to reroute your connections"""

    title = 'checkpoint'
    init_inputs = [
        NodeInputType(type_='data'),
    ]
    init_outputs = [
        NodeOutputType(type_='data'),
    ]
    
    def __init__(self, params):
        super().__init__(params)

        self.active = False

    """
    state transitions
    """

    def clear_ports(self):
        # remove all outputs
        for i in range(len(self.outputs)):
            self.delete_output(0)

        # remove all inputs
        for i in range(len(self.inputs)):
            self.delete_input(0)

    def make_active(self):
        num_outputs = len(self.outputs)
        self.clear_ports()
        super().make_active()
        for i in range(1, num_outputs):
            self.add_output()


    def make_passive(self):
        num_outputs = len(self.outputs)
        super().make_passive()
        self.clear_ports()
        for i in range(num_outputs):
            self.add_output()

    def add_output(self):
        self.create_output(type_='exec' if self.active else 'data')

    def remove_output(self, index):
        self.delete_output(index)

    """
    update
    """

    def update_event(self, inp=-1):
        if self.active and inp == 0:
            for i in range(len(self.outputs)):
                self.exec_output(i)

        elif not self.active:
            data = self.input(0)
            for i in range(len(self.outputs)):
                self.set_output_val(i, data)


class Button_Node(NodeBase):
    title = 'Button'
    init_inputs = []
    init_outputs = [
        NodeOutputType(type_='exec')
    ]

    def update_event(self, inp=-1):
        self.exec_output(0)


class Print_Node(DualNodeBase):
    title = 'Print'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType(),
    ]
    init_outputs = [
        NodeOutputType(type_='exec'),
    ]

    def __init__(self, params):
        super().__init__(params, active=True)

    def update_event(self, inp=-1):
        if inp == 0:
            print(self.input(1 if self.active else 0).payload)


import logging


class Log_Node(DualNodeBase):
    title = 'Log'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType('msg', type_='data'),
    ]
    init_outputs = [
        NodeOutputType(type_='exec'),
    ]

    logs: Dict[int, logging.Logger] = {}   # {int: Logger}
    in_use: Set[int] = set()  # make sure we don't reuse numbers on copy & paste

    def __init__(self, params):
        super().__init__(params, active=True)

        self.number: int = None
        self.logger: logging.Logger = None

    def place_event(self):
        if self.number is None:
            # didn't load; initialize
            self.number = len(self.logs)
            self.logs[self.number] = \
                self.logs_ext().new_logger(self, 'Log Node')
            self.in_use.add(self.number)

    def logs_ext(self) -> LoggingAddon:
        return self.get_addon('Logging')

    def update_event(self, inp=-1):
        if inp == 0:
            msg = self.input(1 if self.active and inp == 0 else 0).payload
            self.logs[self.number].log(logging.INFO, msg=msg)
            # TODO: support more than INFO, with a dropdown menu in main widget

    def get_state(self) -> dict:
        return {
            **super().get_state(),
            'number': self.number,
        }

    def set_state(self, data: dict, version):
        if Version(version) < Version('0.2'):
            # ignore old version
            return
        super().set_state(data, version)
        n = data['number']
        if n not in self.in_use:
            self.number = n
        else:
            # number already in use; generate a new one
            # happens on copy & paste
            self.number = len(self.logs)

        # the logging addon will have re-created the logger
        # for us already
        l = self.logs_ext().new_logger(self, 'Log Node')
        if l is None:
            print(f'WARNING: logger {self.number} for Log Node {self} already exists')
        else:
            self.logs[self.number] = l


class Clock_Node(NodeBase):
    title = 'clock'
    init_inputs = [
        NodeInputType('delay'),
        NodeInputType('iterations'),
    ]
    init_outputs = [
        NodeOutputType(type_='exec')
    ]

    # When running with GUI, this node uses QTime which doesn't
    # block the GUI. When running without GUI, it uses time.sleep()

    def __init__(self, params):
        super().__init__(params)

        self.running_with_qt = False

    def place_event(self):
        self.running_with_qt = self.GUI is not None

        if self.running_with_qt:
            from qtpy.QtCore import QTimer
            self.timer = QTimer()
            self.timer.timeout.connect(self.timeouted)
            self.iteration = 0

    def timeouted(self):
        self.exec_output(0)
        self.iteration += 1
        if -1 < self.input(1).payload <= self.iteration:
            self.stop()

    def start(self):
        if self.running_with_qt:
            self.timer.setInterval(self.input(0).payload)
            self.timer.start()
        else:
            import time
            for i in range(self.input(1).payload):
                self.exec_output(0)
                time.sleep(self.input(0).payload/1000)

    def stop(self):
        assert self.running_with_qt
        self.timer.stop()
        self.iteration = 0

    def toggle(self):
        # triggered from main widget
        if self.running_with_qt:
            if self.timer.isActive():
                self.stop()
            else:
                self.start()
        # toggling is impossible when using time.sleep()

    def update_event(self, inp=-1):
        if self.running_with_qt:
            self.timer.setInterval(self.input(0).payload)

    def remove_event(self):
        if self.running_with_qt:
            self.stop()


class Slider_Node(NodeBase):
    title = 'slider'
    init_inputs = [
        NodeInputType('scl'),
        NodeInputType('round'),
    ]
    init_outputs = [
        NodeOutputType(),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.val = 0

    def place_event(self):
        self.update()

    def update_event(self, inp=-1):
        v = self.input(0).payload * self.val
        if self.input(1).payload:
            v = round(v)
        self.set_output_val(0, Data(v))

    def get_state(self) -> dict:
        return {'val': self.val}

    def set_state(self, data: dict, version):
        self.val = data['val']


class _DynamicPorts_Node(NodeBase):
    init_inputs = []
    init_outputs = []

    def add_input(self):
        self.create_input()

    def remove_input(self, index):
        self.delete_input(index)

    def add_output(self):
        self.create_output()

    def remove_output(self, index):
        self.delete_output(index)


class Exec_Node(_DynamicPorts_Node):
    title = 'exec'

    def __init__(self, params):
        super().__init__(params)

        self.code = None

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
        # NodeInputType(),
    ]
    init_outputs = [
        NodeOutputType(),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.number_param_inputs = 0
        self.expression_code = None

    def place_event(self):
        if self.number_param_inputs == 0:
            self.add_param_input()

    def add_param_input(self):
        self.create_input()

        self.number_param_inputs += 1

    def remove_param_input(self, index):
        self.delete_input(index)
        self.number_param_inputs -= 1

    def update_event(self, inp=-1):
        inp = [
            self.input(i).payload if self.input(i) is not None else None
            for i in range(self.number_param_inputs)
        ]
        self.set_output_val(0, Data(eval(self.expression_code)))

    def get_state(self) -> dict:
        return {
            'num param inputs': self.number_param_inputs,
            'expression code': self.expression_code,
        }

    def set_state(self, data: dict, version):
        self.number_param_inputs = data['num param inputs']
        self.expression_code = data['expression code']


class Interpreter_Node(NodeBase):
    """
    Provides a python interpreter via a basic console with access to the
    node's properties.
    """
    title = 'interpreter'
    init_inputs = []
    init_outputs = []

    """
    commands
    """

    def clear(self):
        self.hist.clear()
        self._hist_updated()

    def reset(self):
        self.interp = code.InteractiveInterpreter(locals=locals())

    COMMANDS = {
        'clear': clear,
        'reset': reset,
    }

    """
    behaviour
    """

    def __init__(self, params):
        super().__init__(params)

        self.interp = None
        self.hist: [str] = []
        self.buffer: [str] = []

        self.reset()

    def _hist_updated(self):
        if self.have_gui():
            self.gui.main_widget().interp_updated()

    def process_input(self, cmds: str):
        m = self.COMMANDS.get(cmds)
        if m is not None:
            m(self)
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
                with redirect_stdout(self), redirect_stderr(self):  # type: ignore
                    run_src()
            else:
                run_src()

    def write(self, line: str):
        self.hist.append(line)
        self._hist_updated()


class Storage_Node(NodeBase):
    """
    Sequentially stores all the data provided at the input in an array.
    A shallow copy of the storage array is provided at the output
    """

    title = 'store'
    init_inputs = [
        NodeInputType(),
    ]
    init_outputs = [
        NodeOutputType(),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.storage = []

    def clear(self):
        self.storage.clear()
        self.set_output_val(0, Data([]))

    def update_event(self, inp=-1):
        self.storage.append(self.input(0).payload)
        self.set_output_val(0, Data(self.storage.copy()))

    def get_state(self) -> dict:
        return {
            'data': self.storage,
        }

    def set_state(self, data: dict, version):
        self.storage = data['data']


import uuid


class LinkIN_Node(NodeBase):
    """
    Whenever a link IN node receives data (or an execution signal),
    if there is a linked LinkOUT node, it will receive the data
    and propagate it further.
    Notice that this breaks the data flow, which can have substantial
    performance implications and is generally not recommended.
    """

    title = 'link IN'
    init_inputs = [
        NodeInputType(),
    ]
    init_outputs = []  # no outputs

    # instances registration
    INSTANCES: Dict[str, Node] = {}

    def __init__(self, params):
        super().__init__(params)

        # register
        self.ID: uuid.UUID = uuid.uuid4()
        self.INSTANCES[str(self.ID)] = self

        self.linked_node: LinkOUT_Node = None

    def add_input(self):
        self.create_input()
        if self.linked_node is not None:
            self.linked_node.add_output()

    def remove_input(self, index):
        self.delete_input(index)
        if self.linked_node is not None:
            self.linked_node.remove_output(index)

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
    init_inputs: List[NodeInputType] = []  # no inputs
    init_outputs: List[NodeOutputType] = []  # will be synchronized with linked IN node

    INSTANCES: List['LinkOUT_Node'] = []
    PENDING_LINK_BUILDS: Dict['LinkOUT_Node', str] = {}
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

        self.INSTANCES.append(self)
        self.linked_node: LinkIN_Node = None

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

    def add_output(self):
        # triggered by linked_node
        self.create_output()

    def remove_output(self, index):
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


node_types = [
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

# account for old package name
for n in node_types:
    n.legacy_identifiers = [
        *getattr(n, 'legacy_identifiers', []),
        f'std.{n.__class__.__name__}',
    ]

export_nodes(
    node_types=node_types,
    sub_pkg_name='special_nodes',
)
