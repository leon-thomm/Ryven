from queue import Queue
from typing import List, Dict, Tuple, Optional, Union, Type

from qtpy.QtCore import QObject, Signal

from .WidgetBaseClasses import NodeMainWidget, NodeInputWidget, NodeInspectorWidget
from .NodeInspector import NodeInspectorDefaultWidget


class NodeGUI(QObject):
    """
    Interface class between nodes and their GUI representation.
    """

    # customizable gui attributes
    description_html: Optional[str] = None
    main_widget_class: Optional[Type[NodeMainWidget]] = None
    main_widget_pos: str = 'below ports'
    input_widget_classes: Dict[str, Type[NodeInputWidget]] = {}
    inspector_widget_class: Type[NodeInspectorWidget] = NodeInspectorDefaultWidget
    wrap_inspector_in_default: bool = False
    init_input_widgets: dict = {}
    style: str = 'normal'
    color: str = '#c69a15'
    display_title: Optional[str] = None
    icon: Optional[str] = None

    # qt signals
    updating = Signal()
    update_error = Signal(object)
    input_added = Signal(int, object)
    output_added = Signal(int, object)
    input_removed = Signal(int, object)
    output_removed = Signal(int, object)
    update_shape_triggered = Signal()
    hide_unconnected_ports_triggered = Signal()
    show_unconnected_ports_triggered = Signal()

    def __init__(self, params):
        QObject.__init__(self)

        node, session_gui = params
        self.node = node
        self.item = None   # set by the node item directly after this __init__ call
        self.session_gui = session_gui
        setattr(node, 'gui', self)

        self.actions = self._init_default_actions()

        if self.display_title is None:
            self.display_title = self.node.title

        self.input_widgets = {}     # {input: widget name}
        for i, widget_data in self.init_input_widgets.items():
            self.input_widgets[self.node.inputs[i]] = widget_data
        # using attach_input_widgets() one can buffer input widget
        # names for inputs that are about to get created
        self._next_input_widgets = Queue()

        self.error_during_update = False

        # turn ryvencore signals into Qt signals
        self.node.updating.sub(self._on_updating)
        self.node.update_error.sub(self._on_update_error)
        self.node.input_added.sub(self._on_new_input_added)
        self.node.output_added.sub(self._on_new_output_added)
        self.node.input_removed.sub(self._on_input_removed)
        self.node.output_removed.sub(self._on_output_removed)

        # create the inspector widget
        inspector_params = (self.node, self)
        if self.wrap_inspector_in_default:
            self.inspector_widget = NodeInspectorDefaultWidget(
                child=self.inspector_widget_class((self.node, self)),
                params=inspector_params,
            )
        else:
            self.inspector_widget = self.inspector_widget_class(inspector_params)

    def initialized(self):
        """
        *VIRTUAL*

        Called after the node GUI has been fully initialized.
        The Node has been created already (including all ports) and loaded.
        No connections have been made to ports of the node yet.
        """
        pass

    """
    slots
    """

    # TODO: displaying update errors is currently prevented by the
    #   lack of an appropriate updated event in ryvencore.
    #   Update: there is an updating event now.

    # def on_updated(self, inp):
    #     if self.error_during_update:
    #         # an error should prevent an update event, so if we
    #         # are here, the update was successful
    #         self.self.error_during_update = False
    #         self.item.remove_error_message()
    #     self.updated.emit()
    #
    def _on_update_error(self, e):
    #     self.item.display_error(e)
    #     self.error_during_update = True
        self.update_error.emit(e)

    def _on_updating(self, inp: int):
        # update input widget
        if inp != -1 and self.item.inputs[inp].widget is not None:
            o = self.node.flow.connected_output(self.node.inputs[inp])
            if o is not None:
                self.item.inputs[inp].widget.val_update_event(o.val)

        self.updating.emit()

    def _on_new_input_added(self, _, index, inp):
        if not self._next_input_widgets.empty():
            self.input_widgets[inp] = self._next_input_widgets.get()
        self.input_added.emit(index, inp)

    def _on_new_output_added(self, _, index, out):
        self.output_added.emit(index, out)

    def _on_input_removed(self, _, index, inp):
        self.input_removed.emit(index, inp)

    def _on_output_removed(self, _, index, out):
        self.output_removed.emit(index, out)

    """
    actions
    
    TODO: move actions to ryvencore?
    """

    def _init_default_actions(self):
        """
        Returns the default actions every node should have
        """
        return {
            'update shape': {'method': self.update_shape},
            'hide unconnected ports': {'method': self.hide_unconnected_ports},
            'change title': {'method': self.change_title},
        }

    def _deserialize_actions(self, actions_data):
        """
        Recursively reconstructs the actions dict from the serialized version
        """

        def _transform(actions_data: dict):
            """
            Mutates the actions_data argument by replacing the method names
            with the actual methods. Doesn't modify the original dict.
            """
            new_actions = {}
            for key, value in actions_data.items():
                if key == 'method':
                    try:
                        value = getattr(self, value)
                    except AttributeError:
                        print(f'Warning: action method "{value}" not found in node "{self.node.title}", skipping.')
                elif isinstance(value, dict):
                    value = _transform(value)
                new_actions[key] = value
            return new_actions

        return _transform(actions_data)

    def _serialize_actions(self, actions):
        """
        Recursively transforms the actions dict into a JSON-compatible dict
        by replacing methods with their name. Doesn't modify the original dict.
        """

        def _transform(actions: dict):
            new_actions = {}
            for key, value in actions.items():
                if key == 'method':
                    new_actions[key] = value.__name__
                elif isinstance(value, dict):
                    new_actions[key] = _transform(value)
                else:
                    new_actions[key] = value
            return new_actions

        return _transform(actions)

    """
    serialization
    """

    def data(self):
        return {
            'actions': self._serialize_actions(self.actions),
            'display title': self.display_title,
            'inspector widget': self.inspector_widget.get_state(),
        }

    def load(self, data):
        if 'actions' in data:   # otherwise keep default
            self.actions = self._deserialize_actions(data['actions'])
        if 'display title' in data:
            self.display_title = data['display title']
        if 'special actions' in data:   # backward compatibility
            self.actions = self._deserialize_actions(data['special actions'])
        if 'inspector widget' in data:
            self.inspector_widget.set_state(data['inspector widget'])

    """
    GUI access methods
    """

    def set_display_title(self, t: str):
        self.display_title = t
        self.update_shape()

    def flow_view(self):
        return self.item.flow_view

    def main_widget(self):
        """Returns the main_widget object, or None if the item doesn't exist (yet)"""

        return self.item.main_widget

    def attach_input_widgets(self, widget_names: List[str]):
        """Attaches the input widget to the next created input."""

        for w in widget_names:
            self._next_input_widgets.queue(w)

    def input_widget(self, index: int):
        """Returns a reference to the widget of the corresponding input"""

        return self.item.inputs[index].widget

    def session_stylesheet(self):
        return self.session_gui.design.global_stylesheet

    def update_shape(self):
        """Causes recompilation of the whole shape of the GUI item."""

        self.update_shape_triggered.emit()

    def hide_unconnected_ports(self):
        """Hides all ports that are not connected to anything."""

        del self.actions['hide unconnected ports']
        self.actions['show unconnected ports'] = {'method': self.show_unconnected_ports}
        self.hide_unconnected_ports_triggered.emit()

    def show_unconnected_ports(self):
        """Shows all ports that are not connected to anything."""

        del self.actions['show unconnected ports']
        self.actions['hide unconnected ports'] = {'method': self.hide_unconnected_ports}
        self.show_unconnected_ports_triggered.emit()

    def change_title(self):
        from qtpy.QtWidgets import QDialog, QVBoxLayout, QLineEdit

        class ChangeTitleDialog(QDialog):
            def __init__(self, title):
                super().__init__()
                self.new_title = None
                self.setLayout(QVBoxLayout())
                self.line_edit = QLineEdit(title)
                self.layout().addWidget(self.line_edit)
                self.line_edit.returnPressed.connect(self.return_pressed)

            def return_pressed(self):
                self.new_title = self.line_edit.text()
                self.accept()

        d = ChangeTitleDialog(self.display_title)
        d.exec_()
        if d.new_title:
            self.set_display_title(d.new_title)
