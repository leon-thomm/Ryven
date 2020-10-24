from PySide2.QtCore import QObject, Signal


class Variable(QObject):
    """Represents a variable. Unfortunately, I can't accomplish the same with a simple dict ({name: val}) in Script,
    because I need a ref to an object in VarsList_VarWidget to always show the current value and stuff"""

    # val_changed = Signal(object)

    def __init__(self, name='', val=None):
        super(Variable, self).__init__()

        self.name = name
        self.val = val
        # self.val_changed.emit(val)
