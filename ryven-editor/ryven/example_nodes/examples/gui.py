import re

from qtpy.QtGui import QFont
from qtpy.QtCore import Qt, Signal, QEvent
from qtpy.QtWidgets import QPushButton, QComboBox, QSlider, QTextEdit, QPlainTextEdit, QWidget, QVBoxLayout, QLineEdit, \
    QDialog, QMessageBox

from ryven.gui_env import *

from . import special_nodes as special_nodes
from . import basic_operators as operator_nodes
from . import control_structures as control_nodes


"""
    generic base classes
"""


class GuiBase(NodeGUI):
    pass


"""
    operator nodes
"""


@node_gui(operator_nodes.OperatorNodeBase)
class OperatorNodeBaseGui(GuiBase):
    input_widget_classes = {
        'in': inp_widgets.Builder.evaled_line_edit(size='s', resizing=True),
    }
    # init_input_widgets = {
    #     0: {'name': 'in', 'pos': 'besides'},
    #     1: {'name': 'in', 'pos': 'besides'},
    # }
    style = 'small'

    def __init__(self, params):
        super().__init__(params)

        self.actions['add input'] = {'method': self.add_operand_input}
        self.actions['remove input'] = {}

        for inp in self.node.inputs:
            self.input_widgets[inp] = {'name': 'in', 'pos': 'besides'}

    def initialized(self):
        super().initialized()
        self.rebuild_remove_actions()

    def add_operand_input(self):
        self.register_new_operand_input(self.node.num_inputs + 1)
        self.node.add_op_input()

    def register_new_operand_input(self, index):
        self.actions[f'remove input'][f'{index}'] = {
            'method': self.remove_operand_input,
            'data': index
        }

    def remove_operand_input(self, index):
        self.node.remove_op_input(index)
        self.rebuild_remove_actions()

    def rebuild_remove_actions(self):
        self.actions['remove input'] = {}
        for i in range(self.node.num_inputs):
            self.actions[f'remove input'][f'{i}'] = \
                {'method': self.remove_operand_input, 'data': i}


@node_gui(operator_nodes.LogicNodeBase)
class LogicNodeBaseGui(OperatorNodeBaseGui):
    color = '#f58142'


@node_gui(operator_nodes.ArithmeticNodeBase)
class ArithNodeBaseGui(OperatorNodeBaseGui):
    color = '#58db53'


@node_gui(operator_nodes.ComparatorNodeBase)
class CompNodeBaseGui(OperatorNodeBaseGui):
    color = '#a1574c'


"""
    control structures
"""


@node_gui(control_nodes.CSNodeBase)
class CSNodeBaseGui(GuiBase):
    style = 'normal'
    color = '#b33a27'


@node_gui(control_nodes.ForLoop_Node)
class ForLoopGui(CSNodeBaseGui):
    input_widget_classes = {
        'RangeFrom': inp_widgets.Builder.int_spinbox(0, (0, 1000000)),
        'RangeTo': inp_widgets.Builder.int_spinbox(10, (0, 1000000)),
    }
    init_input_widgets = {
        1: {'name': 'RangeFrom', 'pos': 'besides'},
        2: {'name': 'RangeTo', 'pos': 'besides'},
    }

    def __init__(self, params):
        super().__init__(params)

        self.actions['add dimension'] = {'method': self.add_dimension}
        self.actions['remove dimension'] = {}

    def add_dimension(self):
        self.attach_input_widgets(['RangeFrom', 'RangeTo'])
        new_dim = self.node.dims + 1
        self.node.add_dimension()

        self.actions[f'remove dimension'][f'{new_dim}'] = {
            'method': self.remove_dimension,
            'data': new_dim
        }

    def remove_dimension(self, dim):
        self.node.remove_dimension(dim)
        self.rebuild_remove_actions()

    def rebuild_remove_actions(self):
        self.actions['remove dimension'] = {}
        for i in range(1, self.dims):
            self.actions[f'remove dimension'][f'{i + 1}'] = \
                {'method': self.remove_dimension, 'data': i + 1}


