import pathlib
from typing import Optional, Literal, List, Dict, Set, Union

from ryven import NodesPackage
from ryven.gui.styling.window_theme import WindowTheme


class Config:
    """
    Internal representation of the configuration that the application is
    currently using.

    The args parser uses the default values of this class for the defaults
    of config arguments (or cmd line). At runtime, this class is
    instantiated and populated with the values of the config arguments.

    WHEN MODIFYING THIS CLASS, make sure to update parse_sys_args() in
    args_parser.py accordingly.
    """

    #
    # config options declaration with default values.
    # the options where the type is a union will be literals
    # initially, but will be converted to actual types
    # by the args parser.
    #

    project: Optional[pathlib.Path] = None
    show_dialog: bool = True
    verbose: bool = False
    nodes: Union[Set[pathlib.Path], Set[NodesPackage]] = []
    example: Optional[str] = None
    window_theme: Union[str, WindowTheme] = 'dark'
    flow_theme: Optional[str] = None  # None means it depends on window_theme
    performance_mode: str = 'pretty'
    animations: bool = True
    window_geometry: Optional[str] = None
    window_title: str = 'Ryven'
    qt_api: str = 'pyside2'
    src_code_edits_enabled: bool = False

    @staticmethod
    def get_available_window_themes() -> Set[str]:
        return {'dark', 'light', 'plain'}

    @staticmethod
    def get_available_flow_themes() -> Set[str]:
        # FIXME: this is not stable api; expose it properly in ryvencore-qt
        from ryvencore_qt.src.Design import Design
        return {t.name for t in Design().flow_themes}

    @staticmethod
    def get_available_performance_modes() -> Set[str]:
        return {'pretty', 'fast'}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        global instance
        if instance is not None:
            raise RuntimeError('Config is a singleton')
        instance = self


instance: Optional[Config] = None
