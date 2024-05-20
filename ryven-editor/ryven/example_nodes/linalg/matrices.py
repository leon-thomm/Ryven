import numpy as np
from itertools import chain
from typing import Optional, List

import ryvencore.addons.Variables

from ryven.node_env import *


class MatrixData(Data):
    # currently, there should not be any implicit
    # data sharing between nodes, because their
    # operations are copying the data anyway

    # notice that numpy arrays are pickle serializable

    pass


class MatrixNodeBase(Node):
    """
    Base class for nodes handling matrices.
    It implements basic forward propagation of a mutated matrix,
    defined by some operation in the get_mat() method, and a GUI
    for displaying the matrix.
    """

    version = 'v0.3'
    init_inputs = [
        NodeInputType()
    ]
    init_outputs = [
        NodeOutputType()
    ]

    def __init__(self, params):
        super().__init__(params)
        self.mat = None

    def get_mat(self):
        """
        Returns the processed matrix.
        Pre: self.inputs_ready() is True.
        """
        raise NotImplementedError

    def inputs_ready(self):
        """Returns True if no input is None."""
        return all(self.input(i) is not None for i in range(len(self.inputs)))

    def update_event(self, inp=-1):
        if not self.inputs_ready():
            return

        self.mat = self.get_mat()

        if self.have_gui():
            self.gui.show_matrix(self.mat)

        self.set_output_val(0, MatrixData(self.mat))

    def have_gui(self):
        return hasattr(self, 'gui')


class ShowMatrix(MatrixNodeBase):
    """Simply displays a matrix"""
    title = 'Show Matrix'

    def get_mat(self):
        return self.input(0).payload


class Conjugate(MatrixNodeBase):
    """Conjugates a matrix"""
    title = 'Conjugate'

    def get_mat(self):
        return np.conjugate(self.input(0).payload)


class Transpose(MatrixNodeBase):
    """Transposes a matrix"""
    title = 'Transpose'

    def get_mat(self):
        return np.transpose(self.input(0).payload)


class DetOfMatrix(MatrixNodeBase):
    """Computes the determinant of a matrix."""
    title = 'Determinant'

    def get_mat(self):
        return np.linalg.det(self.input(0).payload)


class DotProduct(MatrixNodeBase):
    """Computes the dot product of a matrix."""
    title = 'Dot Product'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]
    
    def get_mat(self):
        return np.dot(
            self.input(0).payload,
            self.input(1).payload
        )


class HermMatrix(MatrixNodeBase):
    """Computes the hermetian matrix."""
    title = 'Herm'

    def get_mat(self):
        return np.transpose(np.conjugate(self.input(0).payload))


class IDMatrix(MatrixNodeBase):
    """Creates an identity matrix."""
    title = 'ID Matrix'

    def get_mat(self):
        return np.identity(self.input(0).payload)


class ImagMatrix(MatrixNodeBase):
    """Extracts the imaginary parts of the matrix."""
    title = 'Imag'

    def get_mat(self):
        return np.imag(self.input(0).payload)


class RealMatrix(MatrixNodeBase):
    """Extracts the real parts of the matrix."""
    title = 'Real'

    def get_mat(self):
        return np.real(self.input(0).payload)


class InnerProduct(MatrixNodeBase):
    """Computes the inner product of the input matrices."""
    title = 'Inner'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]
    
    def get_mat(self):
        return np.inner(
            self.input(0).payload,
            self.input(1).payload
        )


class OuterProduct(MatrixNodeBase):
    """Creates the outer product of two matrices."""
    title = 'Outer'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]

    def get_mat(self):
        return np.outer(
            self.input(0).payload,
            self.input(1).payload
        )


class InverseMatrix(MatrixNodeBase):
    """Computes the inverse matrix"""
    title = 'Inverse'

    def get_mat(self):
        return np.linalg.inv(
            self.input(0).payload
        )


class KronMatrix(MatrixNodeBase):
    """"""
    title = 'Kron'

    def get_mat(self):
        return np.kron(
            self.input(0).payload,
            self.input(1).payload
        )


class MaskLower(MatrixNodeBase):
    """"""
    title = 'Mask Lower'

    def get_mat(self):
        return np.tril(
            self.input(0).payload
        )


class MaskUpper(MatrixNodeBase):
    """"""
    title = 'Mask Upper'

    def get_mat(self):
        return np.triu(
            self.input(0).payload
        )


class MatMul(MatrixNodeBase):
    """Performs a matrix multiplication."""
    title = 'Mult'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]

    def get_mat(self):
        return np.matmul(
            self.input(0).payload,
            self.input(1).payload
        )


class MatPower(MatrixNodeBase):
    """Powers a matrix."""
    title = 'Power'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]

    def get_mat(self):
        return np.linalg.matrix_power(
            self.input(0).payload,
            self.input(1).payload
        )


class NullMatrix(MatrixNodeBase):
    """Creates a matrix of zeros."""
    title = 'Null'

    def get_mat(self):
        return np.zeros(shape=(self.input(0).payload, self.input(1).payload))


class OnesMatrix(MatrixNodeBase):
    """Creates a matrix of ones."""
    title = 'Ones'

    def get_mat(self):
        return np.ones(shape=(self.input(0).payload, self.input(1).payload))


