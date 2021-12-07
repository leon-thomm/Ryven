from ryven.NENV import *

# import math


class OperatorNodeBase(Node):

    version = 'v0.0'

    init_inputs = [
        NodeInputBP(dtype=dtypes.Data(size='s')),
        NodeInputBP(dtype=dtypes.Data(size='s')),
    ]

    init_outputs = [
        NodeOutputBP(),
    ]

    style = 'small'

    def __init__(self, params):
        super().__init__(params)

        self.num_inputs = 0
        self.actions['add input'] = {'method': self.add_operand_input}

    def place_event(self):
        for i in range(len(self.inputs)):
            self.register_new_operand_input(i)

    def add_operand_input(self):
        self.create_input_dt(dtype=dtypes.Data(size='s'))
        self.register_new_operand_input(self.num_inputs)
        self.update()

    def remove_operand_input(self, index):
        self.delete_input(index)
        self.num_inputs -= 1
        # del self.actions[f'remove input {index}']
        self.rebuild_remove_actions()
        self.update()

    def register_new_operand_input(self, index):
        self.actions[f'remove input {index}'] = {
            'method': self.remove_operand_input,
            'data': index
        }
        self.num_inputs += 1

    def rebuild_remove_actions(self):

        remove_keys = []
        for k, v in self.actions.items():
            if k.startswith('remove input'):
                remove_keys.append(k)

        for k in remove_keys:
            del self.actions[k]

        for i in range(self.num_inputs):
            self.actions[f'remove input {i}'] = {'method': self.remove_operand_input, 'data': i}

    def update_event(self, inp=-1):
        self.set_output_val(0, self.apply_op([self.input(i) for i in range(len(self.inputs))]))

    def apply_op(self, elements: list):
        return None


# LOGIC -------------------------------------

class LogicNodeBase(OperatorNodeBase):
    color = '#f58142'


class NOT_Node(LogicNodeBase):
    title = 'not'

    def apply_op(self, elements: list):
        return all([not bool(e) for e in elements])


class AND_Node(LogicNodeBase):
    title = 'and'

    def apply_op(self, elements: list):
        return all(elements)


class NAND_Node(LogicNodeBase):
    title = 'nand'

    def apply_op(self, elements: list):
        return not all(elements)


class OR_Node(LogicNodeBase):
    title = 'or'

    def apply_op(self, elements: list):
        return any(elements)


class NOR_Node(LogicNodeBase):
    title = 'nor'

    def apply_op(self, elements: list):
        return not any(elements)


class XOR_Node(LogicNodeBase):
    title = 'xor'

    def apply_op(self, elements: list):
        # XOR definition for unbound number of operands:
        #   odd number of operands must be true
        return len(list(filter((lambda x: bool(x)), elements))) % 2 != 0


class XNOR_Node(LogicNodeBase):
    title = 'xnor'

    def apply_op(self, elements: list):
        # XNOR definition for unbound number of operands:
        #   even number of operands must be true
        return len(list(filter((lambda x: bool(x)), elements))) % 2 == 0


logic_nodes = [
    NOT_Node,
    AND_Node,
    NAND_Node,
    OR_Node,
    NOR_Node,
    XOR_Node,
    XNOR_Node,
]

# -------------------------------------------


# ARITHMETIC --------------------------------

class ArithmeticNodeBase(OperatorNodeBase):
    color = '#58db53'


class Plus_Node(ArithmeticNodeBase):
    title = '+'

    def apply_op(self, elements: list):
        v = elements[0]
        for e in elements[1:]:
            v = v + e
        return v
        # return sum(elements)


class Minus_Node(ArithmeticNodeBase):
    title = '-'

    def apply_op(self, elements: list):
        v = elements[0]
        for e in elements[1:]:
            v = v - e
        return v
        # return sum(elements[:1])-sum(elements[1:])


class Multiply_Node(ArithmeticNodeBase):
    title = '*'

    def apply_op(self, elements: list):
        v = elements[0]
        for e in elements[1:]:
            v *= e
        return v
        # return math.prod(elements)


class Divide_Node(ArithmeticNodeBase):
    title = '/'

    def apply_op(self, elements: list):
        v = elements[0]
        for e in elements[1:]:
            v = v / e
        return v
        # if len(elements) > 0:
        #     x = elements[0]
        #     for e in elements[1:]:
        #         x /= e
        #     return x
        # else:
        #     return None


class Power_Node(ArithmeticNodeBase):
    title = '**'

    def apply_op(self, elements: list):
        v = elements[0]
        for e in elements[1:]:
            v = v ** e
        return v
        # if len(elements) > 0:
        #     x = elements[0]
        #     for e in elements[1:]:
        #         x **= e
        #     return x
        # else:
        #     return None


arithmetic_nodes = [
    Plus_Node,
    Minus_Node,
    Multiply_Node,
    Divide_Node,
    Power_Node,
]

# -------------------------------------------


# COMPARATORS -------------------------------

class ComparatorNodeBase(OperatorNodeBase):
    color = '#a1574c'

    def apply_op(self, elements: list):
        # if len(elements) > 0:
        b = True
        for i in range(1, len(elements)):
            b = b and (self.comp(elements[i-1], elements[i]))
        return b
        # return None

    def comp(self, a, b) -> bool:
        return False


class Equal_Node(ComparatorNodeBase):
    title = '=='

    def comp(self, a, b) -> bool:
        return a == b


class NotEqual_Node(ComparatorNodeBase):
    title = '!='

    def comp(self, a, b) -> bool:
        return a != b


class Greater_Node(ComparatorNodeBase):
    title = '>'

    def comp(self, a, b) -> bool:
        return a > b


class GreaterEq_Node(ComparatorNodeBase):
    title = '>='

    def comp(self, a, b) -> bool:
        return a >= b


class Less_Node(ComparatorNodeBase):
    title = '<'

    def comp(self, a, b) -> bool:
        return a < b


class LessEq_Node(ComparatorNodeBase):
    title = '<='

    def comp(self, a, b) -> bool:
        return a <= b


comparator_nodes = [
    Equal_Node,
    NotEqual_Node,
    Greater_Node,
    GreaterEq_Node,
    Less_Node,
    LessEq_Node,
]

# -------------------------------------------


nodes = [
    *logic_nodes,
    *arithmetic_nodes,
    *comparator_nodes,
]
