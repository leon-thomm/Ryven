"""
This module includes the whole Ryven Console application.
It's quite short as all functionality is nicely split between backend and frontend
so here we can just load a project into the backend and provide the session.
"""

import os
from os.path import join, dirname
import json
import sys

from ryvencore_qt.src.ryvencore import *

from nodes_package import NodesPackage
from tools import import_nodes_package


cmds = [

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
    os.environ['RYVEN_MODE'] = 'no-gui'

    # CLASSES['node base'] = NodeBaseWrapper
    session = Session(gui=False)
    session.register_nodes(
        import_nodes_package(
            NodesPackage(
                directory=join(dirname(__file__), 'nodes/built_in/')
            )
        )
    )

    print(
        """COMMANDS:
>>> import nodes
>>> load project
anything else will be evaluated/executed
built-in nodes are already imported
        """
    )

    while True:

        # process input commands

        cmd = _input()

        if cmd == 'import nodes':
            pkg_dir = _input('abs path to your package dir: ')
            try:
                # package_name = os.path.basename(pkg_dir)
                nodes = import_nodes_package(package=NodesPackage(pkg_dir))
                session.register_nodes(nodes)
                print('registered nodes: ', nodes)
            except Exception as e:
                print(e)

        elif cmd == 'load project':
            project_file_path = _input('abs path to your project file: ')
            try:
                f = open(project_file_path, 'r')
                project = json.loads(f.read())
                f.close()
                del f
                scripts = session.load(project)
                print(f'added scripts: {scripts}')
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


if __name__ == '__main__':
    run()
