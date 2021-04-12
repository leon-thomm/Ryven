"""This file automatically imports all requirements for custom widgets.
It should lie in the same location as Ryven.py so it can get imported directly from the custom sources."""

from ryvencore_qt import Node, IWB, MWB


class WidgetsRegistry:
    """
    Just for holding the widgets specified in export_widgets to access them in NENV.import_widgets
    without causing naming conflicts with possible a 'exported_widgets' variable in the widgets file.
    """
    exported_widgets = []


class WidgetsContainer:
    pass


def export_widgets(*args):
    wc = WidgetsContainer()
    for w in args:
        setattr(wc, w.__name__, w)
    WidgetsRegistry.exported_widgets.append(wc)
