# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ..FlowView import FlowView

import traceback
from typing import Optional, Tuple, List

from qtpy.QtWidgets import QGraphicsItem, QGraphicsObject, QMenu, QGraphicsDropShadowEffect
from qtpy.QtCore import Qt, QRectF, QObject, QPointF
from qtpy.QtGui import QColor

from .NodeErrorIndicator import NodeErrorIndicator
from .NodeGUI import NodeGUI
from ...GUIBase import GUIBase
from .NodeItemAction import NodeItemAction
from .NodeItemAnimator import NodeItemAnimator
from .NodeItemWidget import NodeItemWidget
from .PortItem import InputPortItem, OutputPortItem
from ...utils import serialize, deserialize, MovementEnum, generate_name

from ryvencore_qt.src.Design import Design

from ryvencore import Node
from ryvencore.NodePort import NodeInput, NodeOutput


class NodeItem(GUIBase, QGraphicsObject):  # QGraphicsItem, QObject):
    """The GUI representative for nodes. Unlike the Node class, this class is not subclassed individually and works
    the same for every node."""

    def __init__(self, node: Node, node_gui: NodeGUI, flow_view: FlowView, design: Design):
        GUIBase.__init__(self, representing_component=node)
        QGraphicsObject.__init__(self)

        self.node = node
        self.node_gui = node_gui
        self.node_gui.item = self
        self.flow_view = flow_view
        self.session_design: Design = design
        self.movement_state: Optional[MovementEnum] = None
        self.movement_pos_from: Optional[QPointF] = None
        self.painted_once: bool = False
        self.inputs: List[InputPortItem] = []
        self.outputs: List[OutputPortItem] = []
        self.color = QColor(self.node_gui.color)  # manipulated by self.animator

        self.collapsed = False
        self.hovered = False
        self.hiding_unconnected_ports = False
        self.displaying_error = False

        # 'initializing' will be set to False below. It's needed for the ports setup, to prevent shape updating stuff
        self.initializing = True

        # self.temp_state_data = None
        self.init_data = self.node.load_data

        # CONNECT TO NODE
        self.node_gui.updating.connect(self.node_updating)
        self.node_gui.update_shape_triggered.connect(self.update_shape)
        self.node_gui.hide_unconnected_ports_triggered.connect(self.hide_unconnected_ports_triggered)
        self.node_gui.show_unconnected_ports_triggered.connect(self.show_unconnected_ports_triggered)
        self.node_gui.input_added.connect(self.on_node_input_added)
        self.node_gui.output_added.connect(self.on_node_output_added)
        self.node_gui.input_removed.connect(self.on_node_input_removed)
        self.node_gui.output_removed.connect(self.on_node_output_removed)

        # FLAGS
        self.setFlags(
            QGraphicsItem.ItemIsSelectable |
            QGraphicsItem.ItemIsMovable |
            QGraphicsItem.ItemSendsScenePositionChanges
        )

        self.setAcceptHoverEvents(True)
        self.setCacheMode(QGraphicsItem.DeviceCoordinateCache)

        # UI
        self.shadow_effect = None
        self.main_widget = None
        if self.node_gui.main_widget_class is not None:
            self.main_widget = self.node_gui.main_widget_class((self.node, self, self.node_gui))
        self.widget = NodeItemWidget(self.node_gui, self)  # QGraphicsWidget(self)
        self.animator = NodeItemAnimator(self)  # needs self.title_label
        self.error_indicator = NodeErrorIndicator(self)
        self.error_indicator.hide()

        # TOOLTIP
        self.tooltip_descr_html_content = \
            self.node_gui.description_html \
            if self.node_gui.description_html is not None \
            else \
            f'<p>{self.node.__doc__}</p>'

        self.setToolTip(f'<html><head/><body>{self.tooltip_descr_html_content}</body></html>')

        # DESIGN THEME
        self.session_design.flow_theme_changed.connect(self.update_design)
        self.session_design.performance_mode_changed.connect(self.update_design)

    def initialize(self):
        """All ports and the main widget get finally created here."""

        # LOADING DATA
        if self.init_data is not None:
            if self.main_widget:
                try:
                    self.main_widget.set_state(deserialize(self.init_data['main widget data']))
                except Exception as e:
                    print('Exception while setting data in', self.node.title, 'Node\'s main widget:', e,
                          ' (was this intended?)')

        # catch up on init ports
        for inp in self.node.inputs:
            self.add_new_input(inp)

        for out in self.node.outputs:
            self.add_new_output(out)

        if self.init_data is not None:
            if self.init_data.get('unconnected ports hidden'):
                self.hide_unconnected_ports_triggered()
            if self.init_data.get('collapsed'):
                self.collapse()

        if self.init_data is not None:
            self.node_gui.load(self.init_data)

        self.node_gui.initialized()

        self.initializing = False

        # No self.update_shape() here because for some reason, the bounding rect hasn't been initialized yet, so
        # self.update_shape() gets called when the item is being drawn the first time (see paint event in NI painter)
        # https://forum.qt.io/topic/117179/force-qgraphicsitem-to-update-immediately-wait-for-update-event

        self.update_design()  # load current design, update QGraphicsItem

        self.update()  # ... not sure if I need that

    def __str__(self):
        name = self.node.__class__.title if self.node else f'{NodeItem.__name__}'
        obj = self.node if self.node else self
        return generate_name(obj, name)
    
    # UI STUFF

    def node_updating(self):
        if self.session_design.animations_enabled:
            if not self.animator.running():
                self.animator.start()
            elif self.animator.fading_out():
                self.animator.set_animation_max()

        self.update()

    def display_error(self, e):
        self.error_indicator.set_error(e)
        self.error_indicator.show()
        self.displaying_error = True

    def remove_error_message(self):
        self.error_indicator.hide()
        self.setToolTip(f'<html><head/><body>{self.tooltip_descr_html_content}</body></html>')

    def set_tooltip(self, error_msg=None):

        if error_msg is not None:
            err = f'<p style="background: red; color: white">{error_msg}</p>'
        else:
            err = ''

        if self.node.description_html:
            html = self.node.description_html + f'<html><head/><body>{err}</body></html>'
        elif self.node.__doc__:
            html = f'<html><head/><body><p>{self.node.__doc__}</p>{err}</body></html>'

        self.setToolTip(html)
        self.setCursor(Qt.SizeAllCursor)

    def on_node_input_added(self, index, inp: NodeInput):
        insert = index if index == len(self.node.inputs) - 1 else None
        self.add_new_input(inp, insert)

    def add_new_input(self, inp: NodeInput, insert: Optional[int] = None):

        if inp in self.node_gui.input_widgets:
            widget_name = self.node_gui.input_widgets[inp]['name']
            widget_class = self.node_gui.input_widget_classes[widget_name]
            widget_pos = self.node_gui.input_widgets[inp]['pos']
            widget = (widget_class, widget_pos)
        else:
            widget = None

        # create item
        item = InputPortItem(self.node_gui, self, inp, input_widget=widget)

        if insert is not None:
            self.inputs.insert(insert, item)
            self.widget.insert_input_into_layout(insert, item)
        else:
            self.inputs.append(item)
            self.widget.add_input_to_layout(item)

        if not self.initializing:
            self.update_shape()
            self.update()

    def on_node_input_removed(self, index, inp: NodeInput):
        self.remove_input(inp)

    def remove_input(self, inp: NodeInput):
        item: InputPortItem
        for inp_item in self.inputs:
            if inp_item.port == inp:
                item = inp_item
                break
        else:
            return

        # index = self.node.inputs.index(inp)
        # item = self.inputs[index]

        # for some reason, I have to remove all widget items manually from the scene too. setting the items to
        # ownedByLayout(True) does not work, I don't know why.
        self.scene().removeItem(item.pin)
        self.scene().removeItem(item.label)
        if item.proxy is not None:
            self.scene().removeItem(item.proxy)

        self.inputs.remove(item)
        self.widget.remove_input_from_layout(item)

        if not self.initializing:
            self.update_shape()
            self.update()

    def on_node_output_added(self, index, out: NodeOutput):
        insert = index if index == len(self.node.outputs) - 1 else None
        self.add_new_output(out, insert)

    def add_new_output(self, out: NodeOutput, insert: Optional[int] = None):

        # create item
        # out.item = OutputPortItem(out.node, self, out)
        item = OutputPortItem(self.node_gui, self, out)

        if insert is not None:
            self.outputs.insert(insert, item)
            self.widget.insert_output_into_layout(insert, item)
        else:
            self.outputs.append(item)
            self.widget.add_output_to_layout(item)

        if not self.initializing:
            self.update_shape()
            self.update()

    def on_node_output_removed(self, index, out: NodeOutput):
        self.remove_output(out)

    def remove_output(self, out: NodeOutput):
        item: OutputPortItem
        for out_item in self.outputs:
            if out_item.port == out:
                item = out_item
                break
        else:
            return

        # index = self.node.outputs.index(out)
        # item = self.outputs[index]

        # see remove_input() for info!
        self.scene().removeItem(item.pin)
        self.scene().removeItem(item.label)

        self.outputs.remove(item)
        self.widget.remove_output_from_layout(item)

        if not self.initializing:
            self.update_shape()
            self.update()

    def update_shape(self):
        self.widget.update_shape()
        self.update_conn_pos()
        self.flow_view.viewport().update()

    def update_design(self):
        """Loads the shadow effect option and causes redraw with active theme."""

        if self.session_design.node_item_shadows_enabled:
            self.shadow_effect = QGraphicsDropShadowEffect()
            self.shadow_effect.setXOffset(12)
            self.shadow_effect.setYOffset(12)
            self.shadow_effect.setBlurRadius(20)
            self.shadow_effect.setColor(self.session_design.flow_theme.node_item_shadow_color)
            self.setGraphicsEffect(self.shadow_effect)
        else:
            self.setGraphicsEffect(None)

        self.widget.update_shape()
        self.animator.reload_values()

        QGraphicsItem.update(self)

    def boundingRect(self):
        # remember: (0, 0) shall be the NI's center!
        rect = QRectF()
        w = self.widget.layout().geometry().width()
        h = self.widget.layout().geometry().height()
        rect.setLeft(-w / 2)
        rect.setTop(-h / 2)
        rect.setWidth(w)
        rect.setHeight(h)
        return rect

    def get_left_body_header_vertex_scene_pos(self) -> QPointF:
        assert self.widget.header_widget is not None
        return self.mapToScene(
            QPointF(
                -self.boundingRect().width() / 2,
                -self.boundingRect().height() / 2 + self.widget.header_widget.rect().height()
            )
        )

    def get_right_body_header_vertex_scene_pos(self) -> QPointF:
        assert self.widget.header_widget is not None
        return self.mapToScene(
            QPointF(
                +self.boundingRect().width() / 2,
                -self.boundingRect().height() / 2 + self.widget.header_widget.rect().height()
            )
        )

    def hide_unconnected_ports_triggered(self):
        self.widget.hide_unconnected_ports()
        self.hiding_unconnected_ports = True
        self.update_shape()

    def show_unconnected_ports_triggered(self):
        self.widget.show_unconnected_ports()
        self.hiding_unconnected_ports = False
        self.update_shape()

    def expand(self):
        self.collapsed = False
        self.widget.expand()
        self.update_shape()

    def collapse(self):
        self.collapsed = True
        self.widget.collapse()
        self.update_shape()

    #   PAINTING

    def paint(self, painter, option, widget=None):
        """All painting is done by NodeItemPainter"""

        # in order to access a meaningful geometry of GraphicsWidget contents in update_shape(), the paint event
        # has to be called once.
        # https://forum.qt.io/topic/117179/force-qgraphicsitem-to-update-immediately-wait-for-update-event/4
        if not self.painted_once:
            # Since I am using a NodeItemWidget, calling self.update_design() here (again)
            # leads to a QT crash without error, which is strange. In pronciple, calling update_design multiple times
            # shouldn't be a problem. It's not necessary anymore, so I removed it.
            # self.update_design()

            self.update_shape()
            self.update_conn_pos()
            self.error_indicator.setPos(self.boundingRect().bottomRight())

        self.session_design.flow_theme.paint_NI(
            node_gui=self.node_gui,
            selected=self.isSelected(),
            hovered=self.hovered,
            node_style=self.node_gui.style,
            painter=painter,
            option=option,
            color=self.color,
            w=self.boundingRect().width(),
            h=self.boundingRect().height(),
            bounding_rect=self.boundingRect(),
            title_rect=self.widget.header_widget.boundingRect()
            if self.widget.header_widget
            else self.widget.title_label.boundingRect()
        )

        # useful for widget development:

        # painter.setBrush(Qt.NoBrush)
        # painter.setPen(QPen(QColor('black')))
        #
        # painter.drawRect(
        #         self.boundingRect()
        # )
        #
        # header_rect = QRectF(
        #         -self.boundingRect().width()/2, -self.boundingRect().height()/2,
        #         self.widget.header_widget.geometry().width(), self.widget.header_widget.geometry().height()
        #     )
        # painter.drawRect(header_rect)
        #
        # # note that the widget's layout has spacing 0
        # body_rect = QRectF(
        #     -self.boundingRect().width()/2, -self.boundingRect().height()/2 + header_rect.height(),
        #     self.widget.body_widget.geometry().width(), self.widget.body_widget.geometry().height()
        # )
        # painter.drawRect(body_rect)

        self.painted_once = True

    # MOUSE INTERACTION

    def get_context_menu(self):
        menu = QMenu(self.flow_view)

        actions = self.get_actions(self.node_gui.actions, menu)
        for a in actions:  # menu needed for 'parent'
            if type(a) == NodeItemAction:
                menu.addAction(a)
            elif type(a) == QMenu:
                menu.addMenu(a)

        return menu

    def itemChange(self, change, value):
        """Ensures that all connections, selection borders etc. that get drawn in the FlowView get
        constantly redrawn during a drag of the item"""

        if change == QGraphicsItem.ItemPositionChange:
            if self.session_design.performance_mode == 'pretty':
                self.flow_view.viewport().update()
            if self.movement_state == MovementEnum.mouse_clicked:
                self.movement_state = MovementEnum.position_changed

            self.update_conn_pos()

        return QGraphicsItem.itemChange(self, change, value)

    def on_move(self):
        self.update_conn_pos()
    
    def update_conn_pos(self):
        """Updates the scene positions of connections"""

        for o in self.node.outputs:
            for i in self.node.flow.connected_inputs(o):
                # c.item.recompute()

                if (o, i) not in self.flow_view.connection_items:
                    # it can happen that the connection item hasn't been
                    # created yet
                    continue

                item = self.flow_view.connection_items[(o,i)]
                item.recompute()
        for i in self.node.inputs:
            o = self.node.flow.connected_output(i)
            # c.item.recompute()

            if (o, i) not in self.flow_view.connection_items:
                # it can happen that the connection item hasn't been
                # created yet
                continue

            item = self.flow_view.connection_items[(o,i)]
            item.recompute()

    def hoverEnterEvent(self, event):
        self.hovered = True
        self.widget.title_label.set_NI_hover_state(hovering=True)
        QGraphicsItem.hoverEnterEvent(self, event)

    def hoverLeaveEvent(self, event):
        self.hovered = False
        self.widget.title_label.set_NI_hover_state(hovering=False)
        QGraphicsItem.hoverLeaveEvent(self, event)

    def mousePressEvent(self, event):
        """Used for Moving-Commands in FlowView - may be replaced later by a nicer determination of a moving action."""

        self.flow_view.mouse_event_taken = True

        if event.button() == Qt.LeftButton:
            self.movement_state = MovementEnum.mouse_clicked
            self.movement_pos_from = self.pos()
        return QGraphicsItem.mousePressEvent(self, event)

    def mouseReleaseEvent(self, event):
        """Used for Moving-Commands in FlowView - may be replaced later by a nicer determination of a moving action."""

        self.flow_view.mouse_event_taken = True

        if self.movement_state == MovementEnum.position_changed:
            self.flow_view._move_selected_copmonents__cmd(
                pos_diff=self.pos() - self.movement_pos_from,
                already_moved=True,
            )
        self.movement_state = None
        return QGraphicsItem.mouseReleaseEvent(self, event)

    # ACTIONS

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
                action = NodeItemAction(node_gui=self.node_gui, text=k, method=method, menu=menu, data=data)
                actions.append(action)
            except KeyError:
                action_menu = QMenu(k, menu)
                sub_actions = self.get_actions(v_dict, action_menu)
                for a in sub_actions:
                    action_menu.addAction(a)
                actions.append(action_menu)

        return actions

    # DATA

    def complete_data(self, data: dict) -> dict:
        """completes the node's data by adding all frontend info"""

        data['pos x'] = self.pos().x()
        data['pos y'] = self.pos().y()
        if self.main_widget:
            data['main widget data'] = serialize(self.main_widget.get_state())

        data['unconnected ports hidden'] = self.hiding_unconnected_ports
        data['collapsed'] = self.collapsed

        data = {**data, **self.node_gui.data()}

        return data
