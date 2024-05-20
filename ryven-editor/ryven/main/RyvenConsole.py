# TODO this could be improved

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
import code

from ryvencore import *

# import ryven utils to load node packages and parse projects
from ryven.main.packages.nodes_package  import NodesPackage, process_nodes_packages, import_nodes_package
from ryven.main.packages.node_env       import init_node_env
from ryven.main.utils                   import find_project


def parse_args() -> argparse.Namespace:
    """Parse the command line arguments.

    :return: args: The parsed command line arguments.
    """

    parser = argparse.ArgumentParser(
        description='''
            Console REPL for interactively running a ryven project 
            without any GUI components. This should now require any
            dependencies.
            ''',
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


def repl(session: Session):
    context = {'session': session}
    
    code.interact(local=context, banner=
                  f'Welcome to the Ryven Console! Your project has been loaded.\n'
                  f'You can access the ryvencore session by typing `session`.\n'
                  f'For more information, visit https://leon-thomm.github.io/ryvencore/\n'
                  f'\n\n')


def run():

    args = parse_args()

    #
    # initialize session
    #

    os.environ['RYVEN_MODE'] = 'no-gui'
    init_node_env()

    # import built-in nodes
    nodes, data_types = import_nodes_package(NodesPackage(
        directory=join(dirname(__file__), 'packages/built_in/')
    ))

    # init session
    session = Session(gui=False, load_addons=True)
    session.register_data_types(data_types)
    session.register_node_types(nodes)

    # 
    # load project and node packages
    # 

    project_path = args.project[0]
    node_packages, nodes_not_found, project = process_nodes_packages(
        project_or_nodes=project_path, 
        requested_packages=args.nodes
    )

    if nodes_not_found:
        exit_missing_nodes(nodes_not_found)

    for np in node_packages:
        nodes, data_types = import_nodes_package(package=np)
        session.register_data_types(data_types)
        session.register_node_types(nodes)
    
    session.load(project)

    #
    # deploy REPL
    #

    repl(session)


def exit_missing_nodes(nodes_not_found):
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


if __name__ == '__main__':
    run()
