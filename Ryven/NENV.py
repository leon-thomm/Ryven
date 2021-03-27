"""This file automatically imports all requirements for custom nodes.
It should lie in the same location as Ryven.py so it can get imported directly from the custom sources."""

from ryvencore_qt import Node

from PySide2.QtCore import Signal


from os.path import normpath, join, dirname, abspath
def node_pp(f):
    return normpath(join(dirname(abspath(f)), '../../'))
def ni_pp(f):  # old signature
    return node_pp(f)
