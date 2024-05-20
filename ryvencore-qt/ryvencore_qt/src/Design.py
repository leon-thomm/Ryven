import json
from typing import Optional, List, Tuple

from qtpy.QtCore import QObject, Signal
from qtpy.QtGui import QFontDatabase

from .flows.FlowTheme import FlowTheme, flow_themes
from .GlobalAttributes import Location


class Design(QObject):
    """Design serves as a container for the stylesheet and flow themes, and sends signals to notify GUI elements
    on change of the flow theme. A configuration for the flow themes can be loaded from a json file.
    """

    global_stylesheet = ''

    flow_theme_changed = Signal(str)
    performance_mode_changed = Signal(str)

    def __init__(self) -> None:
        super().__init__()

        self.flow_themes: List[FlowTheme] = flow_themes
        self.flow_theme: FlowTheme
        self.default_flow_size: Tuple[int, int]
        self.performance_mode: str
        self.node_item_shadows_enabled: bool
        self.animations_enabled: bool
        self.node_selection_stylesheet: str

        # load standard default values
        self._default_flow_theme = self.flow_themes[-1]
        self.set_performance_mode('pretty')
        self.set_animations_enabled(True)
        self.default_flow_size = (1000, 700)
        self.set_flow_theme(self._default_flow_theme)

    @staticmethod
    def register_fonts():
        db = QFontDatabase()
        db.addApplicationFont(Location.PACKAGE_PATH + '/resources/fonts/poppins/Poppins-Medium.ttf')
        db.addApplicationFont(Location.PACKAGE_PATH + '/resources/fonts/source_code_pro/SourceCodePro-Regular.ttf')
        db.addApplicationFont(Location.PACKAGE_PATH + '/resources/fonts/asap/Asap-Regular.ttf')

    def load_from_config(self, filepath: str):
        """Loads design configs from a config json file"""

        f = open(filepath, 'r')
        data = f.read()
        f.close()

        IMPORT_DATA = json.loads(data)

        if 'flow themes' in IMPORT_DATA:
            # load flow theme configs
            FTID = IMPORT_DATA['flow themes']
            for flow_theme in self.flow_themes:
                flow_theme.load(FTID)

        if 'init flow theme' in IMPORT_DATA:
            self._default_flow_theme = self.flow_theme_by_name(IMPORT_DATA.get('init flow theme'))
            self.set_flow_theme(self._default_flow_theme)

        if 'init performance mode' in IMPORT_DATA:
            self.set_performance_mode(IMPORT_DATA['init performance mode'])

        if 'init animations enabled' in IMPORT_DATA:
            self.set_animations_enabled(IMPORT_DATA['init animations enabled'])

        if 'default flow size' in IMPORT_DATA:
            self.default_flow_size = IMPORT_DATA['default flow size']

    def available_flow_themes(self) -> dict:
        return {theme.name: theme for theme in self.flow_themes}

    def flow_theme_by_name(self, name: str) -> FlowTheme:
        for theme in self.flow_themes:
            if theme.name.casefold() == name.casefold():
                return theme
        raise ValueError(f'Flow theme with name "{name}" not found')

    def set_flow_theme(self, theme: Optional[FlowTheme] = None, name: Optional[str] = None):
        """You can either specify the theme by name, or directly provide a FlowTheme object"""
        if theme is not None:
            self.flow_theme = theme
        elif name is not None and name != '':
            self.flow_theme = self.flow_theme_by_name(name)
        else:
            return

        self.node_selection_stylesheet = self.flow_theme.build_node_selection_stylesheet()

        self.flow_theme_changed.emit(self.flow_theme.name)

    def set_performance_mode(self, new_mode: str):
        if new_mode == 'fast':
            self.node_item_shadows_enabled = False
        else:
            self.node_item_shadows_enabled = True
        self.performance_mode = new_mode
        self.performance_mode_changed.emit(self.performance_mode)

    def set_animations_enabled(self, b: bool):
        self.animations_enabled = b

    def set_node_item_shadows(self, b: bool):
        self.node_item_shadows_enabled = b
