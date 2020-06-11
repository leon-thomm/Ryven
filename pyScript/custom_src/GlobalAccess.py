import enum
import inspect
import math


class GlobalStorage:
    storage = {'design style': 'dark std',
               'debugging': False}

    def debug(*args):
        s = ''
        for arg in args:
            s += ' '+str(arg)
        if GlobalStorage.storage['debugging']:
            print('        --> DEBUG:', s)

def pythagoras(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def find_type_in_object(obj, base):
    """Determines, whether a given object is - at any level of abstraction - type of a given base class."""
    return base in inspect.getmro(type(obj))

def find_type_in_objects(objects, base):
    for o in objects:
        found = find_type_in_object(o, base)
        if found:
            return True
    return False


class MovementEnum(enum.Enum):
    """bug test: click on NI, drag, then use shortcut movement and release. Should result in a double undo stack push
    this should get removed later, it's an ugly implementation"""
    mouse_clicked = 1
    position_changed = 2
    mouse_released = 3


def get_longest_line(s: str):
    lines = s.split('\n')
    lines = [line.replace('\n', '') for line in lines]
    longest_line_found = ''
    for line in lines:
        if len(line) > len(longest_line_found):
            longest_line_found = line
    return line


def sort_nodes(nodes):
    return sorted(nodes, key=lambda x: x.title.lower())