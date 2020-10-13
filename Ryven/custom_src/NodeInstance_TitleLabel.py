from PySide2.QtCore import QRectF, QPointF, QSizeF, Qt, Property
from PySide2.QtGui import QFont, QFontMetricsF, QColor, QPen
from PySide2.QtWidgets import QGraphicsWidget, QGraphicsLayoutItem, QGraphicsItem

from custom_src.Design import Design
from custom_src.global_tools.strings import get_longest_line


class TitleLabel(QGraphicsWidget):
    def __init__(self, parent_node_instance):
        super(TitleLabel, self).__init__(parent_node_instance)

        self.setGraphicsItem(self)

        self.parent_node_instance = parent_node_instance
        self.title_str = self.parent_node_instance.parent_node.title
        font = QFont('Poppins', 15) if self.parent_node_instance.parent_node.design_style == 'extended' else \
            QFont('K2D', 20, QFont.Bold, True)  # should be quite similar to every specific font chosen by the painter
        fm = QFontMetricsF(font)

        # approximately!
        self.width = fm.width(get_longest_line(self.title_str)+'___')
        self.height = fm.height() * 0.7 * (self.title_str.count('\n') + 1)

        self.color = QColor(30, 43, 48)
        self.pen_width = 1.5
        self.hovering = False  # whether the mouse is hovering over the parent NI (!)

        # Design.flow_theme_changed.connect(self.theme_changed)
        self.update_design()

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(self.width, self.height)

    def paint(self, painter, option, widget=None):

        Design.flow_theme.node_inst_painter.paint_NI_title_label(
            painter, option, self.hovering,
            self.design_style(), self.title_str, self.parent_node_instance.color,
            self.boundingRect()
        )

    def design_style(self):
        return self.parent_node_instance.parent_node.design_style

    def set_NI_hover_state(self, hovering: bool):
        self.hovering = hovering
        self.update_design()
    
    def theme_changed(self, new_theme):
        """Gets called from the parent node instance because the order of the different updates matters.""" # not working yet
        self.update_design()

    def update_design(self):

        self.update()


    # ANIMATION STUFF
    def get_color(self):
        return self.color

    def set_color(self, val):
        self.color = val
        QGraphicsItem.update(self)

    p_color = Property(QColor, get_color, set_color)