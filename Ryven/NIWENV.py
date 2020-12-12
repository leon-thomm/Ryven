"""This file automatically imports all requirements for custom NI widgets, so that they only need to import
this file. his file should lie in the same location as Ryven.py in order to be able to get imported directly."""

from custom_src.WidgetBaseClasses import MWB, IWB
from custom_src.retain import M
from os.path import normpath, join, dirname, abspath


def widget_pp(f):
    return normpath(join(dirname(abspath(f)), '../../../'))+'/'
