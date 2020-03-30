from PySide2.QtWidgets import QGraphicsItem, QLineEdit, QSpinBox
from PySide2.QtCore import Qt, QRectF, QPointF
from PySide2.QtGui import QColor, QBrush, QPen, QFontMetricsF, QFont

from custom_src.GlobalAccess import GlobalStorage

from custom_src.FlowProxyWidget import FlowProxyWidget


class PortInstance:
    def __init__(self, parent_node_instance, direction, type_='', label_str='',
                 configuration=None, widget_type='', widget_name=None, widget_pos=''):
        # general attributes
        self.val = None
        self.parent_node_instance = parent_node_instance
        # self.parent_port = parent_port NOT ANYMORE BRAH!
        self.direction = direction
        self.type_ = type_
        # GlobalStorage.debug('label_str:', label_str)
        self.label_str = label_str
        self.connected_port_instances = []
        self.proxy: FlowProxyWidget = None
        self.widget_type = widget_type
        self.widget_name = widget_name
        self.widget_pos = widget_pos

        self.waiting_for_data = False

        self.width = -1
        self.height = -1

        self.widget: 'StdLineEdit_PortInstanceWidget' = None

        if configuration:
            self.type_ = configuration['type']
            self.label_str = configuration['label']
            # GlobalStorage.debug('label str now:', self.label_str)

            if direction == 'input':
                if configuration['has widget']:
                    self.widget_type = configuration['widget type']
                    self.widget_name = configuration['widget name']
                    self.widget_pos = configuration['widget position']

                    if configuration['widget data'] != None:
                        self.create_widget()
                        self.widget.set_data(configuration['widget data'])
        else:
            self.create_widget()

        self.gate = PortInstanceGate(self, parent_node_instance)
        self.label = PortInstanceLabel(self, parent_node_instance)
        # self.compute_size()

    def exec(self):    # OUTPUT; call from inside
        for cpi in self.connected_port_instances:
            cpi.update()

    def update(self):  # INPUT; call from outside
        if (self.parent_node_instance.is_active() and self.type_ == 'exec') or \
           not self.parent_node_instance.is_active():
            self.parent_node_instance.update(self.parent_node_instance.inputs.index(self))


    def set_val(self, val):  # INPUT DATA; call from inside
        GlobalStorage.debug('setting value of', self.direction, 'port of', self.parent_node_instance.parent_node.title,
                            'NodeInstance to', val)
        if self.val is val:  # no update if value didn't change
            return

        self.val = val
        self.updated_val()

    def get_val(self):  # DATA; call from inside OR outside (see below)
        GlobalStorage.debug('get value in', self.direction, 'port instance',
                            self.parent_node_instance.inputs.index(
                                self) if self.direction == 'input' else self.parent_node_instance.outputs.index(self),
                            'of', self.parent_node_instance.parent_node.title)
        GlobalStorage.debug('my value is', self.val)
        if self.direction == 'input':
            if len(self.connected_port_instances) == 0:
                if self.widget:
                    return self.widget.get_val()
                else:
                    return None
            else:
                GlobalStorage.debug('calling connected port for val')
                return self.connected_port_instances[0].get_val()
        elif self.direction == 'output':
            GlobalStorage.debug('returning val directly')
            if self.parent_node_instance.gen_data_on_request:
                self.parent_node_instance.update()
            return self.val

    def updated_val(self):  # OUTPUT DATA; call from inside
        for cpi in self.connected_port_instances:
            cpi.update()

    def create_widget(self, configuration=None):
        if self.direction == 'input' and (
                self.type_ and self.type_ == 'data' or configuration and configuration['type'] == 'data'):
            # self.widget = None
            if self.widget_type == 'None':
                return
            elif self.widget_type == 'std line edit':
                self.widget = StdLineEdit_PortInstanceWidget(self, self.parent_node_instance)
            elif self.widget_type == 'std spin box':
                self.widget = StdSpinBox_PortInstanceWidget(self, self.parent_node_instance)
            elif self.widget_type == 'custom widget':
                self.widget = self.get_input_widget_class(self.widget_name)(self, self.parent_node_instance)
            self.proxy = FlowProxyWidget(self.parent_node_instance.flow, self.parent_node_instance)
            self.proxy.setWidget(self.widget)

    def get_input_widget_class(self, widget_name):
        custom_node_input_widget_classes = self.parent_node_instance.flow.parent_script.main_window.custom_node_input_widget_classes
        widget_class = custom_node_input_widget_classes[self.parent_node_instance.parent_node][widget_name]
        return widget_class

    def compute_size_and_positions(self):
        # GlobalStorage.debug('computing size in', self.parent_node_instance.parent_node.title)
        self.width = 0
        self.height = 0

        gate_label_buffer = 10  # adds space between the gate and the label (vertical)
        label_widget_buffer = 10

        label_FM = QFontMetricsF(self.label.font)

        self.width = self.gate.width + self.label.width + gate_label_buffer
        self.height = self.gate.height if self.gate.height > self.label.height else self.label.height
        self.height *= 1.3

        if self.direction == 'input':
            if self.widget:
                widget_width = self.widget.width()
                widget_height = self.widget.height()
                if self.widget_pos == 'under':
                    self.width = widget_width if widget_width > self.width else self.width
                    self.height += widget_height
                    upper_row_height = self.gate.height if self.gate.height > self.label.height else self.label.height
                    self.widget.port_local_pos = QPointF(-self.width / 2 + self.widget.width() / 2,
                                                         -self.height / 2 + upper_row_height + self.widget.height() / 2)  # - self.widget.height()/2)
                    self.gate.port_local_pos = QPointF(-self.width / 2 + self.gate.width / 2,
                                                       -self.height / 2 + upper_row_height / 2)
                    self.label.port_local_pos = QPointF(
                        -self.width / 2 + self.gate.width + gate_label_buffer + self.label.width / 2,
                        -self.height / 2 + upper_row_height / 2)
                elif self.widget_pos == 'besides':
                    self.width += label_widget_buffer + widget_width
                    self.height = self.height if self.height > self.widget.height() else self.widget.height()
                    self.widget.port_local_pos = QPointF(-self.width / 2 + self.gate.width + gate_label_buffer +
                                                         self.label.width + label_widget_buffer + self.widget.width() / 2,
                                                         0)
                    self.gate.port_local_pos = QPointF(-self.width / 2 + self.gate.width / 2, 0)
                    self.label.port_local_pos = QPointF(
                        -self.width / 2 + self.gate.width + gate_label_buffer + self.label.width / 2, 0)
                if self.widget.width() > self.width:
                    self.width = self.widget.width()

            else:
                self.gate.port_local_pos = QPointF(-self.width / 2 + self.gate.width / 2, 0)
                self.label.port_local_pos = QPointF(
                    -self.width / 2 + self.gate.width + gate_label_buffer + self.label.width / 2, 0)
        elif self.direction == 'output':
            self.gate.port_local_pos = QPointF(+self.width / 2 - self.gate.width / 2, 0)
            self.label.port_local_pos = QPointF(
                +self.width / 2 - self.gate.width - gate_label_buffer - self.label.width / 2, 0)

    def connected(self):
        if self.widget:
            self.widget.setEnabled(False)
        if self.direction == 'input' and self.type_ == 'data':
            self.update()

    def disconnected(self):
        if self.widget:
            self.widget.setEnabled(True)

    def get_json_data(self):
        data_dict = {'label': self.label_str,
                     'type': self.type_}

        if self.direction == 'input':
            has_widget = True if self.widget else False
            data_dict['has widget'] = has_widget
            if has_widget:
                data_dict['widget type'] = self.widget_type
                data_dict['widget name'] = self.widget_name
                data_dict['widget data'] = None if self.type_ == 'exec' else self.widget.get_data()
                data_dict['widget position'] = self.widget_pos

        return data_dict


