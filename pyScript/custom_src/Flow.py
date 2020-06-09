from PySide2.QtWidgets import QGraphicsView, QGraphicsScene, QListWidgetItem, QShortcut, QMenu, QGraphicsItem, \
    QUndoStack
from PySide2.QtGui import QPainter, QPainterPath, QPen, QColor, QRadialGradient, QKeySequence, QTabletEvent, \
    QImage, QGuiApplication
from PySide2.QtCore import Qt, QPointF, QPoint, QRectF, QSizeF
import math, json

from custom_src.GlobalAccess import GlobalStorage, find_type_in_object, pythagoras, find_type_in_objects

from custom_src.FlowCommands import MoveComponents_Command, PlaceNodeInstanceInScene_Command, \
    PlaceDrawingObject_Command, RemoveComponents_Command, ConnectGates_Command, Paste_Command
from custom_src.FlowProxyWidget import FlowProxyWidget
from custom_src.Node import Node
from custom_src.NodeInstance import NodeInstance
from custom_src.PortInstance import PortInstance, PortInstanceGate
from custom_src.NodeChoiceWidget.NodeChoiceWidget import NodeChoiceWidget
from custom_src.DrawingObject import DrawingObject
from custom_src.FlowStylusModesWidget import FlowStylusModesWidget
from custom_src.FlowZoomWidget import FlowZoomWidget


