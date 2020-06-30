import inspect
import types

def override_code(obj: object, new_class_code):
    """This method is used when editing the source of an existing object in the Flow (NodeInstance or a widget).
    It is meant to override the implementation of any custom method of the original object according to the code
    written in the new_class_code parameter."""

    original_module = inspect.getmodule(obj.__class__)
    original_module_source_code = inspect.getsource(original_module)
    original_class_source_code = inspect.getsource(obj.__class__)
    new_module_code = original_module_source_code.replace(original_class_source_code, new_class_code)

    module = types.ModuleType('new_class_module')
    exec(new_module_code, module.__dict__)
    new_obj_class = getattr(module, type(obj).__name__)

    method_names = [func for func in dir(new_obj_class)
                    if callable(getattr(new_obj_class, func)) and not func.startswith("__")]

    for m in method_names:
        method = getattr(new_obj_class, m)
        setattr(obj, m, types.MethodType(method, obj))