@node_gui(control_nodes.ForEachLoop_Node)
class ForEachLoopGui(CSNodeBaseGui):
    input_widget_classes = {
        'List': inp_widgets.Builder.evaled_line_edit(),
    }
    init_input_widgets = {
        1: {'name': 'List', 'pos': 'besides'},
    }


"""
    special nodes
"""


@node_gui(special_nodes.NodeBase)
class SpecialNodeGuiBase(GuiBase):
    color = '#FFCA00'


@node_gui(special_nodes.DualNodeBase)
class DualNodeBaseGui(SpecialNodeGuiBase):
    def initialized(self):
        super().initialized()
        self.clean_actions()

    def clean_actions(self):
        if 'make passive' in self.actions:
            del self.actions['make passive']
        if 'make active' in self.actions:
            del self.actions['make active']

        if self.node.active:
            self.actions['make passive'] = {'method': self.make_passive}
        else:
            self.actions['make active'] = {'method': self.make_active}

    def make_passive(self):
        del self.actions['make passive']
        self.actions['make active'] = {'method': self.make_active}
        self.node.make_passive()

    def make_active(self):
        del self.actions['make active']
        self.actions['make passive'] = {'method': self.make_passive}
        self.node.make_active()


@node_gui(special_nodes.Checkpoint_Node)
class CheckpointNodeGui(DualNodeBaseGui):
    style = 'small'
    display_title = ''

    def initialized(self):
        super().initialized()
        self.actions['add output'] = {'method': self.add_output}
        self.actions['remove output'] = {}
        self.rebuild_remove_actions()

    def add_output(self):
        self.node.add_output()
        self.rebuild_remove_actions()

    def remove_output(self, index):
        self.node.remove_output(index)
        self.rebuild_remove_actions()

    def rebuild_remove_actions(self):
        self.actions['remove output'] = {}
        for i in range(len(self.node.outputs)):
            self.actions['remove output'][f'{i}'] = \
                {'method': self.remove_output, 'data': i}


class ButtonNode_MainWidget(NodeMainWidget, QPushButton):

    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QPushButton.__init__(self)

        self.clicked.connect(self.update_node)


@node_gui(special_nodes.Button_Node)
class ButtonNodeGui(SpecialNodeGuiBase):
    main_widget_class = ButtonNode_MainWidget
    main_widget_pos = 'between ports'
    color = '#99dd55'


class ClockNode_MainWidget(NodeMainWidget, QPushButton):

    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QPushButton.__init__(self)

        self.clicked.connect(self.node.toggle)


@node_gui(special_nodes.Clock_Node)
class ClockNodeGui(SpecialNodeGuiBase):
    main_widget_class = ClockNode_MainWidget
    main_widget_pos = 'below ports'
    input_widget_classes = {
        'delay': inp_widgets.Builder.int_slider(1, (0, 10000)),
        'iter': inp_widgets.Builder.int_spinbox(-1, (-1, 1000)),
    }
    init_input_widgets = {
        0: {'name': 'delay', 'pos': 'besides'},
        1: {'name': 'iter', 'pos': 'besides'},
    }
    color = '#5d95de'

    def __init__(self, params):
        super().__init__(params)

        self.actions['start'] = {'method': self.start}
        self.actions['stop'] = {'method': self.stop}

    def start(self):
        self.node.start()

    def stop(self):
        self.node.stop()


@node_gui(special_nodes.Log_Node)
class LogNodeGui(SpecialNodeGuiBase):
    color = '#5d95de'


class SliderNode_MainWidget(NodeMainWidget, QSlider):
    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QSlider.__init__(self, Qt.Horizontal)

        self.setRange(0, 1000)
        self.setValue(self.node.val*1000)
        self.valueChanged.connect(self.value_changed)

    def value_changed(self, v):
        self.node.val = v/1000
        self.update_node()


