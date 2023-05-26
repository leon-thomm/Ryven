"""
This module provides some frequently useful convenience input widgets for nodes.
It replaces what was previously the dtypes system.
"""
from typing import Tuple

from ryvencore import Data

from ryvencore_qt import NodeInputWidget

from qtpy.QtWidgets import QLineEdit, QSpinBox, QCheckBox, QSlider
from qtpy.QtGui import QFont, QFontMetrics


class Builder:
    """
    Provides functions for creating parametrized input widgets.
    """

    @staticmethod
    def evaled_line_edit(init=None, size='m', descr: str = '', resizing: bool = True, data_type: type[Data] = Data):
        """
        Creates a line edit input widget which evaluates its input.
        :param init: the initial value shown in the widget
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

                # initial value
                self.setText(str(init))

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
            def val(self) -> data_type:
                try:
                    return data_type(eval(self.text()))
                except:
                    return data_type(self.text())

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
    def str_line_edit(init: str = '', size='m', descr: str = '', resizing: bool = True, data_type: type[Data] = Data):
        """
        Creates a line edit input widget which evaluates its input.
        :param init: the initial value shown in the widget
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

                # initial value
                self.setText(str(init))

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
            def val(self) -> data_type:
                return data_type(self.text())

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

    @staticmethod
    def int_spinbox(init: int = 0, range: Tuple[int, int] = (0, 99), descr: str = '', data_type: type[Data] = Data):
        """
        Creates a spinbox input widget for integers.
        :param init: the initial value shown in the widget
        :param range: the range of the spinbox
        :param descr: the description of the input
        """

        class StdInpWidget_IntSpinBox(NodeInputWidget, QSpinBox):
            def __init__(self, params):
                NodeInputWidget.__init__(self, params)
                QSpinBox.__init__(self)

                # tooltip
                self.setToolTip(self.__doc__)

                # initial value and rage
                self.setValue(init)
                self.setRange(*range)

                self.valueChanged.connect(self.value_changed)

            @property
            def val(self) -> data_type:
                return data_type(self.value())

            def value_changed(self, _):
                """Updates the node input."""
                self.update_node_input(self.val)

            def val_update_event(self, val: Data):
                if not isinstance(val.payload, int):
                    # TODO: error handling, show error in widget somehow
                    return

                self.setValue(val.payload)

            def get_state(self) -> dict:
                return {'value': self.val}

            def set_state(self, data: dict):
                # just show value, do not update node input
                self.val_update_event(data['value'])

        StdInpWidget_IntSpinBox.__doc__ = descr

        return StdInpWidget_IntSpinBox

    @staticmethod
    def int_slider(init: int = 0, range: Tuple[int, int] = (0, 10), descr: str = '', data_type: type[Data] = Data):
        """
        Creates a slider input widget for ints.
        :param init: the initial value shown in the widget
        :param range: the range of the slider
        :param descr: the description of the input
        """

        class StdInpWidget_IntSlider(NodeInputWidget, QSlider):
            def __init__(self, params):
                NodeInputWidget.__init__(self, params)
                QSlider.__init__(self)

                # tooltip
                self.setToolTip(self.__doc__)

                # initial value and rage
                self.setValue(init)
                self.setRange(*range)

                self.valueChanged.connect(self.value_changed)

            @property
            def val(self) -> data_type:
                return data_type(self.value())

            def value_changed(self, _):
                """Updates the node input."""
                self.update_node_input(self.val)

            def val_update_event(self, val: Data):
                if not isinstance(val.payload, int):
                    return

                self.setValue(val.payload)

            def get_state(self) -> dict:
                return {'value': self.val}

            def set_state(self, data: dict):
                # just show value, do not update node input
                self.val_update_event(data['value'])

        StdInpWidget_IntSlider.__doc__ = descr

        return StdInpWidget_IntSlider

    @staticmethod
    def bool_checkbox(init: bool = False, descr: str = '', data_type: type[Data] = Data):
        """
        Creates a checkbox input widget for booleans.
        :param init: the initial value shown in the widget
        :param descr: the description of the input
        """

        class StdInpWidget_BoolCheckBox(NodeInputWidget, QCheckBox):
            def __init__(self, params):
                NodeInputWidget.__init__(self, params)
                QCheckBox.__init__(self)

                # tooltip
                self.setToolTip(self.__doc__)

                # initial value
                self.setChecked(init)

                self.stateChanged.connect(self.state_changed)

            @property
            def val(self) -> data_type:
                return data_type(self.isChecked())

            def state_changed(self, _):
                """Updates the node input."""
                self.update_node_input(self.val)

            def val_update_event(self, val: Data):
                if not isinstance(val.payload, bool):
                    return

                self.setChecked(val.payload)

            def get_state(self) -> dict:
                return {'value': self.val}

            def set_state(self, data: dict):
                # just show value, do not update node input
                self.val_update_event(data['value'])

        StdInpWidget_BoolCheckBox.__doc__ = descr

        return StdInpWidget_BoolCheckBox
