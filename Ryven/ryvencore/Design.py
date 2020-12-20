from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtGui import QPen, QColor

from ryvencore.NodeInstancePainter import NIPainter_DarkStd, NIPainter_DarkTron, NIPainter_Ghostly, NIPainter_Blender, \
    NIPainter_Easy, NIPainter_Peasy, NIPainter_Ueli


class FlowTheme:
    """A FlowTheme holds all design information for the flow. And it defines what
    themes exist. Notice, that all drawing of NodeInstances and PortInstances
    is done by NIPainter classes, while for each FlowTheme there exists exactly
    one NIPainter class.

    HOW TO CREATE NEW THEMES
    - Create a new subclass of NIPainter in NodeInstancePainter.py, and implement
    all methods that are passed in NIPainter (take a look at the other already
    existing NIPainter subclasses there for reference)
    - Add a new theme entry to the flow_themes array of DesignContainer and
    reference the new NIPainter subclass for your new theme you just made"""

    def __init__(self, name,
                 flow_conn_exec_color, flow_conn_exec_width, flow_conn_exec_pen_style,
                 flow_conn_data_color, flow_conn_data_width, flow_conn_data_pen_style,
                 node_instance_painter,
                 flow_background_color=QColor('#333333')):
        self.name = name
        self.node_inst_painter = node_instance_painter

        self.flow_conn_exec_pen = QPen(flow_conn_exec_color, flow_conn_exec_width)
        self.flow_conn_exec_pen.setStyle(flow_conn_exec_pen_style)
        self.flow_conn_exec_pen.setCapStyle(Qt.RoundCap)

        self.flow_conn_data_pen = QPen(flow_conn_data_color, flow_conn_data_width)
        self.flow_conn_data_pen.setStyle(flow_conn_data_pen_style)
        self.flow_conn_data_pen.setCapStyle(Qt.RoundCap)

        self.flow_background_color = flow_background_color

    def get_flow_conn_pen_inst(self, connection_type):
        if connection_type == 'data':
            return self.flow_conn_data_pen.__copy__()
        else:
            return self.flow_conn_exec_pen.__copy__()



class Design(QObject):

    global_stylesheet = None

    flow_theme_changed = Signal(str)

    def __init__(self):
        super().__init__()

        self.flow_themes = [
            FlowTheme('dark std',
                      QColor(188, 187, 242),
                      5,
                      Qt.SolidLine,
                      QColor(188, 187, 242),
                      5,
                      Qt.DashLine,
                      NIPainter_DarkStd),
            FlowTheme('dark tron',
                      QColor(0, 120, 180),
                      4,
                      Qt.SolidLine,
                      QColor(0, 120, 180),
                      4,
                      Qt.DashLine,
                      NIPainter_DarkTron),
            FlowTheme('ghostly',
                      QColor(0, 17, 25),
                      2,
                      Qt.SolidLine,
                      QColor(0, 17, 25),
                      2,
                      Qt.DashLine,
                      NIPainter_Ghostly),
            FlowTheme('blender',
                      QColor(0, 17, 25),
                      2,
                      Qt.SolidLine,
                      QColor(0, 17, 25),
                      2,
                      Qt.DashLine,
                      NIPainter_Blender),
            FlowTheme('easy',
                      QColor('#989c9f'),
                      2,
                      Qt.SolidLine,
                      QColor('#989c9f'),
                      2,
                      Qt.DashLine,
                      NIPainter_Easy,
                      QColor('#212429')),
            FlowTheme('peasy',
                      QColor('#989c9f'),
                      2,
                      Qt.SolidLine,
                      QColor('#989c9f'),
                      2,
                      Qt.DashLine,
                      NIPainter_Peasy,
                      QColor('#3f4044')),
            FlowTheme('ueli',
                      QColor('#989c9f'),
                      2,
                      Qt.SolidLine,
                      QColor('#989c9f'),
                      2,
                      Qt.DashLine,
                      NIPainter_Ueli,
                      QColor('#3f4044'))
        ]

        self.default_flow_theme = self.flow_themes[-1]
        self.flow_theme = None  # initialized by MainWindow

        self.performance_mode = ''
        self.node_instance_shadows_shown = False
        self.set_performance_mode('pretty')

        self.animations_enabled = True
        self.node_choice_stylesheet = default_node_choice_stylesheet

    def set_flow_theme(self, new_theme=None):
        if type(new_theme) == str:
            for theme in self.flow_themes:
                if theme.name == new_theme:
                    self.flow_theme = theme
                    self.flow_theme_changed.emit(new_theme)
                    return

        self.flow_theme = new_theme if new_theme is not None else self.default_flow_theme
        self.flow_theme_changed.emit(self.flow_theme.name)

    def set_performance_mode(self, new_mode):
        self.performance_mode = new_mode
        if new_mode == 'fast':
            self.node_instance_shadows_shown = False
        else:
            self.node_instance_shadows_shown = True

        # the performance mode affects the flow's foreground theme
        self.flow_theme_changed.emit(self.flow_theme)


    def set_node_choice_stylesheet(self, s: str):
        self.node_choice_stylesheet = s





default_node_choice_stylesheet = '''
QWidget {
	background-color: #2b2b2b;
	border-radius: 3px;
	border: 1px solid #404040;;
	color: #dddddd;
}

QPushButton {
	border-radius: 5px;
	padding: 4px;
	background-color: #333333;
	min-width: 60px;
}
QPushButton:pressed {
	background-color: #3B9CD9;
}

QGroupBox {
	border: 1px solid #3B9CD9;;
	padding-top: 10px;
}

QLineEdit {
	padding: 3px;
}

QScrollArea {
	border: none;
}



QScrollBar:horizontal {
	border: none;
	background: #3f3f46;
	height: 12px;
	margin: 0 22px 0 22px;
	border-radius: 7px;
}
QScrollBar::handle:horizontal {
	background: #BCBBF2;
	min-height: 12px;
	border-radius: 5px;
}
QScrollBar::add-line:horizontal {
	background: none;
}
QScrollBar::sub-line:horizontal {
	background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
	background: none;
}

QScrollBar:vertical {
	border: none;
	background: #3f3f46;
	width: 12px;
	margin: 14px 0 14px 0;
	border-radius: 5px;
}
QScrollBar::handle:vertical {
	background: #BCBBF2;
	min-height: 20px;
	border-radius: 5px;
}
QScrollBar::add-line:vertical {
	background: none;
}
QScrollBar::sub-line:vertical {
	background: none;
}
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
	background: none;
	border: none;
}
'''