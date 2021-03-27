"""This file automatically imports all requirements for custom widgets.
It should lie in the same location as Ryven.py so it can get imported directly from the custom sources."""

from ryvencore_qt import MWB, IWB

from PySide2.QtCore import Signal


class M:
    """Method retaining mechanism; important when overriding methods that were used to connect so Qt signals"""
    def __init__(self, method):
        self.method_name = method.__name__
        self.method = lambda *args, **kwargs: getattr(method.__self__, method.__name__)(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        self.method(*args, **kwargs)


from os.path import normpath, join, dirname, abspath
def widget_pp(f):
    return normpath(join(dirname(abspath(f)), '../../../'))+'/'
