"""
This module includes the whole Ryven Console application.
It's quite short as all functionality is nicely split between backend and frontend
so here we can just load a project into the backend and provide the session.
"""

import os
from os.path import join, dirname
import json
import sys

from ryvencore import *

from ryven.main.nodes_package import NodesPackage
from ryven.main.utils import import_nodes_package
from ryven.NENV import init_node_env


cmds = [

]


class ContextContainer:
    pass


def next_input(msg: str = ''):

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
    init_node_env()

    # CLASSES['node base'] = NodeBaseWrapper
    session = Session(gui=False)
    session.register_nodes(
        import_nodes_package(
            NodesPackage(
                directory=join(dirname(__file__), 'nodes/built_in/')
            )
        )
    )

    c = ContextContainer()
    setattr(c, 'session', session)

    print(
        """COMMANDS:
>>> import nodes
>>> load project
anything else will be evaluated/executed
built-in nodes are already imported
        """
    )

    try:

        while True:

            # process input commands

            cmd = next_input()

            # special commands
            if cmd == 'import nodes':
                import_nodes(session, c)
                continue
            elif cmd == 'load project':
                load_project(session, c)
                continue

            # REPL
            locals_ = c.__dict__

            try:
                try:
                    print(eval(cmd, globals(), locals_))

                except SyntaxError:
                    out = exec(cmd, globals(), locals_)

                    if out is not None:
                        print(out)
            except Exception as e:
                print(e)
                continue

            # merge locals
            for name, val in locals_.items():
                setattr(c, name, val)

    except:
        sys.exit('exiting...')


if __name__ == '__main__':
    run()


# specific commands

def import_nodes(session, context_container):
    pkg_dir = next_input('abs path to your package dir: ')
    try:
        # package_name = os.path.basename(pkg_dir)
        nodes = import_nodes_package(package=NodesPackage(pkg_dir))
        session.register_nodes(nodes)
        print('registered nodes: ', nodes)
    except Exception as e:
        print(e)


def load_project(session, context_container):
    project_file_path = next_input('abs path to your project file: ')
    try:
        f = open(project_file_path, 'r')
        project = json.loads(f.read())
        f.close()
        del f
        scripts = session.load(project)
        print(f'added scripts: {scripts}')
    except Exception as e:
        print(e)
