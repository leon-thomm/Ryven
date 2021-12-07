from ryven.NENV import *


class CSNodeBase(Node):
    version = 'v0.1'
    style = 'normal'
    color = '#b33a27'


class If_Node(CSNodeBase):
    title = 'branch'
    version = 'v0.1'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Boolean(), label='cond'),
    ]
    init_outputs = [
        NodeOutputBP('true', type_='exec', ),
        NodeOutputBP('false', type_='exec'),
    ]

    def update_event(self, inp=-1):
        if inp == 0:
            if self.input(1):
                self.exec_output(0)
            else:
                self.exec_output(1)


class ForLoop_Node(CSNodeBase):
    """n dimensional for loop!"""

    title = 'for'
    version = 'v0.1'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label='from'),
        NodeInputBP(dtype=dtypes.Integer(), label='to'),
    ]
    init_outputs = [
        NodeOutputBP('loop', type_='exec'),
        NodeOutputBP('i', type_='data'),
        NodeOutputBP('finished', type_='exec'),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.actions['add dimension'] = {'method': self.add_dimension}

        self.dims = 1

    def add_dimension(self):
        new_dim = self.dims + 1
        self.create_input_dt(dtype=dtypes.Integer(), label=f'{new_dim} from')
        self.create_input_dt(dtype=dtypes.Integer(), label=f'{new_dim} to')
        self.create_output(f'loop {new_dim}', 'exec', insert=-1)
        self.create_output(f'i {new_dim}', 'data', insert=-1)
        self.dims += 1

        self.actions[f'remove dimension {new_dim}'] = {
            'method': self.remove_dimension,
            'data': new_dim
        }

    def remove_dimension(self, dim):
        inp_index = self.input_from_dim(dim)
        self.delete_input(inp_index)
        self.delete_input(inp_index)
        out_index = self.output_from_dim(dim)
        self.delete_output(out_index)
        self.delete_output(out_index)
        self.dims -= 1
        # del self.actions[f'remove dimension {dim}']
        self.rebuild_remove_actions()

    def rebuild_remove_actions(self):

        remove_keys = []
        for k, v in self.actions.items():
            if k.startswith('remove dimension'):
                remove_keys.append(k)

        for k in remove_keys:
            del self.actions[k]

        for i in range(1, self.dims):
            self.actions[f'remove dimension {i+1}'] = {'method': self.remove_dimension, 'data': i+1}

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

        for i in range(self.input(inp_index),
                       self.input(inp_index+1)):

            self.set_output_val(data_out_index, i)
            self.exec_output(exec_out_index)

            if dim < self.dims:
                self.iterate(dim+1)


class ForEachLoop_Node(CSNodeBase):
    title = 'for each'
    version = 'v0.1'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Integer(), label='elements'),
    ]
    init_outputs = [
        NodeOutputBP('loop', type_='exec'),
        NodeOutputBP('e', type_='data'),
        NodeOutputBP('finished', type_='exec'),
    ]

    def update_event(self, inp=-1):
        for e in self.input(0):
            self.set_output_val(1, e)
            self.exec_output(0)

        self.exec_output(2)


class WhileLoop_Node(CSNodeBase):
    title = 'while'
    version = 'v0.1'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Boolean(), label='cond'),
    ]
    init_outputs = [
        NodeOutputBP('loop', type_='exec'),
        NodeOutputBP('finished', type_='exec'),
    ]

    def update_event(self, inp=-1):
        while self.input(0):
            self.exec_output(0)

        self.exec_output(1)


class DoWhileLoop_Node(CSNodeBase):
    title = 'do while'
    version = 'v0.1'
    init_inputs = [
        NodeInputBP(type_='exec'),
        NodeInputBP(dtype=dtypes.Boolean(), label='cond'),
    ]
    init_outputs = [
        NodeOutputBP('loop', type_='exec'),
        NodeOutputBP('finished', type_='exec'),
    ]

    def update_event(self, inp=-1):
        self.exec_output(0)
        while self.input(0):
            self.exec_output(0)
        self.exec_output(1)


nodes = [
    If_Node,
    ForLoop_Node,
    ForEachLoop_Node,
    WhileLoop_Node,
    DoWhileLoop_Node,
]