@node_gui(special_nodes.Slider_Node)
class SliderNodeGui(SpecialNodeGuiBase):
    main_widget_class = SliderNode_MainWidget
    main_widget_pos = 'below ports'
    input_widget_classes = {
        'scale': inp_widgets.Builder.int_spinbox(1, (1, 99)),
        'round': inp_widgets.Builder.bool_checkbox(True),
    }
    init_input_widgets = {
        0: {'name': 'scale', 'pos': 'besides'},
        1: {'name': 'round', 'pos': 'besides'},
    }

    def initialized(self):
        self.main_widget().setValue(self.node.val*1000)


@node_gui(special_nodes._DynamicPorts_Node)
class DynamicPortsGui(SpecialNodeGuiBase):
    def __init__(self, params):
        super().__init__(params)

        self.actions['add input'] = {'method': self.add_input}
        self.actions['remove input'] = {}
        self.actions['add output'] = {'method': self.add_output}
        self.actions['remove output'] = {}

    def add_input(self):
        self.node.add_input()
        index = len(self.node.inputs)-1
        self.actions['remove input'][str(index)] = \
            {'method': self.remove_input, 'data': index}

    def remove_input(self, index: int):
        self.node.remove_input(index)
        del self.actions['remove input'][str(index)]

    def add_output(self):
        self.node.add_output()
        index = len(self.node.outputs)-1
        self.actions['remove output'][str(index)] = \
            {'method': self.remove_output, 'data': index}

    def remove_output(self, index: int):
        self.node.remove_output(index)
        del self.actions['remove output'][str(index)]


class ExecNode_MainWidget(NodeMainWidget, QTextEdit):
    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QTextEdit.__init__(self)

        self.setFont(QFont('Consolas', 9))
        self.textChanged.connect(self.text_changed)
        self.setFixedHeight(150)
        self.setFixedWidth(300)

    def text_changed(self):
        self.node.code = self.toPlainText()
        self.update_node()

    def get_state(self) -> dict:
        return {
            'text': self.toPlainText(),
        }

    def set_state(self, data: dict):
        self.setPlainText(data['text'])


@node_gui(special_nodes.Exec_Node)
class ExecNodeGui(DynamicPortsGui):
    main_widget_class = ExecNode_MainWidget
    main_widget_pos = 'between ports'


class EvalNode_MainWidget(NodeMainWidget, QPlainTextEdit):
    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QPlainTextEdit.__init__(self)

        self.setFont(QFont('Consolas', 9))
        self.textChanged.connect(self.text_changed)
        self.setMaximumHeight(50)
        self.setMaximumWidth(200)

    def text_changed(self):
        self.node.expression_code = self.toPlainText()
        self.update_node()

    def get_state(self) -> dict:
        return {
            'text': self.toPlainText(),
        }

    def set_state(self, data: dict):
        self.setPlainText(data['text'])


@node_gui(special_nodes.Eval_Node)
class EvalNodeGui(SpecialNodeGuiBase):
    main_widget_class = EvalNode_MainWidget
    main_widget_pos = 'between ports'

    def __init__(self, params):
        super().__init__(params)

        self.actions['add input'] = {'method': self.add_input}
        self.actions['remove input'] = {}

    def add_input(self):
        self.node.add_param_input()
        index = self.node.param_inputs-1
        self.actions['remove input'][str(index)] = \
            {'method': self.remove_input, 'data': index}

    def remove_input(self, index: int):
        self.node.remove_param_input(index)
        del self.actions['remove input'][str(index)]


