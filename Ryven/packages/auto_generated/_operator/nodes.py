import ryvencore_qt as rc
import _operator


class AutoNode__operator__compare_digest(rc.Node):
    title = '_compare_digest'
    type_ = '_operator'
    doc = '''Return 'a == b'.

This function uses an approach designed to prevent
timing analysis, making it appropriate for cryptography.

a and b must both be of the same type: either str (ASCII only),
or any bytes-like object.

Note: If a and b are of different lengths, or if an error occurs,
a timing attack could theoretically reveal information about the
types and lengths of a and b--but not their values.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator._compare_digest(self.input(0), self.input(1)))
        


class AutoNode__operator_abs(rc.Node):
    title = 'abs'
    type_ = '_operator'
    doc = '''Same as abs(a).'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.abs(self.input(0)))
        


class AutoNode__operator_add(rc.Node):
    title = 'add'
    type_ = '_operator'
    doc = '''Same as a + b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.add(self.input(0), self.input(1)))
        


class AutoNode__operator_and_(rc.Node):
    title = 'and_'
    type_ = '_operator'
    doc = '''Same as a & b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.and_(self.input(0), self.input(1)))
        


class AutoNode__operator_concat(rc.Node):
    title = 'concat'
    type_ = '_operator'
    doc = '''Same as a + b, for a and b sequences.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.concat(self.input(0), self.input(1)))
        


class AutoNode__operator_contains(rc.Node):
    title = 'contains'
    type_ = '_operator'
    doc = '''Same as b in a (note reversed operands).'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.contains(self.input(0), self.input(1)))
        


class AutoNode__operator_countOf(rc.Node):
    title = 'countOf'
    type_ = '_operator'
    doc = '''Return the number of times b occurs in a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.countOf(self.input(0), self.input(1)))
        


class AutoNode__operator_delitem(rc.Node):
    title = 'delitem'
    type_ = '_operator'
    doc = '''Same as del a[b].'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.delitem(self.input(0), self.input(1)))
        


class AutoNode__operator_eq(rc.Node):
    title = 'eq'
    type_ = '_operator'
    doc = '''Same as a == b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.eq(self.input(0), self.input(1)))
        


class AutoNode__operator_floordiv(rc.Node):
    title = 'floordiv'
    type_ = '_operator'
    doc = '''Same as a // b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.floordiv(self.input(0), self.input(1)))
        


class AutoNode__operator_ge(rc.Node):
    title = 'ge'
    type_ = '_operator'
    doc = '''Same as a >= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ge(self.input(0), self.input(1)))
        


class AutoNode__operator_getitem(rc.Node):
    title = 'getitem'
    type_ = '_operator'
    doc = '''Same as a[b].'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.getitem(self.input(0), self.input(1)))
        


class AutoNode__operator_gt(rc.Node):
    title = 'gt'
    type_ = '_operator'
    doc = '''Same as a > b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.gt(self.input(0), self.input(1)))
        


class AutoNode__operator_iadd(rc.Node):
    title = 'iadd'
    type_ = '_operator'
    doc = '''Same as a += b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.iadd(self.input(0), self.input(1)))
        


class AutoNode__operator_iand(rc.Node):
    title = 'iand'
    type_ = '_operator'
    doc = '''Same as a &= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.iand(self.input(0), self.input(1)))
        


class AutoNode__operator_iconcat(rc.Node):
    title = 'iconcat'
    type_ = '_operator'
    doc = '''Same as a += b, for a and b sequences.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.iconcat(self.input(0), self.input(1)))
        


class AutoNode__operator_ifloordiv(rc.Node):
    title = 'ifloordiv'
    type_ = '_operator'
    doc = '''Same as a //= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ifloordiv(self.input(0), self.input(1)))
        


class AutoNode__operator_ilshift(rc.Node):
    title = 'ilshift'
    type_ = '_operator'
    doc = '''Same as a <<= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ilshift(self.input(0), self.input(1)))
        


class AutoNode__operator_imatmul(rc.Node):
    title = 'imatmul'
    type_ = '_operator'
    doc = '''Same as a @= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.imatmul(self.input(0), self.input(1)))
        


class AutoNode__operator_imod(rc.Node):
    title = 'imod'
    type_ = '_operator'
    doc = '''Same as a %= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.imod(self.input(0), self.input(1)))
        


class AutoNode__operator_imul(rc.Node):
    title = 'imul'
    type_ = '_operator'
    doc = '''Same as a *= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.imul(self.input(0), self.input(1)))
        


class AutoNode__operator_index(rc.Node):
    title = 'index'
    type_ = '_operator'
    doc = '''Same as a.__index__()'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.index(self.input(0)))
        


class AutoNode__operator_indexOf(rc.Node):
    title = 'indexOf'
    type_ = '_operator'
    doc = '''Return the first index of b in a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.indexOf(self.input(0), self.input(1)))
        


class AutoNode__operator_inv(rc.Node):
    title = 'inv'
    type_ = '_operator'
    doc = '''Same as ~a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.inv(self.input(0)))
        


class AutoNode__operator_invert(rc.Node):
    title = 'invert'
    type_ = '_operator'
    doc = '''Same as ~a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.invert(self.input(0)))
        


class AutoNode__operator_ior(rc.Node):
    title = 'ior'
    type_ = '_operator'
    doc = '''Same as a |= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ior(self.input(0), self.input(1)))
        


