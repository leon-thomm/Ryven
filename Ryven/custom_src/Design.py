from PySide2.QtCore import QObject, Signal


class DesignContainer(QObject):

    flow_themes = ['dark std', 'dark tron', 'ghostly', 'blender']
    start_flow_theme = 'blender'
    flow_theme = None  # initialized by MainWindow
    flow_theme_changed = Signal(str)
    performance_mode = 'fast'

    def set_flow_theme(self, new_theme: str = None):
        self.flow_theme = new_theme if new_theme is not None else self.start_flow_theme
        self.flow_theme_changed.emit(self.flow_theme)

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