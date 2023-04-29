"""
This module provides some frequently useful convenience input widgets for nodes.
It replaces what was previously the dtypes system.
"""

from ryvencore import Data

from ryvencore_qt import NodeInputWidget

from qtpy.QtWidgets import QLineEdit
from qtpy.QtGui import QFont, QFontMetrics


class Builder:
    """
    Provides functions for creating parametrized input widgets.
    """

    @staticmethod
    def evaled_line_edit(size='m', descr: str = '', resizing: bool = True):
        """
        Creates a line edit input widget which evaluates its input.
        :param descr: the description of the input
        :param size: 's', 'm' or 'l'
        """

        if size == 's':
            base_width = 30
        elif size == 'm':
            base_width = 70
        else:  # size == 'l':
            base_width = 150
        max_width = base_width * 3 if resizing else base_width

        class StdInpWidget_EvaledLineEdit(NodeInputWidget, QLineEdit):
            def __init__(self, params):
                NodeInputWidget.__init__(self, params)
                QLineEdit.__init__(self)

                # set size
                self.base_width = base_width
                self.max_width = max_width
                self.setFixedWidth(self.base_width)

                # font
                self.setFont(QFont('source code pro', 10))
                self.fm = QFontMetrics(self.font())

                # tooltip
                self.setToolTip(self.__doc__)

                self.textChanged.connect(self.text_changed)
                self.editingFinished.connect(self.editing_finished)

            def text_changed(self, new_text):
                """Manages resizing of the widget to content."""
                if not resizing:
                    return

                text_width = self.fm.width(new_text)
                new_width = text_width + 15  # add some buffer
                self.setFixedWidth(min(
                    max(new_width, self.base_width),
                    self.max_width
                ))
                self.node_gui.update_shape()

            def editing_finished(self):
                """Updates the node input."""
                self.update_node_input(self.val)

            @property
            def val(self) -> Data:
                try:
                    return Data(eval(self.text()))
                except:
                    return Data(self.text())

            def val_update_event(self, val: Data):
                try:
                    self.setText(str(val.payload))
                except:
                    self.setText("<can't stringify>")

            def get_state(self) -> dict:
                return {'text': self.val}

            def set_state(self, data: dict):
                # just show value, do not update node input
                self.val_update_event(data['text'])

        StdInpWidget_EvaledLineEdit.__doc__ = descr

        return StdInpWidget_EvaledLineEdit

    @staticmethod
    def str_line_edit(size='m', descr: str = '', resizing: bool = True):
        """
        Creates a line edit input widget which evaluates its input.
        :param descr: the description of the input
        :param size: 's', 'm' or 'l'
        """

        if size == 's':
            base_width = 30
        elif size == 'm':
            base_width = 70
        else:  # size == 'l':
            base_width = 150
        max_width = base_width * 3 if resizing else base_width

        class StdInpWidget_StrLineEdit(NodeInputWidget, QLineEdit):
            def __init__(self, params):
                NodeInputWidget.__init__(self, params)
                QLineEdit.__init__(self)

                # set size
                self.base_width = base_width
                self.max_width = max_width
                self.setFixedWidth(self.base_width)

                # font
                self.setFont(QFont('source code pro', 10))
                self.fm = QFontMetrics(self.font())

                # tooltip
                self.setToolTip(self.__doc__)

                self.textChanged.connect(self.text_changed)
                self.editingFinished.connect(self.editing_finished)

            def text_changed(self, new_text):
                """Manages resizing of the widget to content."""
                if not resizing:
                    return

                text_width = self.fm.width(new_text)
                new_width = text_width + 15  # add some buffer
                self.setFixedWidth(min(
                    max(new_width, self.base_width),
                    self.max_width
                ))
                self.node_gui.update_shape()

            def editing_finished(self):
                """Updates the node input."""
                self.update_node_input(self.val)

            @property
            def val(self) -> Data:
                return Data(self.text())

            def val_update_event(self, val: Data):
                try:
                    self.setText(str(val.payload))
                except:
                    self.setText("<can't stringify>")

            def get_state(self) -> dict:
                return {'text': self.val}

            def set_state(self, data: dict):
                # just show value, do not update node input
                self.val_update_event(data['text'])

        StdInpWidget_StrLineEdit.__doc__ = descr

        return StdInpWidget_StrLineEdit
