from NENV import *
widgets = import_widgets(__file__)

import numpy as np


class MatrixNodeBase(Node):
    main_widget_class = widgets.MatrixWidget
    main_widget_pos = 'below ports'
    init_inputs = [
        NodeInputBP()
    ]
    init_outputs = [
        NodeOutputBP()
    ]
    color = '#3344ff'

    def __init__(self, params):
        super().__init__(params)
        self.mat = None

    def show_matrix(self):
        if self.session.gui and self.main_widget():
            self.main_widget().update_matrix(self.mat)
    
    def update_event(self, input_called=-1):
        self.mat = self.get_mat()
        self.show_matrix()
        self.set_output_val(0, self.mat)


class ShowMatrix(MatrixNodeBase):
    title = 'Show Matrix'
    description = 'Shows a matrix.'

    def get_mat(self):
        return self.input(0)

# ------------------------------------------------------------------------------


class Matrix_Node(Node):
    title = 'Matrix'
    description = 'Evaluates a matrix'
    init_inputs = []
    init_outputs = [
        NodeOutputBP()
    ]
    main_widget_class = widgets.MatrixNode_MainWidget
    main_widget_pos = 'below ports'
    color = '#3344ff'

    def __init__(self, params):
        super(Matrix_Node, self).__init__(params)

        self.special_actions['hide preview'] = {'method': self.action_hide_mw}
        self.main_widget_hidden = False
        self.expression_matrix = None
        self.evaluated_matrix = None
        self.used_variable_names = []

    def place_event(self):
        self.update()

    def update_event(self, input_called=-1):
        self.set_output_val(0, self.evaluated_matrix)
        
    def parse_matrix(self, s):
        lines = s.splitlines()
        # the list(filter(...)) creates an array of strings for every line
        try:
            self.expression_matrix = np.array([[exp for exp in list(filter(lambda s: s != '', l.split(' ')))] for l in lines])
            self.eval_expression_matrix()
            self.update()
        except ValueError:
            # something like 2+ (which could become 2+1j) can't get parsed yet
            return

    def eval_expression_matrix(self):
        if not self.register_vars(self.expression_matrix):
            return  # return if parsing failed

        self.evaluated_matrix = self.eval_matrix(self.expression_matrix)

        if self.evaluated_matrix is None:
            return  # matrix could not be evaluated
        # custom_array = [list(map(number_type, list(filter(lambda s: s != '', l.split(' '))))) for l in lines]

        try:
            self.evaluated_matrix = np.array(self.evaluated_matrix)
        except Exception:
            return

    def eval_matrix(self, lines):
        v = self.get_var_val
        evaled_exp_array = []
        for l in lines:
            evaled_exp_array.append([])
            for exp in l:
                evaled_exp_array[-1].append(eval(exp))
        float_exp_array = [[float(exp) if type(exp) == int else exp for exp in l] for l in evaled_exp_array]
        return np.array(float_exp_array)

    def register_vars(self, lines):
        try:
            # clear used variables
            for name in self.used_variable_names:
                self.unregister_var_receiver(name)
            self.used_variable_names.clear()

            v = self.register_variable
            for l in lines:
                for exp in l:
                    eval(exp)
            return True
        except Exception:
            return False

    def register_variable(self, name):
        # connect to variable changes
        self.register_var_receiver(name, self.var_val_updated)
        self.used_variable_names.append(name)

    def var_val_updated(self, name, val):
        self.evaluated_matrix = self.eval_matrix(self.expression_matrix)
        self.update()

    def action_hide_mw(self):
        self.main_widget().hide()
        del self.special_actions['hide preview']
        self.special_actions['show preview'] = {'method': self.action_show_mw}
        self.main_widget_hidden = True
        self.update_shape()

    def action_show_mw(self):
        self.main_widget().show()
        del self.special_actions['show preview']
        self.special_actions['hide preview'] = {'method': self.action_hide_mw}
        self.main_widget_hidden = False
        self.update_shape()

    def get_state(self):
        expression_matrix_list = self.expression_matrix
        if expression_matrix_list is not None:  # ndarrays are not json serializaple
            expression_matrix_list = expression_matrix_list.tolist()

        data = {'main widget hidden': self.main_widget_hidden,
                'expression matrix': expression_matrix_list}
        return data

    def set_state(self, data):
        if self.session.gui:
            self.main_widget_hidden = data['main widget hidden']
            if self.main_widget_hidden:
                self.action_hide_mw()
            # shown by default
        
        self.expression_matrix = np.array(data['expression matrix'])
        self.eval_expression_matrix()


