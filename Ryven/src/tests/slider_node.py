import ryvencore_qt as rc
from PySide2.QtWidgets import QApplication, QMainWindow, QSlider
from PySide2.QtGui import Qt
import sys


class SliderIW(QSlider, rc.IWB):
    def __init__(self, params):
        QSlider.__init__(self, Qt.Horizontal)
        rc.IWB.__init__(self, params)

        self.setRange(0, 10)
        self.setSingleStep(1)


class MyNode(rc.Node):
    title = 'sehr lecker'
    input_widget_classes = {
        'slider': SliderIW,
    }
    init_inputs = [
        rc.NodeInputBP(add_config={'widget name': 'slider', 'widget pos': 'besides'})
    ]


if __name__ == '__main__':
    app = QApplication()
    mw = QMainWindow()

    session = rc.Session(flow_theme_name='Samuel 1l')
    session.register_node(MyNode)
    script = session.create_script('hello world')
    mw.setCentralWidget(session.flow_views[script])

    mw.show()
    sys.exit(app.exec_())
