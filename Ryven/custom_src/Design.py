from PySide2.QtCore import QObject, Signal, Qt
from PySide2.QtGui import QPen, QColor, QBrush

from custom_src.NodeInstancePainter import NIPainter_DarkStd, NIPainter_DarkTron, NIPainter_Ghostly, NIPainter_Blender, \
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

    # def draw_NI_extended_background(self, painter, c, w, h, bounding_rect):
    #     pass
    #
    # def draw_NI_minimalistic(self, painter, c, w, h, bounding_rect, background_color):
    #     pass


# class FlowThemeStdDark(FlowTheme):
#     def __init__(self):
#         super(FlowThemeStdDark, self).__init__(name='std dark',
#                                                flow_conn_exec_color=QColor(188, 187, 242),
#                                                flow_conn_exec_width=5,
#                                                flow_conn_exec_pen_style=Qt.SolidLine,
#                                                flow_conn_data_color=QColor(188, 187, 242),
#                                                flow_conn_data_width=5,
#                                                flow_conn_data_pen_style=Qt.DashLine)
#


class DesignContainer(QObject):

    # flow_themes = ['dark std', 'dark tron', 'ghostly', 'blender']
    flow_themes = [
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

    start_flow_theme = flow_themes[-1]
    flow_theme = None  # initialized by MainWindow
    flow_theme_changed = Signal(str)
    performance_mode = 'fast'

    def set_flow_theme(self, new_theme: str = None):
        self.flow_theme = new_theme if new_theme is not None else self.start_flow_theme
        self.flow_theme_changed.emit(self.flow_theme.name)

    def set_performance_mode(self, new_mode):
        self.performance_mode = new_mode
        if new_mode == 'fast':
            Design.node_instance_shadows_shown = False
        else:
            Design.node_instance_shadows_shown = True

        # the performance mode affects the flow's foreground theme
        self.flow_theme_changed.emit(self.flow_theme)

    ryven_stylesheet = None
    node_instance_shadows_shown = False
    animations_enabled = True


# I have to instantiate the Design in order to execute Qt Signals
Design = DesignContainer()