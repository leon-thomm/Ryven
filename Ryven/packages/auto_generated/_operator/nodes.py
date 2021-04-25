
from NENV import *

import _operator


class NodeBase(Node):
    pass


class AutoNode__operator__compare_digest(NodeBase):
    title = '_compare_digest'
    type_ = '_operator'
    doc = """Return 'a == b'.

This function uses an approach designed to prevent
timing analysis, making it appropriate for cryptography.

a and b must both be of the same type: either str (ASCII only),
or any bytes-like object.

Note: If a and b are of different lengths, or if an error occurs,
a timing attack could theoretically reveal information about the
types and lengths of a and b--but not their values."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator._compare_digest(self.input(0), self.input(1)))
        

class AutoNode__operator_abs(NodeBase):
    title = 'abs'
    type_ = '_operator'
    doc = """Same as abs(a)."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.abs(self.input(0)))
        

class AutoNode__operator_add(NodeBase):
    title = 'add'
    type_ = '_operator'
    doc = """Same as a + b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.add(self.input(0), self.input(1)))
        

class AutoNode__operator_and_(NodeBase):
    title = 'and_'
    type_ = '_operator'
    doc = """Same as a & b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.and_(self.input(0), self.input(1)))
        

class AutoNode__operator_concat(NodeBase):
    title = 'concat'
    type_ = '_operator'
    doc = """Same as a + b, for a and b sequences."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.concat(self.input(0), self.input(1)))
        

class AutoNode__operator_contains(NodeBase):
    title = 'contains'
    type_ = '_operator'
    doc = """Same as b in a (note reversed operands)."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.contains(self.input(0), self.input(1)))
        

class AutoNode__operator_countOf(NodeBase):
    title = 'countOf'
    type_ = '_operator'
    doc = """Return the number of times b occurs in a."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.countOf(self.input(0), self.input(1)))
        

class AutoNode__operator_delitem(NodeBase):
    title = 'delitem'
    type_ = '_operator'
    doc = """Same as del a[b]."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.delitem(self.input(0), self.input(1)))
        

class AutoNode__operator_eq(NodeBase):
    title = 'eq'
    type_ = '_operator'
    doc = """Same as a == b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.eq(self.input(0), self.input(1)))
        

class AutoNode__operator_floordiv(NodeBase):
    title = 'floordiv'
    type_ = '_operator'
    doc = """Same as a // b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.floordiv(self.input(0), self.input(1)))
        

class AutoNode__operator_ge(NodeBase):
    title = 'ge'
    type_ = '_operator'
    doc = """Same as a >= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ge(self.input(0), self.input(1)))
        

class AutoNode__operator_getitem(NodeBase):
    title = 'getitem'
    type_ = '_operator'
    doc = """Same as a[b]."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.getitem(self.input(0), self.input(1)))
        

class AutoNode__operator_gt(NodeBase):
    title = 'gt'
    type_ = '_operator'
    doc = """Same as a > b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.gt(self.input(0), self.input(1)))
        

class AutoNode__operator_iadd(NodeBase):
    title = 'iadd'
    type_ = '_operator'
    doc = """Same as a += b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.iadd(self.input(0), self.input(1)))
        

class AutoNode__operator_iand(NodeBase):
    title = 'iand'
    type_ = '_operator'
    doc = """Same as a &= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.iand(self.input(0), self.input(1)))
        

class AutoNode__operator_iconcat(NodeBase):
    title = 'iconcat'
    type_ = '_operator'
    doc = """Same as a += b, for a and b sequences."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.iconcat(self.input(0), self.input(1)))
        

class AutoNode__operator_ifloordiv(NodeBase):
    title = 'ifloordiv'
    type_ = '_operator'
    doc = """Same as a //= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ifloordiv(self.input(0), self.input(1)))
        

class AutoNode__operator_ilshift(NodeBase):
    title = 'ilshift'
    type_ = '_operator'
    doc = """Same as a <<= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ilshift(self.input(0), self.input(1)))
        

