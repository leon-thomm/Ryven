"""The base classes for node custom widgets for nodes."""
from ryvencore import Data


class NodeMainWidget:
    """Base class for the main widget of a node."""

    def __init__(self, params):
        self.node, self.node_item, self.node_gui = params

    def get_state(self) -> dict:
        """
        *VIRTUAL*

        Return the state of the widget, in a (pickle) serializable format.
        """
        data = {}
        return data

    def set_state(self, data: dict):
        """
        *VIRTUAL*

        Set the state of the widget, where data corresponds to the dict
        returned by get_state().
        """
        pass

    def update_node(self):
        self.node.update()

    def update_node_shape(self):
        self.node_item.update_shape()


class NodeInputWidget:
    """Base class for the input widget of a node."""

    def __init__(self, params):
        self.input, self.input_item, self.node, self.node_gui, self.position = \
            params

    def get_state(self) -> dict:
        """
        *VIRTUAL*

        Return the state of the widget, in a (pickle) serializable format.
        """
        data = {}
        return data

    def set_state(self, data: dict):
        """
        *VIRTUAL*

        Set the state of the widget, where data corresponds to the dict
        returned by get_state().
        """
        pass

    def val_update_event(self, val: Data):
        """
        *VIRTUAL*

        Called when the input's value is updated through a connection.
        This can be used to represent the value in the widget.
        The widget is disabled when the port is connected.
        """
        pass

    # API methods

    def update_node_input(self, val: Data, silent=False):
        """
        Update the input's value and update the node.
        """
        self.input.default = val
        if not silent:
            self.input.node.update(self.node.inputs.index(self.input))

    def update_node(self):
        self.node.update(self.node.inputs.index(self.input))

    def update_node_shape(self):
        self.node_gui.update_shape()
