"""
This module includes the whole Ryven Console application.
It simply deploys a session with the project provided and implements a REPL.
This is supposed to be used in an interactive way. For scripting and deploying
projects without GUI programmatically, the ryvencore lib should be used directly.
"""
import argparse
import os
from os.path import join, dirname
import json
import sys

from ryvencore import *

from ryven.main.nodes_package import NodesPackage
from ryven.main.utils import import_nodes_package, process_nodes_packages, find_project
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


def import_nodes(session: Session, context_container, nodes_package: NodesPackage):
    try:
        nodes = import_nodes_package(package=nodes_package)
        session.register_nodes(nodes)
        print('registered nodes: ', nodes)
    except Exception as e:
        print(e)


def load_project(session, context_container, project_file_path):
    try:
        f = open(project_file_path, 'r')
        project = json.loads(f.read())
        f.close()
        del f
        scripts = session.load(project)
        print(f'added scripts: {scripts}')
    except Exception as e:
        print(e)


def parse_args():
    """Parse the command line arguments.

    Returns
    -------
    args : argparse.Namespace
        The parsed command line arguments.
    """

    parser = argparse.ArgumentParser(
        description='''
            Console REPL for interactively running a ryven project 
            without any GUI components. This should now require any
            dependencies.
            ''',
        epilog='Copyright (C) 2020-2022 Leon Thomm, licensed under MIT'
    )

    parser.add_argument(
        nargs=1,
        dest='project',
        metavar='PROJECT',
        help='the project file to be loaded'
    )

    parser.add_argument(
        '-n', '--nodes',
        action='append',
        # nargs='+', action='extend',
        default=[],
        dest='nodes',
        metavar='NODES_PKG',
        help='''
            load a nodes package\\
            • If you want to load multiple packages, use the option again.\\
            • Nodes packages loaded here take precedence over nodes packages
            with the same name specified in the project file!\\
            • Nodes package names containing spaces must be enclosed in quotes.
            '''
    )

    args, remaining_args = parser.parse_known_args()

    return args


def run():

    args = parse_args()

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

    #
    # LOAD PROJECT AND NODE PACKAGES -----------------------------------------------------------------------------------
    #

    # check if project file exists
    project = find_project(args.project[0])
    if project is None:
        sys.exit('Could not find specified project.')

    # process node packages
    manual_nodes, _, _ = process_nodes_packages(args.nodes)

    node_packages, nodes_not_found, project_dict = process_nodes_packages(
        project, requested_nodes=manual_nodes,
    )

    if nodes_not_found:
        mul = len(nodes_not_found) > 1  # multiple packages missing ?
        sys.exit(
            f'The package{"s" if mul else ""} '
            f''''{"', '".join([str(p) for p in nodes_not_found])}' '''
            f'{"were" if mul else "was"} requested, '
            f'but {"they are" if mul else "it is"} not available.'
            f'\n'
            f'Update the project file or supply the missing package{"s" if mul else ""} '
            f''''{"', '".join([p.name for p in nodes_not_found])}' '''
            f'on the command line with the "-n" switch.')

    for np in node_packages:
        import_nodes(session, c, np)

    load_project(session, c, project)

    #
    # DEPLOY REPL ------------------------------------------------------------------------------------------------------
    #

    try:

        print("you dan directly access the ryvencore session through 'session'")
        print("REPL STARTED")

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
