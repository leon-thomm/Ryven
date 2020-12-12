from PySide6.QtWidgets import QMainWindow, QApplication, QGraphicsView, QGraphicsScene, QGestureRecognizer, QGesture
from PySide6.QtCore import QEvent


class PanGesture(QGesture):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.pos = None
        self.press = None
        self.last = None

class PanGestureRecognizer(QGestureRecognizer):
    """Not complete, just some test"""
    def create(self, target) -> QGesture:
        return PanGesture()

    def reset(self, state: QGesture) -> None:
        pass

    def recognize(self, state: QGesture, watched, event: QEvent) -> QGestureRecognizer.Result:
        """not doing anything yet"""
        return QGestureRecognizer.Ignore

class View(QGraphicsView):
    def __init__(self):
        super().__init__()

        scene = QGraphicsScene(self)
        scene.setSceneRect(0,0,10,10)
        self.setScene(scene)

        recognizer = PanGestureRecognizer()

        # CRASH HERE
        pan_gesture_id = QGestureRecognizer.registerRecognizer(recognizer)

        self.grabGesture(pan_gesture_id)

class ViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(View())

if __name__ == '__main__':
    app = QApplication()
    widget = ViewWindow()
    widget.show()
    app.exec_()