# CONTENTS -------------------------------------------------------------------------------------------------------------

class PortInstanceGate(QGraphicsItem):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(PortInstanceGate, self).__init__(parent_node_instance)
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        self.width = 15
        self.height = 15
        self.port_local_pos = None

    def boundingRect(self):
        return QRectF(-self.width / 2, -self.height / 2, self.width, self.height)

    def paint(self, painter, option, widget=None):
        if GlobalStorage.storage['design style'] == 'dark std':
            color = '#2E688C' if self.parent_port_instance.type_ == 'data' else '#3880ad'
            brush = QBrush(QColor(color))
            painter.setBrush(brush)
            painter.setPen(Qt.NoPen)
        elif GlobalStorage.storage['design style'] == 'dark tron':
            color = ''
            if self.parent_port_instance.type_ == 'exec':
                color = '#FFFFFF'
            elif self.parent_port_instance.type_ == 'data':
                color = self.parent_node_instance.parent_node.color
            pen = QPen(color)
            pen.setWidth(2)
            painter.setPen(pen)
            if len(self.parent_port_instance.connected_port_instances) > 0:
                c = self.parent_node_instance.parent_node.color
                r = c.red()
                g = c.green()
                b = c.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)
        painter.drawEllipse(QPointF(0, 0), self.width / 2, self.height / 2)


