import bisect
import enum
import json
import pathlib
from math import sqrt
from typing import List, Dict

from qtpy.QtCore import QPointF, QByteArray

from ryvencore.utils import serialize, deserialize
from .GlobalAttributes import *


class Container:
    """used for threading; accessed from multiple threads"""

    def __init__(self):
        self.payload = None
        self.has_been_set = False

    def set(self, val):
        self.payload = val
        self.has_been_set = True

    def is_set(self):
        return self.has_been_set


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



def translate_project(project: Dict) -> Dict:
    """
    Transforms a v3.0 project file into something that can be loaded in v3.1,
    i.e. turns macros into scripts and removes macro nodes from the flows.
    """
    # TODO: this needs to be changed to match ryvencore 0.4 structure
    new_project = project.copy()

    # turn macros into scripts

    fixed_scripts = []

    for script in (project['macro scripts']+project['scripts']):

        new_script = script.copy()

        # remove macro nodes
        new_nodes, removed_node_indices = remove_macro_nodes(script['flow']['nodes'])
        new_script['flow']['nodes'] = new_nodes

        # fix connections
        new_script['flow']['connections'] = fix_connections(script['flow']['connections'], removed_node_indices)

        fixed_scripts.append(new_script)

    del new_project['macro scripts']
    new_project['scripts'] = fixed_scripts

    return new_project


def remove_macro_nodes(nodes):
    """
    removes all macro nodes from the nodes list and returns the new list as well as the indices of the removed nodes
    """

    new_nodes = []
    removed_node_indices = []

    for n_i in range(len(nodes)):
        node = nodes[n_i]

        if node['identifier'] in ('BUILTIN_MacroInputNode', 'BUILTIN_MacroOutputNode') or \
                node['identifier'].startswith('MACRO_NODE_'):
            removed_node_indices.append(n_i)
        else:
            new_nodes.append(node)

    return new_nodes, removed_node_indices


def fix_connections(connections: Dict, removed_node_indices: List) -> List:
    """
    removes connections to removed nodes and fixes node indices of the other ones
    """

    import bisect

    new_connections = []

    for conn in connections:
        if conn['parent node index'] in removed_node_indices or conn['connected node'] in removed_node_indices:
            # remove connection
            continue
        else:
            # fix node indices
            pni = conn['parent node index']
            cni = conn['connected node']

            #   calculate the number of removed nodes with indices < pni | cni
            num_smaller_removed_pni = bisect.bisect_left(removed_node_indices, pni)
            num_smaller_removed_cni = bisect.bisect_left(removed_node_indices, cni)

            c = conn.copy()

            #   decrease indices accordingly
            c['parent node index'] = pni - num_smaller_removed_pni
            c['connected node'] = cni - num_smaller_removed_cni

            new_connections.append(c)

    return new_connections
