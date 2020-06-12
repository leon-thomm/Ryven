from PySide2.QtWidgets import QGraphicsProxyWidget


class FlowProxyWidget(QGraphicsProxyWidget):
    def __init__(self, flow, parent=None):
        super(FlowProxyWidget, self).__init__(parent)

        self.flow = flow


    def mousePressEvent(self, arg__1):
        QGraphicsProxyWidget.mousePressEvent(self, arg__1)
        if arg__1.isAccepted():
            self.flow.ignore_mouse_event = True

    def mouseReleaseEvent(self, arg__1):
        self.flow.ignore_mouse_event = True
        QGraphicsProxyWidget.mouseReleaseEvent(self, arg__1)

    def wheelEvent(self, event):
        QGraphicsProxyWidget.wheelEvent(self, event)

    def keyPressEvent(self, arg__1):
        QGraphicsProxyWidget.keyPressEvent(self, arg__1)
        if arg__1.isAccepted():
            self.flow.ignore_key_event = True