"""This file automatically imports all requirements for custom NodeInstances, so that they only need to import this
file. This file should lie in the same location as Ryven.py in order to be able to get imported directly."""

from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import M
from os.path import normpath, join, dirname, abspath


def ni_pp(f):
    return normpath(join(dirname(abspath(f)), '../../'))
