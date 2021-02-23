"""This file automatically imports all requirements for custom Nodes, so that they only need to import this
file. This file should lie in the same location as Ryven.py in order to be able to get imported directly."""

from ryvencore import Node, Retain
M = Retain.M

from os.path import normpath, join, dirname, abspath

from PySide2.QtCore import Signal


def ni_pp(f):
    return normpath(join(dirname(abspath(f)), '../../'))
