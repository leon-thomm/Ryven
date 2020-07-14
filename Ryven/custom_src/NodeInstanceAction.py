from PySide2.QtCore import Signal
from PySide2.QtWidgets import QAction


class NodeInstanceAction(QAction):
    """A custom implementation of QAction that additionally stores transmitted 'data' which can be intuitively used
    in subclasses f.ex. to determine the exact source of the action triggered. For more info see GitHub docs.
    It shall not be a must to use the data parameter though. For that reason, there are two different signals,
    one that triggers with transmitted data, one without.
    So, if a special action does not have 'data', the connected method does not need to have a data parameter.
    Both signals get connected to the target method but only if data isn't None, the signal with the data parameter
    is used."""

    triggered_with_data = Signal(object)
    triggered_without_data = Signal()

    def __init__(self, text, menu, data=None):
        super(NodeInstanceAction, self).__init__(text=text, parent=menu)

        self.data = data
        self.triggered.connect(self.triggered_)  # yeah, I think that's ugly but I didn't find a nicer way; it works

    def triggered_(self):
        if self.data is not None:
            self.triggered_with_data.emit(self.data)
        else:
            self.triggered_without_data.emit()