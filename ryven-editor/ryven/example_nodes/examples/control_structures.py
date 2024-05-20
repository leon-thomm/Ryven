from ryven.node_env import *


class CSNodeBase(Node):
    version = 'v0.3'


class If_Node(CSNodeBase):
    title = 'branch'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType(label='cond'),
    ]
    init_outputs = [
        NodeOutputType('true', type_='exec', ),
        NodeOutputType('false', type_='exec'),
    ]

    def update_event(self, inp=-1):
        if inp == 0:
            if self.input(1).payload:
                self.exec_output(0)
            else:
                self.exec_output(1)


class ForLoop_Node(CSNodeBase):
    """n dimensional for loop!"""

    title = 'for'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType(label='from'),
        NodeInputType(label='to'),
    ]
    init_outputs = [
        NodeOutputType('loop', type_='exec'),
        NodeOutputType('i', type_='data'),
        NodeOutputType('finished', type_='exec'),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.dims = 1

    def add_dimension(self):
        new_dim = self.dims + 1
        self.create_input(label=f'{new_dim} from')
        self.create_input(label=f'{new_dim} to')
        self.create_output(f'loop {new_dim}', 'exec', insert=-1)
        self.create_output(f'i {new_dim}', 'data', insert=-1)
        self.dims += 1

    def remove_dimension(self, dim):
        inp_index = self.input_from_dim(dim)
        self.delete_input(inp_index)
        self.delete_input(inp_index)
        out_index = self.output_from_dim(dim)
        self.delete_output(out_index)
        self.delete_output(out_index)
        self.dims -= 1

    def input_from_dim(self, dim):
        return 1 + 2*(dim-1)

    def output_from_dim(self, dim):
        return 2*(dim-1)

    def update_event(self, inp=-1):
        if inp == 0:
            self.iterate(1)
            self.exec_output(len(self.outputs)-1)

    def iterate(self, dim):

        inp_index = self.input_from_dim(dim)

        exec_out_index = self.output_from_dim(dim)
        data_out_index = exec_out_index+1

        for i in range(self.input(inp_index).payload,
                       self.input(inp_index+1).payload):

            self.set_output_val(data_out_index, Data(i))
            self.exec_output(exec_out_index)

            if dim < self.dims:
                self.iterate(dim+1)


class ForEachLoop_Node(CSNodeBase):
    title = 'for each'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType(label='elements'),
    ]
    init_outputs = [
        NodeOutputType('loop', type_='exec'),
        NodeOutputType('e', type_='data'),
        NodeOutputType('finished', type_='exec'),
    ]

    def update_event(self, inp=-1):
        for e in self.input(0).payload:
            self.set_output_val(1, e)
            self.exec_output(0)

        self.exec_output(2)


class WhileLoop_Node(CSNodeBase):
    title = 'while'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType(label='cond'),
    ]
    init_outputs = [
        NodeOutputType('loop', type_='exec'),
        NodeOutputType('finished', type_='exec'),
    ]

    def update_event(self, inp=-1):
        while self.input(0).payload:
            self.exec_output(0)

        self.exec_output(1)


class DoWhileLoop_Node(CSNodeBase):
    title = 'do while'
    init_inputs = [
        NodeInputType(type_='exec'),
        NodeInputType(label='cond'),
    ]
    init_outputs = [
        NodeOutputType('loop', type_='exec'),
        NodeOutputType('finished', type_='exec'),
    ]

    def update_event(self, inp=-1):
        self.exec_output(0)
        while self.input(0).payload:
            self.exec_output(0)
        self.exec_output(1)

node_types = [
    If_Node,
    ForLoop_Node,
    ForEachLoop_Node,
    WhileLoop_Node,
    DoWhileLoop_Node,
]

# account for old package name
for n in node_types:
    n.legacy_identifiers = [
        *getattr(n, 'legacy_identifiers', []),
        f'std.{n.__class__.__name__}',
    ]

export_nodes(
    node_types=node_types,
    sub_pkg_name='control_structures'
)
