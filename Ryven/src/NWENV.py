"""This module automatically imports all requirements for custom widgets.
It should lie in the same location as Ryven.py so it can get imported directly from the custom sources
without path modifications which caused issues in the past."""

import inspect

from ryvencore_qt import Node, IWB, MWB  # for use in the widgets module importing NWENV


class WidgetsRegistry:
    """
    Just for holding the widgets specified in export_widgets to access them in NENV.import_widgets
    without causing naming conflicts with possible a 'exported_widgets' variable in the widgets file.
    """
    exported_widgets = []
    exported_widget_sources: [[str]] = []


class WidgetsContainer:
    pass


def export_widgets(*args):
    """
    Exports/exposes the specified widgets to the nodes file importing them via import_widgets().
    Returns an object with all exported widgets as attributes for direct access.
    """

    widgets = list(args)

    wc = WidgetsContainer()
    for w in widgets:
        setattr(wc, w.__name__, w)
    WidgetsRegistry.exported_widgets.append(wc)

    # get sources
    widget_sources = [inspect.getsource(w) for w in widgets]
    WidgetsRegistry.exported_widget_sources.append(widget_sources)
