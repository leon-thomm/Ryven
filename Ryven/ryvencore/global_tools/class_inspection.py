import inspect


def find_type_in_object(obj, base):
    """Determines, whether a given object is - at any level of abstraction - type of a given base class."""
    return base in inspect.getmro(type(obj))


def find_type_in_objects(objects, base):
    for o in objects:
        found = find_type_in_object(o, base)
        if found:
            return True
    return False