import bisect
import enum
import json
import pathlib
from math import sqrt
from typing import List, Dict

from qtpy.QtCore import QPointF, QByteArray

from ryvencore.utils import serialize, deserialize
from .GlobalAttributes import *

def generate_name(obj, name):
   return f'{name}:[{id(obj)}]'
    
def pythagoras(a, b):
    return sqrt(a ** 2 + b ** 2)


def get_longest_line(s: str):
    lines = s.split('\n')
    lines = [line.replace('\n', '') for line in lines]
    longest_line_found = ''
    for line in lines:
        if len(line) > len(longest_line_found):
            longest_line_found = line
    return line


def shorten(s: str, max_chars: int, line_break: bool = False):
    """Ensures, that a given string does not exceed a given max length. If it would, its cut in the middle."""
    l = len(s)
    if l > max_chars:
        insert = ' . . . '
        if line_break:
            insert = '\n'+insert+'\n'
        insert_length = len(insert)
        left = s[:round((max_chars-insert_length)/2)]
        right = s[round(l-((max_chars-insert_length)/2)):]
        return left+insert+right
    else:
        return s


def pointF_mapped(p1, p2):
    """adds the floating part of p2 to p1"""
    p2.setX(p1.x() + p2.x()%1)
    p2.setY(p1.y() + p2.y()%1)
    return p2

def points_dist(p1, p2):
    return sqrt(abs(p1.x() - p2.x())**2 + abs(p1.y() - p2.y())**2)

def middle_point(p1, p2):
    return QPointF((p1.x() + p2.x())/2, (p1.y() + p2.y())/2)


class MovementEnum(enum.Enum):
    # this should maybe get removed later
    mouse_clicked = 1
    position_changed = 2
    mouse_released = 3


def get_resource(filepath: str):
    return pathlib.Path(Location.PACKAGE_PATH, 'resources', filepath)


def change_svg_color(filepath: str, color_hex: str):
    """Loads an SVG, changes all '#xxxxxx' occurrences to color_hex, renders it into and a pixmap and returns it"""

    # https://stackoverflow.com/questions/15123544/change-the-color-of-an-svg-in-qt

    from qtpy.QtSvg import QSvgRenderer
    from qtpy.QtGui import QPixmap, QPainter
    from qtpy.QtCore import Qt

    with open(filepath) as f:
        data = f.read()
    data = data.replace('fill:#xxxxxx', 'fill:'+color_hex)

    svg_renderer = QSvgRenderer(QByteArray(bytes(data, 'ascii')))

    pix = QPixmap(svg_renderer.defaultSize())
    pix.fill(Qt.transparent)
    pix_painter = QPainter(pix)
    svg_renderer.render(pix_painter)

    return pix