class AutoNode__operator_imatmul(NodeBase):
    title = 'imatmul'
    type_ = '_operator'
    doc = """Same as a @= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.imatmul(self.input(0), self.input(1)))
        

class AutoNode__operator_imod(NodeBase):
    title = 'imod'
    type_ = '_operator'
    doc = """Same as a %= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.imod(self.input(0), self.input(1)))
        

class AutoNode__operator_imul(NodeBase):
    title = 'imul'
    type_ = '_operator'
    doc = """Same as a *= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.imul(self.input(0), self.input(1)))
        

class AutoNode__operator_index(NodeBase):
    title = 'index'
    type_ = '_operator'
    doc = """Same as a.__index__()"""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.index(self.input(0)))
        

class AutoNode__operator_indexOf(NodeBase):
    title = 'indexOf'
    type_ = '_operator'
    doc = """Return the first index of b in a."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.indexOf(self.input(0), self.input(1)))
        

class AutoNode__operator_inv(NodeBase):
    title = 'inv'
    type_ = '_operator'
    doc = """Same as ~a."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.inv(self.input(0)))
        

class AutoNode__operator_invert(NodeBase):
    title = 'invert'
    type_ = '_operator'
    doc = """Same as ~a."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.invert(self.input(0)))
        

class AutoNode__operator_ior(NodeBase):
    title = 'ior'
    type_ = '_operator'
    doc = """Same as a |= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ior(self.input(0), self.input(1)))
        

class AutoNode__operator_ipow(NodeBase):
    title = 'ipow'
    type_ = '_operator'
    doc = """Same as a **= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ipow(self.input(0), self.input(1)))
        

class AutoNode__operator_irshift(NodeBase):
    title = 'irshift'
    type_ = '_operator'
    doc = """Same as a >>= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.irshift(self.input(0), self.input(1)))
        

class AutoNode__operator_is_(NodeBase):
    title = 'is_'
    type_ = '_operator'
    doc = """Same as a is b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.is_(self.input(0), self.input(1)))
        

class AutoNode__operator_is_not(NodeBase):
    title = 'is_not'
    type_ = '_operator'
    doc = """Same as a is not b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.is_not(self.input(0), self.input(1)))
        

class AutoNode__operator_isub(NodeBase):
    title = 'isub'
    type_ = '_operator'
    doc = """Same as a -= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.isub(self.input(0), self.input(1)))
        

class AutoNode__operator_itruediv(NodeBase):
    title = 'itruediv'
    type_ = '_operator'
    doc = """Same as a /= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.itruediv(self.input(0), self.input(1)))
        

class AutoNode__operator_ixor(NodeBase):
    title = 'ixor'
    type_ = '_operator'
    doc = """Same as a ^= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ixor(self.input(0), self.input(1)))
        

class AutoNode__operator_le(NodeBase):
    title = 'le'
    type_ = '_operator'
    doc = """Same as a <= b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.le(self.input(0), self.input(1)))
        

class AutoNode__operator_length_hint(NodeBase):
    title = 'length_hint'
    type_ = '_operator'
    doc = """Return an estimate of the number of items in obj.

This is useful for presizing containers when building from an iterable.

If the object supports len(), the result will be exact.
Otherwise, it may over- or under-estimate by an arbitrary amount.
The result will be an integer >= 0."""
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='default'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.length_hint(self.input(0), self.input(1)))
        

class AutoNode__operator_lshift(NodeBase):
    title = 'lshift'
    type_ = '_operator'
    doc = """Same as a << b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.lshift(self.input(0), self.input(1)))
        

class AutoNode__operator_lt(NodeBase):
    title = 'lt'
    type_ = '_operator'
    doc = """Same as a < b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.lt(self.input(0), self.input(1)))
        

class AutoNode__operator_matmul(NodeBase):
    title = 'matmul'
    type_ = '_operator'
    doc = """Same as a @ b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.matmul(self.input(0), self.input(1)))
        

class AutoNode__operator_mod(NodeBase):
    title = 'mod'
    type_ = '_operator'
    doc = """Same as a % b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.mod(self.input(0), self.input(1)))
        

class AutoNode__operator_mul(NodeBase):
    title = 'mul'
    type_ = '_operator'
    doc = """Same as a * b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.mul(self.input(0), self.input(1)))
        

