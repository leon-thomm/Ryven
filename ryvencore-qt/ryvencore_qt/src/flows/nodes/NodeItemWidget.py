# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .NodeGUI import NodeGUI
    from .NodeItem import NodeItem
    from ..FlowView import FlowView

from qtpy.QtCore import QPointF, QRectF, Qt, QSizeF
from qtpy.QtWidgets import QGraphicsWidget, QGraphicsLinearLayout, QSizePolicy, QWidget

from typing import Optional

from .NodeItem_CollapseButton import NodeItem_CollapseButton
from ..FlowViewProxyWidget import FlowViewProxyWidget
# from .Node import Node
from .NodeItem_Icon import NodeItem_Icon
from .NodeItem_TitleLabel import TitleLabel
from .PortItem import InputPortItem, OutputPortItem

from ryvencore import Flow


class NodeItemWidget(QGraphicsWidget):
    """The QGraphicsWidget managing all GUI components of a NodeItem in widgets and layouts."""

    def __init__(self, node_gui: NodeGUI, node_item: NodeItem) -> None:
        super().__init__(parent=node_item)

        self.node_gui: NodeGUI = node_gui
        self.node_item: NodeItem = node_item
        self.flow_view: FlowView = self.node_item.flow_view
        self.flow: Flow = self.flow_view.flow

        self.body_padding = 6
        self.header_padding = (0, 0, 0, 0)  # theme dependent and hence updated in setup_layout()!

        self.icon = NodeItem_Icon(node_gui, node_item) if node_gui.icon else None
        self.title_label = TitleLabel(node_gui, node_item)
        self.main_widget_proxy: Optional[FlowViewProxyWidget] = None
        if self.node_item.main_widget:
            assert isinstance(self.node_item.main_widget, QWidget)
            self.main_widget_proxy = FlowViewProxyWidget(self.flow_view)
            self.main_widget_proxy.setWidget(self.node_item.main_widget)
        self.header_layout: Optional[QGraphicsWidget]
        self.header_widget: Optional[QGraphicsWidget]
        self.collapse_button: Optional[NodeItem_CollapseButton]
        self.body_layout: QGraphicsLinearLayout
        self.body_widget: QGraphicsWidget
        self.inputs_layout: QGraphicsLinearLayout
        self.outputs_layout: QGraphicsLinearLayout
        self.setLayout(self.setup_layout())

    def setup_layout(self) -> QGraphicsLinearLayout:

        self.header_padding = self.node_item.session_design.flow_theme.header_padding

        #   main layout
        layout = QGraphicsLinearLayout(Qt.Vertical)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        if self.node_gui.style == 'normal':
            self.collapse_button = NodeItem_CollapseButton(self.node_gui, self.node_item)

            self.header_widget = QGraphicsWidget()
            # self.header_widget.setContentsMargins(0, 0, 0, 0)
            self.header_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            self.header_layout = QGraphicsLinearLayout(Qt.Horizontal)
            self.header_layout.setSpacing(5)
            self.header_layout.setContentsMargins(
                *self.header_padding
            )
            if self.icon:
                self.header_layout.addItem(self.icon)
                self.header_layout.setAlignment(self.icon, Qt.AlignVCenter | Qt.AlignLeft)

            self.header_layout.addItem(self.title_label)

            self.header_layout.addItem(self.collapse_button)
            self.header_layout.setAlignment(self.collapse_button, Qt.AlignVCenter | Qt.AlignRight)

            self.header_widget.setLayout(self.header_layout)
            # layout.addItem(self.header_layout)
            layout.addItem(self.header_widget)
            # layout.setAlignment(self.title_label, Qt.AlignTop)
        else:
            self.collapse_button = None
            self.header_widget = None
            self.header_layout = None
            self.setZValue(self.title_label.zValue() + 1)

        #   inputs
        self.inputs_layout = QGraphicsLinearLayout(Qt.Vertical)
        self.inputs_layout.setSpacing(2)

        #   outputs
        self.outputs_layout = QGraphicsLinearLayout(Qt.Vertical)
        self.outputs_layout.setSpacing(2)

        #   body
        self.body_widget = QGraphicsWidget()
        # self.body_widget.setContentsMargins(0, 0, 0, 0)
        self.body_layout = QGraphicsLinearLayout(Qt.Horizontal)
        self.body_layout.setContentsMargins(
            self.body_padding,
            self.body_padding,
            self.body_padding,
            self.body_padding
        )

        self.body_layout.setSpacing(4)
        self.body_layout.addItem(self.inputs_layout)
        self.body_layout.setAlignment(self.inputs_layout, Qt.AlignVCenter | Qt.AlignLeft)
        self.body_layout.addStretch()
        self.body_layout.addItem(self.outputs_layout)
        self.body_layout.setAlignment(self.outputs_layout, Qt.AlignVCenter | Qt.AlignRight)

        self.body_widget.setLayout(self.body_layout)

        # layout.addItem(self.body_layout)
        layout.addItem(self.body_widget)

        return layout

    def rebuild_ui(self):
        """Due to some really strange and annoying behaviour of these QGraphicsWidgets, they don't want to shrink
        automatically when content is removed, they just stay large, even with a Minimum SizePolicy. I didn't find a
        way around that yet, so for now I have to recreate the whole layout and make sure the widget uses the smallest
        size possible."""

        # if I don't manually remove the ports from the layouts,
        # they get deleted when setting the widget's layout to None below
        for i, inp in enumerate(self.node_item.inputs):
            self.inputs_layout.removeAt(0)
            # inp.rebuild_ui()
        for i, out in enumerate(self.node_item.outputs):
            self.outputs_layout.removeAt(0)
            # out.rebuild_ui()

        self.setLayout(None)
        self.resize(self.minimumSize())
        self.setLayout(self.setup_layout())

        if self.node_item.collapsed:
            return

        for inp_item in self.node_item.inputs:
            self.add_input_to_layout(inp_item)
        for out_item in self.node_item.outputs:
            self.add_output_to_layout(out_item)

        if self.node_item.main_widget:
            self.add_main_widget_to_layout()

    def update_shape(self):

        self.title_label.update_shape()

        # makes extended node items shrink according to resizing input widgets
        if not self.node_item.initializing:
            self.rebuild_ui()
        # strangely, this only works for small node items without this, not for normal ones

        mw = self.node_item.main_widget
        if mw is not None:  # maybe the main_widget got resized
            assert self.main_widget_proxy is not None

            # self.main_widget_proxy.setMaximumSize(mw.size())

            # self.main_widget_proxy.setMaximumSize(mw.maximumSize())

            self.main_widget_proxy.setMaximumSize(QSizeF(mw.size()))
            self.main_widget_proxy.setMinimumSize(QSizeF(mw.size()))

            self.adjustSize()
            self.adjustSize()

        self.body_layout.invalidate()
        self.layout().invalidate()
        self.layout().activate()
        # very essential; repositions everything in case content has changed (inputs/outputs/widget)

        if self.node_gui.style == 'small':

            # making it recompute its true minimumWidth here
            self.adjustSize()

            if self.layout().minimumWidth() < self.title_label.width + 15:
                self.layout().setMinimumWidth(self.title_label.width + 15)
                self.layout().activate()

        w = self.boundingRect().width()
        h = self.boundingRect().height()
        rect = QRectF(QPointF(-w / 2, -h / 2),
                      QPointF(w / 2, h / 2))
        self.setPos(rect.left(), rect.top())

        if not self.node_gui.style == 'normal':
            if self.icon:
                self.icon.setPos(
                    QPointF(-self.icon.boundingRect().width() / 2,
                            -self.icon.boundingRect().height() / 2)
                )
                self.title_label.hide()
            else:
                self.title_label.setPos(
                    QPointF(-self.title_label.boundingRect().width() / 2,
                            -self.title_label.boundingRect().height() / 2)
                )


    def add_main_widget_to_layout(self):
        assert self.main_widget_proxy is not None
        if self.node_gui.main_widget_pos == 'between ports':
            self.body_layout.insertItem(1, self.main_widget_proxy)
            self.body_layout.insertStretch(2)

        elif self.node_gui.main_widget_pos == 'below ports':
            self.layout().addItem(self.main_widget_proxy)
            self.layout().setAlignment(self.main_widget_proxy, Qt.AlignHCenter)

    def add_input_to_layout(self, inp: InputPortItem):
        if self.inputs_layout.count() > 0:
            self.inputs_layout.addStretch()
        self.inputs_layout.addItem(inp)
        self.inputs_layout.setAlignment(inp, Qt.AlignLeft)

    def insert_input_into_layout(self, index: int, inp: InputPortItem):
        self.inputs_layout.insertItem(index * 2 + 1, inp)  # *2 bcs of the stretches
        self.inputs_layout.setAlignment(inp, Qt.AlignLeft)
        if len(self.node_gui.node.inputs) > 1:
            self.inputs_layout.insertStretch(index * 2 + 1)  # *2+1 because of the stretches, too

    def remove_input_from_layout(self, inp: InputPortItem):
        self.inputs_layout.removeItem(inp)

        # just a temporary workaround for the issues discussed here:
        # https://forum.qt.io/topic/116268/qgraphicslayout-not-properly-resizing-to-change-of-content
        self.rebuild_ui()

    def add_output_to_layout(self, out: OutputPortItem):
        if self.outputs_layout.count() > 0:
            self.outputs_layout.addStretch()
        self.outputs_layout.addItem(out)
        self.outputs_layout.setAlignment(out, Qt.AlignRight)

    def insert_output_into_layout(self, index: int, out: OutputPortItem):
        self.outputs_layout.insertItem(index * 2 + 1, out)  # *2 because of the stretches
        self.outputs_layout.setAlignment(out, Qt.AlignRight)
        if len(self.node_gui.node.outputs) > 1:
            self.outputs_layout.insertStretch(index * 2 + 1)  # *2+1 because of the stretches, too

    def remove_output_from_layout(self, out: OutputPortItem):
        self.outputs_layout.removeItem(out)

        # just a temporary workaround for the issues discussed here:
        # https://forum.qt.io/topic/116268/qgraphicslayout-not-properly-resizing-to-change-of-content
        self.rebuild_ui()

    def collapse(self):
        self.body_widget.hide()
        if self.main_widget_proxy is not None:
            self.main_widget_proxy.hide()

    def expand(self):
        self.body_widget.show()
        if self.main_widget_proxy is not None:
            self.main_widget_proxy.show()

    def hide_unconnected_ports(self):
        for inp in self.node_item.node.inputs:
            if self.flow.connected_output(inp) is None:
                inp.hide()
        for out in self.node_item.node.outputs:
            if len(self.flow.connected_inputs(out)):
                out.hide()

    def show_unconnected_ports(self):
        for inp in self.node_item.inputs:
            inp.show()
        for out in self.node_item.outputs:
            out.show()
