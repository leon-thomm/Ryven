from PySide2.QtWidgets import QGraphicsItem, QMenu, QGraphicsDropShadowEffect
from PySide2.QtCore import Qt, QRectF
from PySide2.QtGui import QColor

# import custom_src.Console.MainConsole as MainConsole
from ryvencore.NodeInstanceAction import NodeInstanceAction
from ryvencore.NodeInstanceAnimator import NodeInstanceAnimator
from ryvencore.NodeInstanceWidget import NodeInstanceWidget
from ryvencore.global_tools.Debugger import Debugger
from ryvencore.global_tools.MovementEnum import MovementEnum

from ryvencore.PortInstance import InputPortInstance, OutputPortInstance
from ryvencore.retain import M


class NodeInstance(QGraphicsItem):
    def __init__(self, params):
        super(NodeInstance, self).__init__()


        # GENERAL ATTRIBUTES

        # the constructor parameters are stored in a tuple to make the source code of custom NIs cleaner
        parent_node, flow, design, config = params

        self.parent_node = parent_node
        self.flow = flow
        self.session_design = design
        self.script = flow.script
        self.movement_state = None
        self.movement_pos_from = None
        self.painted_once = False
        self.inputs = []
        self.outputs = []
        self.color = QColor(self.parent_node.color)  # manipulated by self.animator

        self.default_actions = {'remove': {'method': self.action_remove},
                                'update shape': {'method': self.update_shape}}
                                # 'console ref': {'method': self.set_console_scope}}  # for context menus
        self.special_actions = {}  # only gets written in custom NodeInstance-subclasses
        self.personal_logs = []

        # 'initializing' will be set to False below. It's needed for the ports setup, to prevent shape updating stuff
        self.initializing = True

        self.temp_state_data = None
        self.init_config = config


        # FLAGS
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)
        self.setAcceptHoverEvents(True)



        # UI
        self.shadow_effect = None
        self.main_widget = None
        if self.parent_node.main_widget_class is not None:
            self.main_widget = self.parent_node.main_widget_class(self)
        self.widget = NodeInstanceWidget(self)  # QGraphicsWidget(self)

        self.animator = NodeInstanceAnimator(self)  # needs self.title_label

        # TOOLTIP
        if self.parent_node.description != '':
            self.setToolTip('<html><head/><body><p>'+self.parent_node.description+'</p></body></html>')
        self.setCursor(Qt.SizeAllCursor)

        # DESIGN THEME
        self.session_design.flow_theme_changed.connect(self.update_design)



    def initialized(self):
        """All ports and the main widget get finally created here."""

        # LOADING CONFIG
        if self.init_config is not None:
            # self.setPos(config['position x'], config['position y'])
            self.setup_ports(self.init_config['inputs'], self.init_config['outputs'])
            if self.main_widget:
                try:
                    self.main_widget.set_data(self.init_config['main widget data'])
                except Exception as e:
                    print('Exception while setting data in', self.parent_node.title, 'NodeInstance\'s main widget:', e,
                          ' (was this intended?)')

            self.special_actions = self.set_special_actions_data(self.init_config['special actions'])
            self.temp_state_data = self.init_config['state data']
        else:
            self.setup_ports()

        # LOADING DATA
        if self.temp_state_data is not None:
            try:
                self.set_data(self.temp_state_data)
            except Exception as e:
                print('Exception while setting data in', self.parent_node.title, 'NodeInstance:', e,
                      ' (was this intended?)')

        self.initializing = False

        # No self.update_shape() here because for some reason, the bounding rect hasn't been initialized yet, so
        # self.update_shape() gets called when the item is being drawn the first time (see paint event in NI painter)
        # TODO: change that ^ once there is a solution for this: https://forum.qt.io/topic/117179/force-qgraphicsitem-to-update-immediately-wait-for-update-event

        self.update_design()  # load current design, update QGraphicsItem

        self.update()  # and finally update the NodeInstance once

    #                        __                             _    __     __
    #              ____ _   / /  ____ _   ____     _____   (_)  / /_   / /_     ____ ___
    #             / __ `/  / /  / __ `/  / __ \   / ___/  / /  / __/  / __ \   / __ `__ \
    #            / /_/ /  / /  / /_/ /  / /_/ /  / /     / /  / /_   / / / /  / / / / / /
    #            \__,_/  /_/   \__, /   \____/  /_/     /_/   \__/  /_/ /_/  /_/ /_/ /_/
    #                         /____/

    def update(self, input_called=-1, output_called=-1):
        """This is the method used to activate a NodeInstance. Note that this signature shadows the update() method from
        QGraphicsItem used to graphically update a QGraphicsItem which can be accessed via
        QGraphicsItem.update(self)."""

        if self.session_design.animations_enabled:
            self.animator.start()

        Debugger.write('update in', self.parent_node.title, 'on input', input_called)
        try:
            self.update_event(input_called)
        except Exception as e:
            Debugger.write_err('EXCEPTION IN', self.parent_node.title, 'NI:', e)

    def update_event(self, input_called=-1):
        """Gets called when an input received a signal. This is where the magic begins in subclasses."""

        pass

    def input(self, index):
        """Returns the value of a data input.
        If the input is connected, the value of the connected output is used:
        If not, the value of the widget is used."""

        Debugger.write('input called in', self.parent_node.title, 'NI:', index)
        return self.inputs[index].get_val()

    def exec_output(self, index):
        """Executes an execution output, sending a signal to all connected execution inputs causing the connected
        NIs to update."""
        self.outputs[index].exec()

    def set_output_val(self, index, val):
        """Sets the value of a data output.
        self.data_outputs_updated() has to be called manually after all values are set."""

        if self.flow.viewport_update_mode == 'async':  # asynchronous viewport updates
            vp = self.flow.viewport()
            vp.repaint(self.flow.mapFromScene(self.sceneBoundingRect()))

        self.outputs[index].set_val(val)

    def remove_event(self):
        """Method to stop all threads in hold of the NI itself."""

        pass

    #                                 _
    #              ____ _   ____     (_)
    #             / __ `/  / __ \   / /
    #            / /_/ /  / /_/ /  / /
    #            \__,_/  / .___/  /_/
    #                   /_/
    #
    # all algorithm-unrelated api methods:

    #   LOGGING
    def new_log(self, title):
        """Requesting a new personal Log. Handy method for subclasses."""
        # new_log = self.script.logger.new_log(self, title)
        new_log = self.script.logger.new_log(title)
        self.personal_logs.append(new_log)
        return new_log

    def disable_logs(self):
        """Disables personal Logs. They remain visible unless the user closes them via the appearing button."""
        for log in self.personal_logs:
            log.disable()

    def enable_logs(self):
        """Resets personal Logs to normal state (hiding close button, changing style sheet)."""
        for log in self.personal_logs:
            log.enable()

    def log_message(self, message: str, target: str):
        """Writes a string to a default log with title target"""

        self.script.logger.log_message(message, target)

    # SHAPE
    def update_shape(self):
        """Causes recompilation of the whole shape."""
        self.widget.update_shape()
        self.flow.viewport().update()


    # PORTS
    def create_new_input(self, type_, label, widget_name=None, widget_pos='under', pos=-1, config=None):
        """Creates and adds a new input. Handy for subclasses."""
        Debugger.write('create_new_input called')
        pi = InputPortInstance(self, type_, label,
                               config_data=config,
                               widget_name=widget_name,
                               widget_pos=widget_pos)
        if pos < -1:
            pos += len(self.inputs)
        if pos == -1:
            self.inputs.append(pi)
            self.widget.add_input_to_layout(pi)
        else:
            self.inputs.insert(pos, pi)
            self.widget.insert_input_into_layout(pos, pi)

        if not self.initializing:
            self.update_shape()
            self.update()

    def delete_input(self, i):
        """Disconnects and removes input. Handy for subclasses."""
        inp: InputPortInstance = None
        if type(i) == int:
            inp = self.inputs[i]
        elif type(i) == InputPortInstance:
            inp = i

        for c in inp.connections:
            self.flow.connect_pins(c.out, inp)

        # for some reason, I have to remove all widget items manually from the scene too. setting the items to
        # ownedByLayout(True) does not work, I don't know why.
        self.scene().removeItem(inp.pin)
        self.scene().removeItem(inp.label)
        if inp.proxy is not None:
            self.scene().removeItem(inp.proxy)

        self.inputs.remove(inp)
        self.widget.remove_input_from_layout(inp)

        if not self.initializing:
            self.update_shape()
            self.update()


    def create_new_output(self, type_, label, pos=-1):
        """Creates and adds a new output. Handy for subclasses."""

        pi = OutputPortInstance(self, type_, label)
        if pos < -1:
            pos += len(self.outputs)
        if pos == -1:
            self.outputs.append(pi)
            self.widget.add_output_to_layout(pi)
        else:
            self.outputs.insert(pos, pi)
            self.widget.insert_output_into_layout(pos, pi)

        if not self.initializing:
            self.update_shape()
            self.update()

    def delete_output(self, o):
        """Disconnects and removes output. Handy for subclasses."""
        out: OutputPortInstance = None
        if type(o) == int:
            out = self.outputs[o]
        elif type(o) == OutputPortInstance:
            out = o

        for cpi in out.connections:
            self.flow.connect_pins(out, cpi)

        # see delete_input() for info!
        self.scene().removeItem(out.pin)
        self.scene().removeItem(out.label)

        self.outputs.remove(out)
        self.widget.remove_output_from_layout(out)

        if not self.initializing:
            self.update_shape()
            self.update()

    # GET, SET DATA
    def get_data(self):
        """
        This method gets subclassed and specified. If the NI has states (so, the behavior depends on certain values),
        all these values must be stored in JSON-able format in a dict here. This dictionary will be used to reload the
        node's state when loading a project or pasting copied/cut nodes in the Flow (the states get copied too), see
        self.set_data(self, data) below.
        Unfortunately, I can't use pickle or something like that due to PySide2 which runs on C++, not Python.
        :return: Dictionary representing all values necessary to determine the NI's current state
        """
        return {}

    def set_data(self, data):
        """
        If the NI has states, it's state should get reloaded here according to what was previously provided by the same
        class in get_data(), see above.
        :param data: Dictionary representing all values necessary to determine the NI's current state
        """
        pass

    def session_stylesheet(self):
        return self.session_design.global_stylesheet

    # VARIABLES

    def get_vars_manager(self):
        return self.script.vars_manager

    def get_var_val(self, name):
        return self.get_vars_manager().get_var_val(name)

    def set_var_val(self, name, val):
        return self.get_vars_manager().set_var(name, val)

    def register_var_receiver(self, name, method):
        self.get_vars_manager().register_receiver(self, name, method)

    def unregister_var_receiver(self, name):
        self.get_vars_manager().unregister_receiver(self, name)

    # --------------------------------------------------------------------------------------
    # UI STUFF ----------------------------------------

    # def set_console_scope(self):
    #     # extensive_dict = {}  # unlike self.__dict__, it also includes methods to call! :)
    #     # for att in dir(self):
    #     #     extensive_dict[att] = getattr(self, att)
    #     MainConsole.main_console.add_obj_context(self)

    def update_design(self):
        """Loads the shadow effect option and causes redraw with active theme."""

        if self.session_design.node_instance_shadows_shown:
            self.shadow_effect = QGraphicsDropShadowEffect()
            self.shadow_effect.setXOffset(12)
            self.shadow_effect.setYOffset(12)
            self.shadow_effect.setBlurRadius(20)
            self.shadow_effect.setColor(QColor('#2b2b2b'))
            self.setGraphicsEffect(self.shadow_effect)
        else:
            self.setGraphicsEffect(None)

        self.widget.update()
        self.animator.reload_values()

        QGraphicsItem.update(self)

    def boundingRect(self):
        # remember: (0, 0) shall be the NI's center!
        rect = QRectF()
        w = self.widget.layout().geometry().width()
        h = self.widget.layout().geometry().height()
        rect.setLeft(-w/2)
        rect.setTop(-h/2)
        rect.setWidth(w)
        rect.setHeight(h)
        return rect

    #   PAINTING
    def paint(self, painter, option, widget=None):
        """All painting is done by NodeInstancePainter"""

        # in order to access a meaningful geometry of GraphicsWidget contents in update_shape(), the paint event
        # has to be called once. See here:
        # https://forum.qt.io/topic/117179/force-qgraphicsitem-to-update-immediately-wait-for-update-event/4
        if not self.painted_once:

            # ok, quick notice. Since I am using a NodeInstanceWidget, calling self.update_design() here (again)
            # leads to a QT crash without error, which is really strange. Calling update_design multiple times
            # principally isn't a problem, but, for some reason, here it leads to a crash in QT. It's not necessary
            # anymore, so I just removed it.
            # self.update_design()

            self.update_shape()
            self.update_conn_pos()

        self.session_design.flow_theme.node_inst_painter.paint_NI(
            design_style=self.parent_node.design_style,
            painter=painter,
            option=option,
            c=self.color,
            w=self.boundingRect().width(),
            h=self.boundingRect().height(),
            bounding_rect=self.boundingRect(),
            title_rect=self.widget.title_label.boundingRect()
        )

        self.painted_once = True

    def get_context_menu(self):
        menu = QMenu(self.flow)

        for a in self.get_actions(self.get_extended_default_actions(), menu):  # menu needed for 'parent'
            if type(a) == NodeInstanceAction:
                menu.addAction(a)
            elif type(a) == QMenu:
                menu.addMenu(a)

        menu.addSeparator()

        actions = self.get_actions(self.special_actions, menu)
        for a in actions:  # menu needed for 'parent'
            if type(a) == NodeInstanceAction:
                menu.addAction(a)
            elif type(a) == QMenu:
                menu.addMenu(a)

        return menu

    def itemChange(self, change, value):
        """This method ensures that all connections, selection borders etc. that get drawn in the Flow are constantly
        redrawn during a NI drag. Also updates the positions of connections"""

        if change == QGraphicsItem.ItemPositionChange:
            if self.session_design.performance_mode == 'pretty':
                self.flow.viewport().update()
            if self.movement_state == MovementEnum.mouse_clicked:
                self.movement_state = MovementEnum.position_changed

        self.update_conn_pos()

        return QGraphicsItem.itemChange(self, change, value)

    def update_conn_pos(self):
        """Updates the global positions of connections at outputs"""
        for o in self.outputs:
            for c in o.connections:
                c.update_pos()

    def hoverEnterEvent(self, event):
        self.widget.title_label.set_NI_hover_state(hovering=True)
        QGraphicsItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.widget.title_label.set_NI_hover_state(hovering=False)
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
                action.triggered_with_data.connect(method)  # see NodeInstanceAction for explanation
                action.triggered_without_data.connect(method)  # see NodeInstanceAction for explanation
                actions.append(action)
            except KeyError:
                action_menu = QMenu(k, menu)
                sub_actions = self.get_actions(v_dict, action_menu)
                for a in sub_actions:
                    action_menu.addAction(a)
                actions.append(action_menu)

        return actions

    def action_remove(self):
        self.flow.remove_node_instance_triggered(self)

    def get_special_actions_data(self, actions):
        cleaned_actions = actions.copy()
        for key in cleaned_actions:
            v = cleaned_actions[key]
            if type(v) == M:  # callable(v):
                cleaned_actions[key] = v.method_name
            elif callable(v):
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
                if key == 'method':
                    try:
                        actions['method'] = M(getattr(self, actions_data[key]))
                    except AttributeError:  # outdated method referenced
                        pass
                elif key == 'data':
                    actions['data'] = actions_data[key]
            else:
                actions[key] = self.set_special_actions_data(actions_data[key])
        return actions

    # PORTS
    def setup_ports(self, inputs_config=None, outputs_config=None):
        if not inputs_config and not outputs_config:
            for i in range(len(self.parent_node.inputs)):
                inp = self.parent_node.inputs[i]
                self.create_new_input(inp.type_, inp.label,
                                      widget_name=self.parent_node.inputs[i].widget_name,
                                      widget_pos =self.parent_node.inputs[i].widget_pos)

            for o in range(len(self.parent_node.outputs)):
                out = self.parent_node.outputs[o]
                self.create_new_output(out.type_, out.label)
        else:  # when loading saved NIs, the port instances might not be synchronised to the parent's ports anymore
            for inp in inputs_config:
                has_widget = inp['has widget']

                self.create_new_input(inp['type'], inp['label'],
                                      widget_name=inp['widget name'] if has_widget else None,
                                      widget_pos =inp['widget position'] if has_widget else None,
                                      config=inp['widget data'] if has_widget else None)

            for out in outputs_config:
                self.create_new_output(out['type'], out['label'])

    # def get_input_widget_class(self, widget_name):
    #     """Returns a reference to the widget class of a given name for instantiation."""
    #     custom_node_input_widget_classes = self.script.main_window.custom_node_input_widget_classes
    #     widget_class = custom_node_input_widget_classes[self.parent_node][widget_name]
    #     return widget_class

    def add_input_to_scene(self, i):
        self.flow.scene().addItem(i.pin)
        self.flow.scene().addItem(i.label)
        if i.widget:
            self.flow.scene().addItem(i.proxy)

    def del_and_remove_input_from_scene(self, i_index):
        inp = self.inputs[i_index]
        for c in self.inputs[i_index].connections:
            self.flow.connect_pins(c.out, inp)

        self.flow.scene().removeItem(inp.pin)
        self.flow.scene().removeItem(inp.label)
        if inp.widget:
            self.flow.scene().removeItem(inp.proxy)
            inp.widget.remove_event()
        self.inputs.remove(inp)


    def add_output_to_scene(self, o):
        self.flow.scene().addItem(o.pin)
        self.flow.scene().addItem(o.label)

    def del_and_remove_output_from_scene(self, o_index):
        out = self.outputs[o_index]
        for c in self.outputs[o_index].connections:
            self.flow.connect_pins(out, c.inp)

        self.flow.scene().removeItem(out.pin)
        self.flow.scene().removeItem(out.label)
        self.outputs.remove(out)

    # GENERAL
    def about_to_remove_from_scene(self):
        """Called from Flow when the NI gets removed from the scene
        to stop all running threads and disable personal logs."""

        if self.main_widget:
            self.main_widget.remove_event()
        self.remove_event()

        self.disable_logs()

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

    def config_data(self):
        """Returns all metadata of the NI including position, package etc. in a JSON-able dict format.
        Used to rebuild the Flow when loading a project."""

        # general attributes
        node_instance_dict = {'parent node title': self.parent_node.title,
                              'parent node type': self.parent_node.type_,
                              # 'parent node package': self.parent_node.package,
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
            input_dict = i.config_data()
            node_instance_inputs_list.append(input_dict)
        node_instance_dict['inputs'] = node_instance_inputs_list

        # outputs
        node_instance_outputs_list = []
        for o in self.outputs:
            output_dict = o.config_data()
            node_instance_outputs_list.append(output_dict)
        node_instance_dict['outputs'] = node_instance_outputs_list

        return node_instance_dict