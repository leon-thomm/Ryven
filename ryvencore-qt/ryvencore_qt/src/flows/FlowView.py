# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..SessionGUI import SessionGUI

import json

from typing import Tuple, Optional

from qtpy.QtCore import (
    Qt,
    QPointF,
    QPoint,
    QRectF,
    QSizeF,
    Signal,
    QTimer,
    QTimeLine,
    QEvent,
)
from qtpy.QtGui import (
    QPainter,
    QPen,
    QColor,
    QKeySequence,
    QTabletEvent,
    QDropEvent,
    QContextMenuEvent,
    QImage,
    QGuiApplication,
    QFont,
    QTouchEvent,
    QTransform,
)
from qtpy.QtWidgets import (
    QGraphicsView,
    QGraphicsScene,
    QShortcut,
    QMenu,
    QGraphicsItem,
    QPushButton,
    QHBoxLayout,
    QWidget,
)

# for compatibility between qt5 and qt6
try:
    from qtpy.QtGui import QUndoStack
except ImportError:
    from qtpy.QtWidgets import QUndoStack  # type: ignore

from ryvencore.Flow import Flow
from ryvencore.Node import Node
from ryvencore.NodePort import NodePort, NodeInput, NodeOutput

# from ryvencore.Connection import Connection, DataConnection
from ryvencore.InfoMsgs import InfoMsgs
from ryvencore.RC import PortObjPos
from ryvencore.utils import node_from_identifier

from ..GUIBase import GUIBase
from ..utils import *
from .FlowCommands import (
    MoveComponents_Command,
    PlaceNode_Command,
    PlaceDrawing_Command,
    RemoveComponents_Command,
    ConnectPorts_Command,
    Paste_Command,
    FlowUndoCommand,
    SelectComponents_Command,
)
from .FlowViewProxyWidget import *
from .FlowViewStylusModesWidget import FlowViewStylusModesWidget
from .node_list_widget.NodeListWidget import NodeListWidget
from .nodes.NodeGUI import NodeGUI
from .nodes.NodeItem import NodeItem
from .nodes.PortItem import PortItemPin, PortItem
from .connections.ConnectionItem import (
    default_cubic_connection_path,
    ConnectionItem,
    DataConnectionItem,
    ExecConnectionItem,
)
from .drawings.DrawingObject import DrawingObject

from ..Design import Design
from enum import Enum


class _SelectionMode(Enum):
    """
    Determines how selection change events will be handled.
    If INSTANT, then they happen instantly.
    If UNDO, the event is pushed unto the undo stack
    """

    INSTANT = 1
    UNDOABLE_CLICK = 2
    UNDOABLE_RUBBERBANDDRAG = 3