class PortInstanceLabel(QGraphicsItem):
    # parent_port_instance = None #: PortInstance
    # parent_node_instance = None #: NodeInstance

    def __init__(self, parent_port_instance, parent_node_instance):
        super(PortInstanceLabel, self).__init__(parent_node_instance)
        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance

        self.font = QFont("Source Code Pro", 10, QFont.Bold)
        font_metrics = QFontMetricsF(self.font)
        self.width = font_metrics.width(self.get_longest_line(self.parent_port_instance.label_str))
        self.height = font_metrics.height() * (self.parent_port_instance.label_str.count('\n') + 1)
        # GlobalStorage.debug('label height:', self.height)
        # GlobalStorage.debug('\\n count:', self.parent_port_instance.label_str.count('\n'))
        # GlobalStorage.debug(self.parent_port_instance.label_str)
        self.port_local_pos = None

    def get_longest_line(self, s: str):
        lines = s.split('\n')
        lines = [line.replace('\n', '') for line in lines]
        longest_line_found = ''
        for line in lines:
            if len(line) > len(longest_line_found):
                longest_line_found = line
        return line

    def boundingRect(self):
        return QRectF(-self.width / 2, -self.height / 2, self.width, self.height)

    def paint(self, painter, option, widget=None):
        painter.setBrush(Qt.NoBrush)
        c = ''
        if GlobalStorage.storage['design style'] == 'dark std':
            c = '#ffffff'
        elif GlobalStorage.storage['design style'] == 'dark tron':
            if self.parent_port_instance.type_ == 'exec':
                c = '#ffffff'
            elif self.parent_port_instance.type_ == 'data':
                c = self.parent_node_instance.parent_node.color
        pen = QPen(c)
        painter.setPen(pen)
        painter.setFont(self.font)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.parent_port_instance.label_str)
        # GlobalStorage.debug('painting: ',self.parent_port_instance.parent_port.label, painter)
        # GlobalStorage.debug(self.scene())


# class PortInstanceWidget:
#     def __init__(self, parent_port_instance, parent_node_instance):
#         self.parent_port_instance = parent_port_instance
#         self.parent_node_instance = parent_node_instance
#         self.port_local_pos = None
#
#     def get_data(self):
#         pass
#
#     def set_data(self, data):
#         pass


class StdLineEdit_PortInstanceWidget(QLineEdit):
    def __init__(self, parent_port_instance, parent_node_instance):
        # PortInstanceWidget.__init__(self)
        # QLineEdit.__init__(self)
        super(StdLineEdit_PortInstanceWidget, self).__init__()

        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        self.port_local_pos = None

        self.setFixedWidth(70)
        self.setFixedHeight(25)
        self.setPlaceholderText('')
        self.setStyleSheet("""
            QLineEdit{
                border-radius: 10px;
                background-color: transparent;
                border: 1px solid #404040;
                color: #aaaaaa;
                padding: 3px;
            }
        """)
        f = self.font()
        f.setPointSize(10)
        self.setFont(f)
        self.editingFinished.connect(self.editing_finished)

    def editing_finished(self):
        self.parent_node_instance.update(self.parent_node_instance.inputs.index(self.parent_port_instance))

    def removing(self):
        pass

    def get_val(self):
        val = None
        try:
            val = eval(self.text())
        except Exception as e:
            # type(eval(json.dumps(self.text()))) could be 'dict' <- need that for typing in dicts later if I want to
            val = self.text()
        return val

    def get_data(self):
        return self.text()

    def set_data(self, data):
        if type(data) == str:
            self.setText(data)


class StdSpinBox_PortInstanceWidget(QSpinBox):
    def __init__(self, parent_port_instance, parent_node_instance):
        # PortInstanceWidget.__init__(self)
        # QLineEdit.__init__(self)
        super(StdSpinBox_PortInstanceWidget, self).__init__()

        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        self.port_local_pos = None

        self.setFixedWidth(50)
        self.setFixedHeight(25)
        self.setStyleSheet("""
            QSpinBox {
                color: white;
                background: transparent;
            }
        """)
        self.setMaximum(1000000)
        self.editingFinished.connect(self.editing_finished)

    def editing_finished(self):
        self.parent_node_instance.update(self.parent_node_instance.inputs.index(self.parent_port_instance))

    def removing(self):
        pass

    def get_val(self):
        return self.value()

    def get_data(self):
        return self.value()

    def set_data(self, data):
        self.setValue(data)