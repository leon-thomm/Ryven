import inspect
import os
from os.path import normpath, join, dirname, abspath, basename
import importlib.util

from nodes_package import NodesPackage


def path_from_file(f):
    return normpath(dirname(abspath(f)))


def load_from_file(file: str = None, components_list: [str] = []) -> tuple:
    """
    Imports the specified components from a python module with given file path.
    """

    # if abs_file_path:
    name = basename(file).split('.')[0]
    spec = importlib.util.spec_from_file_location(name, file)
    # else:
    #     # file = getframeinfo(sys._getframe(1)).filename
    #     spec = importlib.util.spec_from_file_location(file, path_from_file(caller_file) + '/' + file)

    importlib.util.module_from_spec(spec)

    mod = spec.loader.load_module(name)
    # using load_module(name) instead of exec_module(mod) here,
    # because exec_module() somehow then registers it as "built-in"
    # which is wrong and causes effects like inspect not parsing the source

    comps = tuple([getattr(mod, c) for c in components_list])

    return comps


def import_nodes_package(package: NodesPackage) -> list:
    import NENV
    load_from_file(package.file_path)

    nodes = NENV.NodesRegistry.exported_nodes[-1]

    if os.environ['RYVEN_MODE'] == 'gui':

        # ADD SOURCES

        # because all the node package modules are named 'nodes.py' now, we need to retrieve the sources via inspect here
        # since inspect will be unable to do so once we imported another 'nodes' module.

        node_cls_sources = NENV.NodesRegistry.exported_node_sources[-1]
        node_mod_sources = [inspect.getsource(inspect.getmodule(n)) for n in nodes]

        for i in range(len(nodes)):
            n = nodes[i]

            mw_cls_src = inspect.getsource(n.main_widget_class) if n.main_widget_class else None
            mw_mod_src = inspect.getsource(inspect.getmodule(n.main_widget_class)) if n.main_widget_class else None

            n.__class_codes__ = {
                'node cls': node_cls_sources[i],
                'node mod': node_mod_sources[i],
                'main widget cls': mw_cls_src,
                'main widget mod': mw_mod_src,
                'custom input widgets': {
                    name: {
                        'cls': inspect.getsource(inp_cls),
                        'mod': inspect.getsource(inspect.getmodule(inp_cls))
                    } for name, inp_cls in n.input_widget_classes.items()
                }
            }

    # -----------

    # add package name to identifiers and define custom types

    for n in nodes:
        n.identifier_prefix = package.name  #  + '.' + (n.identifier if n.identifier else n.__name__)
        n.type_ = package.name if not n.type_ else package.name+f'[{n.type_}]'

    return nodes
