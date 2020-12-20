from PySide2.QtWidgets import QGraphicsItem, QLineEdit, QSpinBox, QGraphicsGridLayout, QGraphicsWidget, \
    QGraphicsLayoutItem
from PySide2.QtCore import Qt, QRectF, QPointF, QSizeF
from PySide2.QtGui import QFontMetricsF, QFont, QFontMetrics

from ryvencore.global_tools.Debugger import Debugger
from ryvencore.global_tools.strings import get_longest_line, shorten
from ryvencore.WidgetBaseClasses import MWB, IWB
from ryvencore.retain import M

from ryvencore.FlowProxyWidget import FlowProxyWidget


class PortInstance(QGraphicsGridLayout):

    def __init__(self, parent_node_instance, direction, type_='', label_str='',
                 widget_name=None, widget_pos=''):
        super(PortInstance, self).__init__()

        # GENERAL ATTRIBUTES
        self.val = None
        self.parent_node_instance = parent_node_instance
        self.direction = direction
        self.type_ = type_
        self.label_str = label_str
        self.connections = []  # connections stored here

        # CONTENTS
        # widget
        self.widget = None
        self.proxy: FlowProxyWidget = None
        self.widget_name = widget_name
        self.widget_pos = widget_pos

        # gate/pin
        self.pin = PortInstPin(self, parent_node_instance)

        # label
        self.label = PortInstLabel(self, parent_node_instance)


    def setup_ui(self):
        pass  # reimplemented in subclasses

    def get_val(self):
        """applies on DATA; called NI internally AND externally"""
        Debugger.write('get value in', self.direction, 'port instance',
                       self.parent_node_instance.inputs.index(
                                self) if self.direction == 'input' else self.parent_node_instance.outputs.index(self),
                            'of', self.parent_node_instance.parent_node.title)
        Debugger.write('val is', self.val)

        if self.direction == 'input':
            if len(self.connections) == 0:
                if self.widget:
                    return self.widget.get_val()
                else:
                    return None
            else:
                Debugger.write('calling connected port for val')
                return self.connections[0].get_val()
        elif self.direction == 'output':
            # Debugger.debug('returning val directly')
            if self.parent_node_instance.flow.algorithm_mode == 'exec flow':
                self.parent_node_instance.update()
            return self.val

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

    def config_data(self):
        pass  # reimplemented


class InputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_='', label_str='',
                 config_data=None, widget_name=None, widget_pos=''):
        super(InputPortInstance, self).__init__(parent_node_instance, 'input', type_, label_str,
                                                widget_name, widget_pos)

        if config_data is not None:
            self.create_widget()
            try:
                self.widget.set_data(config_data)
            except Exception as e:
                print('Exception while setting data in', self.parent_node_instance.parent_node.title,
                      'NodeInstance\'s input widget:', e, ' (was this intended?)')
        else:
            self.create_widget()

        self.setup_ui()

    def setup_ui(self):
        self.setSpacing(5)
        self.addItem(self.pin, 0, 0)
        self.setAlignment(self.pin, Qt.AlignVCenter | Qt.AlignLeft)
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
                self.widget = StdLineEdit_PortInstWidget(self, self.parent_node_instance, size='small')
            elif self.widget_name == 'std line edit m' or self.widget_name == 'std line edit':
                self.widget = StdLineEdit_PortInstWidget(self, self.parent_node_instance)
            elif self.widget_name == 'std line edit l':
                self.widget = StdLineEdit_PortInstWidget(self, self.parent_node_instance, size='large')
            elif self.widget_name == 'std line edit s r':
                self.widget = StdLineEdit_PortInstWidget(self, self.parent_node_instance, size='small', resize=True)
            elif self.widget_name == 'std line edit m r':
                self.widget = StdLineEdit_PortInstWidget(self, self.parent_node_instance, resize=True)
            elif self.widget_name == 'std line edit l r':
                self.widget = StdLineEdit_PortInstWidget(self, self.parent_node_instance, size='large', resize=True)
            elif self.widget_name == 'std line edit s r nb':
                self.widget = StdLineEdit_NoBorder_PortInstWidget(self, self.parent_node_instance, size='small',
                                                                  resize=True)
            elif self.widget_name == 'std line edit m r nb':
                self.widget = StdLineEdit_NoBorder_PortInstWidget(self, self.parent_node_instance,
                                                                  resize=True)
            elif self.widget_name == 'std line edit l r nb':
                self.widget = StdLineEdit_NoBorder_PortInstWidget(self, self.parent_node_instance, size='large',
                                                                  resize=True)
            elif self.widget_name == 'std spin box':
                self.widget = StdSpinBox_PortInstWidget(self, self.parent_node_instance)
            else:  # custom input widget
                self.widget = self.get_input_widget_class(self.widget_name)((self, self.parent_node_instance))
            self.proxy = FlowProxyWidget(self.parent_node_instance.flow, self.parent_node_instance)
            self.proxy.setWidget(self.widget)

    def get_input_widget_class(self, widget_name):
        """Returns the CLASS of a defined custom input widget by given name"""
        # custom_node_input_widget_classes = \
        #     self.parent_node_instance.flow.script.main_window.custom_node_input_widget_classes
        # widget_class = custom_node_input_widget_classes[self.parent_node_instance.parent_node][widget_name]
        # return widget_class
        return self.parent_node_instance.parent_node.custom_input_widgets[widget_name]

    def update(self):
        """applies on INPUT; called NI externally (from another NI)"""
        if (self.parent_node_instance.is_active() and self.type_ == 'exec') or \
           not self.parent_node_instance.is_active():
            self.parent_node_instance.update(self.parent_node_instance.inputs.index(self))

    def config_data(self):
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
        self.addItem(self.pin, 0, 1)

        self.setAlignment(self.pin, Qt.AlignVCenter | Qt.AlignRight)

    def exec(self):
        """applies on OUTPUT; called NI internally (from parentNI)"""
        for c in self.connections:
            c.activate()

    def set_val(self, val):
        """applies on OUTPUT; called NI internally"""
        Debugger.write('setting value of', self.direction, 'port of', self.parent_node_instance.parent_node.title,
                            'NodeInstance to', val)

        # note that val COULD be of object type and therefore already changed (because the original object did)
        self.val = val

        # if algorithm mode would be exec flow, all data will be required instead of actively forward propagated
        if self.parent_node_instance.flow.algorithm_mode == 'data flow' and \
                not self.parent_node_instance.initializing:
            self.updated_val()

    def updated_val(self):
        """applies on DATA OUTPUT; called NI internally"""
        for c in self.connections:
            c.activate()

    def config_data(self):
        data_dict = {'type': self.type_,
                     'label': self.label_str}

        return data_dict

