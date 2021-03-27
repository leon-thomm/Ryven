import inspect
import types


class SrcCodeUpdater:

    @staticmethod
    def override_code(obj: object, new_class_code):
        """This method is used when editing the source of an existing object in the Flow (Node or a widget).
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

        # get all custom methods/functions from the new class and override/add them in obj
        methods = inspect.getmembers(new_obj_class, predicate=inspect.ismethod)
        functions = inspect.getmembers(new_obj_class, predicate=inspect.isfunction)
        for m_name, m_obj in methods + functions:
            setattr(obj, m_name, types.MethodType(m_obj, obj))
