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

    # yyep, that's it....
    # you must be kidding...
    # you MUST be
    # it's actually true....
    # that's ridiculous.
    # indeed.



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