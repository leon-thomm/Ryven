from PySide2.QtWidgets import QGraphicsItem, QMenu, QAction, QStyle
from PySide2.QtCore import Qt, QRectF, QPointF, Signal
from PySide2.QtGui import QColor, QBrush, QPen, QPainterPath, QFont, QFontMetricsF, QLinearGradient, QRadialGradient, \
    QPainter

from custom_src.GlobalAccess import GlobalStorage, pythagoras, MovementEnum, get_longest_line

from custom_src.Node import Node
from custom_src.PortInstance import PortInstance
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
        self.main_widget = None
        self.main_widget_proxy: FlowProxyWidget = None
        self.default_actions = {'remove': {'method': self.action_remove,
                                           'data': 123},
                                'compute shape': {'method': self.compute_content_positions}}  # for context menus
        self.gen_data_on_request = False
        self.personal_logs = []
        self.special_actions = {}  # only gets written in custom NodeInstance-subclasses - dynamic
        self.width = -1
        self.height = -1
        self.display_name_font = QFont('Poppins', 15) if parent_node.design_style == 'extended' else \
                                 QFont('K2D', 20, QFont.Bold, True)
        self.display_name_FM = QFontMetricsF(self.display_name_font)
        # self.port_label_font = QFont("Source Code Pro", 10, QFont.Bold, True)

        # 'initializing' will be set to False below. It's needed for the ports setup, to prevent shape updating stuff
        self.initializing = True

        self.temp_state_data = None

        if self.parent_node.has_main_widget:
            self.main_widget = self.parent_node.main_widget_class(self)
            self.main_widget_proxy = FlowProxyWidget(self.flow, self)
            self.main_widget_proxy.setWidget(self.main_widget)

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
        self.setToolTip(self.parent_node.description)
        self.setCursor(Qt.SizeAllCursor)

        self.initializing = False

    #                        __                             _    __     __
    #              ____ _   / /  ____ _   ____     _____   (_)  / /_   / /_     ____ ___
    #             / __ `/  / /  / __ `/  / __ \   / ___/  / /  / __/  / __ \   / __ `__ \
    #            / /_/ /  / /  / /_/ /  / /_/ /  / /     / /  / /_   / / / /  / / / / / /
    #            \__,_/  /_/   \__, /   \____/  /_/     /_/   \__/  /_/ /_/  /_/ /_/ /_/
    #                         /____/

    def update(self, input_called=-1, output_called=-1):
        GlobalStorage.debug('update in', self.parent_node.title, 'on input', input_called)
        try:
            self.update_event(input_called)
        except Exception as e:
            GlobalStorage.debug('EXCEPTION IN', self.parent_node.title, 'NI:', e)

    def update_event(self, input_called=-1):     # API  (gets overwritten)
        """Gets called when an input received a signal. This is where the magic begins in subclasses."""

        pass

    def data_outputs_updated(self):
        """Sends update signals to all data outputs causing connected NIs to update."""

        GlobalStorage.debug('updating data outputs in', self.parent_node.title)
        for o in self.outputs:
            if o.type_ == 'data':
                o.updated_val()
        GlobalStorage.debug('data outputs in', self.parent_node.title, 'updated')

    def input(self, index):     # API
        """Returns the value of a data input.
        If the input is connected, the value of the connected output is used:
        If not, the value of the widget is used."""

        GlobalStorage.debug('input called in', self.parent_node.title,'NI:', index)
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
        """Access to global Script Logs ('global' or 'error')."""
        self.flow.parent_script.logger.log_message(self, message, target)

    # SHAPE
    def update_shape(self):
        """Just a handy method for subclasses. Causes recompilation of the whole shape."""
        self.compute_content_positions()
        self.flow.viewport().update()

    # PORTS
    def create_new_input(self, type_, label, widget_type='', widget_name='', widget_pos='under', pos=-1):
        """Creates and adds a new input. Handy for subclasses."""
        GlobalStorage.debug('create_new_input called with widget pos:', widget_pos)
        pi = PortInstance(self, 'input', type_, label,
                          widget_type=widget_type,
                          widget_name=widget_name,
                          widget_pos=widget_pos)
        if pos == -1:
            self.inputs.append(pi)
        else:
            if pos == -1:
                self.inputs.insert(0, pi)
            else:
                self.inputs.insert(pos, pi)
        if self.scene():
            self.add_input_to_scene(pi)

        if not self.initializing:
            self.update_shape()

    def create_new_input_from_config(self, input_config):
        """Called only at NI creation."""
        pi = PortInstance(self, 'input', configuration=input_config)
        self.inputs.append(pi)

    def delete_input(self, i):
        """Disconnects and removes input. Handy for subclasses."""
        if type(i) == int:
            self.del_and_remove_input_from_scene(i)
        elif type(i) == PortInstance:
            self.del_and_remove_input_from_scene(self.inputs.index(i))

        if not self.initializing:
            self.update_shape()


    def create_new_output(self, type_, label, pos=-1):
        """Creates and adds a new output. Handy for subclasses."""
        pi = PortInstance(self, 'output', type_, label)
        if pos == -1:
            self.outputs.append(pi)
        else:
            if pos == -1:
                self.outputs.insert(0, pi)
            else:
                self.outputs.insert(pos, pi)
        if self.scene():
            self.add_output_to_scene(pi)

        if not self.initializing:
            self.update_shape()

    def create_new_output_from_config(self, output_config=None):
        """Called only at NI creation."""
        pi = PortInstance(self, 'output', configuration=output_config)
        self.outputs.append(pi)

    def delete_output(self, o):
        """Disconnects and removes output. Handy for subclasses."""
        if type(o) == int:
            self.del_and_remove_output_from_scene(o)
        else:
            self.del_and_remove_output_from_scene(self.outputs.index(o))

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
        return QRectF(-self.width/2, -self.height/2, self.width, self.height)

    #   PAINTING
    def paint(self, painter, option, widget=None):

        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(QColor(100, 100, 100, 150))  # QBrush(QColor('#3B9CD9'))
        painter.setBrush(brush)
        std_pen = QPen(QColor(30, 43, 48))  # QColor(30, 43, 48)  # used for header title and minimal std dark border
        std_pen.setWidthF(1.5)
        # painter.setPen(std_pen)


        if self.parent_node.design_style == 'extended':

            header_pen = std_pen  # differs from std_pen in tron design

            if GlobalStorage.storage['design style'] == 'dark std':
                self.draw_dark_extended_background(painter)

                if option.state & QStyle.State_MouseOver:  # make title color white when mouse hovers
                    c = self.parent_node.color.lighter()
                    header_pen = QPen(c)
                    header_pen.setWidth(2)

            elif GlobalStorage.storage['design style'] == 'dark tron':
                self.draw_tron_extended_background(painter)

                c = self.parent_node.color
                if option.state & QStyle.State_MouseOver:  # make title color lighter when mouse hovers
                    c = self.parent_node.color.lighter()
                header_pen = QPen(c)
                header_pen.setWidth(2)

            # HEADER
            painter.setFont(self.display_name_font)
            painter.setPen(header_pen)
            painter.drawText(self.get_title_rect(), Qt.AlignVCenter | Qt.AlignLeft, self.parent_node.title)
            painter.setBrush(Qt.NoBrush)
            painter.setPen(QPen(Qt.white, 1))

        elif self.parent_node.design_style == 'minimalistic':

            if GlobalStorage.storage['design style'] == 'dark std':
                self.draw_dark_minimalistic(painter, std_pen)
                if option.state & QStyle.State_MouseOver:  # make title color light when mouse hovers
                    pen = QPen(self.parent_node.color.lighter())
                    painter.setPen(pen)

            elif GlobalStorage.storage['design style'] == 'dark tron':
                if option.state & QStyle.State_MouseOver:  # use special dark background color when mouse hovers
                    self.draw_tron_minimalistic(painter, background_color=self.parent_node.color.darker())
                else:
                    self.draw_tron_minimalistic(painter)

            # HEADER
            painter.setFont(self.display_name_font)
            painter.drawText(self.boundingRect(), Qt.AlignCenter, self.parent_node.title)

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

    def draw_dark_minimalistic(self, painter, pen):
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
        painter.setPen(pen)

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
        header_height = 35 * (self.parent_node.title.count('\n')+1)

        header_rect = QRectF()
        header_rect.setTopLeft(QPointF(-self.width/2, -self.height/2))
        header_rect.setRight(self.width/2)
        header_rect.setBottom(-self.height/2 + header_height)
        return header_rect

    def get_title_rect(self):
        title_rect_offset_factor = 0.56

        header_rect = self.get_header_rect()
        rect = QRectF()
        rect.setTop(header_rect.top()+(header_rect.height()/2)*(1-title_rect_offset_factor))
        rect.setLeft(header_rect.left() + 10 )
        rect.setHeight(header_rect.height()*title_rect_offset_factor)
        w = header_rect.width()*title_rect_offset_factor
        title_width = self.display_name_FM.width(get_longest_line(self.parent_node.title))
        rect.setWidth(w if w > title_width else title_width)
        return rect


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
            # self.flow.viewport().update()
            if self.movement_state == MovementEnum.mouse_clicked:
                self.movement_state = MovementEnum.position_changed

        return QGraphicsItem.itemChange(self, change, value)

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
                self.create_new_input(inp.type, inp.label,
                                      widget_type=self.parent_node.inputs[i].widget_type,
                                      widget_name=self.parent_node.inputs[i].widget_name,
                                      widget_pos =self.parent_node.inputs[i].widget_pos)

            for o in range(len(self.parent_node.outputs)):
                out = self.parent_node.outputs[o]
                self.create_new_output(out.type, out.label)
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

    # # SHAPE
    def del_and_remove_content_from_scene(self):  # everything get's reset here
        """OLD: SHOULD GET REMOVED, I THINK"""
        for i in range(len(self.inputs)):
            self.del_and_remove_input_from_scene(0)

        for o in range(len(self.outputs)):
            self.del_and_remove_output_from_scene(0)

        # lists are cleared here

        self.width = -1
        self.height = -1

    def compute_content_positions(self):
        """BAD - This might become unnecessary once I implemented use of QGraphicsLayout"""
        for i in self.inputs:
            i.compute_size_and_positions()
        for o in self.outputs:
            o.compute_size_and_positions()

        display_name_height = self.display_name_FM.height()*(self.parent_node.title.count('\n')+1)
        display_name_width = self.display_name_FM.width(get_longest_line(self.parent_node.title))
        display_name_width_extended = self.display_name_FM.width('__' + get_longest_line(self.parent_node.title) + '__')

        # label_FM = QFontMetricsF(self.port_label_font)

        # all sizes and buffers
        space_between_io = 10
        # the following function creates additional space at the top and the bottom of the NI - the more ports, the more space
        left_largest_width = 0
        right_largest_width = 0
        height_buffer_between_ports = 0 #10  # adds vertical buffer between single ports
        horizontal_buffer_to_border = 10  # adds a little bit of space between port and border of the NI
        left_ports_edge_height = -height_buffer_between_ports
        right_ports_edge_height = -height_buffer_between_ports
        for i in self.inputs:
            if i.width > left_largest_width:
                left_largest_width = i.width

            left_ports_edge_height += i.height + height_buffer_between_ports

        for o in self.outputs:
            if o.width > right_largest_width:
                right_largest_width = o.width

            right_ports_edge_height += o.height + height_buffer_between_ports

        ports_edge_height = left_ports_edge_height if left_ports_edge_height > right_ports_edge_height else right_ports_edge_height
        ports_edge_width = left_largest_width + space_between_io + right_largest_width + 2*horizontal_buffer_to_border

        body_height = 0
        body_width = 0
        body_top = 0
        body_left = 0
        body_right = 0

        if self.parent_node.design_style == 'minimalistic':
            height_buffer = 10


            body_height = ports_edge_height if ports_edge_height > display_name_height else display_name_height
            self.height = body_height + height_buffer
            self.width = display_name_width_extended if display_name_width_extended > ports_edge_width else ports_edge_width
            if self.main_widget:
                if self.parent_node.main_widget_pos == 'under ports':
                    self.width = self.width if self.width > self.main_widget.width()+2*horizontal_buffer_to_border else self.main_widget.width()+2*horizontal_buffer_to_border
                    self.height += self.main_widget.height() + height_buffer_between_ports
                elif self.parent_node.main_widget_pos == 'between ports':
                    #self.width += self.main_widget.width()
                    self.width = display_name_width_extended if \
                        display_name_width_extended > ports_edge_width+self.main_widget.width() else \
                        ports_edge_width+self.main_widget.width()
                    self.height = self.height if self.height > self.main_widget.height() + height_buffer else self.main_widget.height() + height_buffer


            body_top = -self.height / 2 + height_buffer / 2
            body_left = -self.width / 2 + horizontal_buffer_to_border
            body_right = self.width / 2 - horizontal_buffer_to_border


        elif self.parent_node.design_style == 'extended':
            header_height = self.get_header_rect().height() #50 * (self.parent_node.title.count('\n')+1)
            vertical_body_buffer = 16  # half above, half below


            body_height = ports_edge_height
            self.height = header_height + body_height + vertical_body_buffer
            self.width = display_name_width_extended if display_name_width_extended > ports_edge_width else ports_edge_width
            if self.main_widget:
                if self.parent_node.main_widget_pos == 'under ports':
                    self.width = self.width if self.width > self.main_widget.width()+2*horizontal_buffer_to_border else self.main_widget.width()+2*horizontal_buffer_to_border
                    self.height += self.main_widget.height() + height_buffer_between_ports
                elif self.parent_node.main_widget_pos == 'between ports':
                    self.width = display_name_width_extended if \
                        display_name_width_extended > ports_edge_width+self.main_widget.width() else \
                        ports_edge_width+self.main_widget.width()
                    self.height = self.height if self.height > self.main_widget.height() + header_height + vertical_body_buffer else \
                                    self.main_widget.height() + header_height + vertical_body_buffer

            body_top = -self.height / 2 + header_height + vertical_body_buffer/2
            body_left = -self.width / 2 + horizontal_buffer_to_border
            body_right = self.width / 2 - horizontal_buffer_to_border

            # here, the width and height are final

        self.set_content_positions(body_height=body_height,
                                   body_top=body_top,
                                   body_left=body_left,
                                   body_right=body_right,
                                   left_ports_edge_height=left_ports_edge_height,
                                   right_ports_edge_height=right_ports_edge_height,
                                   height_buffer_between_ports=height_buffer_between_ports,
                                   left_largest_width=left_largest_width,
                                   right_largest_width=right_largest_width,
                                   space_between_io=space_between_io)

    def set_content_positions(self, body_height, body_top, body_left, body_right, left_ports_edge_height,
                              right_ports_edge_height, height_buffer_between_ports, left_largest_width, right_largest_width,
                              space_between_io):
        """BAD - This might become unnecessary once I implemented use of QGraphicsLayout"""
        # set positions
        # # calculating the vertical space  between two inputs - without their heights, just between them
        space_between_inputs = (body_height - left_ports_edge_height) / (len(self.inputs) - 1) if len(self.inputs) > 2 else body_height - left_ports_edge_height
        offset = 0
        if len(self.inputs) == 1:
            offset = (body_height - left_ports_edge_height) / 2
        for x in range(len(self.inputs)):
            i = self.inputs[x]
            y = body_top + i.height/2 + offset
            port_pos_x = body_left + i.width/2
            port_pos_y = y
            i.gate.setPos(port_pos_x + i.gate.port_local_pos.x(), port_pos_y + i.gate.port_local_pos.y())
            i.label.setPos(port_pos_x + i.label.port_local_pos.x(), port_pos_y + i.label.port_local_pos.y())
            if i.widget:
                # GlobalStorage.debug(self.parent_node.title)
                i.proxy.setPos(port_pos_x + i.widget.port_local_pos.x() - i.widget.width()/2,
                               port_pos_y + i.widget.port_local_pos.y() - i.widget.height()/2)
            offset += i.height + height_buffer_between_ports + space_between_inputs

        space_between_outputs = (body_height - right_ports_edge_height) / (len(self.outputs) - 1) if len(self.outputs) > 2 else body_height - right_ports_edge_height
        offset = 0
        if len(self.outputs) == 1:
            offset = (body_height - right_ports_edge_height) / 2
        for x in range(len(self.outputs)):
            o = self.outputs[x]
            y = body_top + o.height/2 + offset
            port_pos_x = body_right - o.width/2
            port_pos_y = y
            o.gate.setPos(port_pos_x + o.gate.port_local_pos.x(), port_pos_y + o.gate.port_local_pos.y())
            o.label.setPos(port_pos_x + o.label.port_local_pos.x(), port_pos_y + o.label.port_local_pos.y())
            offset += o.height + height_buffer_between_ports + space_between_outputs

        if self.main_widget:
            if self.parent_node.main_widget_pos == 'under ports':
                self.main_widget_proxy.setPos(-self.main_widget.width() / 2,
                                              body_top + body_height + height_buffer_between_ports)  # self.height/2 - height_buffer/2 - self.main_widget.height())
            elif self.parent_node.main_widget_pos == 'between ports':
                body_incl_widget_height = body_height if body_height > self.main_widget.height() else self.main_widget.height()
                self.main_widget_proxy.setPos(body_left + left_largest_width + space_between_io/2, body_top+body_incl_widget_height/2 -self.main_widget.height()/2)

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


    def get_json_data(self):
        """Returns all metadata of the NI including position, package etc. in a JSON-able dict format.
        Used to rebuild the Flow when loading a project."""

        # general attributes
        node_instance_dict = {'parent node title': self.parent_node.title,
                              'parent node type': self.parent_node.type,
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