# CONTENTS -------------------------------------------------------------------------------------------------------------

class PortInstPin(QGraphicsWidget):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(PortInstPin, self).__init__(parent_node_instance)

        self.setGraphicsItem(self)
        self.setAcceptHoverEvents(True)
        self.hovered = False
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
        self.parent_node_instance.session_design.flow_theme.node_inst_painter.paint_PI(
            painter, option, self.parent_node_instance.color,
            self.parent_port_instance.type_,
            len(self.parent_port_instance.connections) > 0,
            self.padding, self.painting_width, self.painting_height
        )

    def mousePressEvent(self, event):
        event.accept()

    def hoverEnterEvent(self, event):
        if self.parent_port_instance.type_ == 'data' and self.parent_port_instance.direction == 'output':
            self.setToolTip(shorten(str(self.parent_port_instance.val), 1000, line_break=True))

        # hover all connections
        # self.parent_node_instance.flow.hovered_port_inst_gate = self
        # self.parent_node_instance.flow.update()
        self.hovered = True

        QGraphicsItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):

        # turn connection highlighting off
        # self.parent_node_instance.flow.hovered_port_inst_gate = None
        # self.parent_node_instance.flow.update()
        self.hovered = False

        QGraphicsItem.hoverLeaveEvent(self, event)

    def get_scene_center_pos(self):
        return QPointF(self.scenePos().x() + self.boundingRect().width()/2,
                       self.scenePos().y() + self.boundingRect().height()/2)


class PortInstLabel(QGraphicsWidget):
    def __init__(self, parent_port_instance, parent_node_instance):
        super(PortInstLabel, self).__init__(parent_node_instance)
        self.setGraphicsItem(self)

        self.parent_port_instance = parent_port_instance
        self.parent_node_instance = parent_node_instance

        self.font = QFont("Source Code Pro", 10, QFont.Bold)
        font_metrics = QFontMetricsF(self.font)  # approximately! the designs can use different fonts
        self.width = font_metrics.width(get_longest_line(self.parent_port_instance.label_str))
        self.height = font_metrics.height() * (self.parent_port_instance.label_str.count('\n') + 1)
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
        self.parent_node_instance.session_design.flow_theme.node_inst_painter.paint_PI_label(
            painter, option,
            self.parent_port_instance.type_,
            len(self.parent_port_instance.connections) > 0,
            self.parent_port_instance.label_str,
            self.parent_node_instance.color,
            self.boundingRect()
        )


class StdLineEdit_PortInstWidget(QLineEdit, IWB):
    def __init__(self, parent_port_instance, parent_node_instance, size='medium', resize=False):
        # PortInstanceWidget.__init__(self)
        # QLineEdit.__init__(self)
        super(StdLineEdit_PortInstWidget, self).__init__()

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
            QLineEdit:hover {
                background-color: rgba(59, 156, 217, 150);
            }
            QLineEdit:disabled{
                color: #777777;
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
            # self.parent_node_instance.rebuild_ui()  # see rebuild_ui() for explanation

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


class StdLineEdit_NoBorder_PortInstWidget(StdLineEdit_PortInstWidget, IWB):
    def __init__(self, parent_port_instance, parent_node_instance, size='medium', resize=False):
        super(StdLineEdit_NoBorder_PortInstWidget, self).__init__(parent_port_instance, parent_node_instance, size,
                                                                  resize)

        self.setStyleSheet("""
            QLineEdit{
                border: none;
                border-radius: 5px;
                background-color: transparent;
                color: #aaaaaa;
                padding: 3px;
            }
            QLineEdit:hover {
                background-color: rgba(59, 156, 217, 150);
            }
            QLineEdit:disabled{
                color: #777777;
            }
        """)


class StdSpinBox_PortInstWidget(QSpinBox, IWB):
    def __init__(self, parent_port_instance, parent_node_instance):
        # PortInstanceWidget.__init__(self)
        # QLineEdit.__init__(self)
        super(StdSpinBox_PortInstWidget, self).__init__()

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