class Conjugate(MatrixNodeBase):
    title = 'Conjugate'
    description = 'Conjugates a matrix.'

    def get_mat(self):
        return np.conjugate(self.input(0))


class Transpose(MatrixNodeBase):
    title = 'Transpose'
    description = 'Transposes a matrix.'

    def get_mat(self):
        return np.transpose(self.input(0))


class DetOfMatrix(MatrixNodeBase):
    title = 'Determinant'
    description = 'Computes the determinant of a matrix.'
    
    def get_mat(self):
        return np.linalg.det(self.input(0))


class DotProduct(MatrixNodeBase):
    title = 'Dot Product'
    description = 'Computes the dot product of a matrix.'
    init_inputs = [
        NodeInputBP(),
        NodeInputBP(),
    ]
    
    def get_mat(self):
        return np.dot(self.input(0), self.input(1))


class HermMatrix(MatrixNodeBase):
    title = 'Herm'
    description = 'Computes the hermetian matrix.'
    
    def get_mat(self):
        return np.transpose(np.conjugate(self.input(0)))


class IDMatrix(MatrixNodeBase):
    title = 'ID Matrix'
    description = 'Creates an identity matrix.'
    
    def get_mat(self):
        return np.identity(self.input(0))


class ImagMatrix(MatrixNodeBase):
    title = 'Imag'
    description = 'Extracts the imaginary parts of the patrix.'
    
    def get_mat(self):
        return np.imag(self.input(0))


class RealMatrix(MatrixNodeBase):
    title = 'Real'
    description = 'Extracts the real parts of the patrix.'
    
    def get_mat(self):
        return np.real(self.input(0))


class InnerProduct(MatrixNodeBase):
    title = 'Inner'
    description = 'Computes the inner product of the input matrices.'
    init_inputs = [
        NodeInputBP(),
        NodeInputBP(),
    ]
    
    def get_mat(self):
        return np.inner(self.input(0), self.input(1))


class OuterProduct(MatrixNodeBase):
    title = 'Outer'
    description = 'Creates the outer product of two matrices.'
    init_inputs = [
        NodeInputBP(),
        NodeInputBP(),
    ]

    def get_mat(self):
        return np.outer(self.input(0), self.input(1))


class InverseMatrix(MatrixNodeBase):
    title = 'Inverse'
    description = 'Computes the inverse matrix'

    def get_mat(self):
        return np.linalg.inv(self.input(0))


class KronMatrix(MatrixNodeBase):
    title = 'Kron'
    description = ''

    def get_mat(self):
        return np.kron(self.input(0), self.input(1))


class MaskLower(MatrixNodeBase):
    title = 'Mask Lower'
    description = ''

    def get_mat(self):
        return np.tril(self.input(0))


class MaskUpper(MatrixNodeBase):
    title = 'Mask Upper'
    description = ''

    def get_mat(self):
        return np.triu(self.input(0))


class MatMul(MatrixNodeBase):
    title = 'Mult'
    description = 'Performs a matrix multiplication.'
    init_inputs = [
        NodeInputBP(),
        NodeInputBP(),
    ]

    def get_mat(self):
        return np.matmul(self.input(0), self.input(1))


class MatPower(MatrixNodeBase):
    title = 'Power'
    description = 'Powers a matrix.'
    init_inputs = [
        NodeInputBP(),
        NodeInputBP(),
    ]

    def get_mat(self):
        return np.linalg.matrix_power(self.input(0), self.input(1))


class NullMatrix(MatrixNodeBase):
    title = 'Null'
    description = 'Creates a matrix of zeros.'

    def get_mat(self):
        return np.zeros(shape=(self.input(0), self.input(1)))


class OnesMatrix(MatrixNodeBase):
    title = 'Ones'
    description = 'Creates a matrix of ones.'

    def get_mat(self):
        return np.ones(shape=(self.input(0), self.input(1)))


class RandomMatrix(MatrixNodeBase):
    title = 'Rand'
    description = 'Creates a patrix with random values between 0 and 1.'
    init_inputs = [
        NodeInputBP(),
        NodeInputBP(),
    ]

    def get_mat(self):
        m = np.random.rand(self.input(0), self.input(1))
        return m


class SolveLEq(MatrixNodeBase):
    title = 'Solve'
    description = 'Solves a linear equasion system.'
    init_inputs = [
        NodeInputBP(),
        NodeInputBP(),
    ]

    def get_mat(self):
        return np.linalg.solve(self.input(0), self.input(1))


export_nodes(
    Matrix_Node,
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
)
