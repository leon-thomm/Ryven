import inspect
import types


class SrcCodeUpdater:

    @staticmethod
    def override_code(obj: object, new_class_code):
        """This method is used when editing the source of an existing object in the Flow (NodeInstance or a widget).
        It overrides the implementation of any custom method of the original object according to the code
        provided through the new_class_code parameter."""

        original_module = inspect.getmodule(obj.__class__)
        original_module_source_code = inspect.getsource(original_module)
        original_class_source_code = inspect.getsource(obj.__class__)
        new_module_code = original_module_source_code.replace(original_class_source_code, new_class_code)

        # creating temporary module
        module = types.ModuleType('new_class_module')
        exec(new_module_code, module.__dict__)

        # extracting the class
        new_obj_class = getattr(module, type(obj).__name__)

        # get all custom method names (string list)
        method_names = [func for func in dir(new_obj_class)
                        if callable(getattr(new_obj_class, func)) and not func.startswith("__")]

        for m in method_names:
            method = getattr(new_obj_class, m)  # get actual method object
            setattr(obj, m, types.MethodType(method, obj))  # override the original method or add if not existing yet