class FlowView(GUIBase, QGraphicsView):
    """Manages the GUI of flows"""

    nodes_selection_changed = Signal(list)
    node_placed = Signal(Node)

    create_node_request = Signal(object, dict)
    remove_node_request = Signal(Node)

    check_connection_validity_request = Signal((NodeOutput, NodeInput), bool)
    connect_request = Signal(NodePort, NodePort)

    # get_nodes_data_request = Signal(list)
    # get_connections_data_request = Signal(list)
    get_flow_data_request = Signal()

    viewport_update_mode_changed = Signal(str)

    def __init__(self, session_gui: SessionGUI, flow: Flow, parent=None) -> None:
        GUIBase.__init__(self, representing_component=flow)
        QGraphicsView.__init__(self, parent=parent)

        # UNDO STACK
        self._undo_stack = QUndoStack(self)
        self._undo_action = self._undo_stack.createUndoAction(self, 'undo')
        self._undo_action.setShortcuts(QKeySequence.Undo)
        self._redo_action = self._undo_stack.createRedoAction(self, 'redo')
        self._redo_action.setShortcuts(QKeySequence.Redo)

        # SHORTCUTS
        self._init_shortcuts()

        # GENERAL ATTRIBUTES
        self.session_gui = session_gui
        self.design: Design = session_gui.design  # type hinting and quicker access

        self.flow: Flow = flow
        self.node_items: Dict = {}  # {Node: NodeItem}
        self.node_items__cache: Dict = {}
        self.connection_items: Dict = {}  # {Connection: ConnectionItem}
        self.connection_items__cache: Dict = {}
        self.selection_mode: _SelectionMode = _SelectionMode.UNDOABLE_CLICK

        # PRIVATE FIELDS
        self._loaded_state: Optional[Dict] = None # h and v scrollbars are changed on import, so we need to defer
        self._tmp_data = None
        self._selected_pin: Optional[PortItemPin] = None
        self._dragging_connection = False
        self._temp_connection_ports: Optional[Tuple[NodeOutput, NodeInput]] = None
        self._waiting_for_connection_request: bool = False
        self.mouse_event_taken = False  # for stylus - see tablet event
        self._last_mouse_move_pos: Optional[QPointF] = None
        self._node_place_pos = QPointF()
        self._left_mouse_pressed_in_flow = False
        self._right_mouse_pressed_in_flow = False
        self._mouse_press_pos: Optional[QPointF] = None
        self._multi_selection = False
        self._current_selected: List[QGraphicsItem] = []
        self._auto_connection_pin: Optional[PortItemPin] = None  # stores the gate that we may try to auto connect to a newly placed NI
        self._panning = False
        self._pan_last_x: Optional[int] = None
        self._pan_last_y: Optional[int] = None
        self._current_scale = 1
        self._total_scale_div = 1
        self._zoom_data = {
            'viewport pos': None,
            'scene pos': None,
            'delta': 0,
        }

        # CONNECTIONS TO FLOW
        self.create_node_request.connect(self.flow.create_node)
        self.remove_node_request.connect(self.flow.remove_node)
        self.check_connection_validity_request.connect(self.flow.check_connection_validity)
        # TODO: need to check if the 2 lines below are used
        # self.get_nodes_data_request.connect(self.flow.gen_nodes_data)
        # self.get_connections_data_request.connect(self.flow.gen_conns_data)
        self.get_flow_data_request.connect(self.flow.data)

        # CONNECTIONS FROM FLOW
        self.flow.node_added.sub(self.add_node)
        self.flow.node_removed.sub(self.remove_node)
        self.flow.connection_added.sub(self.add_connection)
        self.flow.connection_removed.sub(self.remove_connection)
        self.flow.connection_request_valid.sub(self.connection_request_valid)

        # CREATE UI
        scene = QGraphicsScene(self)
        scene.setItemIndexMethod(QGraphicsScene.NoIndex)
        scene.setSceneRect(0, 0, 10000, 7000)

        self.setScene(scene)
        self.setCacheMode(QGraphicsView.CacheBackground)
        self.setViewportUpdateMode(QGraphicsView.BoundingRectViewportUpdate)
        self.setRenderHint(QPainter.Antialiasing)
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)
        self.setDragMode(QGraphicsView.RubberBandDrag)
        self._watch_scene_selection()
        self.setAcceptDrops(True)

        self.centerOn(QPointF(self.viewport().width() / 2, self.viewport().height() / 2))

        self.scene_rect_width = self.mapFromScene(self.sceneRect()).boundingRect().width()
        self.scene_rect_height = self.mapFromScene(self.sceneRect()).boundingRect().height()

        # for proper background painting
        # we could probably use the no cache flag
        on_pan = lambda scroll: self.resetCachedContent()
        
        self.horizontalScrollBar().valueChanged.connect(on_pan)
        self.verticalScrollBar().valueChanged.connect(on_pan)
        
        # NODE LIST WIDGET
        self._node_list_widget = NodeListWidget(self.session_gui)
        self._node_list_widget.setMinimumWidth(260)
        self._node_list_widget.setFixedHeight(300)
        self._node_list_widget.escaped.connect(self.hide_node_list_widget)
        self._node_list_widget.node_chosen.connect(self.create_node__cmd)

        self._node_list_widget_proxy = FlowViewProxyWidget(self)
        self._node_list_widget_proxy.setZValue(1000)
        self._node_list_widget_proxy.setWidget(self._node_list_widget)
        self.scene().addItem(self._node_list_widget_proxy)

        self.hide_node_list_widget()

        # ZOOM WIDGET
        # self._zoom_proxy = FlowViewProxyWidget(self)
        # self._zoom_proxy.setFlag(QGraphicsItem.ItemIgnoresTransformations, True)
        # self._zoom_proxy.setZValue(1001)
        # self._zoom_widget = FlowViewZoomWidget(self)
        # self._zoom_proxy.setWidget(self._zoom_widget)
        # self.scene().addItem(self._zoom_proxy)
        # self.set_zoom_proxy_pos()

        def init_proxy_widget(widget: QWidget, proxy: FlowViewProxyWidget):
            proxy.setFlag(QGraphicsItem.ItemIgnoresTransformations, True)
            proxy.setZValue(1001)
            proxy.setWidget(widget)
            self.scene().addItem(proxy)
            return proxy

        # STYLUS
        self.stylus_mode = ''
        self._current_drawing = None
        self._drawing = False
        self.drawings: List[DrawingObject] = []
        self._stylus_modes_widget = FlowViewStylusModesWidget(self)
        self._stylus_modes_proxy = init_proxy_widget(
            self._stylus_modes_widget, FlowViewProxyWidget(self)
        )
        self.set_stylus_proxy_pos()
        self.setAttribute(Qt.WA_TabletTracking)

        # MENU
        self._menu = QMenu()
        
        # just to add some space for the button
        menu_layout_widget = self._create_no_background_widget("FlowMenu")
        # just to add some space for the button
        menu_layout_widget.setLayout(QHBoxLayout())
        menu_button = QPushButton("Menu")
        self._menu_button = menu_button
        menu_layout_widget.layout().addWidget(menu_button)

        def menu_button_clicked():
            # prob not entirely correct, since menu is part of a layout
            # but since it's the first item, it's the same
            menu_pos = self._menu_button.pos()
            menu_pos = self.mapToGlobal(menu_pos) + QPoint(8, self._menu_button.height() + 10)
            self._menu.exec_(menu_pos)

        menu_button.clicked.connect(menu_button_clicked)

        menu_layout_proxy = init_proxy_widget(menu_layout_widget, FlowViewProxyWidget(self))
        self._menu_widget = menu_button
        self._menu_layout_proxy = menu_layout_proxy
        self.set_menu_proxy_pos()

        # # TOUCH GESTURES
        # recognizer = PanGestureRecognizer()
        # pan_gesture_id = QGestureRecognizer.registerRecognizer(recognizer) <--- CRASH HERE
        # self.grabGesture(pan_gesture_id)
        self.viewport().setAttribute(Qt.WA_AcceptTouchEvents)
        self.last_pinch_points_dist = 0

        # DESIGN
        self.session_gui.design.flow_theme_changed.connect(self._theme_changed)
        self.session_gui.design.performance_mode_changed.connect(self._perf_mode_changed)

        # DATA
        data = self.flow.load_data
        if data is not None:
            view_data = data['flow view']
            if 'drawings' in view_data:  # not all (old) project files have drawings arr
                self.place_drawings_from_data(view_data['drawings'])
            if 'view size' in view_data:
                self.setSceneRect(0, 0, view_data['view size'][0], view_data['view size'][1])

            self._undo_stack.clear()

        # CATCH UP ON FLOW
        for node in self.flow.nodes:
            self.add_node(node)
        for c in [(o, i) for o, conns in self.flow.graph_adj.items() for i in conns]:
            self.add_connection(c)

    def menu(self) -> QMenu:
        """The menu for this flow view"""
        return self._menu

    def _create_no_background_widget(self, name: str):
        result = QWidget()
        result.setObjectName(name)
        result.setStyleSheet(
            f'''
        QWidget#{name} {{
            background: transparent; 
        }}
                '''
        )
        return result

    def _init_shortcuts(self):
        place_new_node_shortcut = QShortcut(QKeySequence('Shift+P'), self)
        place_new_node_shortcut.activated.connect(self._place_new_node_by_shortcut)
        move_selected_components_left_shortcut = QShortcut(QKeySequence('Shift+Left'), self)
        move_selected_components_left_shortcut.activated.connect(self._move_selected_comps_left)
        move_selected_components_up_shortcut = QShortcut(QKeySequence('Shift+Up'), self)
        move_selected_components_up_shortcut.activated.connect(self._move_selected_comps_up)
        move_selected_components_right_shortcut = QShortcut(QKeySequence('Shift+Right'), self)
        move_selected_components_right_shortcut.activated.connect(self._move_selected_comps_right)
        move_selected_components_down_shortcut = QShortcut(QKeySequence('Shift+Down'), self)
        move_selected_components_down_shortcut.activated.connect(self._move_selected_comps_down)
        select_all_shortcut = QShortcut(QKeySequence('Ctrl+A'), self)
        select_all_shortcut.activated.connect(self._select_all_action)
        copy_shortcut = QShortcut(QKeySequence.Copy, self)
        copy_shortcut.activated.connect(self._copy)
        cut_shortcut = QShortcut(QKeySequence.Cut, self)
        cut_shortcut.activated.connect(self._cut)
        paste_shortcut = QShortcut(QKeySequence.Paste, self)
        paste_shortcut.activated.connect(self._paste)

        undo_shortcut = QShortcut(QKeySequence.Undo, self)
        undo_shortcut.activated.connect(self._undo_activated)
        redo_shortcut = QShortcut(QKeySequence.Redo, self)
        redo_shortcut.activated.connect(self._redo_activated)

    def _theme_changed(self, t):
        self._node_list_widget.setStyleSheet(self.session_gui.design.node_selection_stylesheet)
        for n, ni in self.node_items.items():
            ni.widget.rebuild_ui()

        # https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QGraphicsView.html#PySide2.QtWidgets.PySide2.QtWidgets.QGraphicsView.resetCachedContent
        self.resetCachedContent()
        self.update()

    def _perf_mode_changed(self, mode):
        # set widget value update rule for port inputs, because this takes up quite a bit of performance
        update_widget_value = mode == 'pretty'
        for n, ni in self.node_items.items():
            for inp in ni.inputs:
                inp.update_widget_value = update_widget_value and inp.widget

        self.viewport().update()
        self.scene().update(self.sceneRect())

    def push_undo(self, cmd: FlowUndoCommand):
        self._undo_stack.push(cmd)
        cmd.activate()

    def _undo_activated(self):
        """Triggered by ctrl+z"""
        self._undo_stack.undo()
        self.viewport().update()

    def _redo_activated(self):
        """Triggered by ctrl+y"""
        self._undo_stack.redo()
        self.viewport().update()

    def mousePressEvent(self, event):
        # InfoMsgs.write('mouse press event received, point:', event.pos())

        self._set_selection_mode(_SelectionMode.UNDOABLE_CLICK)

        # to catch tablet events (for some reason, it results in a mousePrEv too)
        if self.mouse_event_taken:
            self.mouse_event_taken = False
            return

        # this allows to chain the selection event when multi-selecting
        hover_item = self.itemAt(event.pos())
        if hover_item is None:
            self._set_selection_mode(_SelectionMode.UNDOABLE_RUBBERBANDDRAG)

        if event.button() != Qt.RightButton:
            QGraphicsView.mousePressEvent(self, event)

        # don't process the event if it has been processed by a specific component in the scene
        # this includes node items, node port pins, proxy widgets etc.
        if self.mouse_event_taken:
            self.mouse_event_taken = False
            self._set_selection_mode(_SelectionMode.UNDOABLE_CLICK)
            return

        if event.button() == Qt.LeftButton:
            if self._node_list_widget_proxy.isVisible():
                self.hide_node_list_widget()

        elif event.button() == Qt.RightButton:
            self._right_mouse_pressed_in_flow = True
            event.accept()

        self._mouse_press_pos = self.mapToScene(event.pos())

    def mouseMoveEvent(self, event):
        if self._right_mouse_pressed_in_flow:  # PAN
            if not self._panning:
                self._panning = True
                self._pan_last_x = event.x()
                self._pan_last_y = event.y()

            self.pan(event.pos())
            event.accept()

        else:
            QGraphicsView.mouseMoveEvent(self, event)

        self._last_mouse_move_pos = self.mapToScene(event.pos())

        if self._dragging_connection:
            self.viewport().repaint()

    def mouseReleaseEvent(self, event):
        # there might be a proxy widget meant to receive the event instead of the flow
        QGraphicsView.mouseReleaseEvent(self, event)

        node_item_at_event_pos = None
        for item in self.items(event.pos()):
            if isinstance(item, NodeItem):
                node_item_at_event_pos = item

        if self.mouse_event_taken:
            self.mouse_event_taken = False
            self.viewport().repaint()
            self._set_selection_mode(_SelectionMode.UNDOABLE_CLICK)
            return

        elif self._panning:
            self._panning = False

        elif event.button() == Qt.RightButton:
            self._right_mouse_pressed_in_flow = False
            if self._mouse_press_pos == self._last_mouse_move_pos and not self.itemAt(event.pos()):
                self.show_place_node_widget(event.pos())
                self._set_selection_mode(_SelectionMode.UNDOABLE_CLICK)
                return

        if self._dragging_connection:
            # connection dropped over port item
            port_items = {i: isinstance(i, PortItem) for i in self.items(event.pos())}
            if any(port_items.values()):
                # gets the first PortItem
                p_i = list(port_items.keys())[list(port_items.values()).index(True)]

                # the validity of the connection is checked in connect_node_ports__cmd
                self.connect_node_ports__cmd(self._selected_pin.port, p_i.port)

            # connection dropped above NodeItem -> auto connect
            elif node_item_at_event_pos:
                # find node item
                ni_under_drop = None
                for item in self.items(event.pos()):
                    if isinstance(item, NodeItem):
                        ni_under_drop = item
                        self.auto_connect(self._selected_pin.port, ni_under_drop.node)
                        break

            # connection dropped somewhere else -> show node choice widget
            else:
                self._auto_connection_pin = self._selected_pin
                self.show_place_node_widget(event.pos())

            self._dragging_connection = False
            self._selected_pin = None

        # if event.button() == Qt.LeftButton:
        #     self._left_mouse_pressed_in_flow = False
        elif event.button() != Qt.RightButton:
            if self.selection_mode == _SelectionMode.UNDOABLE_RUBBERBANDDRAG:
                self._select__cmd()

        else:
            self._right_mouse_pressed_in_flow = False

        self._set_selection_mode(_SelectionMode.UNDOABLE_CLICK)
        self.viewport().repaint()

    def keyPressEvent(self, event):
        QGraphicsView.keyPressEvent(self, event)
        if event.isAccepted():
            return

        if event.key() == Qt.Key_Escape:  # do I need that... ?
            self.clearFocus()
            self.setFocus()
            return True

        elif event.key() == Qt.Key_Delete and self.selection_mode != _SelectionMode.UNDOABLE_RUBBERBANDDRAG:
            self.remove_selected_components__cmd()

    def wheelEvent(self, event):
        if event.modifiers() & Qt.ControlModifier:
            event.accept()

            view_pos = event.position()
            self._zoom_data['viewport pos'] = view_pos
            self._zoom_data['scene pos'] = self.mapToScene(view_pos.toPoint())

            y_delta = event.angleDelta().y()
            self._zoom_data['delta'] += y_delta

            if self._zoom_data['delta'] * y_delta < 0:
                self._zoom_data['delta'] = y_delta

            anim = QTimeLine(100, self)
            anim.setUpdateInterval(10)
            anim.valueChanged.connect(self._scaling_time)
            anim.start()

        else:
            super().wheelEvent(event)

    def _scaling_time(self, x):
        delta = self._zoom_data['delta'] / 8
        if abs(delta) <= 5:
            delta = self._zoom_data['delta']
        self._zoom_data['delta'] -= delta

        self.zoom(self._zoom_data['viewport pos'], self._zoom_data['scene pos'], delta)

    def viewportEvent(self, event: QEvent) -> bool:
        """handling some touch features here"""

        if event.type() == QEvent.TouchBegin:
            self.setDragMode(QGraphicsView.NoDrag)
            return True

        elif event.type() == QEvent.TouchUpdate:
            if len(event.touchPoints()) == 2:
                tp0, tp1 = event.touchPoints()[0], event.touchPoints()[1]

                p0, p1 = tp0.pos(), tp1.pos()
                # sp0, sp1 = tp0.scenePos(), tp1.scenePos()

                pinch_points_dist = points_dist(p0, p1)

                if self.last_pinch_points_dist == 0:
                    self.last_pinch_points_dist = pinch_points_dist

                center = middle_point(p0, p1)
                self.zoom(
                    p_abs=center,
                    p_mapped=self.mapToScene(center.toPoint()),
                    angle=((pinch_points_dist / self.last_pinch_points_dist) ** 10 - 1) * 100,
                )

                self.last_pinch_points_dist = pinch_points_dist

            return True

        elif event.type() == QEvent.TouchEnd:
            self.last_pinch_points_dist = 0
            self.setDragMode(QGraphicsView.RubberBandDrag)
            return True

        else:
            return super().viewportEvent(event)

    def tabletEvent(self, event: QTabletEvent) -> None:
        """tabletEvent gets called by stylus operations.
        LeftButton: std, no button pressed
        RightButton: upper button pressed"""

        # if in edit mode and not panning or starting a pan, pass on to std mouseEvent handlers above
        if (
            self.stylus_mode == 'edit'
            and not self._panning
            and not (event.type() == QTabletEvent.TabletPress and event.button() == Qt.RightButton)
        ):
            return  # let the mousePress/Move/Release-Events handle it

        scaled_event_pos: QPointF = event.posF()
        scaled_event_pos /= self._current_scale  # type: ignore
        # mypy thinks the above results in a float, but it doesn't

        if event.type() == QTabletEvent.TabletPress:
            self.mouse_event_taken = True

            if event.button() == Qt.LeftButton:
                if self.stylus_mode == 'comment':
                    view_pos = self.mapToScene(self.viewport().pos())
                    new_drawing = self._create_and_place_drawing__cmd(
                        view_pos + scaled_event_pos,
                        data={
                            **self._stylus_modes_widget.get_pen_settings(),
                            'viewport pos': view_pos,
                        },
                    )
                    self._current_drawing = new_drawing
                    self._drawing = True
            elif event.button() == Qt.RightButton:
                self._panning = True
                self._pan_last_x = event.x()
                self._pan_last_y = event.y()

        elif event.type() == QTabletEvent.TabletMove:
            self.mouse_event_taken = True
            if self._panning:
                self.pan(event.pos())

            elif event.pointerType() == QTabletEvent.Eraser:
                if self.stylus_mode == 'comment':
                    for i in self.items(event.pos()):
                        if isinstance(i, DrawingObject):
                            self.remove_drawing(i)
                            break
            elif self.stylus_mode == 'comment' and self._drawing:
                assert self._current_drawing is not None
                if self._current_drawing.append_point(scaled_event_pos):
                    self._current_drawing.stroke_weights.append(
                        event.pressure() * self._stylus_modes_widget.pen_width()
                    )
                self._current_drawing.update()
                self.viewport().update()

        elif event.type() == QTabletEvent.TabletRelease:
            if self._panning:
                self._panning = False
            if self.stylus_mode == 'comment' and self._drawing:
                assert self._current_drawing is not None
                self._current_drawing.finish()
                InfoMsgs.write('drawing finished')
                self._current_drawing = None
                self._drawing = False

    """
    --> https://forum.qt.io/topic/121473/qgesturerecognizer-registerrecognizer-crashes-using-pyside2

    def event(self, event) -> bool:
        # if event.type() == QEvent.Gesture:
        #     if event.gesture(PanGesture) is not None:
        #         return self.pan_gesture(event)

        return QGraphicsView.event(self, event)

    def pan_gesture(self, event: QGestureEvent) -> bool:
        pan: PanGesture = event.gesture(PanGesture)
        print(pan)
        return True
    """

    def dragEnterEvent(self, event):
        if event.mimeData().hasFormat('application/json'):
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasFormat('application/json'):
            event.acceptProposedAction()

    def dropEvent(self, event: QDropEvent):
        try:
            text = str(event.mimeData().data('application/json'), 'utf-8')
            data: Dict = json.loads(text)

            if data['type'] == 'node':
                self._node_place_pos = self.mapToScene(event.pos())
                self.create_node__cmd(
                    node_from_identifier(
                        data['node identifier'],
                        list(self.session_gui.core_session.nodes)
                    )
                )
            # without this keyPressed function isn't called if we don't click in the view
            self.setFocus()
        except Exception:
            pass
    
    def contextMenuEvent(self, event: QContextMenuEvent):
        QGraphicsView.contextMenuEvent(self, event)
        # in the case of the menu already being shown by a widget under the mouse, the event is accepted here
        if event.isAccepted():
            return
        
        for i in self.items(event.pos()):
            if isinstance(i, NodeItem):
                ni: NodeItem = i
                menu: QMenu = ni.get_context_menu()
                menu.exec_(event.globalPos())
                event.accept()

    # PAINTING
    def drawBackground(self, painter, rect):
        painter.setBrush(self.session_gui.design.flow_theme.flow_background_brush)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.sceneRect())

        if self.session_gui.design.performance_mode == 'pretty':
            theme = self.session_gui.design.flow_theme
            if theme.flow_background_grid and self._current_scale >= 0.7:
                if theme.flow_background_grid[0] == 'points':
                    color = theme.flow_background_grid[1]
                    pen_width = theme.flow_background_grid[2]
                    diff_x = theme.flow_background_grid[3]
                    diff_y = theme.flow_background_grid[4]

                    pen = QPen(color)
                    pen.setWidthF(pen_width)
                    painter.setPen(pen)

                    points_rect = rect.toRect()
                    top_left = points_rect.topLeft()
                    for x in range(
                        diff_x + top_left.x(), points_rect.width() + top_left.x(), diff_x
                    ):
                        for y in range(
                            diff_y + top_left.y(), points_rect.height() + top_left.y(), diff_y
                        ):
                            painter.drawPoint(x, y)

        # has to be called here instead of in drawForeground to prevent lagging
        self.set_stylus_proxy_pos()
        self.set_menu_proxy_pos()
        # self.set_zoom_proxy_pos()

    def drawForeground(self, painter, rect):
        # DRAW CURRENTLY DRAGGED CONNECTION
        if self._dragging_connection:
            pen = QPen(QColor('#101520'))
            pen.setWidth(3)
            pen.setStyle(Qt.DotLine)
            painter.setPen(pen)

            pin_pos = self._selected_pin.get_scene_center_pos()
            spp = self._selected_pin.port
            cursor_pos = self._last_mouse_move_pos

            pos1 = pin_pos if spp.io_pos == PortObjPos.OUTPUT else cursor_pos
            pos2 = pin_pos if spp.io_pos == PortObjPos.INPUT else cursor_pos

            painter.drawPath(default_cubic_connection_path(pos1, pos2))

        # # DRAW SELECTED NIs BORDER
        # for ni in self.selected_node_items():
        #     pen = QPen(self.session.design.flow_theme.flow_highlight_pen_color)
        #     pen.setWidth(3)
        #     painter.setPen(pen)
        #     painter.setBrush(Qt.NoBrush)
        #
        #     size_factor = 1.2
        #     x = ni.pos().x() - ni.boundingRect().width() / 2 * size_factor
        #     y = ni.pos().y() - ni.boundingRect().height() / 2 * size_factor
        #     w = ni.boundingRect().width() * size_factor
        #     h = ni.boundingRect().height() * size_factor
        #     painter.drawRoundedRect(x, y, w, h, 10, 10)

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

    def get_viewport_img(self) -> QImage:
        """Returns a clear image of the viewport"""

        self.hide_proxies()
        img = QImage(
            size=QSizeF(
                self.viewport().rect().width(),
                self.viewport().height(),
            ),
            format=QImage.Format_ARGB32,
        )
        img.fill(Qt.transparent)

        painter = QPainter(img)
        painter.setRenderHint(QPainter.Antialiasing)
        self.render(painter, self.viewport().rect(), self.viewport().rect())
        self.show_proxies()
        return img

    def get_whole_scene_img(self) -> QImage:
        """Returns an image of the whole scene, scaled accordingly to current scale factor.
        Due to a bug this only works from the viewport position down and right, so the user has to scroll to
        the top left corner in order to get the full scene"""

        self.hide_proxies()
        img = QImage(
            size=QSizeF(
                self.sceneRect().width() / self._total_scale_div,
                self.sceneRect().height() / self._total_scale_div,
            ),
            format=QImage.Format_RGB32,
        )
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

    # def set_zoom_proxy_pos(self):
    #     self._zoom_proxy.setPos(self.mapToScene(self.viewport().width() - self._zoom_widget.width(), 0))

    def set_stylus_proxy_pos(self):
        self._stylus_modes_proxy.setPos(
            self.mapToScene(self.viewport().width() - self._stylus_modes_widget.width(), 0)
        )
        # self.mapToScene(self.viewport().width() - self._stylus_modes_widget.width() - self._zoom_widget.width(), 0))
    
    def set_menu_proxy_pos(self):
        self._menu_layout_proxy.setPos(self.mapToScene(0, 0))
        
    def hide_proxies(self):
        self._stylus_modes_proxy.hide()
        self._menu_layout_proxy.hide()
        # self._zoom_proxy.hide()

    def show_proxies(self):
        self._stylus_modes_proxy.show()
        self._menu_layout_proxy.show()
        # self._zoom_proxy.show()

    # PLACE NODE WIDGET
    def show_place_node_widget(self, pos, nodes=None):
        """Opens the place node dialog in the scene."""

        # calculating position
        self._node_place_pos = self.mapToScene(pos)
        dialog_pos = QPoint(pos.x() + 1, pos.y() + 1)

        # ensure that the node_list_widget stays in the viewport
        if (
            dialog_pos.x() + self._node_list_widget.width() / self._total_scale_div
            > self.viewport().width()
        ):
            dialog_pos.setX(
                dialog_pos.x()
                - (
                    dialog_pos.x()
                    + self._node_list_widget.width() / self._total_scale_div
                    - self.viewport().width()
                )
            )
        if (
            dialog_pos.y() + self._node_list_widget.height() / self._total_scale_div
            > self.viewport().height()
        ):
            dialog_pos.setY(
                dialog_pos.y()
                - (
                    dialog_pos.y()
                    + self._node_list_widget.height() / self._total_scale_div
                    - self.viewport().height()
                )
            )
        dialog_pos = self.mapToScene(dialog_pos)

        # open nodes dialog
        # the dialog emits 'node_chosen' which is connected to self.place_node__cmd
        self._node_list_widget.update_list(
            nodes if nodes is not None else self.session_gui.core_session.nodes
        )
        self._node_list_widget_proxy.setPos(dialog_pos)
        self._node_list_widget_proxy.show()
        self._node_list_widget.refocus()

    def hide_node_list_widget(self):
        self._node_list_widget_proxy.hide()
        self._node_list_widget.clearFocus()
        self._auto_connection_pin = None

    def _place_new_node_by_shortcut(self):  # Shift+P
        point_in_viewport = None
        selected_NIs = self.selected_node_items()
        if len(selected_NIs) > 0:
            x = selected_NIs[-1].pos().x() + 150
            y = selected_NIs[-1].pos().y()
            self._node_place_pos = QPointF(x, y)
            point_in_viewport = self.mapFromScene(QPoint(x, y))
        else:  # place in center
            viewport_x = self.viewport().width() / 2
            viewport_y = self.viewport().height() / 2
            point_in_viewport = QPointF(viewport_x, viewport_y).toPoint()
            self._node_place_pos = self.mapToScene(point_in_viewport)

        self.show_place_node_widget(point_in_viewport)

    # PAN
    def pan(self, new_pos):
        self.horizontalScrollBar().setValue(
            self.horizontalScrollBar().value() - (new_pos.x() - self._pan_last_x)
        )
        self.verticalScrollBar().setValue(
            self.verticalScrollBar().value() - (new_pos.y() - self._pan_last_y)
        )
        self._pan_last_x = new_pos.x()
        self._pan_last_y = new_pos.y()

    # ZOOM
    def zoom_in(self, amount):
        local_viewport_center = QPoint(self.viewport().width() / 2, self.viewport().height() / 2)
        self.zoom(local_viewport_center, self.mapToScene(local_viewport_center), amount)

    def zoom_out(self, amount):
        local_viewport_center = QPoint(self.viewport().width() / 2, self.viewport().height() / 2)
        self.zoom(local_viewport_center, self.mapToScene(local_viewport_center), -amount)

    def zoom(self, p_abs, p_mapped, angle):
        # print(f'zooming to {p_abs} / {p_mapped} with angle: {angle}')

        by = 0
        velocity = 2 * (1 / self._current_scale) + 0.5
        if velocity > 3:
            velocity = 3
        if self._current_scale < 1:
            velocity *= self._current_scale

        zoom_dir_IN = angle > 0
        if zoom_dir_IN:
            by = 1 + (angle / 4000) * velocity
        else:
            by = 1 - (-angle / 4000) * velocity

        if zoom_dir_IN:
            if self._current_scale * by < 3:
                self.scale(by, by)
                self._current_scale *= by
        else:
            if (
                self.scene_rect_width * by >= self.viewport().size().width()
                and self.scene_rect_height * by >= self.viewport().size().height()
            ):
                self.scale(by, by)
                self._current_scale *= by

        w = self.viewport().width()
        h = self.viewport().height()
        wf = self.mapToScene(QPoint(w - 1, 0)).x() - self.mapToScene(QPoint(0, 0)).x()
        hf = self.mapToScene(QPoint(0, h - 1)).y() - self.mapToScene(QPoint(0, 0)).y()
        lf = p_mapped.x() - p_abs.x() * wf / w
        tf = p_mapped.y() - p_abs.y() * hf / h

        self.ensureVisible(lf, tf, wf, hf, 0, 0)

        target_rect = QRectF(QPointF(lf, tf), QSizeF(wf, hf))
        self._total_scale_div = target_rect.width() / self.viewport().width()

        self.ensureVisible(target_rect, 0, 0)

    # NODES
    def create_node__cmd(self, node_class):
        self.push_undo(PlaceNode_Command(self, node_class, self._node_place_pos))

    def add_node(self, node: Node):
        # create item
        item: NodeItem

        if node in self.node_items__cache.keys():  # load from cache
            # print('using a cached item')
            item = self.node_items__cache[node]
            self._add_node_item(item)

        else:  # create new item
            item = NodeItem(
                node=node,
                node_gui=
                    (node.GUI if hasattr(node, 'GUI') else NodeGUI)     # use custom GUI class if available
                    ((node, self.session_gui)),                         # calls __init__ of NodeGUI class with tuple arg
                flow_view=self,
                design=self.session_gui.design,
            )
            item.initialize()

            self.node_placed.emit(node)

            item_data = node.load_data
            if item_data is not None and 'pos x' in item_data:
                pos = QPointF(item_data['pos x'], item_data['pos y'])
            else:
                pos = self._node_place_pos

            self._add_node_item(item, pos)

        # auto connect
        if self._auto_connection_pin:
            self.auto_connect(self._auto_connection_pin.port, node)

    def _add_node_item(self, item: NodeItem, pos=None):
        self.node_items[item.node] = item

        self._set_selection_mode(_SelectionMode.INSTANT)

        self.scene().addItem(item)
        if pos:
            item.setPos(pos)

        # select new item
        self.clear_selection()
        item.setSelected(True)

    def remove_node(self, node):
        item = self.node_items[node]
        self._remove_node_item(item)
        del self.node_items[node]

    def _remove_node_item(self, item: NodeItem):
        # store item in case the remove action gets undone later
        self._set_selection_mode(_SelectionMode.INSTANT)
        self.node_items__cache[item.node] = item
        self.scene().removeItem(item)

    # CONNECTIONS
    def connect_node_ports__cmd(self, p1: NodePort, p2: NodePort):
        # Need to check order of ports since Flow.check_connection_validity needs (NodeOutput, NodeInput)
        if isinstance(p1, NodeOutput) and isinstance(p2, NodeInput):
            self._temp_connection_ports = (p1, p2)
            self._waiting_for_connection_request = True
            self.check_connection_validity_request.emit((p1, p2), True)

        elif isinstance(p1, NodeInput) and isinstance(p2, NodeOutput):
            self._temp_connection_ports = (p2, p1)
            self._waiting_for_connection_request = True
            self.check_connection_validity_request.emit((p2, p1), True)

        else:
            self.connection_request_valid(False)

    def connection_request_valid(self, valid: bool):
        """
        Triggered after the abstract flow evaluated validity of pending connect request.
        This can also lead to a disconnect!
        """
        
        # TODO: this stuff is too complicated, simplify

        if self._waiting_for_connection_request:
            self._waiting_for_connection_request = False
        else:
            return

        assert self._temp_connection_ports is not None

        if valid:
            out: NodeOutput
            inp: NodeInput
            out, inp = self._temp_connection_ports

            if self.flow.graph_adj_rev[inp] not in (None, out): # out connected to something else
                # remove existing connection
                self.push_undo(
                    ConnectPorts_Command(self, out=self.flow.graph_adj_rev[inp], inp=inp)
                )

            if self.flow.connected_output(inp) == out:
                # if the exact connection exists, we want to remove it by command
                self.push_undo(
                    ConnectPorts_Command(self, out=self.flow.connected_output(inp), inp=inp)
                )
            else:
                self.push_undo(ConnectPorts_Command(self, out=out, inp=inp))

    def add_connection(self, c: Tuple[NodeOutput, NodeInput]):
        out, inp = c

        # TODO: need to verify that connection_items_cache still works fine with new connection object
        item: ConnectionItem
        if c in self.connection_items__cache.keys():
            item = self.connection_items__cache[c]
        else:
            if inp.type_ == 'data':
                # item = self.CLASSES['data conn item'](c, self.session.design)
                item = DataConnectionItem(c, self.session_gui.design)
            else:
                # item = self.CLASSES['exec conn item'](c, self.session.design)
                item = ExecConnectionItem(c, self.session_gui.design)

        self._add_connection_item(item)

        item.out_item.port_connected()
        item.inp_item.port_connected()
        # for updating the visual state
        for i in c:
            self.node_items[i.node].update()

    def _add_connection_item(self, item: ConnectionItem):
        self._set_selection_mode(_SelectionMode.INSTANT)
        self.connection_items[item.connection] = item
        self.scene().addItem(item)
        item.recompute()
        item.setZValue(-1)
        # self.viewport().repaint()

    def remove_connection(self, c: Tuple[NodeOutput, NodeInput]):
        item = self.connection_items[c]
        self._remove_connection_item(item)

        item.out_item.port_disconnected()
        item.inp_item.port_disconnected()
        # for updating the visual state
        for i in c:
            self.node_items[i.node].update()
        del self.connection_items[c]

    def _remove_connection_item(self, item: ConnectionItem):
        self._set_selection_mode(_SelectionMode.INSTANT)
        self.connection_items__cache[item.connection] = item
        self.scene().removeItem(item)

    def auto_connect(self, p: NodePort, n: Node):
        if p.io_pos == PortObjPos.OUTPUT:
            for inp in n.inputs:
                if p.type_ == inp.type_:
                    # connect exactly once
                    self.connect_node_ports__cmd(p, inp)
                    return
        elif p.io_pos == PortObjPos.INPUT:
            for out in n.outputs:
                if p.type_ == out.type_:
                    # connect exactly once
                    self.connect_node_ports__cmd(p, out)
                    return

    def update_conn_item(self, c: Tuple[NodeOutput, NodeInput]):
        if c in self.connection_items:
            self.connection_items[c].changed = True
            self.connection_items[c].update()

    # DRAWINGS
    def create_drawing(self, data=None) -> DrawingObject:
        """Creates and returns a new DrawingObject."""

        new_drawing = DrawingObject(self, data)
        return new_drawing

    def add_drawing(self, drawing_obj: DrawingObject, posF=None):
        """Adds a DrawingObject to the scene."""

        self._set_selection_mode(_SelectionMode.INSTANT)
        self.scene().addItem(drawing_obj)
        if posF:
            drawing_obj.setPos(posF)
        self.drawings.append(drawing_obj)

    def add_drawings(self, drawings):
        """Adds a list of DrawingObjects to the scene."""

        for d in drawings:
            self.add_drawing(d)

    def remove_drawing(self, drawing: DrawingObject):
        """Removes a drawing from the scene."""

        # TODO https://github.com/leon-thomm/ryvencore/issues/4
        self._set_selection_mode(_SelectionMode.INSTANT)
        self.scene().removeItem(drawing)
        self.drawings.remove(drawing)

    def place_drawings_from_data(self, drawings_data: list, offset_pos=QPoint(0, 0)):
        """Creates and places drawings from drawings. The same list is returned by the data_() method
        at 'drawings'."""

        new_drawings = []
        for d_data in drawings_data:
            x = d_data['pos x'] + offset_pos.x()
            y = d_data['pos y'] + offset_pos.y()
            new_drawing = self.create_drawing(data=d_data)
            self.add_drawing(new_drawing, QPointF(x, y))
            new_drawings.append(new_drawing)

        return new_drawings

    def _create_and_place_drawing__cmd(self, posF, data=None):
        new_drawing_obj = self.create_drawing(data)
        place_command = PlaceDrawing_Command(self, posF, new_drawing_obj)
        self.push_undo(place_command)
        return new_drawing_obj

    # ADDING/REMOVING COMPONENTS
    def add_component(self, e: QGraphicsItem):
        if isinstance(e, NodeItem):
            self.add_node(e.node)
        elif isinstance(e, DrawingObject):
            self.add_drawing(e)

    def remove_components(self, comps: List[QGraphicsItem]):
        for c in comps:
            self.remove_component(c)

    def remove_component(self, e: QGraphicsItem):
        if isinstance(e, NodeItem):
            self.remove_node(e.node)
        elif isinstance(e, DrawingObject):
            self.remove_drawing(e)

    def remove_selected_components__cmd(self):
        if self._current_selected:
            self.push_undo(RemoveComponents_Command(self, self._current_selected))

        self.viewport().update()

    # MOVING COMPONENTS
    def _move_selected_copmonents__cmd(self, pos_diff: QPointF, already_moved=False):

        # if one node item would leave the scene (f.ex. pos.x < 0), stop
        left = False
        for i in self.scene().selectedItems():
            new_pos = i.pos() + pos_diff
            w = i.boundingRect().width()
            h = i.boundingRect().height()
            if (
                new_pos.x() - w / 2 < 0
                or new_pos.x() + w / 2 > self.scene().width()
                or new_pos.y() - h / 2 < 0
                or new_pos.y() + h / 2 > self.scene().height()
            ):
                left = True
                break

        if not left:
            # moving the items
            if not already_moved:
                items_group = self.scene().createItemGroup(self.scene().selectedItems())
                items_group.moveBy(pos_diff.x(), pos_diff.y())
                self.scene().destroyItemGroup(items_group)

            # saving the command
            self.push_undo(
                MoveComponents_Command(
                    self,
                    self.scene().selectedItems(),
                    p_from=-pos_diff,
                    p_to=QPointF(0, 0),
                )
            )

        self.viewport().repaint()

    def _move_selected_comps_left(self):
        self._move_selected_copmonents__cmd(QPointF(-40, 0))

    def _move_selected_comps_up(self):
        self._move_selected_copmonents__cmd(QPointF(0, -40))

    def _move_selected_comps_right(self):
        self._move_selected_copmonents__cmd(QPointF(+40, 0))

    def _move_selected_comps_down(self):
        self._move_selected_copmonents__cmd(QPointF(0, +40))

    # SELECTION
    def _scene_selection_changed(self):
        if self.selection_mode == _SelectionMode.INSTANT:
            self._current_selected = self.scene().selectedItems()
            self.emit_selected_items()
        elif self.selection_mode == _SelectionMode.UNDOABLE_CLICK:
            self._select__cmd()

    def _watch_scene_selection(self):
        self.scene().selectionChanged.connect(self._scene_selection_changed)

    def _unwatch_scene_selection(self):
        self.scene().selectionChanged.disconnect(self._scene_selection_changed)

    def emit_selected_items(self):
        """Emits signals indicating selection changes."""

        self.nodes_selection_changed.emit(self.selected_nodes())

    def _set_selection_mode(self, mode: _SelectionMode):
        self.selection_mode = mode

    def _select__cmd(self):
        items = self.scene().selectedItems()
        if items != self._current_selected:
            self.push_undo(
                SelectComponents_Command(self, items, self._current_selected)
            )

    def selected_node_items(self, item_list: Optional[List[NodeItem]] = None) -> List[NodeItem]:
        """Returns a list of the currently selected NodeItems."""

        search_list = item_list if item_list is not None else self.scene().selectedItems()
        return [node_item for node_item in search_list if isinstance(node_item, NodeItem)]

    def selected_nodes(self, item_list: Optional[List[NodeItem]] = None) -> List[Node]:
        """Returns a list of the currently selected nodes."""
        
        return [node_item.node for node_item in self.selected_node_items(item_list)]

    def selected_drawings(self) -> List[DrawingObject]:
        """Returns a list of the currently selected drawings."""

        return [
            drawing
            for drawing in self.scene().selectedItems()
            if isinstance(drawing, DrawingObject)
        ]

    def select_items(self, items: list):
        """
        Selects a list of items in the scene.
        It always clears the current selection
        Does not cause any command to be pushed to the undo stack.
        Emits signals indicating selection changes.
        """
        
        self._unwatch_scene_selection()
        self._current_selected = items
        for i in self.scene().items():
            if i.flags() & QGraphicsItem.ItemIsSelectable != 0:
                i.setSelected(False)
                
        for i in items:
            if i.flags() & QGraphicsItem.ItemIsSelectable != 0:
                i.setSelected(True)
        self.emit_selected_items()
        self.viewport().repaint()
        self._watch_scene_selection()

    def select_all(self):
        self.select_items(self.scene().items())

    def clear_selection(self):
        self.select_items([])

    # ACTIONS
    def _select_all_action(self):  # ctrl+a
        all_items = self.scene().items()
        if all_items != self._current_selected:
            self.push_undo(SelectComponents_Command(self, all_items, self._current_selected))

    def _copy(self):  # ctrl+c
        data = {
            'nodes': self._get_nodes_data(self.selected_nodes()),
            'connections': self._get_connections_data(self.selected_nodes()),
            'output data': self._get_output_data(self.selected_nodes()),
            'drawings': self._get_drawings_data(self.selected_drawings()),
        }
        QGuiApplication.clipboard().setText(json.dumps(data))

    def _cut(self):  # ctrl+x
        data = {
            'nodes': self._get_nodes_data(self.selected_nodes()),
            'connections': self._get_connections_data(self.selected_nodes()),
            'drawings': self._get_drawings_data(self.selected_drawings()),
        }
        QGuiApplication.clipboard().setText(json.dumps(data))
        self.remove_selected_components__cmd()

    def _paste(self):  # ctrl+v
        data = {}
        try:
            data = json.loads(QGuiApplication.clipboard().text())
        except Exception as e:
            return

        self.clear_selection()

        # calculate offset
        positions = []
        for d in data['drawings']:
            positions.append({
                'x': d['pos x'], 
                'y': d['pos y']
            })
        for n in data['nodes']:
            positions.append({
                'x': n['pos x'], 
                'y': n['pos y']
            })

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

            offset_for_middle_pos = self._last_mouse_move_pos - rect.center()

        self.push_undo(Paste_Command(self, data, offset_for_middle_pos))

    # DATA
    def complete_data(self, data: Dict):
        data['flow view'] = {
            'drawings': self._get_drawings_data(self.drawings),
            'view size': [
                self.sceneRect().size().width(),
                self.sceneRect().size().height(),
            ],
        }

        return data

    def _get_nodes_data(self, nodes):
        """generates the data for the specified list of nodes"""
        f_complete_data = self.session_gui.core_session.complete_data
        return f_complete_data(self.flow._gen_nodes_data(nodes))

    def _get_connections_data(self, nodes):
        """generates the connections data for connections between a specified list of nodes"""
        f_complete_data = self.session_gui.core_session.complete_data
        return f_complete_data(self.flow._gen_conns_data(nodes))

    def _get_output_data(self, nodes):
        """generates the serialized data of output ports of the specified nodes"""
        f_complete_data = self.session_gui.core_session.complete_data
        return f_complete_data(self.flow._gen_output_data(nodes))

    def _get_drawings_data(self, drawings):
        """generates the data for a list of drawings"""

        return [d.data() for d in drawings]

    def save_state(self) -> dict:
        """Save the state of the view in a json-compliant dict"""
        transform = self.transform()
        return {
            'm11': transform.m11(),  # Horizontal scaling
            'm12': transform.m12(),  # Horizontal shearing
            'm13': transform.m13(),  # Horizontal projection
            'm21': transform.m21(),  # Vertical shearing
            'm22': transform.m22(),  # Vertical scaling
            'm23': transform.m23(),  # Vertical projection
            'm31': transform.m31(),  # Horizontal translation
            'm32': transform.m32(),  # Vertical translation
            'm33': transform.m33(),  # Perspective division
            'v_scroll': self.horizontalScrollBar().value(),
            'h_scroll': self.verticalScrollBar().value(),
        }
    
    def load(self, state: Dict):
        """Load the state of the view"""
        transform = QTransform(
            state['m11'], state['m12'], state['m13'],
            state['m21'], state['m22'], state['m23'],
            state['m31'], state['m32'], state['m33']
        )
        
        self.setTransform(transform)
        self.horizontalScrollBar().setValue(state['v_scroll'])
        self.verticalScrollBar().setValue(state['h_scroll'])
        
        self._loaded_state = state
    
    def reload(self):
        if self._loaded_state is not None:
            self.load(self._loaded_state)
        