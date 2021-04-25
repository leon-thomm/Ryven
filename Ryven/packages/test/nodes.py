from NENV import *

#
# ButtonWidget, \
#  = load_from_file(file='widgets.py', caller_file=__file__, components_list=[
#         'ButtonWidget',
#     ], gui=True)



class NodeBase(Node):

    def get_custom_identifier(self):
        return 'my_node_base'



class Node1(NodeBase):
    # identifiers = NodeBase.identifiers + ['test']

    def __init__(self, params):
        super().__init__(params)
        self.identifiers += 'test'




nodes = [
    Node1,
]
