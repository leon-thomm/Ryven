from PySide2.QtWidgets import QGraphicsItem, QMenu, QAction, QStyle, QGraphicsLinearLayout, QGraphicsWidget, \
    QGraphicsLayoutItem
from PySide2.QtCore import Qt, QRectF, QPointF, Signal, QSizeF
from PySide2.QtGui import QColor, QBrush, QPen, QPainterPath, QFont, QFontMetricsF, QLinearGradient, QRadialGradient, \
    QPainter

from custom_src.global_tools.Debugger import Debugger
from custom_src.global_tools.math import pythagoras
from custom_src.global_tools.MovementEnum import MovementEnum
from custom_src.global_tools.strings import get_longest_line
from custom_src.GlobalAttributes import Design, PerformanceMode

from custom_src.Node import Node
from custom_src.PortInstance import InputPortInstance, OutputPortInstance
from custom_src.FlowProxyWidget import FlowProxyWidget


class NodeInstance(QGraphicsItem):
    def __init__(self, parent_node: Node, flow, config=None):
        super(NodeInstance, self).__init__()

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)

        # GENERAL ATTRIBUTES
        self.parent_node = parent_node
        self.flow = flow
        self.movement_state = None
        self.movement_pos_from = None
        self.inputs = []
        self.outputs = []

        self.default_actions = {'remove': {'method': self.action_remove,
                                           'data': 123},
                                'update shape': {'method': self.update_shape}}  # for context menus
        self.special_actions = {}  # only gets written in custom NodeInstance-subclasses
        self.personal_logs = []

        # 'initializing' will be set to False below. It's needed for the ports setup, to prevent shape updating stuff
        self.initializing = True

        self.temp_state_data = None


        # UI
        self.width = -1
        self.height = -1

        self.title_label = TitleLabel(self)

        self.main_widget = None
        self.main_widget_proxy: FlowProxyWidget = None
        if self.parent_node.has_main_widget:
            self.main_widget = self.parent_node.main_widget_class(self)
            self.main_widget_proxy = FlowProxyWidget(self.flow)
            self.main_widget_proxy.setWidget(self.main_widget)

        self.body_layout: QGraphicsLinearLayout = None
        self.inputs_layout: QGraphicsLinearLayout = None
        self.outputs_layout: QGraphicsLinearLayout = None
        self.layout: QGraphicsLinearLayout = self.setup_ui()
        self.widget = QGraphicsWidget(self)
        self.widget.setLayout(self.layout)



        # LOADING CONFIG
        if config:
            # self.setPos(config['position x'], config['position y'])
            self.setup_ports(config['inputs'], config['outputs'])
            if self.main_widget:
                try:
                    self.main_widget.set_data(config['main widget data'])
                except KeyError:
                    pass

            self.special_actions = self.set_special_actions_data(config['special actions'])
            self.temp_state_data = config['state data']
        else:
            self.setup_ports()


        # TOOLTIP
        if self.parent_node.description != '':
            self.setToolTip('<html><head/><body><p>'+self.parent_node.description+'</p></body></html>')
        self.setCursor(Qt.SizeAllCursor)

        self.initializing = False

    def setup_ui(self):
        """Creates the empty layouts for the NI's widget."""

        #   main layout
        layout = QGraphicsLinearLayout(Qt.Vertical)
        layout.setSpacing(5)

        if self.parent_node.design_style == 'extended':
            layout.addItem(self.title_label)
            layout.setAlignment(self.title_label, Qt.AlignTop)

        #   inputs
        self.inputs_layout = QGraphicsLinearLayout(Qt.Vertical)
        self.inputs_layout.setSpacing(2)

        #   outputs
        self.outputs_layout = QGraphicsLinearLayout(Qt.Vertical)
        self.outputs_layout.setSpacing(2)

        #   body
        self.body_layout = QGraphicsLinearLayout(Qt.Horizontal)

        self.body_layout.setSpacing(4)
        self.body_layout.addItem(self.inputs_layout)
        self.body_layout.setAlignment(self.inputs_layout, Qt.AlignVCenter | Qt.AlignLeft)
        self.body_layout.addStretch()
        self.body_layout.addItem(self.outputs_layout)
        self.body_layout.setAlignment(self.outputs_layout, Qt.AlignVCenter | Qt.AlignRight)

        if self.main_widget is not None:
            if self.parent_node.main_widget_pos == 'between ports':
                self.body_layout.insertItem(1, self.main_widget_proxy)
                self.body_layout.insertStretch(2)
                layout.addItem(self.body_layout)

            elif self.parent_node.main_widget_pos == 'under ports':
                layout.addItem(self.body_layout)
                layout.addItem(self.main_widget_proxy)
                layout.setAlignment(self.main_widget_proxy, Qt.AlignHCenter)
        else:
            layout.addItem(self.body_layout)

        return layout

    def rebuild_ui(self):
        for inp in self.inputs:
            self.inputs_layout.removeAt(0)
        for out in self.outputs:
            self.outputs_layout.removeAt(0)

        self.layout = self.setup_ui()
        self.widget.setLayout(self.layout)

        # add inputs
        for inp in self.inputs:
            self.add_input_to_layout(inp)
        for out in self.outputs:
            self.add_output_to_layout(out)


    #                        __                             _    __     __
    #              ____ _   / /  ____ _   ____     _____   (_)  / /_   / /_     ____ ___
    #             / __ `/  / /  / __ `/  / __ \   / ___/  / /  / __/  / __ \   / __ `__ \
    #            / /_/ /  / /  / /_/ /  / /_/ /  / /     / /  / /_   / / / /  / / / / / /
    #            \__,_/  /_/   \__, /   \____/  /_/     /_/   \__/  /_/ /_/  /_/ /_/ /_/
    #                         /____/

    def update(self, input_called=-1, output_called=-1):
        Debugger.debug('update in', self.parent_node.title, 'on input', input_called)
        try:
            self.update_event(input_called)
        except Exception as e:
            Debugger.debug('EXCEPTION IN', self.parent_node.title, 'NI:', e)

    def update_event(self, input_called=-1):     # API  (gets overwritten)
        """Gets called when an input received a signal. This is where the magic begins in subclasses."""

        pass

    def data_outputs_updated(self):
        """Sends update signals to all data outputs causing connected NIs to update."""

        Debugger.debug('updating data outputs in', self.parent_node.title)
        for o in self.outputs:
            if o.type_ == 'data':
                o.updated_val()
        Debugger.debug('data outputs in', self.parent_node.title, 'updated')

    def input(self, index):     # API
        """Returns the value of a data input.
        If the input is connected, the value of the connected output is used:
        If not, the value of the widget is used."""

        Debugger.debug('input called in', self.parent_node.title, 'NI:', index)
        return self.inputs[index].get_val()

    def set_output_val(self, index, val):       # API
        """Sets the value of a data output.
        self.data_outputs_updated() has to be called manually after all values are set."""

        self.outputs[index].set_val(val)

    def exec_output(self, index):       # API
        """Executes an execution output, sending a signal to all connected execution inputs causing the connected
        NIs to update."""
        self.outputs[index].exec()

    def about_to_remove_from_scene(self):
        """Called from Flow when the NI gets removed from the scene to stop all running threads."""
        if self.main_widget:
            self.main_widget.removing()
        self.removing()

        self.disable_personal_logs()

    def removing(self):     # API  (gets overwritten)
        """Method to stop all threads in hold of the NI itself."""
        pass

    #                                 _
    #              ____ _   ____     (_)
    #             / __ `/  / __ \   / /
    #            / /_/ /  / /_/ /  / /
    #            \__,_/  / .___/  /_/
    #                   /_/
    #
    # There are methods in the 'algorithm' section that are part of the API too

    #   LOGGING
    def new_log(self, title):
        """Requesting a new personal Log. Handy method for subclasses."""
        new_log = self.flow.parent_script.logger.new_log(self, title)
        self.personal_logs.append(new_log)
        return new_log

    def disable_personal_logs(self):
        """Disables personal Logs. They remain visible unless the user closes them via the appearing button."""
        for log in self.personal_logs:
            log.disable()

    def enable_personal_logs(self):
        """Resets personal Logs to normal state (hiding close button, changing style sheet)."""
        for log in self.personal_logs:
            log.enable()

    def log_message(self, message: str, target='global'):
        """Access to global_tools Script Logs ('global' or 'error')."""
        self.flow.parent_script.logger.log_message(message, target)

    # SHAPE
    def update_shape(self):
        """Causes recompilation of the whole shape."""

        if self.main_widget is not None:  # maybe the main_widget got resized
            self.main_widget_proxy.setMaximumSize(self.main_widget.size())
            self.widget.adjustSize()

        self.layout.activate()
        self.layout.invalidate()
        # both very essential; repositions everything in case content has changed (inputs/outputs/widget)

        self.width = self.boundingRect().width()
        self.height = self.boundingRect().height()
        rect = QRectF(QPointF(-self.width/2, -self.height/2),
                      QPointF(self.width/2, self.height/2))
        self.widget.setPos(rect.left(), rect.top())

        if not self.parent_node.design_style == 'extended':
            self.title_label.setPos(QPointF(-self.title_label.boundingRect().width()/2,
                                            -self.title_label.boundingRect().height()/2))

        self.flow.viewport().update()


    # PORTS
    def create_new_input(self, type_, label, widget_type='', widget_name='', widget_pos='under', pos=-1):
        """Creates and adds a new input. Handy for subclasses."""
        Debugger.debug('create_new_input called with widget pos:', widget_pos)
        pi = InputPortInstance(self, type_, label,
                               widget_type=widget_type,
                               widget_name=widget_name,
                               widget_pos=widget_pos)
        if pos == -1:
            self.inputs.append(pi)
            self.add_input_to_layout(pi)
        else:
            self.inputs.insert(pos, pi)
            self.insert_input_into_layout(pos, pi)

        if not self.initializing:
            self.update_shape()

    def create_new_input_from_config(self, input_config):
        """Called only at NI creation."""
        pi = InputPortInstance(self, configuration=input_config)
        self.inputs.append(pi)
        self.add_input_to_layout(pi)

    def add_input_to_layout(self, i):
        if self.inputs_layout.count() > 0:
            self.inputs_layout.addStretch()
        self.inputs_layout.addItem(i)
        self.inputs_layout.setAlignment(i, Qt.AlignLeft)

    def insert_input_into_layout(self, index, i):
        self.inputs_layout.insertItem(index, i)
        self.inputs_layout.setAlignment(i, Qt.AlignLeft)
        self.inputs_layout.addStretch()

    def delete_input(self, i):
        """Disconnects and removes input. Handy for subclasses."""
        inp: InputPortInstance = None
        if type(i) == int:
            inp = self.inputs[i]
        elif type(i) == InputPortInstance:
            inp = i

        for cpi in inp.connected_port_instances:
            self.flow.connect_gates(inp.gate, cpi.gate)

        # for some reason, I have to remove all widget items manually from the scene too. setting the items to
        # ownedByLayout(True) does not work, I don't know why.
        self.scene().removeItem(inp.gate)
        self.scene().removeItem(inp.label)
        if inp.proxy is not None:
            self.scene().removeItem(inp.proxy)

        self.inputs_layout.removeItem(inp)
        self.inputs.remove(inp)

        # just a temporary workaround for the issues discussed here:
        # https://forum.qt.io/topic/116268/qgraphicslayout-not-properly-resizing-to-change-of-content
        self.rebuild_ui()

        if not self.initializing:
            self.update_shape()


    def create_new_output(self, type_, label, pos=-1):
        """Creates and adds a new output. Handy for subclasses."""

        pi = OutputPortInstance(self, type_, label)
        if pos == -1:
            self.outputs.append(pi)
            self.add_output_to_layout(pi)
        else:
            self.outputs.insert(pos, pi)
            self.insert_output_into_layot(pos, pi)

        if not self.initializing:
            self.update_shape()

    def create_new_output_from_config(self, output_config=None):
        """Called only at NI creation."""
        pi = OutputPortInstance(self, configuration=output_config)
        self.outputs.append(pi)
        self.add_output_to_layout(pi)

    def add_output_to_layout(self, o):
        if self.outputs_layout.count() > 0:
            self.outputs_layout.addStretch()
        self.outputs_layout.addItem(o)
        self.outputs_layout.setAlignment(o, Qt.AlignRight)

    def insert_output_into_layout(self, index, o):
        self.outputs_layout.insertItem(index, o)
        self.outputs_layout.setAlignment(o, Qt.AlignRight)
        self.outputs_layout.addStretch()

    def delete_output(self, o):
        """Disconnects and removes output. Handy for subclasses."""
        out: OutputPortInstance = None
        if type(o) == int:
            out = self.outputs[o]
        elif type(o) == OutputPortInstance:
            out = o

        for cpi in out.connected_port_instances:
            self.flow.connect_gates(out.gate, cpi.gate)

        # see delete_input() for info!
        self.scene().removeItem(out.gate)
        self.scene().removeItem(out.label)

        self.outputs_layout.removeItem(out)
        self.outputs.remove(out)

        # just a temporary workaround for the issues discussed here:
        # https://forum.qt.io/topic/116268/qgraphicslayout-not-properly-resizing-to-change-of-content
        self.rebuild_ui()

        if not self.initializing:
            self.update_shape()

    # GET, SET DATA
    def get_data(self):
        """ IMPORTANT
        This method gets subclassed and specified. If the NI has states (so, the behavior depends on certain values),
        all these values must be stored in JSON-able format in a dict here. This dictionary will be used to reload the
        node's state when loading a project or pasting copied/cut nodes in the Flow (the states get copied too), see
        self.set_data(self, data) below.
        Unfortunately, I can't use pickle or something like that due to PySide2 which runs on C++, not Python.
        :return: Dictionary representing all values necessary to determine the NI's current state
        """
        return {}

    def set_data(self, data):
        """ IMPORTANT
        If the NI has states, it's state should get reloaded here according to what was previously provided by the same
        class in get_data(), see above.
        :param data: Dictionary representing all values necessary to determine the NI's current state
        """
        pass

    # --------------------------------------------------------------------------------------
    # UI STUFF ----------------------------------------

    def boundingRect(self):
        # remember: (0, 0) shall be the NI's center!
        rect = QRectF()
        w = self.layout.geometry().width()
        h = self.layout.geometry().height()
        rect.setLeft(-w/2)
        rect.setTop(-h/2)
        rect.setWidth(w)
        rect.setHeight(h)
        return rect

    #   PAINTING
    def paint(self, painter, option, widget=None):

        # unfortunately, the boundingRect() is only not 0 when paint() is called the first time
        if self.width == -1 or self.height == -1:
            self.update_shape()

        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(100, 100, 100, 150))  # QBrush(QColor('#3B9CD9'))
        painter.setBrush(brush)

        if self.parent_node.design_style == 'extended':

            if Design.flow_style == 'dark std':
                self.draw_dark_extended_background(painter)

            elif Design.flow_style == 'dark tron':
                self.draw_tron_extended_background(painter)

        elif self.parent_node.design_style == 'minimalistic':

            if Design.flow_style == 'dark std':
                self.draw_dark_minimalistic(painter)

            elif Design.flow_style == 'dark tron':
                if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
                    self.draw_tron_minimalistic(painter, background_color=self.parent_node.color.darker())
                else:
                    self.draw_tron_minimalistic(painter)


    def draw_dark_extended_background(self, painter):
        c = self.parent_node.color

        # main rect
        body_gradient = QRadialGradient(self.boundingRect().topLeft(), pythagoras(self.height, self.width))
        body_gradient.setColorAt(0, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 200))
        body_gradient.setColorAt(1, QColor(c.red() / 10 + 100, c.green() / 10 + 100, c.blue() / 10 + 100, 0))

        painter.setBrush(body_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.boundingRect(), 12, 12)

        header_gradient = QLinearGradient(self.get_header_rect().topRight(), self.get_header_rect().bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRoundedRect(self.get_header_rect(), 12, 12)

    def draw_tron_extended_background(self, painter):
        # main rect
        c = QColor('#212224')
        painter.setBrush(c)
        pen = QPen(self.parent_node.color)
        pen.setWidth(2)
        painter.setPen(pen)
        body_path = self.get_extended_body_path_TRON_DESIGN(10)
        painter.drawPath(body_path)
        # painter.drawRoundedRect(self.boundingRect(), 12, 12)

        c = self.parent_node.color
        header_gradient = QLinearGradient(self.get_header_rect().topRight(), self.get_header_rect().bottomLeft())
        header_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 255))
        header_gradient.setColorAt(0.5, QColor(c.red(), c.green(), c.blue(), 100))
        header_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 0))
        painter.setBrush(header_gradient)
        header_path = self.get_extended_header_path_TRON_DESIGN(10)
        painter.drawPath(header_path)

    def get_extended_body_path_TRON_DESIGN(self, corner_size):
        path = QPainterPath()
        path.moveTo(+self.width/2, -self.height/2+corner_size)
        path.lineTo(+self.width/2-corner_size, -self.height/2)
        path.lineTo(-self.width/2+corner_size, -self.height/2)
        path.lineTo(-self.width/2, -self.height/2+corner_size)
        path.lineTo(-self.width/2, +self.height/2-corner_size)
        path.lineTo(-self.width/2+corner_size, +self.height/2)
        path.lineTo(+self.width/2-corner_size, +self.height/2)
        path.lineTo(+self.width/2, +self.height/2-corner_size)
        path.closeSubpath()
        return path

    def get_extended_header_path_TRON_DESIGN(self, corner_size):
        header_height = 35 * (self.parent_node.title.count('\n')+1)
        header_bottom = -self.height/2+header_height
        path = QPainterPath()
        path.moveTo(+self.width/2, -self.height/2+corner_size)
        path.lineTo(+self.width/2-corner_size, -self.height/2)
        path.lineTo(-self.width/2+corner_size, -self.height/2)
        path.lineTo(-self.width/2, -self.height/2+corner_size)
        path.lineTo(-self.width/2, header_bottom-corner_size)
        path.lineTo(-self.width/2+corner_size, header_bottom)
        path.lineTo(+self.width/2-corner_size, header_bottom)
        path.lineTo(+self.width/2, header_bottom-corner_size)
        path.closeSubpath()
        return path

    def draw_dark_minimalistic(self, painter):
        path = QPainterPath()
        path.moveTo(-self.width / 2, 0)

        path.cubicTo(-self.width / 2, -self.height / 2,
                     -self.width / 2, -self.height / 2,
                     0, -self.height / 2)
        path.cubicTo(+self.width / 2, -self.height / 2,
                     +self.width / 2, -self.height / 2,
                     +self.width / 2, 0)
        path.cubicTo(+self.width / 2, +self.height / 2,
                     +self.width / 2, +self.height / 2,
                     0, +self.height / 2)
        path.cubicTo(-self.width / 2, +self.height / 2,
                     -self.width / 2, +self.height / 2,
                     -self.width / 2, 0)
        path.closeSubpath()

        c = self.parent_node.color
        body_gradient = QLinearGradient(self.boundingRect().bottomLeft(),
                                        self.boundingRect().topRight())
        body_gradient.setColorAt(0, QColor(c.red(), c.green(), c.blue(), 150))
        body_gradient.setColorAt(1, QColor(c.red(), c.green(), c.blue(), 80))

        painter.setBrush(body_gradient)
        painter.setPen(QPen(QColor(30, 43, 48)))

        painter.drawPath(path)

    def draw_tron_minimalistic(self, painter, background_color=QColor('#36383B')):
        path = QPainterPath()
        path.moveTo(-self.width / 2, 0)

        corner_size = 10
        path.lineTo(-self.width / 2 + corner_size / 2, -self.height / 2 + corner_size / 2)
        path.lineTo(0, -self.height / 2)
        path.lineTo(+self.width / 2 - corner_size / 2, -self.height / 2 + corner_size / 2)
        path.lineTo(+self.width / 2, 0)
        path.lineTo(+self.width / 2 - corner_size / 2, +self.height / 2 - corner_size / 2)
        path.lineTo(0, +self.height / 2)
        path.lineTo(-self.width / 2 + corner_size / 2, +self.height / 2 - corner_size / 2)
        path.closeSubpath()

        painter.setBrush(background_color)
        pen = QPen(self.parent_node.color)
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawPath(path)

    def get_header_rect(self):
        header_height = 1.4 * self.title_label.boundingRect().height()  # 35 * (self.parent_node.title.count('\n')+1)

        header_rect = QRectF()
        header_rect.setTopLeft(QPointF(-self.width/2, -self.height/2))
        header_rect.setWidth(self.width)
        header_rect.setHeight(header_height)
        return header_rect


    def get_context_menu(self):
        menu = QMenu(self.flow)

        for a in self.get_actions(self.get_extended_default_actions(), menu):  # menu needed for 'parent'
            if type(a) == NodeInstanceAction:
                menu.addAction(a)
            elif type(a) == QMenu:
                menu.addMenu(a)

        menu.addSeparator()

        for a in self.get_actions(self.special_actions, menu):  # menu needed for 'parent'
            if type(a) == NodeInstanceAction:
                menu.addAction(a)
            elif type(a) == QMenu:
                menu.addMenu(a)

        return menu


    def itemChange(self, change, value):
        """This method ensures that all connections, selection borders etc. that get drawn in the Flow are constantly
        redrawn during a NI drag. Should get disabled when running in performance mode - not implemented yet."""

        if change == QGraphicsItem.ItemPositionChange:
            if PerformanceMode.mode == 'pretty':
                self.flow.viewport().update()
            if self.movement_state == MovementEnum.mouse_clicked:
                self.movement_state = MovementEnum.position_changed

        return QGraphicsItem.itemChange(self, change, value)

    def hoverEnterEvent(self, event):
        self.title_label.set_NI_hover_state(hovering=True)
        QGraphicsItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.title_label.set_NI_hover_state(hovering=False)
        QGraphicsItem.hoverLeaveEvent(self, event)

    def mousePressEvent(self, event):
        """Used for Moving-Commands in Flow - may be replaced later with a nicer determination of a moving action."""
        self.movement_state = MovementEnum.mouse_clicked
        self.movement_pos_from = self.pos()
        return QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        """Used for Moving-Commands in Flow - may be replaced later with a nicer determination of a moving action."""
        if self.movement_state == MovementEnum.position_changed:
            self.flow.selected_components_moved(self.pos()-self.movement_pos_from)
        self.movement_state = None
        return QGraphicsItem.mouseReleaseEvent(self, event)

    # ACTIONS
    def get_extended_default_actions(self):
        actions_dict = self.default_actions.copy()
        for index in range(len(self.inputs)):
            inp = self.inputs[index]
            if inp.type_ == 'exec':
                actions_dict['exec input '+str(index)] = {'method': self.action_exec_input,
                                                          'data': {'input index': index}}
        return actions_dict

    def action_exec_input(self, data):
        self.update(data['input index'])

    def get_actions(self, actions_dict, menu):
        actions = []

        for k in actions_dict:
            v_dict = actions_dict[k]
            try:
                method = v_dict['method']
                data = None
                try:
                    data = v_dict['data']
                except KeyError:
                    pass
                action = NodeInstanceAction(k, menu, data)
                action.custom_triggered.connect(method)
                actions.append(action)
            except KeyError:
                action_menu = QMenu(k, menu)
                sub_actions = self.get_actions(v_dict, action_menu)
                for a in sub_actions:
                    action_menu.addAction(a)
                actions.append(action_menu)

        return actions

    def action_remove(self, data):
        self.flow.remove_node_instance_triggered(self)

    def get_special_actions_data(self, actions):
        cleaned_actions = actions.copy()
        for key in cleaned_actions:
            v = cleaned_actions[key]
            if callable(v):
                cleaned_actions[key] = v.__name__
            elif type(v) == dict:
                cleaned_actions[key] = self.get_special_actions_data(v)
            else:
                cleaned_actions[key] = v
        return cleaned_actions

    def set_special_actions_data(self, actions_data):
        actions = {}
        for key in actions_data:
            if type(actions_data[key]) != dict:
                try:  # maybe the developer changed some special actions...
                    actions[key] = getattr(self, actions_data[key])
                except AttributeError:
                    pass
            else:
                actions[key] = self.set_special_actions_data(actions_data[key])
        return actions

    # PORTS
    def setup_ports(self, inputs_config=None, outputs_config=None):
        if not inputs_config and not outputs_config:
            for i in range(len(self.parent_node.inputs)):
                inp = self.parent_node.inputs[i]
                self.create_new_input(inp.type_, inp.label,
                                      widget_type=self.parent_node.inputs[i].widget_type,
                                      widget_name=self.parent_node.inputs[i].widget_name,
                                      widget_pos =self.parent_node.inputs[i].widget_pos)

            for o in range(len(self.parent_node.outputs)):
                out = self.parent_node.outputs[o]
                self.create_new_output(out.type_, out.label)
        else:  # when loading saved NIs, the port instances might not be synchronised to the parent's ports anymore
            for i in range(len(inputs_config)):
                self.create_new_input_from_config(input_config=inputs_config[i])

            for o in range(len(outputs_config)):
                self.create_new_output_from_config(output_config=outputs_config[o])

    def get_input_widget_class(self, widget_name):
        """Returns a reference to the widget class of a given name for instantiation."""
        custom_node_input_widget_classes = self.flow.parent_script.main_window.custom_node_input_widget_classes
        widget_class = custom_node_input_widget_classes[self.parent_node][widget_name]
        return widget_class

    def add_input_to_scene(self, i):
        self.flow.scene().addItem(i.gate)
        self.flow.scene().addItem(i.label)
        if i.widget:
            self.flow.scene().addItem(i.proxy)

    def del_and_remove_input_from_scene(self, i_index):
        i = self.inputs[i_index]
        for p in self.inputs[i_index].connected_port_instances:
            self.flow.connect_gates(i.gate, p.gate)

        self.flow.scene().removeItem(i.gate)
        self.flow.scene().removeItem(i.label)
        if i.widget:
            self.flow.scene().removeItem(i.proxy)
            i.widget.removing()
        self.inputs.remove(i)


    def add_output_to_scene(self, o):
        self.flow.scene().addItem(o.gate)
        self.flow.scene().addItem(o.label)

    def del_and_remove_output_from_scene(self, o_index):
        o = self.outputs[o_index]
        for p in self.outputs[o_index].connected_port_instances:
            self.flow.connect_gates(o.gate, p.gate)

        self.flow.scene().removeItem(o.gate)
        self.flow.scene().removeItem(o.label)
        self.outputs.remove(o)

    # GENERAL
    def initialized(self):
        """Gets called at the very end of all initialization processes/at the very end of the constructor."""
        if self.temp_state_data is not None:
            self.set_data(self.temp_state_data)
        self.update()

    def is_active(self):
        for i in self.inputs:
            if i.type_ == 'exec':
                return True
        for o in self.outputs:
            if o.type_ == 'exec':
                return True
        return False

    def has_main_widget(self):
        """Might be used later in CodePreview_Widget to enable not only showing the NI's class but also it's
        main_widget's class."""
        return self.main_widget is not None

    def get_input_widgets(self):
        """Might be used later in CodePreview_Widget to enable not only showing the NI's class but its input widgets'
        classes."""
        input_widgets = []
        for i in range(len(self.inputs)):
            inp = self.inputs[i]
            if inp.widget is not None:
                input_widgets.append({i: inp.widget})
        return input_widgets

    def get_json_data(self):
        """Returns all metadata of the NI including position, package etc. in a JSON-able dict format.
        Used to rebuild the Flow when loading a project."""

        # general attributes
        node_instance_dict = {'parent node title': self.parent_node.title,
                              'parent node type': self.parent_node.type_,
                              'parent node package': self.parent_node.package,
                              'parent node description': self.parent_node.description,
                              'position x': self.pos().x(),
                              'position y': self.pos().y()}
        if self.main_widget:
            node_instance_dict['main widget data'] = self.main_widget.get_data()

        node_instance_dict['state data'] = self.get_data()
        node_instance_dict['special actions'] = self.get_special_actions_data(self.special_actions)

        # inputs
        node_instance_inputs_list = []
        for i in self.inputs:
            input_dict = i.get_json_data()
            node_instance_inputs_list.append(input_dict)
        node_instance_dict['inputs'] = node_instance_inputs_list

        # outputs
        node_instance_outputs_list = []
        for o in self.outputs:
            output_dict = o.get_json_data()
            node_instance_outputs_list.append(output_dict)
        node_instance_dict['outputs'] = node_instance_outputs_list

        return node_instance_dict







