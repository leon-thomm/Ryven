from PySide2.QtWidgets import QGraphicsItem, QLineEdit, QSpinBox, QStyle, QGraphicsGridLayout, QGraphicsWidget, \
    QGraphicsLayoutItem, QSizePolicy
from PySide2.QtCore import Qt, QRectF, QPointF, QSizeF
from PySide2.QtGui import QColor, QBrush, QPen, QFontMetricsF, QFont, QPainterPath, QFontMetrics

from custom_src.global_tools.Debugger import Debugger
from custom_src.GlobalAttributes import Design, Algorithm
from custom_src.global_tools.strings import get_longest_line, shorten

from custom_src.FlowProxyWidget import FlowProxyWidget
from custom_src.retain import M


class PortInstance(QGraphicsGridLayout):
    """The PortInstance class represents input-as well as output-instances of a NI. It wasn't really necessary yet, but
    I will probably subclass it later into InputPortInstance and OutputPortInstance - so far both are just
    PortInstances."""

    def __init__(self, parent_node_instance, direction, type_='', label_str='',
                 widget_name=None, widget_pos=''):
        super(PortInstance, self).__init__()

        # GENERAL ATTRIBUTES
        self.val = None
        self.parent_node_instance = parent_node_instance
        self.direction = direction
        self.type_ = type_
        self.label_str = label_str
        self.connected_port_instances = []  # connections stored here

        # CONTENTS
        # widget
        self.widget: 'StdLineEdit_PortInstanceWidget' = None
        self.proxy: FlowProxyWidget = None
        self.widget_name = widget_name
        self.widget_pos = widget_pos

        # gate/pin
        self.gate = PortInstanceGate(self, parent_node_instance)

        # label
        self.label = PortInstanceLabel(self, parent_node_instance)


    def setup_ui(self):
        pass  # reimplemented in subclasses

    def exec(self):
        """applies on OUTPUT; called NI internally (from parentNI)"""
        for cpi in self.connected_port_instances:
            cpi.update()

    def update(self):
        """applies on INPUT; called NI externally (from another NI)"""
        if (self.parent_node_instance.is_active() and self.type_ == 'exec') or \
           not self.parent_node_instance.is_active():
            self.parent_node_instance.update(self.parent_node_instance.inputs.index(self))


    def set_val(self, val):
        """applies on INPUT; called NI internally"""
        Debugger.debug('setting value of', self.direction, 'port of', self.parent_node_instance.parent_node.title,
                            'NodeInstance to', val)

        # note that val COULD be of object type and therefore already changed (because the original object did)
        self.val = val

        # if gen_data_on_request is set to true, all data will be required instead of actively forward propagated
        if not Algorithm.gen_data_on_request and not self.parent_node_instance.initializing:
            self.updated_val()

    def get_val(self):
        """applies on DATA; called NI internally AND externally"""
        Debugger.debug('get value in', self.direction, 'port instance',
                       self.parent_node_instance.inputs.index(
                                self) if self.direction == 'input' else self.parent_node_instance.outputs.index(self),
                            'of', self.parent_node_instance.parent_node.title)
        Debugger.debug('val is', self.val)

        if self.direction == 'input':
            if len(self.connected_port_instances) == 0:
                if self.widget:
                    return self.widget.get_val()
                else:
                    return None
            else:
                Debugger.debug('calling connected port for val')
                return self.connected_port_instances[0].get_val()
        elif self.direction == 'output':
            Debugger.debug('returning val directly')
            if Algorithm.gen_data_on_request:
                self.parent_node_instance.update()
            return self.val

    def updated_val(self):
        """applies on DATA OUTPUT; called NI internally"""
        for cpi in self.connected_port_instances:
            cpi.update()

    def get_input_widget_class(self, widget_name):
        """Returns the CLASS of a defined custom input widget by given name"""
        custom_node_input_widget_classes = \
            self.parent_node_instance.flow.parent_script.main_window.custom_node_input_widget_classes
        widget_class = custom_node_input_widget_classes[self.parent_node_instance.parent_node][widget_name]
        return widget_class

    def connected(self):
        """Disables the widget and causes update"""
        if self.widget:
            self.widget.setEnabled(False)
        if self.direction == 'input' and self.type_ == 'data':
            self.update()

    def disconnected(self):
        """Enables the widget again"""
        if self.widget:
            self.widget.setEnabled(True)

    def get_json_data(self):
        pass  # reimplemented


class InputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_='', label_str='',
                 config_data=None, widget_name=None, widget_pos=''):
        super(InputPortInstance, self).__init__(parent_node_instance, 'input', type_, label_str,
                                                widget_name, widget_pos)

        if config_data is not None:
            self.create_widget()
            self.widget.set_data(config_data)
        else:
            self.create_widget()

        self.setup_ui()

    def setup_ui(self):
        self.setSpacing(5)
        self.addItem(self.gate, 0, 0)
        self.setAlignment(self.gate, Qt.AlignVCenter | Qt.AlignLeft)
        self.addItem(self.label, 0, 1)
        self.setAlignment(self.label, Qt.AlignVCenter | Qt.AlignLeft)
        if self.widget is not None:
            if self.widget_pos == 'besides':
                self.addItem(self.proxy, 0, 2)
            elif self.widget_pos == 'under':
                self.addItem(self.proxy, 1, 0, 1, 2)
            self.setAlignment(self.proxy, Qt.AlignCenter)

    def create_widget(self, configuration=None):
        if self.type_ and self.type_ == 'data' or configuration and configuration['type'] == 'data':
            if self.widget_name is None:  # no input widget
                return
            elif self.widget_name == 'std line edit s':
                self.widget = StdLineEdit_PortInstanceWidget(self, self.parent_node_instance, size='small')
            elif self.widget_name == 'std line edit m' or self.widget_name == 'std line edit':
                self.widget = StdLineEdit_PortInstanceWidget(self, self.parent_node_instance)
            elif self.widget_name == 'std line edit l':
                self.widget = StdLineEdit_PortInstanceWidget(self, self.parent_node_instance, size='large')
            elif self.widget_name == 'std line edit s r':
                self.widget = StdLineEdit_PortInstanceWidget(self, self.parent_node_instance, size='small', resize=True)
            elif self.widget_name == 'std line edit m r':
                self.widget = StdLineEdit_PortInstanceWidget(self, self.parent_node_instance, resize=True)
            elif self.widget_name == 'std line edit l r':
                self.widget = StdLineEdit_PortInstanceWidget(self, self.parent_node_instance, size='large', resize=True)
            elif self.widget_name == 'std line edit s r nb':
                self.widget = StdLineEdit_NoBorder_PortInstanceWidget(self, self.parent_node_instance, size='small',
                                                                      resize=True)
            elif self.widget_name == 'std line edit m r nb':
                self.widget = StdLineEdit_NoBorder_PortInstanceWidget(self, self.parent_node_instance,
                                                                      resize=True)
            elif self.widget_name == 'std line edit l r nb':
                self.widget = StdLineEdit_NoBorder_PortInstanceWidget(self, self.parent_node_instance, size='large',
                                                                      resize=True)
            elif self.widget_name == 'std spin box':
                self.widget = StdSpinBox_PortInstanceWidget(self, self.parent_node_instance)
            else:  # custom input widget
                self.widget = self.get_input_widget_class(self.widget_name)(self, self.parent_node_instance)
            self.proxy = FlowProxyWidget(self.parent_node_instance.flow, self.parent_node_instance)
            self.proxy.setWidget(self.widget)

    def get_json_data(self):
        data_dict = {'type': self.type_,
                     'label': self.label_str}

        has_widget = True if self.widget else False
        data_dict['has widget'] = has_widget
        if has_widget:
            data_dict['widget name'] = self.widget_name
            data_dict['widget data'] = None if self.type_ == 'exec' else self.widget.get_data()
            data_dict['widget position'] = self.widget_pos

        return data_dict

class OutputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_='', label_str=''):
        super(OutputPortInstance, self).__init__(parent_node_instance, 'output', type_, label_str)

        self.setup_ui()

    def setup_ui(self):
        self.setSpacing(5)
        self.addItem(self.label, 0, 0)
        self.setAlignment(self.label, Qt.AlignVCenter | Qt.AlignRight)
        self.addItem(self.gate, 0, 1)

        self.setAlignment(self.gate, Qt.AlignVCenter | Qt.AlignRight)

    def get_json_data(self):
        data_dict = {'type': self.type_,
                     'label': self.label_str}

        return data_dict

# CONTENTS -------------------------------------------------------------------------------------------------------------