class RandomMatrix(MatrixNodeBase):
    """Creates a matrix with random values between 0 and 1."""
    title = 'Rand'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]

    def get_mat(self):
        return np.random.rand(
            self.input(0).payload,
            self.input(1).payload
        )


class SolveLEq(MatrixNodeBase):
    """Solves a linear equation system."""
    title = 'Solve'
    init_inputs = [
        NodeInputType(),
        NodeInputType(),
    ]

    def get_mat(self):
        return np.linalg.solve(
            self.input(0).payload,
            self.input(1).payload
        )


class EditMatrixNode(Node):
    """
    A special node for hand-designing matrices with specific
    numerical values. It also supports Ryven variables and
    automatically adapts the matrix when they change.
    """
    title = 'Matrix'
    identifier = 'EditMatrix_Node'
    legacy_identifiers = ['Matrix_Node', 'linalg.Matrix_Node']
    init_inputs = []
    init_outputs = [
        NodeOutputType()
    ]

    def __init__(self, params):
        super().__init__(params)

        self.expression_matrix: Optional[np.ndarray] = None
        self.evaluated_matrix: Optional[MatrixData] = None

        self.used_variable_names = []

    def update_event(self, inp=-1):
        if self.expression_matrix is not None:
            self.set_output_val(0, self.evaluated_matrix)

    def parse_matrix(self, s):  # called from gui
        lines = s.splitlines()

        try:
            # this throws a ValueError if the matrix is not rectangular
            exp_mat = np.array([
                list(filter(lambda s: s != '', l.split(' ')))  # array of expression strings
                for l in lines
            ])

            # check if all expressions are valid
            for exp in self.flatten_2d(exp_mat):
                if not self.exp_is_var(exp):
                    eval(exp)
                elif not self.var_exists(exp):
                    raise NameError
        except (ValueError, NameError):
            # something like 2+ (which could become 2+1j) can't get parsed yet
            return

        self.expression_matrix = exp_mat
        self.register_vars_and_eval_matrix()
        self.update()

    def register_vars_and_eval_matrix(self):
        if not self.register_vars(self.expression_matrix):
            return  # abort if vars registration failed
        self.evaluated_matrix = self.eval_matrix(self.expression_matrix)

    def register_vars(self, lines: np.ndarray) -> bool:
        """Updates subscriptions for the variables used in the matrix."""

        for _ in range(len(self.used_variable_names)):
            self.unsub_var(self.used_variable_names[0])

        var_names = set()
        for exp in filter(self.exp_is_var, self.flatten_2d(lines)):
            if self.var_exists(exp):
                var_names.add(exp)
            else:
                return False

        for var_name in var_names:
            self.sub_var(var_name)

        return True

    def eval_matrix(self, lines) -> MatrixData:
        """
        Evaluates a matrix from string expressions of numerals and variables.
        """

        # replace old v('name') syntax with new 'name' syntax
        lines = [
            [exp.replace('v(', '').replace(')', '') if 'v(' in exp else exp
             for exp in l]
            for l in lines
        ]

        # evaluate expressions
        evaled_exp_array = [
            [
                eval(exp)
                if not self.exp_is_var(exp) else
                self.var_val(exp)
                for exp in l
            ]
            for l in lines
        ]

        # convert ints to floats; leave complex numbers
        int_to_float = lambda v: float(v) if isinstance(v, int) else v
        float_exp_array = [
            list(map(int_to_float, l))
            for l in evaled_exp_array
        ]

        # build matrix and wrap in MatrixData
        return MatrixData(np.array(float_exp_array))

    def var_exists(self, name):
        return self.get_addon('Variables').var_exists(self.flow, name)

    def sub_var(self, name) -> bool:
        if not self.var_exists(name):
            return False

        self.get_addon('Variables').subscribe(self, name, self.var_val_updated)
        self.used_variable_names.append(name)
        return True

    def unsub_var(self, name):
        self.get_addon('Variables').unsubscribe(self, name, self.var_val_updated)
        self.used_variable_names.remove(name)

    def var_val_updated(self, var: ryvencore.addons.Variables.Variable):
        self.evaluated_matrix = self.eval_matrix(self.expression_matrix)
        self.update()

    def var(self, name) -> ryvencore.addons.Variables.Variable:
        return self.get_addon('Variables').var(self.flow, name)

    def var_val(self, name):
        return self.var(name).get()

    def exp_is_var(self, s: str):
        return s.isidentifier()

    def flatten_2d(self, mat: np.ndarray) -> np.ndarray:
        return np.array(list(chain(*mat)))

    def get_state(self):
        data = {'expression matrix': serialize(self.expression_matrix)}
        return data

    def set_state(self, data, version):
        self.expression_matrix = deserialize(data['expression matrix'])
        self.register_vars_and_eval_matrix()


export_nodes(
    node_types=[
        EditMatrixNode,
        ShowMatrix,
        Conjugate,
        Transpose,
        DetOfMatrix,
        DotProduct,
        HermMatrix,
        IDMatrix,
        ImagMatrix,
        RealMatrix,
        InnerProduct,
        OuterProduct,
        InverseMatrix,
        KronMatrix,
        MaskLower,
        MaskUpper,
        MatMul,
        MatPower,
        NullMatrix,
        OnesMatrix,
        RandomMatrix,
        SolveLEq,
    ],
    data_types=[MatrixData]
)