class ConsoleInpLineEdit(QLineEdit):

    returned = Signal(str)

    def __init__(self):
        super().__init__()

        self.hist_index = 0
        self.hist = []

    def event(self, ev: QEvent) -> bool:

        if ev.type() == QEvent.KeyPress:

            if ev.key() == Qt.Key_Tab:
                self.insert(' '*4)
                return True

            elif ev.key() == Qt.Key_Backtab:
                ccp = self.cursorPosition()
                text_left = self.text()[:ccp]
                text_right = self.text()[ccp:]
                ends_with_tab = re.match(r"(.*)\s\s\s\s$", text_left)
                if ends_with_tab:
                    self.setText(text_left[:-4]+text_right)
                    self.setCursorPosition(ccp-4)
                    return True

            elif ev.key() == Qt.Key_Up:
                self.recall(self.hist_index - 1)
                return True

            elif ev.key() == Qt.Key_Down:
                self.recall(self.hist_index + 1)
                return True

            elif ev.key() == Qt.Key_Return:
                self.return_key()
                return True

        return super().event(ev)

    def return_key(self) -> None:
        text = self.text()
        for line in text.splitlines():
            self.record(line)
        self.returned.emit(text)
        self.clear()

    def record(self, line: str) -> None:
        """store line in history buffer and update hist_index"""

        self.hist.append(line)

        if self.hist_index == len(self.hist)-1 or line != self.hist[self.hist_index]:
            self.hist_index = len(self.hist)

    def recall(self, index: int) -> None:
        """select a line from the history list"""

        if len(self.hist) > 0 and 0 <= index < len(self.hist):
            self.setText(self.hist[index])
            self.hist_index = index


class ConsoleOutDisplay(QPlainTextEdit):
    def __init__(self):
        super().__init__()

        self.setReadOnly(True)
        self.setFont(QFont('Source Code Pro', 9))


class InterpreterConsole(NodeMainWidget, QWidget):
    def __init__(self, params):
        NodeMainWidget.__init__(self, params)
        QWidget.__init__(self)

        self.inp_line_edit = ConsoleInpLineEdit()
        self.output_text_edit = ConsoleOutDisplay()

        self.inp_line_edit.returned.connect(self.node.process_input)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.output_text_edit)
        self.layout().addWidget(self.inp_line_edit)

        self.last_hist_len = 0

    def interp_updated(self):

        if self.last_hist_len < len(self.node.hist):
            self.output_text_edit.appendPlainText('\n'.join(self.node.hist[self.last_hist_len:]))
        else:
            self.output_text_edit.clear()
            self.output_text_edit.setPlainText('\n'.join(self.node.hist))

        self.last_hist_len = len(self.node.hist)


@node_gui(special_nodes.Interpreter_Node)
class InterpreterConsoleGui(SpecialNodeGuiBase):
    main_widget_class = InterpreterConsole
    main_widget_pos = 'between ports'


@node_gui(special_nodes.Storage_Node)
class StorageNodeGui(SpecialNodeGuiBase):
    color = '#aadd55'

    def __init__(self, params):
        super().__init__(params)

        self.actions['clear'] = {'method': self.clear}

    def clear(self):
        self.node.clear()


@node_gui(special_nodes.LinkIN_Node)
class LinkIN_NodeGui(SpecialNodeGuiBase):
    def __init__(self, params):
        super().__init__(params)

        self.actions['add input'] = {'method': self.add_inp}
        self.actions['remove inp'] = {}
        self.actions['copy ID'] = {'method': self.copy_ID}

    def copy_ID(self):
        from qtpy.QtWidgets import QApplication
        QApplication.clipboard().setText(str(self.node.ID))

    def add_inp(self):
        self.node.add_input()
        index = self.node.inputs-1
        self.actions['remove inp'][str(index)] = {
            'method': self.remove_inp,
            'data': index
        }

    def remove_inp(self, index: int):
        self.node.remove_input(index)
        del self.actions['remove inp'][str(index)]


@node_gui(special_nodes.LinkOUT_Node)
class LinkOUT_NodeGui(SpecialNodeGuiBase):

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

    def __init__(self, params):
        super().__init__(params)

        self.actions['link to ID'] = {'method': self.link_to_ID}

    def link_to_ID(self):
        d = self.IDInpDialog()
        d.exec_()

        if d.id_str is not None:
            n = special_nodes.LinkIN_Node.INSTANCES.get(d.id_str)
            if n is not None:
                self.node.link_to(n)
            else:
                QMessageBox.warning(
                    self,
                    title='link failed',
                    text=f'No node with ID "{d.id_str}" found'
                )
