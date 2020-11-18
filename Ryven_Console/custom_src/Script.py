from custom_src.Flow import Flow

# import sys
# sys.path.append('../Ryven/')
# sys.path.append('../Ryven/custom_src/script_variables/')
from custom_src.script_variables.VariablesHandler import VariablesHandler


class Script:
    def __init__(self, config, nodes, node_instance_classes):
        self.name = config['name']
        self.variables = []
        self.variables_handler = VariablesHandler(self, config['variables'])
        self.flow = Flow(self, config['flow'], nodes, node_instance_classes)
        self.variables_handler.flow = self.flow