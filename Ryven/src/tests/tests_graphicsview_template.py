from PySide2.QtCore import QRectF, QPointF, QSizeF
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsItem, QGraphicsView, QGraphicsScene, QMainWindow, QApplication


class Item(QGraphicsItem):
    def __init__(self):
        super().__init__()

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)

    def mousePressEvent(self, event):
        event.accept()

        print('doing something here!!')
        # ...

    def boundingRect(self) -> QRectF:
        return QRectF(0,0,50,50)

    def paint(self, painter, option, widget=...) -> None:
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