from ryvencore_qt.src.ryvencore import *
import json
from tests.test_nodes import Button_Node, Print_Node
from nodes.built_in.nodes import Val_Node

if __name__ == '__main__':

    f = open('C:/Users/nutri/OneDrive - ETH Zurich/projects/ryven projects/Ryven/saves/test48.rpo', 'r')
    project_str = f.read()
    f.close()

    project_dict = json.loads(project_str)

    # creating session and loading the contents
    session = Session(gui=False)
    session.register_nodes([Button_Node, Print_Node, Val_Node])
    scripts, function_scripts = session.load(project_dict)
    script = scripts[0]
    flow = script.flow

    button_node, print_node, val_node = flow.nodes
    button_node.update()  # prints 'hi'