class PortInstanceGate(QGraphicsWidget):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(PortInstanceGate, self).__init__(parent_node_instance)

        self.setGraphicsItem(self)
        self.setAcceptHoverEvents(True)
        self.setCursor(Qt.CrossCursor)
        self.tool_tip_pos = None

        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        self.padding = 2
        self.painting_width = 15
        self.painting_height = 15
        self.width = self.painting_width+2*self.padding
        self.height = self.painting_height+2*self.padding
        self.port_local_pos = None

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):
        if Design.flow_style == 'dark std':
            color = QColor('#2E688C') if self.parent_port_instance.type_ == 'data' else QColor('#3880ad')
            if option.state & QStyle.State_MouseOver:
                color = color.lighter()

            brush = QBrush(QColor(color))
            painter.setBrush(brush)
            painter.setPen(Qt.NoPen)

            painter.drawEllipse(QRectF(self.padding, self.padding, self.painting_width, self.painting_height))

        elif Design.flow_style == 'dark tron':
            color = ''
            if self.parent_port_instance.type_ == 'exec':
                color = '#FFFFFF'
            elif self.parent_port_instance.type_ == 'data':
                color = self.parent_node_instance.parent_node.color
            pen = QPen(color)
            pen.setWidth(2)
            painter.setPen(pen)
            if len(self.parent_port_instance.connected_port_instances) > 0 or \
                    option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                c = self.parent_node_instance.parent_node.color
                r = c.red()
                g = c.green()
                b = c.blue()
                brush = QBrush(QColor(r, g, b, 100))
                painter.setBrush(brush)
            else:
                painter.setBrush(Qt.NoBrush)

            painter.drawEllipse(QRectF(self.padding, self.padding, self.painting_width, self.painting_height))

        elif Design.flow_style == 'ghostly' or Design.flow_style == 'blender':
            color = ''
            if self.parent_port_instance.type_ == 'exec':
                color = '#FFFFFF'

                if len(self.parent_port_instance.connected_port_instances) > 0 or \
                        option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                    brush = QBrush(QColor(255, 255, 255, 100))
                    painter.setBrush(brush)
                else:
                    painter.setBrush(Qt.NoBrush)
            elif self.parent_port_instance.type_ == 'data':
                color = self.parent_node_instance.parent_node.color

                if len(self.parent_port_instance.connected_port_instances) > 0 or \
                        option.state & QStyle.State_MouseOver:  # also fill when mouse hovers
                    c = self.parent_node_instance.parent_node.color
                    r = c.red()
                    g = c.green()
                    b = c.blue()
                    brush = QBrush(QColor(r, g, b, 100))
                    painter.setBrush(brush)
                else:
                    painter.setBrush(Qt.NoBrush)

            pen = QPen(color)
            pen.setWidth(1)
            painter.setPen(pen)

            rect = QRectF()
            rect.moveCenter(QPointF(self.width / 2, self.height / 2))
            rect.setWidth(self.painting_width)
            rect.setHeight(self.painting_height)
            painter.drawEllipse(QPointF(self.width / 2, self.height / 2), self.painting_width/3, self.painting_height/3)


    def mousePressEvent(self, event):
        event.accept()

    def hoverEnterEvent(self, event):
        if self.parent_port_instance.type_ == 'data' and self.parent_port_instance.direction == 'output':
            self.setToolTip(shorten(str(self.parent_port_instance.val), 1000, line_break=True))
        QGraphicsItem.hoverEnterEvent(self, event)

    def get_scene_center_pos(self):
        return QPointF(self.scenePos().x() + self.boundingRect().width()/2,
                       self.scenePos().y() + self.boundingRect().height()/2)


class PortInstanceLabel(QGraphicsWidget):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(PortInstanceLabel, self).__init__(parent_node_instance)
        self.setGraphicsItem(self)

        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance

        self.font = QFont("Source Code Pro", 10, QFont.Bold)
        font_metrics = QFontMetricsF(self.font)
        self.width = font_metrics.width(get_longest_line(self.parent_port_instance.label_str))
        self.height = font_metrics.height() * (self.parent_port_instance.label_str.count('\n') + 1)
        # print('self.height:', self.height)
        # self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.port_local_pos = None

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):
        painter.setBrush(Qt.NoBrush)
        c = ''
        if Design.flow_style == 'dark std':
            c = '#ffffff'
        elif Design.flow_style == 'dark tron' or Design.flow_style == 'ghostly' or Design.flow_style == 'blender':
            if self.parent_port_instance.type_ == 'exec':
                c = '#ffffff'
            elif self.parent_port_instance.type_ == 'data':
                c = self.parent_node_instance.parent_node.color
        pen = QPen(c)
        painter.setPen(pen)
        painter.setFont(self.font)
        painter.drawText(self.boundingRect(), Qt.AlignCenter, self.parent_port_instance.label_str)


class StdLineEdit_PortInstanceWidget(QLineEdit):
    def __init__(self, parent_port_instance, parent_node_instance, size='medium', resize=False):
        # PortInstanceWidget.__init__(self)
        # QLineEdit.__init__(self)
        super(StdLineEdit_PortInstanceWidget, self).__init__()

        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance
        self.port_local_pos = None
        self.resizing = resize

        if size == 'small':
            self.base_width = 30
        elif size == 'medium':
            self.base_width = 70
        elif size == 'large':
            self.base_width = 150

        self.setFixedWidth(self.base_width)

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
        self.textChanged.connect(M(self.text_changed))
        self.editingFinished.connect(M(self.editing_finished))

    def text_changed(self, new_text):
        if self.resizing:
            fm = QFontMetrics(self.font())
            text_width = fm.width(new_text)
            new_width = text_width+15
            self.setFixedWidth(new_width if new_width > self.base_width else self.base_width)

            self.parent_node_instance.update_shape()
            self.parent_node_instance.rebuild_ui()  # see rebuild_ui() for explanation

    def editing_finished(self):
        self.parent_node_instance.update(self.parent_node_instance.inputs.index(self.parent_port_instance))

    def remove_event(self):
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


class StdLineEdit_NoBorder_PortInstanceWidget(StdLineEdit_PortInstanceWidget):
    def __init__(self, parent_port_instance, parent_node_instance, size='medium', resize=False):
        super(StdLineEdit_NoBorder_PortInstanceWidget, self).__init__(parent_port_instance, parent_node_instance, size,
                                                                      resize)

        self.setStyleSheet("""
            QLineEdit{
                border: none;
                background-color: transparent;
                color: #aaaaaa;
                padding: 3px;
            }
        """)


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

    def remove_event(self):
        pass

    def get_val(self):
        return self.value()

    def get_data(self):
        return self.value()

    def set_data(self, data):
        self.setValue(data)