from PySide2.QtCore import QRectF, QPointF, QSizeF, QThread, Signal, QObject
from PySide2.QtGui import QColor
from PySide2.QtWidgets import QGraphicsItem, QGraphicsView, QGraphicsScene, QMainWindow, QApplication


class Node(QObject):
    def __init__(self, view):
        super().__init__()

        self.item = NodeItem(view, self)
        self.moveToThread(view.worker)

    def update(self):
        print('helloo!')


class NodeItem(QGraphicsItem, QObject):

    triggered = Signal()

    def __init__(self, view, model):
        QGraphicsItem.__init__(self)
        QObject.__init__(self)

        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable |
                      QGraphicsItem.ItemSendsScenePositionChanges)

        self.view = view
        self.model = model
        self.triggered.connect(self.model.update)

    def mousePressEvent(self, event):
        event.accept()

        print('doing something here!!')
        self.triggered.emit()
        for i in range(100):
            print(i)

    def boundingRect(self) -> QRectF:
        return QRectF(0,0,50,50)

    def paint(self, painter, option, widget=...) -> None:
        painter.fillRect(self.boundingRect(), QColor('#555555'))


class ViewWorker(QThread):
    pass


class View(QGraphicsView):

    def __init__(self):
        super().__init__()

        self.resize(400, 300)
        scene = QGraphicsScene(self)
        scene.setSceneRect(0,0,self.width(),self.height())
        self.setScene(scene)

        self.worker = ViewWorker()
        self.worker.start()

    def mousePressEvent(self, event) -> None:
        QGraphicsView.mousePressEvent(self, event)
        if event.isAccepted():
            return

        node = Node(self)
        self.scene().addItem(node.item)
        node.item.setPos(event.pos())


class ViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(View())


if __name__ == '__main__':
    app = QApplication()
    widget = ViewWindow()
    widget.show()
    app.exec_()