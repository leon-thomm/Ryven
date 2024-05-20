from ryven.node_env import *


class OperatorNodeBase(Node):
    """
    Base class for nodes implementing a binary operation.
    """

    version = 'v0.3'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]
    init_outputs = [
        NodeOutputType(),
    ]

    def __init__(self, params):
        super().__init__(params)

        self.num_inputs = 0

    def place_event(self):
        self.num_inputs = len(self.inputs)

    def add_op_inp(self):
        self.create_input()
        self.num_inputs += 1

    def remove_op_input(self, index):
        self.delete_input(index)
        self.num_inputs -= 1

    def update_event(self, inp=-1):
        self.set_output_val(0, Data(self.apply_op([
            self.input(i).payload
            for i in range(len(self.inputs))
        ])))

    def apply_op(self, elements: list):
        return None


"""
    logical operators
"""


class LogicNodeBase(OperatorNodeBase):
    pass


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


"""
    arithmetic operators
"""


class ArithmeticNodeBase(OperatorNodeBase):
    pass


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


class Power_Node(ArithmeticNodeBase):
    title = '**'

    def apply_op(self, elements: list):
        v = elements[0]
        for e in elements[1:]:
            v = v ** e
        return v


arithmetic_nodes = [
    Plus_Node,
    Minus_Node,
    Multiply_Node,
    Divide_Node,
    Power_Node,
]


"""
    comparison operators
"""


class ComparatorNodeBase(OperatorNodeBase):

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


"""
    export
"""

node_types = [
    *logic_nodes,
    *arithmetic_nodes,
    *comparator_nodes,
]

# account for old package name
for n in node_types:
    n.legacy_identifiers = [
        *getattr(n, 'legacy_identifiers', []),
        f'std.{n.__class__.__name__}',
    ]

export_nodes(
    node_types=node_types,
    sub_pkg_name='basic_operators'
)
