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

    # add package name to identifiers
    for n in nodes:
        n.identifier_prefix = package.name  #  + '.' + (n.identifier if n.identifier else n.__name__)

    return nodes