class AutoNode__operator_ne(NodeBase):
    title = 'ne'
    type_ = '_operator'
    doc = """Same as a != b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.ne(self.input(0), self.input(1)))
        

class AutoNode__operator_neg(NodeBase):
    title = 'neg'
    type_ = '_operator'
    doc = """Same as -a."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.neg(self.input(0)))
        

class AutoNode__operator_not_(NodeBase):
    title = 'not_'
    type_ = '_operator'
    doc = """Same as not a."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.not_(self.input(0)))
        

class AutoNode__operator_or_(NodeBase):
    title = 'or_'
    type_ = '_operator'
    doc = """Same as a | b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.or_(self.input(0), self.input(1)))
        

class AutoNode__operator_pos(NodeBase):
    title = 'pos'
    type_ = '_operator'
    doc = """Same as +a."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.pos(self.input(0)))
        

class AutoNode__operator_pow(NodeBase):
    title = 'pow'
    type_ = '_operator'
    doc = """Same as a ** b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.pow(self.input(0), self.input(1)))
        

class AutoNode__operator_rshift(NodeBase):
    title = 'rshift'
    type_ = '_operator'
    doc = """Same as a >> b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.rshift(self.input(0), self.input(1)))
        

class AutoNode__operator_setitem(NodeBase):
    title = 'setitem'
    type_ = '_operator'
    doc = """Same as a[b] = c."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
        NodeInputBP(label='c'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.setitem(self.input(0), self.input(1), self.input(2)))
        

class AutoNode__operator_sub(NodeBase):
    title = 'sub'
    type_ = '_operator'
    doc = """Same as a - b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.sub(self.input(0), self.input(1)))
        

class AutoNode__operator_truediv(NodeBase):
    title = 'truediv'
    type_ = '_operator'
    doc = """Same as a / b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.truediv(self.input(0), self.input(1)))
        

class AutoNode__operator_truth(NodeBase):
    title = 'truth'
    type_ = '_operator'
    doc = """Return True if a is true, False otherwise."""
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.truth(self.input(0)))
        

class AutoNode__operator_xor(NodeBase):
    title = 'xor'
    type_ = '_operator'
    doc = """Same as a ^ b."""
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _operator.xor(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode__operator__compare_digest,
    AutoNode__operator_abs,
    AutoNode__operator_add,
    AutoNode__operator_and_,
    AutoNode__operator_concat,
    AutoNode__operator_contains,
    AutoNode__operator_countOf,
    AutoNode__operator_delitem,
    AutoNode__operator_eq,
    AutoNode__operator_floordiv,
    AutoNode__operator_ge,
    AutoNode__operator_getitem,
    AutoNode__operator_gt,
    AutoNode__operator_iadd,
    AutoNode__operator_iand,
    AutoNode__operator_iconcat,
    AutoNode__operator_ifloordiv,
    AutoNode__operator_ilshift,
    AutoNode__operator_imatmul,
    AutoNode__operator_imod,
    AutoNode__operator_imul,
    AutoNode__operator_index,
    AutoNode__operator_indexOf,
    AutoNode__operator_inv,
    AutoNode__operator_invert,
    AutoNode__operator_ior,
    AutoNode__operator_ipow,
    AutoNode__operator_irshift,
    AutoNode__operator_is_,
    AutoNode__operator_is_not,
    AutoNode__operator_isub,
    AutoNode__operator_itruediv,
    AutoNode__operator_ixor,
    AutoNode__operator_le,
    AutoNode__operator_length_hint,
    AutoNode__operator_lshift,
    AutoNode__operator_lt,
    AutoNode__operator_matmul,
    AutoNode__operator_mod,
    AutoNode__operator_mul,
    AutoNode__operator_ne,
    AutoNode__operator_neg,
    AutoNode__operator_not_,
    AutoNode__operator_or_,
    AutoNode__operator_pos,
    AutoNode__operator_pow,
    AutoNode__operator_rshift,
    AutoNode__operator_setitem,
    AutoNode__operator_sub,
    AutoNode__operator_truediv,
    AutoNode__operator_truth,
    AutoNode__operator_xor,
)