class Flow(QGraphicsView):
    def __init__(self, main_window, parent_script, config=None):
        super(Flow, self).__init__()

        # SHORTCUTS
        place_new_node_shortcut = QShortcut(QKeySequence('Shift+P'), self)
        place_new_node_shortcut.activated.connect(self.place_new_node_by_shortcut)
        move_selected_nodes_left_shortcut = QShortcut(QKeySequence('Shift+Left'), self)
        move_selected_nodes_left_shortcut.activated.connect(self.move_selected_nodes_left)
        move_selected_nodes_up_shortcut = QShortcut(QKeySequence('Shift+Up'), self)
        move_selected_nodes_up_shortcut.activated.connect(self.move_selected_nodes_up)
        move_selected_nodes_right_shortcut = QShortcut(QKeySequence('Shift+Right'), self)
        move_selected_nodes_right_shortcut.activated.connect(self.move_selected_nodes_right)
        move_selected_nodes_down_shortcut = QShortcut(QKeySequence('Shift+Down'), self)
        move_selected_nodes_down_shortcut.activated.connect(self.move_selected_nodes_down)
        select_all_shortcut = QShortcut(QKeySequence('Ctrl+A'), self)
        select_all_shortcut.activated.connect(self.select_all)
        copy_shortcut = QShortcut(QKeySequence.Copy, self)
        copy_shortcut.activated.connect(self.copy)
        cut_shortcut = QShortcut(QKeySequence.Cut, self)
        cut_shortcut.activated.connect(self.cut)
        paste_shortcut = QShortcut(QKeySequence.Paste, self)
        paste_shortcut.activated.connect(self.paste)

        # UNDO/REDO
        self.undo_stack = QUndoStack(self)
        self.undo_action = self.undo_stack.createUndoAction(self, 'undo')
        self.undo_action.setShortcuts(QKeySequence.Undo)
        self.redo_action = self.undo_stack.createRedoAction(self, 'redo')
        self.redo_action.setShortcuts(QKeySequence.Redo)

        undo_shortcut = QShortcut(QKeySequence.Undo, self)
        undo_shortcut.activated.connect(self.undo_activated)
        redo_shortcut = QShortcut(QKeySequence.Redo, self)
        redo_shortcut.activated.connect(self.redo_activated)

        # GENERAL ATTRIBUTES
        self.parent_script = parent_script
        self.all_node_instances: [NodeInstance] = []
        self.all_node_instance_classes = main_window.all_node_instance_classes  # ref
        self.all_nodes = main_window.all_nodes  # ref
        self.gate_selected: PortInstanceGate = None
        self.dragging_connection = False
        self.ignore_mouse_event = False  # for stylus - see tablet event
        self.last_mouse_move_pos: QPointF = None
        self.node_place_pos = QPointF()
        self.left_mouse_pressed_in_flow = False
        self.mouse_press_pos: QPointF = None
        self.tablet_press_pos: QPointF = None
        self.last_tablet_move_pos: QPointF = None
        self.auto_connection_gate = None  # stores the gate that we may try to auto connect to a newly placed NI
        self.pan = False
        self.pan_start_x = None
        self.pan_start_y = None
        self.current_scale = 1
        self.total_scale_div = 1

        # CREATE UI
        scene = QGraphicsScene(self)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(0, 0, 10 * self.width(), 10 * self.height())

        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self.setAcceptDrops(True)

        self.centerOn(QPointF(self.viewport().width() / 2, self.viewport().height() / 2))

        # NODE CHOICE WIDGET
        self.node_choice_proxy = FlowProxyWidget(self)
        self.node_choice_widget = NodeChoiceWidget(self, main_window.all_nodes)  # , main_window.node_images)
        self.node_choice_proxy.setWidget(self.node_choice_widget)
        self.scene().addItem(self.node_choice_proxy)
        self.node_choice_proxy.setZValue(1000)
        self.hide_node_choice_widget()

        # ZOOM WIDGET
        self.zoom_proxy = FlowProxyWidget(self)
        self.zoom_proxy.setFlag(QGraphicsItem.ItemIgnoresTransformations, True)
        self.zoom_widget = FlowZoomWidget(self)
        self.zoom_proxy.setWidget(self.zoom_widget)
        self.scene().addItem(self.zoom_proxy)
        self.set_zoom_proxy_pos()

        # STYLUS
        self.stylus_mode = ''
        self.current_drawing = None
        self.drawing = None
        self.drawings = []
        self.stylus_modes_proxy = FlowProxyWidget(self)
        self.stylus_modes_proxy.setFlag(QGraphicsItem.ItemIgnoresTransformations, True)
        self.stylus_modes_widget = FlowStylusModesWidget(self)
        self.stylus_modes_proxy.setWidget(self.stylus_modes_widget)
        self.scene().addItem(self.stylus_modes_proxy)
        self.set_stylus_proxy_pos()

        if config:
            node_instances = self.place_nodes_from_config(config['nodes'])
            self.connect_nodes_from_config(node_instances, config['connections'])
            if list(config.keys()).__contains__('drawings'):
                # the if is here just because it's very new feature and not all project files have drawings arr just yet
                self.place_drawings_from_config(config['drawings'])
            self.undo_stack.clear()

    def design_style_changed(self):
        self.viewport().update()

    def contextMenuEvent(self, event):
        QGraphicsView.contextMenuEvent(self, event)
        # in the case of the menu already being shown by a widget under the mouse, the event is accepted here
        if event.isAccepted():
            return

        for i in self.items(event.pos()):
            if find_type_in_object(i, NodeInstance):
                ni: NodeInstance = i
                menu: QMenu = ni.get_context_menu()
                menu.exec_(event.globalPos())
                event.accept()

    def undo_activated(self):
        """Triggered by ctrl+z"""
        self.undo_stack.undo()
        self.viewport().update()

    def redo_activated(self):
        """Triggered by ctrl+y"""
        self.undo_stack.redo()
        self.viewport().update()

    def mousePressEvent(self, event):
        GlobalStorage.debug('mouse press event received, point:', event.pos())

        # there might be a proxy widget meant to receive the event instead of the flow
        QGraphicsView.mousePressEvent(self, event)

        if self.ignore_mouse_event:
            self.ignore_mouse_event = False
            return

        if event.button() == Qt.LeftButton:
            if self.node_choice_proxy.isVisible():
                self.hide_node_choice_widget()
            else:
                for i in self.items(event.pos()):
                    if find_type_in_object(i, PortInstanceGate):
                        self.gate_selected = i
                        self.dragging_connection = True
                        break

            self.left_mouse_pressed_in_flow = True

        elif event.button() == Qt.RightButton:
            if len(self.items(event.pos())) == 0:
                self.node_choice_widget.reset_list()
                self.show_node_choice_widget(event.pos())

        elif event.button() == Qt.MidButton:
            self.pan = True
            self.pan_start_x = event.x()
            self.pan_start_y = event.y()
            event.accept()

        self.mouse_press_pos = self.mapToScene(event.pos())

    def mouseMoveEvent(self, event):

        QGraphicsView.mouseMoveEvent(self, event)

        if self.pan:  # middle mouse pressed
            self.horizontalScrollBar().setValue(self.horizontalScrollBar().value() - (event.x() - self.pan_start_x))
            self.verticalScrollBar().setValue(self.verticalScrollBar().value() - (event.y() - self.pan_start_y))
            self.pan_start_x = event.x()
            self.pan_start_y = event.y()
            event.accept()

        self.last_mouse_move_pos = self.mapToScene(event.pos())

        if self.dragging_connection:
            self.viewport().repaint()

    def mouseReleaseEvent(self, event):
        # there might be a proxy widget meant to receive the event instead of the flow
        QGraphicsView.mouseReleaseEvent(self, event)

        if event.button() == Qt.RightButton:
            return
        elif event.button() == Qt.MidButton:
            self.pan = False

        if self.ignore_mouse_event or not self.left_mouse_pressed_in_flow:  # for stylus (see tablet event)
            self.ignore_mouse_event = False
            return

        # connection dropped over specific gate
        if self.dragging_connection and self.itemAt(event.pos()) and \
                find_type_in_object(self.itemAt(event.pos()), PortInstanceGate):
            self.connect_gates__cmd(self.gate_selected, self.itemAt(event.pos()))

        # connection dropped over NodeInstance - auto connect
        elif self.dragging_connection and find_type_in_objects(self.items(event.pos()), NodeInstance):
            # find node instance
            ni_under_drop = None
            for item in self.items(event.pos()):
                if find_type_in_object(item, NodeInstance):
                    ni_under_drop = item
                    break
            # connect
            self.try_conn_gate_and_ni(self.gate_selected, ni_under_drop)

        # connection dropped somewhere else - show node choice widget
        elif self.dragging_connection:
            self.auto_connection_gate = self.gate_selected
            self.show_node_choice_widget(event.pos())

        self.left_mouse_pressed_in_flow = False
        self.dragging_connection = False
        self.gate_selected = None

        self.viewport().repaint()

    def keyPressEvent(self, event):
        QGraphicsView.keyPressEvent(self, event)

        if event.key() == Qt.Key_Escape:  # do I need that... ?
            self.clearFocus()
            self.setFocus()
            return True

        elif event.key() == Qt.Key_Delete:
            self.remove_selected_components()

    def wheelEvent(self, event):
        if event.modifiers() == Qt.CTRL and event.angleDelta().x() == 0:
            self.zoom(event.pos(), self.mapToScene(event.pos()), event.angleDelta().y())
            event.accept()
            return True

        QGraphicsView.wheelEvent(self, event)

    def tabletEvent(self, event):
        """tabletEvent gets called by stylus operations."""

        if event.type() == QTabletEvent.TabletPress:
            self.tablet_press_pos = event.pos()

            if event.buttons() == Qt.LeftButton:
                if self.stylus_mode == 'comment':
                    new_drawing = self.create_and_place_drawing__cmd(self.mapToScene(self.tablet_press_pos))
                    self.current_drawing = new_drawing
                    self.drawing = True
            elif event.buttons() == Qt.RightButton:
                self.pan = True
                self.last_tablet_move_pos = self.mapToScene(event.pos())

        elif event.type() == QTabletEvent.TabletMove:
            if event.pointerType() == QTabletEvent.Eraser:
                if self.stylus_mode == 'comment':
                    for i in self.items(event.pos()):
                        if find_type_in_object(i, DrawingObject):
                            self.remove_drawing(i)
                            break
            elif self.stylus_mode == 'comment' and self.drawing:
                self.current_drawing.try_to_append_point(self.mapToScene(event.pos()) - self.current_drawing.pos())
                self.current_drawing.stroke_weights.append(event.pressure())
                self.current_drawing.update()
                self.viewport().update()
            elif self.stylus_mode == 'comment' and self.pan and self.last_tablet_move_pos:
                x_diff = self.mapToScene(event.pos()).x() - self.last_tablet_move_pos.x()
                y_diff = self.mapToScene(event.pos()).y() - self.last_tablet_move_pos.y()
                current_center_x = self.mapToScene(self.viewport().pos()).x() + (
                            self.viewport().width() * self.total_scale_div) / 2
                current_center_y = self.mapToScene(self.viewport().pos()).y() + (
                            self.viewport().height() * self.total_scale_div) / 2
                new_center = QPoint(current_center_x - x_diff,
                                    current_center_y - y_diff)
                self.centerOn(new_center)

            self.last_tablet_move_pos = self.mapToScene(event.pos())

        elif event.type() == QTabletEvent.TabletRelease:
            if self.stylus_mode == 'comment' and self.drawing:
                GlobalStorage.debug('drawing obj finished')
                self.current_drawing.finished()
                self.current_drawing = None
                self.drawing = False

        event.accept()
        if not self.stylus_mode == 'edit':
            self.ignore_mouse_event = True  # accepting the event is not enough even though the docs say it would be...
        return True  # do I really need that ?

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('text/plain'):
            event.acceptProposedAction()

    def dropEvent(self, event):
        text = event.mimeData().text()
        item: QListWidgetItem = event.mimeData()
        GlobalStorage.debug('drop received in Flow:', text)

        # j_obj = json.loads(text)
        # if j_obj['type'] == 'variable':
        # TODO: implement variable drag and drop into the scene - show NodeChoiceWidget with get and set

    def drawBackground(self, painter, rect):
        painter.fillRect(rect.intersected(self.sceneRect()), QColor('#333333'))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.sceneRect())

        self.set_stylus_proxy_pos()  # has to be called here instead of in drawForeground to prevent lagging
        self.set_zoom_proxy_pos()

    def drawForeground(self, painter, rect):
        """Draws all connections and borders around selected items."""

        pen = QPen()
        if GlobalStorage.storage['design style'] == 'dark std':
            # pen.setColor('#BCBBF2')
            pen.setWidth(5)
            pen.setCapStyle(Qt.RoundCap)
        elif GlobalStorage.storage['design style'] == 'dark tron':
            # pen.setColor('#452666')
            pen.setWidth(4)
            pen.setCapStyle(Qt.RoundCap)

        # DRAW CONNECTIONS
        for ni in self.all_node_instances:
            for o in ni.outputs:
                for cpi in o.connected_port_instances:
                    if o.type_ == 'data':
                        pen.setStyle(Qt.DashLine)
                    elif o.type_ == 'exec':
                        pen.setStyle(Qt.SolidLine)
                    path = self.connection_path(ni.pos() + o.gate.pos(),
                                                cpi.parent_node_instance.pos() + cpi.gate.pos())
                    w = path.boundingRect().width()
                    h = path.boundingRect().height()
                    gradient = QRadialGradient(path.boundingRect().center(),
                                               pythagoras(w, h) / 2)
                    r = 0
                    g = 0
                    b = 0
                    if GlobalStorage.storage['design style'] == 'dark std':
                        r = 188
                        g = 187
                        b = 242
                    elif GlobalStorage.storage['design style'] == 'dark tron':
                        r = 0
                        g = 120
                        b = 180
                    gradient.setColorAt(0.0, QColor(r, g, b, 255))
                    gradient.setColorAt(0.75, QColor(r, g, b, 200))
                    gradient.setColorAt(0.95, QColor(r, g, b, 0))
                    gradient.setColorAt(1.0, QColor(r, g, b, 0))
                    pen.setBrush(gradient)
                    painter.setPen(pen)
                    painter.drawPath(path)

        # DRAW CURRENTLY DRAGGED CONNECTION
        if self.dragging_connection:
            pen = QPen('#101520')
            pen.setWidth(3)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)
            gate_pos = self.gate_selected.parent_node_instance.pos() + self.gate_selected.pos()
            if self.gate_selected.parent_port_instance.direction == 'output':
                painter.drawPath(
                    self.connection_path(gate_pos,
                                         self.last_mouse_move_pos)
                )
            else:
                painter.drawPath(
                    self.connection_path(self.last_mouse_move_pos, gate_pos)
                )

        # DRAW SELECTED NIs BORDER
        for ni in self.selected_node_instances():
            pen = QPen(QColor('#245d75'))
            pen.setWidth(3)
            painter.setPen(pen)
            painter.setBrush(Qt.NoBrush)

            size_factor = 1.2
            x = ni.pos().x() - ni.width / 2 * size_factor
            y = ni.pos().y() - ni.height / 2 * size_factor
            w = ni.width * size_factor
            h = ni.height * size_factor
            painter.drawRoundedRect(x, y, w, h, 10, 10)

        # DRAW SELECTED DRAWINGS BORDER
        for p_o in self.selected_drawings():
            pen = QPen(QColor('#a3cc3b'))
            pen.setWidth(2)
            painter.setPen(pen)
            painter.setBrush(Qt.NoBrush)

            size_factor = 1.05
            x = p_o.pos().x() - p_o.width / 2 * size_factor
            y = p_o.pos().y() - p_o.height / 2 * size_factor
            w = p_o.width * size_factor
            h = p_o.height * size_factor
            painter.drawRoundedRect(x, y, w, h, 6, 6)
            painter.drawEllipse(p_o.pos().x(), p_o.pos().y(), 2, 2)

    def get_viewport_img(self):
        self.hide_proxies()
        img = QImage(self.viewport().rect().width(), self.viewport().height(), QImage.Format_ARGB32)
        img.fill(Qt.transparent)

        painter = QPainter(img)
        painter.setRenderHint(QPainter.Antialiasing)
        self.render(painter, self.viewport().rect(), self.viewport().rect())
        self.show_proxies()
        return img

    def get_whole_scene_img(self):
        self.hide_proxies()
        img = QImage(self.sceneRect().width() / self.total_scale_div, self.sceneRect().height() / self.total_scale_div,
                     QImage.Format_RGB32)
        img.fill(Qt.transparent)

        painter = QPainter(img)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = QRectF()
        rect.setLeft(-self.viewport().pos().x())
        rect.setTop(-self.viewport().pos().y())
        rect.setWidth(img.rect().width())
        rect.setHeight(img.rect().height())
        # rect is right... but it only renders from the viewport's point down-and rightwards, not from topleft (0,0) ...
        self.render(painter, rect, rect.toRect())
        self.show_proxies()
        return img

    # PROXY POSITIONS
    def set_zoom_proxy_pos(self):
        self.zoom_proxy.setPos(self.mapToScene(self.viewport().width() - self.zoom_widget.width(), 0))

    def set_stylus_proxy_pos(self):
        self.stylus_modes_proxy.setPos(
            self.mapToScene(self.viewport().width() - self.stylus_modes_widget.width() - self.zoom_widget.width(), 0))

    def hide_proxies(self):
        self.stylus_modes_proxy.hide()
        self.zoom_proxy.hide()

    def show_proxies(self):
        self.stylus_modes_proxy.show()
        self.zoom_proxy.show()

    # NODE CHOICE WIDGET
    def show_node_choice_widget(self, pos):
        """Opens the node choice dialog in the scene."""

        # calculating position
        self.node_place_pos = self.mapToScene(pos)
        dialog_pos = QPoint(pos.x() + 1, pos.y() + 1)

        # ensure that the node_choice_widget stays in the viewport
        if dialog_pos.x() + self.node_choice_widget.width() / self.total_scale_div > self.viewport().width():
            dialog_pos.setX(dialog_pos.x() - (
                        dialog_pos.x() + self.node_choice_widget.width() / self.total_scale_div - self.viewport().width()))
        if dialog_pos.y() + self.node_choice_widget.height() / self.total_scale_div > self.viewport().height():
            dialog_pos.setY(dialog_pos.y() - (
                        dialog_pos.y() + self.node_choice_widget.height() / self.total_scale_div - self.viewport().height()))
        dialog_pos = self.mapToScene(dialog_pos)

        # open nodes dialog
        # the dialog emits 'node_chosen' which is connected to self.place_node,
        # so this all continues at self.place_node below
        self.node_choice_widget.update_view()
        self.node_choice_proxy.setPos(dialog_pos)
        self.node_choice_proxy.show()
        self.node_choice_widget.refocus()

    def hide_node_choice_widget(self):
        self.node_choice_proxy.hide()
        self.node_choice_widget.clearFocus()
        self.auto_connection_gate = None

    # ZOOM
    def zoom_in(self, amount):
        local_viewport_center = QPoint(self.viewport().width() / 2, self.viewport().height() / 2)
        self.zoom(local_viewport_center, self.mapToScene(local_viewport_center), amount)

    def zoom_out(self, amount):
        local_viewport_center = QPoint(self.viewport().width() / 2, self.viewport().height() / 2)
        self.zoom(local_viewport_center, self.mapToScene(local_viewport_center), -amount)

    def zoom(self, p_abs, p_mapped, angle):
        by = 0
        velocity = 2 * (1 / self.current_scale) + 0.5
        if velocity > 3:
            velocity = 3

        direction = ''
        if angle > 0:
            by = 1 + (angle / 360 * 0.1 * velocity)
            direction = 'in'
        elif angle < 0:
            by = 1 - (-angle / 360 * 0.1 * velocity)
            direction = 'out'
        else:
            by = 1

        scene_rect_width = self.mapFromScene(self.sceneRect()).boundingRect().width()
        scene_rect_height = self.mapFromScene(self.sceneRect()).boundingRect().height()

        if direction == 'in':
            if self.current_scale * by < 3:
                self.scale(by, by)
                self.current_scale *= by
        elif direction == 'out':
            if scene_rect_width * by >= self.viewport().size().width() and scene_rect_height * by >= self.viewport().size().height():
                self.scale(by, by)
                self.current_scale *= by

        w = self.viewport().width()
        h = self.viewport().height()
        wf = self.mapToScene(QPoint(w - 1, 0)).x() - self.mapToScene(QPoint(0, 0)).x()
        hf = self.mapToScene(QPoint(0, h - 1)).y() - self.mapToScene(QPoint(0, 0)).y()
        lf = p_mapped.x() - p_abs.x() * wf / w
        tf = p_mapped.y() - p_abs.y() * hf / h

        self.ensureVisible(lf, tf, wf, hf, 0, 0)

        target_rect = QRectF(QPointF(lf, tf),
                             QSizeF(wf, hf))
        self.total_scale_div = target_rect.width() / self.viewport().width()

        self.ensureVisible(target_rect, 0, 0)

    # NODE PLACING: -----
    def create_node_instance(self, node, config):
        return self.get_node_instance_class_from_node(node)(node, self, config)

    def add_node_instance(self, ni, pos=None):
        self.scene().addItem(ni)
        ni.enable_personal_logs()
        if pos:
            ni.setPos(pos)
        ni.compute_content_positions()

        # select new NI
        self.scene().clearSelection()
        ni.setSelected(True)

        self.all_node_instances.append(ni)

    def remove_node_instance(self, ni):
        ni.about_to_remove_from_scene()  # to stop running threads

        self.scene().removeItem(ni)

        GlobalStorage.debug('calling ni removed')
        self.all_node_instances.remove(ni)

    def place_new_node_by_shortcut(self):  # Shift+P
        point_in_viewport = None
        selected_NIs = self.selected_node_instances()
        if len(selected_NIs) > 0:
            x = selected_NIs[-1].pos().x() + 150
            y = selected_NIs[-1].pos().y()
            self.node_place_pos = QPointF(x, y)
            point_in_viewport = self.mapFromScene(QPoint(x, y))
        else:  # place in center
            viewport_x = self.viewport().width() / 2
            viewport_y = self.viewport().height() / 2
            point_in_viewport = QPointF(viewport_x, viewport_y).toPoint()
            self.node_place_pos = self.mapToScene(point_in_viewport)

        self.node_choice_widget.reset_list()
        self.show_node_choice_widget(point_in_viewport)

    def place_nodes_from_config(self, nodes_config, offset_pos: QPoint = QPoint(0, 0)):
        new_node_instances = []

        for n_c in nodes_config:
            # find parent node by title, type, package name and description as identifiers
            parent_node_title = n_c['parent node title']
            parent_node_package_name = n_c['parent node package']
            parent_node = None
            for pn in self.all_nodes:
                pn: Node = pn
                if pn.title == parent_node_title and \
                        pn.package == parent_node_package_name:
                    parent_node = pn
                    break

            new_NI = self.create_node_instance(parent_node, n_c)
            self.add_node_instance(new_NI, QPoint(n_c['position x'], n_c['position y']) + offset_pos)
            new_node_instances.append(new_NI)

        return new_node_instances

    def place_node__cmd(self, node: Node, config=None):

        new_NI = self.create_node_instance(node, config)

        place_command = PlaceNodeInstanceInScene_Command(self, new_NI, self.node_place_pos)

        self.undo_stack.push(place_command)

        if self.auto_connection_gate:
            self.try_conn_gate_and_ni(self.auto_connection_gate, place_command.node_instance)

        return place_command.node_instance

    def remove_node_instance_triggered(self, node_instance):  # called from context menu from NodeInstance
        if node_instance in self.selected_node_instances():
            self.remove_selected_components()
        else:
            self.remove_node_instance(node_instance)

    def get_node_instance_class_from_node(self, node):
        return self.all_node_instance_classes[node]

    def get_custom_input_widget_classes(self):
        return self.parent_script.main_window.custom_node_input_widget_classes

    def connect_nodes_from_config(self, node_instances, connections_config):
        for c in connections_config:
            c_parent_node_instance_index = c['parent node instance index']
            c_output_port_index = c['output port index']
            c_connected_node_instance = c['connected node instance']
            c_connected_input_port_index = c['connected input port index']

            if c_connected_node_instance is not None:  # which can be the case when pasting
                parent_node_instance = node_instances[c_parent_node_instance_index]
                connected_node_instance = node_instances[c_connected_node_instance]

                self.connect_gates(parent_node_instance.outputs[c_output_port_index].gate,
                                   connected_node_instance.inputs[c_connected_input_port_index].gate)

    # DRAWINGS
    def create_drawing(self, config=None):
        new_drawing = DrawingObject(self, config)
        return new_drawing

    def add_drawing(self, drawing_obj, pos=None):
        self.scene().addItem(drawing_obj)
        if pos:
            drawing_obj.setPos(pos)
        self.drawings.append(drawing_obj)

    def remove_drawing(self, drawing):
        self.scene().removeItem(drawing)
        self.drawings.remove(drawing)

    def place_drawings_from_config(self, drawings, offset_pos=QPoint(0, 0)):
        new_drawings = []
        for d in drawings:
            x = d['pos x']
            y = d['pos y']
            new_drawing = self.create_drawing(d['points'])
            new_drawings.append(new_drawing)

        return new_drawings

    def create_and_place_drawing__cmd(self, pos, config=None):
        new_drawing_obj = self.create_drawing(config)
        place_command = PlaceDrawingObject_Command(self, pos, new_drawing_obj)
        self.undo_stack.push(place_command)
        return new_drawing_obj

    def move_selected_copmonents__cmd(self, x, y):
        new_rel_pos = QPointF(x, y)

        # if one node item would leave the scene (f.ex. pos.x < 0), stop
        left = False
        for i in self.scene().selectedItems():
            new_pos = i.pos() + new_rel_pos
            if new_pos.x() - i.width / 2 < 0 or \
                    new_pos.x() + i.width / 2 > self.scene().width() or \
                    new_pos.y() - i.height / 2 < 0 or \
                    new_pos.y() + i.height / 2 > self.scene().height():
                left = True
                break

        if not left:
            # moving the items
            items_group = self.scene().createItemGroup(self.scene().selectedItems())
            items_group.moveBy(new_rel_pos.x(), new_rel_pos.y())
            self.scene().destroyItemGroup(items_group)

            # saving the command
            self.undo_stack.push(
                MoveComponents_Command(self, self.scene().selectedItems(), p_from=-new_rel_pos, p_to=QPointF(0, 0))
            )

        self.viewport().repaint()

    def move_selected_nodes_left(self):
        self.move_selected_copmonents__cmd(-40, 0)

    def move_selected_nodes_up(self):
        self.move_selected_copmonents__cmd(0, -40)

    def move_selected_nodes_right(self):
        self.move_selected_copmonents__cmd(+40, 0)

    def move_selected_nodes_down(self):
        self.move_selected_copmonents__cmd(0, +40)

    def selected_components_moved(self, pos_diff):
        items_list = self.scene().selectedItems()

        self.undo_stack.push(MoveComponents_Command(self, items_list, p_from=-pos_diff, p_to=QPointF(0, 0)))

    def selected_node_instances(self):
        selected_NIs = []
        for i in self.scene().selectedItems():
            if find_type_in_object(i, NodeInstance):
                selected_NIs.append(i)
        return selected_NIs

    def selected_drawings(self):
        selected_drawings = []
        for i in self.scene().selectedItems():
            if find_type_in_object(i, DrawingObject):
                selected_drawings.append(i)
        return selected_drawings

    def select_all(self):
        for i in self.scene().items():
            if i.ItemIsSelectable:
                i.setSelected(True)
        self.viewport().repaint()

    def copy(self):  # ctrl+c
        data = {'nodes': self.get_node_instances_json_data(self.selected_node_instances()),
                'connections': self.get_connections_json_data(self.selected_node_instances()),
                'drawings': self.get_drawings_json_data(self.selected_drawings())}
        QGuiApplication.clipboard().setText(json.dumps(data))

    def cut(self):  # called from shortcut ctrl+x
        data = {'nodes': self.get_node_instances_json_data(self.selected_node_instances()),
                'connections': self.get_connections_json_data(self.selected_node_instances()),
                'drawings': self.get_drawings_json_data(self.selected_drawings())}
        QGuiApplication.clipboard().setText(json.dumps(data))
        self.remove_selected_components()

    def paste(self):
        data = {}
        try:
            data = json.loads(QGuiApplication.clipboard().text())
        except Exception as e:
            return

        self.clear_selection()

        # calculate offset
        positions = []
        for d in data['drawings']:
            positions.append({'x': d['pos x'],
                              'y': d['pos y']})
        for n in data['nodes']:
            positions.append({'x': n['position x'],
                              'y': n['position y']})

        offset_for_middle_pos = QPointF(0, 0)
        if len(positions) > 0:
            rect = QRectF(positions[0]['x'], positions[0]['y'], 0, 0)
            for p in positions:
                x = p['x']
                y = p['y']
                if x < rect.left():
                    rect.setLeft(x)
                if x > rect.right():
                    rect.setRight(x)
                if y < rect.top():
                    rect.setTop(y)
                if y > rect.bottom():
                    rect.setBottom(y)

            offset_for_middle_pos = self.last_mouse_move_pos - rect.center()

        self.undo_stack.push(Paste_Command(self, data, offset_for_middle_pos))

    def add_component(self, e):
        if find_type_in_object(e, NodeInstance):
            self.add_node_instance(e)
        elif find_type_in_object(e, DrawingObject):
            self.add_drawing(e)

    def remove_component(self, e):
        if find_type_in_object(e, NodeInstance):
            self.remove_node_instance(e)
        elif find_type_in_object(e, DrawingObject):
            self.remove_drawing(e)

    def remove_selected_components(self):
        self.undo_stack.push(
            RemoveComponents_Command(self, self.scene().selectedItems()))

        self.viewport().update()

    # NODE SELECTION: ----
    def clear_selection(self):
        self.scene().clearSelection()

    # CONNECTIONS: ----
    def connect_gates__cmd(self, parent_gate: PortInstanceGate, child_gate: PortInstanceGate):
        self.undo_stack.push(ConnectGates_Command(self,
                                                  parent_port=parent_gate.parent_port_instance,
                                                  child_port=child_gate.parent_port_instance))

    def connect_gates(self, parent_gate: PortInstanceGate, child_gate: PortInstanceGate):
        parent_port_instance: PortInstance = parent_gate.parent_port_instance
        child_port_instance: PortInstance = child_gate.parent_port_instance

        # if they, their directions and their parent node instances are not equal and if their types are equal
        if parent_port_instance.direction != child_port_instance.direction and \
                parent_port_instance.parent_node_instance != child_port_instance.parent_node_instance and \
                parent_port_instance.type_ == child_port_instance.type_:
            try:  # remove connection if port instances are already connected
                index = parent_port_instance.connected_port_instances.index(child_port_instance)
                parent_port_instance.connected_port_instances.remove(child_port_instance)
                parent_port_instance.disconnected()
                child_port_instance.connected_port_instances.remove(parent_port_instance)
                child_port_instance.disconnected()

            except ValueError:  # connect port instances
                # remove all connections from parent port instance if it's a data input
                if parent_port_instance.direction == 'input' and parent_port_instance.type_ == 'data':
                    for cpi in parent_port_instance.connected_port_instances:
                        self.connect_gates__cmd(parent_gate, cpi.gate)  # actually disconnects the gates

                # remove all connections from child port instance it it's a data input
                if child_port_instance.direction == 'input' and child_port_instance.type_ == 'data':
                    for cpi in child_port_instance.connected_port_instances:
                        self.connect_gates__cmd(child_gate, cpi.gate)  # actually disconnects the gates

                parent_port_instance.connected_port_instances.append(child_port_instance)
                child_port_instance.connected_port_instances.append(parent_port_instance)
                parent_port_instance.connected()
                child_port_instance.connected()

        self.viewport().repaint()

    def try_conn_gate_and_ni(self, parent_gate: PortInstanceGate, child_ni: NodeInstance):
        parent_port_instance: PortInstance = parent_gate.parent_port_instance

        if parent_port_instance.direction == 'output':
            for inp in child_ni.inputs:
                if parent_port_instance.type_ == inp.type_:
                    self.connect_gates__cmd(parent_gate, inp.gate)
                    return
        elif parent_port_instance.direction == 'input':
            for out in child_ni.outputs:
                if parent_port_instance.type_ == out.type_:
                    self.connect_gates__cmd(parent_gate, out.gate)
                    return

    @staticmethod
    def connection_path(p1: QPointF, p2: QPointF):
        """Returns the nice looking QPainterPath of a connection for two given points."""

        path = QPainterPath()

        path.moveTo(p1)

        distance_x = abs(p1.x()) - abs(p2.x())
        distance_y = abs(p1.y()) - abs(p2.y())

        if ((p1.x() < p2.x() - 30) or math.sqrt((distance_x ** 2) + (distance_y ** 2)) < 100) and (p1.x() < p2.x()):
            path.cubicTo(p1.x() + ((p2.x() - p1.x()) / 2), p1.y(),
                         p1.x() + ((p2.x() - p1.x()) / 2), p2.y(),
                         p2.x(), p2.y())
        elif p2.x() < p1.x() - 100 and abs(distance_x) / 2 > abs(distance_y):
            path.cubicTo(p1.x() + 100 + (p1.x() - p2.x()) / 10, p1.y(),
                         p1.x() + 100 + (p1.x() - p2.x()) / 10, p1.y() - (distance_y / 2),
                         p1.x() - (distance_x / 2), p1.y() - (distance_y / 2))
            path.cubicTo(p2.x() - 100 - (p1.x() - p2.x()) / 10, p2.y() + (distance_y / 2),
                         p2.x() - 100 - (p1.x() - p2.x()) / 10, p2.y(),
                         p2.x(), p2.y())
        else:
            path.cubicTo(p1.x() + 100 + (p1.x() - p2.x()) / 3, p1.y(),
                         p2.x() - 100 - (p1.x() - p2.x()) / 3, p2.y(),
                         p2.x(), p2.y())
        return path

    # GET JSON DATA
    def get_json_data(self):
        flow_dict = {'nodes': self.get_node_instances_json_data(self.all_node_instances),
                     'connections': self.get_connections_json_data(self.all_node_instances),
                     'drawings': self.get_drawings_json_data(self.drawings)}
        return flow_dict

    def get_node_instances_json_data(self, node_instances):
        script_node_instances_list = []
        for ni in node_instances:
            node_instance_dict = ni.get_json_data()
            script_node_instances_list.append(node_instance_dict)

        return script_node_instances_list

    def get_connections_json_data(self, node_instances, only_with_connections_to=None):
        script_ni_connections_list = []
        for ni in node_instances:
            for out in ni.outputs:
                if len(out.connected_port_instances) > 0:
                    for connected_port in out.connected_port_instances:

                        # this only applies when saving config data through deleting node instances:
                        if only_with_connections_to is not None and \
                                connected_port.parent_node_instance not in only_with_connections_to and \
                                ni not in only_with_connections_to:
                            continue
                        # because I am not allowed to save connections between nodes connected to each other and both
                        # connected to the deleted node, only the connections to the deleted node shall be saved

                        connection_dict = {'parent node instance index': node_instances.index(ni),
                                           'output port index': ni.outputs.index(out)}

                        # yes, very important: when copying components, there might be connections going outside the
                        # selected lists, these should be ignored. When saving a project, all components are considered,
                        # so then the index values will never be none
                        connected_ni_index = node_instances.index(connected_port.parent_node_instance) if \
                            node_instances.__contains__(connected_port.parent_node_instance) else \
                            None
                        connection_dict['connected node instance'] = connected_ni_index

                        connected_ip_index = connected_port.parent_node_instance.inputs.index(connected_port) if \
                            connected_ni_index is not None else None
                        connection_dict['connected input port index'] = connected_ip_index

                        script_ni_connections_list.append(connection_dict)

        return script_ni_connections_list

    def get_drawings_json_data(self, drawings):
        drawings_list = []
        for drawing in drawings:
            drawing_dict = {'pos x': drawing.pos().x(),
                            'pos y': drawing.pos().y()}
            points_list = []
            for i in range(len(drawing.points)):
                p = drawing.points[i]
                points_list.append({'x': p.x(),
                                    'y': p.y(),
                                    'w': drawing.stroke_weights[i]})
            drawing_dict['points'] = points_list

            drawings_list.append(drawing_dict)

        return drawings_list