import types
from typing import Union, List


def get_method_funcs(cls_def_str: str, obj):
    """
    Parses the class definition string and returns a dict with python functions under their names,
    parsed from the methods in the class definition string using the ast module.
    """

    import sys
    if sys.version_info < (3, 9):
        raise Exception('src code modifications are only supported on Python >=3.9')

    # requires Python >= 3.9 for ast.unparse()
    import ast

    # extract functions
    ast_funcs: List[ast.FunctionDef] = [
        f
        for f in ast.parse(cls_def_str).body[0].body  # type: ignore
        if type(f) == ast.FunctionDef
    ]

    funcs = {}
    for astf in ast_funcs:
        d = __builtins__.__dict__.copy()  # important: provide builtins when parsing the function
        exec(ast.unparse(astf), d)
        f = d[astf.name]
        # # add locals scope of the object to the function
        # f.__dict__ = obj.

        funcs[astf.name] = f

    return funcs


class SrcCodeUpdater:
    """
    Provides functionality to override method implementations of an inspectable object.
    """

    @staticmethod
    def override_code(obj: object, new_class_src) -> Union[None, Exception]:
        try:
            funcs = get_method_funcs(new_class_src, obj)
            for name, f in funcs.items():  # override all methods
                setattr(obj, name, types.MethodType(f, obj))
                # types.MethodType() creates a method bound to obj, from the function f
            return None
        except Exception as e:
            return e


    # below is the old implementation, for documentation purposes only; see discussion below


    @staticmethod
    def override_code_OLD(obj: object, orig_class_src, orig_mod_src, new_class_src):

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
