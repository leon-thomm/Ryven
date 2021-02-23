"""This file automatically imports all requirements for custom NI widgets, so that they only need to import
this file. his file should lie in the same location as Ryven.py in order to be able to get imported directly."""

from ryvencore import MWB, IWB, Retain
M = Retain.M

from os.path import normpath, join, dirname, abspath

from PySide2.QtCore import Signal


def widget_pp(f):
    return normpath(join(dirname(abspath(f)), '../../../'))+'/'