class NodeInstanceAction(QAction):
    """A custom implementation of QAction that additionally stores transmitted 'data' which can be intuitively used
    in subclasses f.ex. to determine the exact source of the action triggered. For more info see GitHub docs."""

    custom_triggered = Signal(object)

    def __init__(self, text, menu, data=None):
        super(NodeInstanceAction, self).__init__(text=text, parent=menu)

        self.data = data
        self.triggered.connect(self.triggered_)  # yeah, I think that's ugly but I didn't find a nicer way; it works

    def triggered_(self):
        self.custom_triggered.emit(self.data)




class TitleLabel(QGraphicsWidget):
    def __init__(self, parent_node_instance):
        super(TitleLabel, self).__init__(parent_node_instance)

        self.setGraphicsItem(self)

        self.parent_node_instance: NodeInstance = parent_node_instance
        self.title_str = self.parent_node_instance.parent_node.title
        self.font = QFont('Poppins', 15) if self.parent_node_instance.parent_node.design_style == 'extended' else \
                                 QFont('K2D', 20, QFont.Bold, True)
        self.fm = QFontMetricsF(self.font)

        self.width = self.fm.width(get_longest_line(self.title_str))
        self.height = self.fm.height() * 0.7 * (self.title_str.count('\n') + 1)

        self.color = QColor(30, 43, 48)
        self.pen_width = 1.5
        self.hovering = False  # whether the mouse is hovering over the parent NI (!)


    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):
        self.set_design()
        
        pen = QPen(self.color)
        pen.setWidth(self.pen_width)

        painter.setPen(pen)
        painter.setFont(self.font)

        text_rect = self.boundingRect()
        text_rect.setTop(text_rect.top()-7)

        painter.drawText(text_rect, Qt.AlignTop, self.title_str)

    def design_style(self):
        return self.parent_node_instance.parent_node.design_style

    def set_NI_hover_state(self, hovering: bool):
        self.hovering = hovering
        self.update()

    def set_design(self):
        if self.design_style() == 'extended':
            if Design.flow_style == 'dark std':
                if self.hovering:
                    self.color = self.parent_node_instance.parent_node.color.lighter()
                    self.pen_width = 2
                else:
                    self.color = QColor(30, 43, 48)
                    self.pen_width = 1.5
            elif Design.flow_style == 'dark tron':
                if self.hovering:
                    self.color = self.parent_node_instance.parent_node.color.lighter()
                else:
                    self.color = self.parent_node_instance.parent_node.color
                self.pen_width = 2
        elif self.design_style() == 'minimalistic':
            if Design.flow_style == 'dark std':
                if self.hovering:
                    self.color = self.parent_node_instance.parent_node.color.lighter()
                    self.pen_width = 1.5
                else:
                    self.color = QColor(30, 43, 48)
                    self.pen_width = 1.5
            elif Design.flow_style == 'dark tron':
                self.color = self.parent_node_instance.parent_node.color
                self.pen_width = 2