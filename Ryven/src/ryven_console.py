from ryvencore_qt.src.ryvencore import *
from tools import import_nodes_package
import json
from os.path import join, dirname
import sys


class NodeBaseWrapper(Node):
    """
    Wraps the nodes s.t. their usages of ryvencore-qt or Ryven features don't brake them.
    """

    def __init__(self, params):
        self.special_actions = dict()
        super().__init__(params)

    # def create_input(self, type_: str = 'data', label: str = '',
    #                  widget_name: str = None, widget_pos: str = 'besides', pos=-1):
    #     """See src.nodes.Node.Node"""
    #     super().create_input(type_=type_, label=label, pos=pos)


cmds = [
    # 'import nodes',
    # 'C:/Users/nutri/OneDrive - ETH Zurich/projects/ryven projects/Ryven/packages/linalg',
    # 'load project',
    # 'C:/Users/nutri/OneDrive - ETH Zurich/projects/ryven projects/Ryven/saves/matrices_MODERN3.rpo',
    # 'script = session.scripts[0]',
    # 'flow = script.flow',
    # 'vars = script.vars_manager.variables',
]


def _input(msg: str = ''):

    if 'test' in sys.argv and len(cmds) > 0:
        if msg != '':
            print(msg)

        cmd = cmds[0]
        cmds.remove(cmd)
    else:
        cmd = input(msg)

    return cmd


def run():

    CLASSES['node base'] = NodeBaseWrapper
    session = Session(gui=False)
    session.register_nodes(import_nodes_package(join(dirname(__file__), 'nodes/built_in')))

    print(
        """COMMANDS:
>>> import nodes
>>> load project
anything else will be evaluated/executed
built-in nodes are already imported
        """
    )

    while True:

        cmd = _input()

        if cmd == 'import nodes':
            pkg_dir = _input('abs path to your package dir: ')
            try:
                # package_name = os.path.basename(pkg_dir)
                nodes = import_nodes_package(package=pkg_dir)
                session.register_nodes(nodes)
            except Exception as e:
                print(e)

        elif cmd == 'load project':
            project_file_path = _input('abs path to your project file: ')
            try:
                f = open(project_file_path, 'r')
                project = json.loads(f.read())
                f.close()
                del f
                scripts, func_scripts = session.load(project)
                print(f'added scripts: {scripts}\nand func scripts: {func_scripts}')
            except Exception as e:
                print(e)

        else:
            try:
                try:
                    print(eval(cmd))
                except SyntaxError:
                    exec(cmd)
            except Exception as e:
                print(e)

  # 35.0    0.0    0.0
  #  0.0 1809.0    0.0
  #  0.0    0.0  157.0

 # 35.0   0.0   0.0
 #  0.0  54.0   0.0
 #  0.0   0.0 157.0