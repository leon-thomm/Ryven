import types
import ast
import traceback


def get_method_funcs(cls_def_str: str, obj):
    """
    Returns a dict with functions under their names parsed from the methods in the class definition string using ast.
    """

    # extracting the functions
    ast_funcs: [ast.FunctionDef] = [f for f in ast.parse(cls_def_str).body[0].body if type(f) == ast.FunctionDef]

    funcs = {}
    for astf in ast_funcs:
        d = __builtins__.copy()  # important: provide builtins when parsing the function

        try:
            exec(ast.unparse(astf), d)  # parse
        except AttributeError as e:     # ast.unparse() was introduced in Python 3.9
            print(traceback.format_exc())
            print('\n\nNOTICE: src code override only works on Python version 3.9+, '
                  'so you may have to update to 3.9 to use it')
            return None

        f = d[astf.name]

        # # add locals scope of the object to the function
        # f.__dict__ = obj.

        # add new function to the list, identified by its name
        funcs = {
            **funcs,
            astf.name: f  # d[astf.name]
        }

    return funcs


class SrcCodeUpdater:
    """
    Provides functionality to override method implementations of an object
    """

    @staticmethod
    def override_code(obj: object, new_class_src):

        funcs = get_method_funcs(new_class_src, obj)

        if funcs is None:
            return

        for name, f in funcs.items():  # override all methods
            setattr(obj, name, types.MethodType(f, obj))
            # types.MethodType() creates a bound method, bound to obj, from the function f

    # -----------------------------------------------------------------------


















    @staticmethod
    def override_code_OLD(obj: object, orig_class_src, orig_mod_src, new_class_src):
        """
        ONLY FOR DOCUMENTATION: THIS IS THE OLD IMPLEMENTATION, SEE DISCUSSION BELOW
        """

        import inspect

        # OLD INSPECT BASED VERSION:
        # original_module = inspect.getmodule(obj.__class__)
        # original_module_source_code = inspect.getsource(original_module)
        # original_class_source_code = inspect.getsource(obj.__class__)
        # new_module_code = original_module_source_code.replace(original_class_source_code, new_class_src)
        # NOT WORKING ANYMORE DUE TO SAME MODULE NAMES ('nodes.py')

        new_module_code = orig_mod_src.replace(orig_class_src, new_class_src)

        # creating temporary module
        module = types.ModuleType('new_class_module')

        # I need to set the __file__ manually to make sure the std loading routine of the parsed source is working
        # setattr(module, '__file__', inspect.getfile(obj.__class__))
        module.__file__ = inspect.getfile(obj.__class__)  # <- only works with distinct __module__ names

        # # make original file location visible
        # mod_dir = os.path.normpath(os.path.dirname(module.__file__))
        # rem = mod_dir not in sys.path
        # sys.path.append(mod_dir)

        exec(new_module_code, module.__dict__)

        # extracting the class
        new_obj_class = getattr(module, type(obj).__name__)

        # get all custom methods/functions from the new class and override/add them in obj
        f_methods = inspect.getmembers(new_obj_class, predicate=inspect.ismethod)
        functions = inspect.getmembers(new_obj_class, predicate=inspect.isfunction)
        for m_name, m_obj in f_methods + functions:
            setattr(obj, m_name, types.MethodType(m_obj, obj))

    #   DISCUSSION
    # I ran into lots of issues with inspect when all the node package modules got same filenames ('nodes.py').
    # I tried to avoid them by parsing their sources right after importing them, because then their 'nodes'
    # module is the one currently visible in path, which is now stored in Node.__class_sources__.
    # However, I also would have to add the origin file paths, which is no big deal but significantly complicates
    # the package loading procedure, because in order to correctly simulate the old module here via types,
    # I also need to add the __file__ and stuff, and even then I am not sure if it would still work if
    # the original module did unconventional imports.
    # The above implementation is in general extremely sketchy and I am kinda amazed that this actually works
    # most of the time. But because I want all the node modules to be names 'nodes.py', I came up with the
    # ast-based solution above, which requires Python 3.9, but I will go with that as it is much better in
    # every way.
