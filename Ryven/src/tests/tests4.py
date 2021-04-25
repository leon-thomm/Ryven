from qtpy.QtCore import QRectF, QPointF, QSizeF
from qtpy.QtGui import QColor
from qtpy.QtWidgets import QGraphicsItem, QGraphicsView, QGraphicsScene, QMainWindow, QApplication, \
    QGraphicsDropShadowEffect, QGraphicsWidget, QGraphicsLinearLayout, QGraphicsLayoutItem


class ItemLabel(QGraphicsWidget):
    def __init__(self, item):
        super(ItemLabel, self).__init__(parent=item)

    def boundingRect(self):
        return QRectF(QPointF(0, 0), self.geometry().size())

    def setGeometry(self, rect):
        self.prepareGeometryChange()
        QGraphicsLayoutItem.setGeometry(self, rect)
        self.setPos(rect.topLeft())

    def sizeHint(self, which, constraint=...):
        return QSizeF(50, 20)

    def paint(self, painter, option, widget=None):
        painter.fillRect(self.boundingRect(), QColor('#bbbb00'))




class ItemWidget(QGraphicsWidget):
    def __init__(self, item):
        super(ItemWidget, self).__init__(parent=item)

        layout = QGraphicsLinearLayout()
        layout.addItem(ItemLabel(item))
        self.setLayout(layout)


class Item(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)

        self.widget = ItemWidget(self)

    def mousePressEvent(self, event):
        event.accept()

        effect = QGraphicsDropShadowEffect()
        effect.setXOffset(12)
        effect.setYOffset(12)
        effect.setBlurRadius(20)
        effect.setColor(QColor('#2b2b2b'))
        self.setGraphicsEffect(effect)

    def boundingRect(self) -> QRectF:
        return QRectF(0,0,50,50)

    def paint(self, painter, option, widget) -> None:
        painter.fillRect(self.boundingRect(), QColor('#555555'))


class View(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        scene = QGraphicsScene(self)
        scene.setSceneRect(0,0,self.width(),self.height())
        self.setScene(scene)

    def mousePressEvent(self, event) -> None:
        QGraphicsView.mousePressEvent(self, event)
        if event.isAccepted():
            return

        newitem = Item()
        self.scene().addItem(newitem)
        newitem.setPos(event.pos())


class ViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(View())


if __name__ == '__main__':
    app = QApplication()
    widget = ViewWindow()
    widget.show()
    app.exec_()