class AutoNode__operator_ipow(rc.Node):
    title = 'ipow'
    type_ = '_operator'
    doc = '''Same as a **= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ipow(self.input(0), self.input(1)))
        


class AutoNode__operator_irshift(rc.Node):
    title = 'irshift'
    type_ = '_operator'
    doc = '''Same as a >>= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.irshift(self.input(0), self.input(1)))
        


class AutoNode__operator_is_(rc.Node):
    title = 'is_'
    type_ = '_operator'
    doc = '''Same as a is b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.is_(self.input(0), self.input(1)))
        


class AutoNode__operator_is_not(rc.Node):
    title = 'is_not'
    type_ = '_operator'
    doc = '''Same as a is not b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.is_not(self.input(0), self.input(1)))
        


class AutoNode__operator_isub(rc.Node):
    title = 'isub'
    type_ = '_operator'
    doc = '''Same as a -= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.isub(self.input(0), self.input(1)))
        


class AutoNode__operator_itruediv(rc.Node):
    title = 'itruediv'
    type_ = '_operator'
    doc = '''Same as a /= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.itruediv(self.input(0), self.input(1)))
        


class AutoNode__operator_ixor(rc.Node):
    title = 'ixor'
    type_ = '_operator'
    doc = '''Same as a ^= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ixor(self.input(0), self.input(1)))
        


class AutoNode__operator_le(rc.Node):
    title = 'le'
    type_ = '_operator'
    doc = '''Same as a <= b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.le(self.input(0), self.input(1)))
        


class AutoNode__operator_length_hint(rc.Node):
    title = 'length_hint'
    type_ = '_operator'
    doc = '''Return an estimate of the number of items in obj.

This is useful for presizing containers when building from an iterable.

If the object supports len(), the result will be exact.
Otherwise, it may over- or under-estimate by an arbitrary amount.
The result will be an integer >= 0.'''
    init_inputs = [
        rc.NodeInputBP(label='obj'),
rc.NodeInputBP(label='default'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.length_hint(self.input(0), self.input(1)))
        


class AutoNode__operator_lshift(rc.Node):
    title = 'lshift'
    type_ = '_operator'
    doc = '''Same as a << b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.lshift(self.input(0), self.input(1)))
        


class AutoNode__operator_lt(rc.Node):
    title = 'lt'
    type_ = '_operator'
    doc = '''Same as a < b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.lt(self.input(0), self.input(1)))
        


class AutoNode__operator_matmul(rc.Node):
    title = 'matmul'
    type_ = '_operator'
    doc = '''Same as a @ b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.matmul(self.input(0), self.input(1)))
        


class AutoNode__operator_mod(rc.Node):
    title = 'mod'
    type_ = '_operator'
    doc = '''Same as a % b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.mod(self.input(0), self.input(1)))
        


class AutoNode__operator_mul(rc.Node):
    title = 'mul'
    type_ = '_operator'
    doc = '''Same as a * b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.mul(self.input(0), self.input(1)))
        


class AutoNode__operator_ne(rc.Node):
    title = 'ne'
    type_ = '_operator'
    doc = '''Same as a != b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ne(self.input(0), self.input(1)))
        


class AutoNode__operator_neg(rc.Node):
    title = 'neg'
    type_ = '_operator'
    doc = '''Same as -a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.neg(self.input(0)))
        


class AutoNode__operator_not_(rc.Node):
    title = 'not_'
    type_ = '_operator'
    doc = '''Same as not a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.not_(self.input(0)))
        


class AutoNode__operator_or_(rc.Node):
    title = 'or_'
    type_ = '_operator'
    doc = '''Same as a | b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.or_(self.input(0), self.input(1)))
        


class AutoNode__operator_pos(rc.Node):
    title = 'pos'
    type_ = '_operator'
    doc = '''Same as +a.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.pos(self.input(0)))
        


class AutoNode__operator_pow(rc.Node):
    title = 'pow'
    type_ = '_operator'
    doc = '''Same as a ** b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.pow(self.input(0), self.input(1)))
        


class AutoNode__operator_rshift(rc.Node):
    title = 'rshift'
    type_ = '_operator'
    doc = '''Same as a >> b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.rshift(self.input(0), self.input(1)))
        


class AutoNode__operator_setitem(rc.Node):
    title = 'setitem'
    type_ = '_operator'
    doc = '''Same as a[b] = c.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
rc.NodeInputBP(label='c'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.setitem(self.input(0), self.input(1), self.input(2)))
        


class AutoNode__operator_sub(rc.Node):
    title = 'sub'
    type_ = '_operator'
    doc = '''Same as a - b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.sub(self.input(0), self.input(1)))
        


class AutoNode__operator_truediv(rc.Node):
    title = 'truediv'
    type_ = '_operator'
    doc = '''Same as a / b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.truediv(self.input(0), self.input(1)))
        


class AutoNode__operator_truth(rc.Node):
    title = 'truth'
    type_ = '_operator'
    doc = '''Return True if a is true, False otherwise.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.truth(self.input(0)))
        


class AutoNode__operator_xor(rc.Node):
    title = 'xor'
    type_ = '_operator'
    doc = '''Same as a ^ b.'''
    init_inputs = [
        rc.NodeInputBP(label='a'),
rc.NodeInputBP(label='b'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.xor(self.input(0), self.input(1)))
        