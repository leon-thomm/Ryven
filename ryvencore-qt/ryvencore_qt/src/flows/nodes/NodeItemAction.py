from qtpy.QtCore import Signal
from qtpy.QtWidgets import QAction


class NodeItemAction(QAction):
    """A custom implementation of QAction that additionally stores transmitted 'data' which can be intuitively used
    in subclasses f.ex. to determine the exact source of the action triggered. For more info see GitHub docs.
    It shall not be a must to use the data parameter though. For that reason, there are two different signals,
    one that triggers with transmitted data, one without.
    So, if a special action does not have 'data', the connected method does not need to have a data parameter.
    Both signals get connected to the target method but only if data isn't None, the signal with the data parameter
    is used."""

    triggered_with_data = Signal(object, object)
    triggered_without_data = Signal(object)

    def __init__(self, node_gui, text, method, menu, data=None):
        super(NodeItemAction, self).__init__(text=text, parent=menu)

        self.node_gui = node_gui
        self.data = data
        self.method = method
        self.triggered.connect(self.triggered_)

    def triggered_(self):
        if self.data is not None:
            self.grab_method()(self.data)
        else:
            self.grab_method()()

    def grab_method(self):
        # the method object could have changed since the action was created
        return getattr(self.node_gui, self.method.__name__)
