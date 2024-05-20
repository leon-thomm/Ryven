"""
This module provides some frequently useful convenience input widgets for nodes.
It replaces what was previously the dtypes system.
"""
from typing import Tuple

from ryvencore import Data

from ryvencore_qt import NodeInputWidget

from qtpy.QtWidgets import QLineEdit, QSpinBox, QCheckBox, QSlider
from qtpy.QtGui import QFont, QFontMetrics, Qt


class StdInputWidgetBase(NodeInputWidget):
    def __init__(self, params):
        super().__init__(params)

        self._prevent_update = PreventUpdateCtx(False)

    @property
    def val(self) -> Data:
        raise NotImplementedError

    def load_from(self, val: Data):
        raise NotImplementedError

    def on_widget_val_changed(self, val: Data):
        """
        This will update the input's default value, and also update
        the node unless it is called in a `with self._prevent_update`
        block.
        """
        self.update_node_input(val, silent=self._prevent_update.blocked)

    def get_state(self) -> dict:
        return {'val': self.val}

    def set_state(self, data: dict):
        with self._prevent_update:
            self.load_from(data['val'])


class PreventUpdateCtx:
    def __init__(self, initial: bool):
        self._blocked: bool = initial

    @property
    def blocked(self) -> bool:
        return self._blocked

    def __enter__(self):
        self._blocked = True

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._blocked = False


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

        class StdInpWidget_EvaledLineEdit(StdInputWidgetBase, QLineEdit):
            def __init__(self, params):
                StdInputWidgetBase.__init__(self, params)
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
                self.returnPressed.connect(self.return_pressed)

                # initial value
                with self._prevent_update:
                    self.setText(str(init))

            def return_pressed(self):
                self.on_widget_val_changed(self.val)

            def text_changed(self, new_text):
                """Manages resizing of the widget to content."""
                if resizing:
                    text_width = self.fm.width(new_text)
                    new_width = text_width + 15  # add some buffer
                    self.setFixedWidth(min(
                        max(new_width, self.base_width),
                        self.max_width
                    ))
                    self.node_gui.update_shape()
                self.on_widget_val_changed(self.val)

            @property
            def val(self) -> Data:
                try:
                    return data_type(eval(self.text()))
                except:
                    return data_type(self.text())

            def load_from(self, val: Data):
                with self._prevent_update:
                    self.setText(str(val.payload))

            def val_update_event(self, val: Data):
                # represent incoming data
                try:
                    with self._prevent_update:
                        self.setText(str(val.payload))
                except:
                    self.setText("<can't stringify>")

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

        class StdInpWidget_StrLineEdit(StdInputWidgetBase, QLineEdit):
            def __init__(self, params):
                StdInputWidgetBase.__init__(self, params)
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
                self.returnPressed.connect(self.return_pressed)

                # initial value
                with self._prevent_update:
                    self.setText(str(init))

            def return_pressed(self):
                self.on_widget_val_changed(self.val)

            def text_changed(self, new_text):
                """Manages resizing of the widget to content."""
                if resizing:
                    text_width = self.fm.width(new_text)
                    new_width = text_width + 15  # add some buffer
                    self.setFixedWidth(min(
                        max(new_width, self.base_width),
                        self.max_width
                    ))
                    self.node_gui.update_shape()
                self.on_widget_val_changed(self.val)

            @property
            def val(self) -> Data:
                return data_type(self.text())

            def load_from(self, val: Data):
                with self._prevent_update:
                    self.setText(str(val.payload))

            def val_update_event(self, val: Data):
                # represent incoming data
                try:
                    with self._prevent_update:
                        self.setText(str(val.payload))
                except:
                    self.setText("<can't stringify>")

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

        class StdInpWidget_IntSpinBox(StdInputWidgetBase, QSpinBox):

            def __init__(self, params):
                StdInputWidgetBase.__init__(self, params)
                QSpinBox.__init__(self)

                # there is no 'valueEdited' signal, only a 'valueChanged' signal
                # so we need to block the signal when a new value is coming from
                # a connection
                self._prevent_update = PreventUpdateCtx(False)

                # tooltip
                self.setToolTip(self.__doc__)

                self.valueChanged.connect(self.value_changed)

                # initial value and rage
                with self._prevent_update:
                    self.setRange(*range)
                    self.setValue(init)


            @property
            def val(self) -> Data:
                return data_type(self.value())

            def load_from(self, val: Data):
                with self._prevent_update:
                    self.setValue(val.payload)

            def value_changed(self, _):
                self.on_widget_val_changed(self.val)

            def val_update_event(self, val: Data):
                if isinstance(val.payload, int):
                    with self._prevent_update:
                        self.setValue(val.payload)

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

        class StdInpWidget_IntSlider(StdInputWidgetBase, QSlider):
            def __init__(self, params):
                StdInputWidgetBase.__init__(self, params)
                QSlider.__init__(self, Qt.Horizontal)

                # tooltip
                self.setToolTip(self.__doc__)

                self.valueChanged.connect(self.value_changed)

                # initial value and rage
                with self._prevent_update:
                    self.setRange(*range)
                    self.setValue(init)

            @property
            def val(self) -> Data:
                return data_type(self.value())

            def load_from(self, val: Data):
                with self._prevent_update:
                    self.setValue(val.payload)

            def value_changed(self, _):
                self.on_widget_val_changed(self.val)

            def val_update_event(self, val: Data):
                if isinstance(val.payload, int):
                    self.setValue(val.payload)

        StdInpWidget_IntSlider.__doc__ = descr

        return StdInpWidget_IntSlider

    @staticmethod
    def bool_checkbox(init: bool = False, descr: str = '', data_type: type[Data] = Data):
        """
        Creates a checkbox input widget for booleans.
        :param init: the initial value shown in the widget
        :param descr: the description of the input
        """

        class StdInpWidget_BoolCheckBox(StdInputWidgetBase, QCheckBox):
            def __init__(self, params):
                StdInputWidgetBase.__init__(self, params)
                QCheckBox.__init__(self)

                # tooltip
                self.setToolTip(self.__doc__)

                self.stateChanged.connect(self.state_changed)

                # initial value
                with self._prevent_update:
                    self.setChecked(init)

            @property
            def val(self) -> Data:
                return data_type(self.isChecked())

            def load_from(self, val: Data):
                with self._prevent_update:
                    self.setChecked(val.payload)

            def state_changed(self, _):
                self.on_widget_val_changed(self.val)

            def val_update_event(self, val: Data):
                if isinstance(val.payload, bool):
                    with self._prevent_update:
                        self.setChecked(val.payload)

        StdInpWidget_BoolCheckBox.__doc__ = descr

        return StdInpWidget_BoolCheckBox
