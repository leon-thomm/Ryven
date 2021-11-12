
from ryven.NENV import *

import operator


class NodeBase(Node):
    pass


class __Abs___Node(NodeBase):
    """
    Same as abs(a)."""
    
    title = '__abs__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__abs__(self.input(0)))
        

class __Add___Node(NodeBase):
    """
    Same as a + b."""
    
    title = '__add__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__add__(self.input(0), self.input(1)))
        

class __And___Node(NodeBase):
    """
    Same as a & b."""
    
    title = '__and__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__and__(self.input(0), self.input(1)))
        

class __Concat___Node(NodeBase):
    """
    Same as a + b, for a and b sequences."""
    
    title = '__concat__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__concat__(self.input(0), self.input(1)))
        

class __Contains___Node(NodeBase):
    """
    Same as b in a (note reversed operands)."""
    
    title = '__contains__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__contains__(self.input(0), self.input(1)))
        

class __Delitem___Node(NodeBase):
    """
    Same as del a[b]."""
    
    title = '__delitem__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__delitem__(self.input(0), self.input(1)))
        

class __Eq___Node(NodeBase):
    """
    Same as a == b."""
    
    title = '__eq__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__eq__(self.input(0), self.input(1)))
        

class __Floordiv___Node(NodeBase):
    """
    Same as a // b."""
    
    title = '__floordiv__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__floordiv__(self.input(0), self.input(1)))
        

class __Ge___Node(NodeBase):
    """
    Same as a >= b."""
    
    title = '__ge__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__ge__(self.input(0), self.input(1)))
        

class __Getitem___Node(NodeBase):
    """
    Same as a[b]."""
    
    title = '__getitem__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__getitem__(self.input(0), self.input(1)))
        

class __Gt___Node(NodeBase):
    """
    Same as a > b."""
    
    title = '__gt__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__gt__(self.input(0), self.input(1)))
        

class __Iadd___Node(NodeBase):
    """
    Same as a += b."""
    
    title = '__iadd__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__iadd__(self.input(0), self.input(1)))
        

class __Iand___Node(NodeBase):
    """
    Same as a &= b."""
    
    title = '__iand__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__iand__(self.input(0), self.input(1)))
        

class __Iconcat___Node(NodeBase):
    """
    Same as a += b, for a and b sequences."""
    
    title = '__iconcat__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__iconcat__(self.input(0), self.input(1)))
        

class __Ifloordiv___Node(NodeBase):
    """
    Same as a //= b."""
    
    title = '__ifloordiv__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__ifloordiv__(self.input(0), self.input(1)))
        

class __Ilshift___Node(NodeBase):
    """
    Same as a <<= b."""
    
    title = '__ilshift__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__ilshift__(self.input(0), self.input(1)))
        

class __Imatmul___Node(NodeBase):
    """
    Same as a @= b."""
    
    title = '__imatmul__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__imatmul__(self.input(0), self.input(1)))
        

class __Imod___Node(NodeBase):
    """
    Same as a %= b."""
    
    title = '__imod__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__imod__(self.input(0), self.input(1)))
        

class __Imul___Node(NodeBase):
    """
    Same as a *= b."""
    
    title = '__imul__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__imul__(self.input(0), self.input(1)))
        

class __Index___Node(NodeBase):
    """
    Same as a.__index__()"""
    
    title = '__index__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__index__(self.input(0)))
        

class __Inv___Node(NodeBase):
    """
    Same as ~a."""
    
    title = '__inv__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__inv__(self.input(0)))
        

class __Invert___Node(NodeBase):
    """
    Same as ~a."""
    
    title = '__invert__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__invert__(self.input(0)))
        

class __Ior___Node(NodeBase):
    """
    Same as a |= b."""
    
    title = '__ior__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__ior__(self.input(0), self.input(1)))
        

class __Ipow___Node(NodeBase):
    """
    Same as a **= b."""
    
    title = '__ipow__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__ipow__(self.input(0), self.input(1)))
        

class __Irshift___Node(NodeBase):
    """
    Same as a >>= b."""
    
    title = '__irshift__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__irshift__(self.input(0), self.input(1)))
        

class __Isub___Node(NodeBase):
    """
    Same as a -= b."""
    
    title = '__isub__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__isub__(self.input(0), self.input(1)))
        

class __Itruediv___Node(NodeBase):
    """
    Same as a /= b."""
    
    title = '__itruediv__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__itruediv__(self.input(0), self.input(1)))
        

class __Ixor___Node(NodeBase):
    """
    Same as a ^= b."""
    
    title = '__ixor__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__ixor__(self.input(0), self.input(1)))
        

class __Le___Node(NodeBase):
    """
    Same as a <= b."""
    
    title = '__le__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__le__(self.input(0), self.input(1)))
        

class __Lshift___Node(NodeBase):
    """
    Same as a << b."""
    
    title = '__lshift__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__lshift__(self.input(0), self.input(1)))
        

class __Lt___Node(NodeBase):
    """
    Same as a < b."""
    
    title = '__lt__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__lt__(self.input(0), self.input(1)))
        

class __Matmul___Node(NodeBase):
    """
    Same as a @ b."""
    
    title = '__matmul__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__matmul__(self.input(0), self.input(1)))
        

class __Mod___Node(NodeBase):
    """
    Same as a % b."""
    
    title = '__mod__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__mod__(self.input(0), self.input(1)))
        

class __Mul___Node(NodeBase):
    """
    Same as a * b."""
    
    title = '__mul__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__mul__(self.input(0), self.input(1)))
        

class __Ne___Node(NodeBase):
    """
    Same as a != b."""
    
    title = '__ne__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__ne__(self.input(0), self.input(1)))
        

class __Neg___Node(NodeBase):
    """
    Same as -a."""
    
    title = '__neg__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__neg__(self.input(0)))
        

class __Not___Node(NodeBase):
    """
    Same as not a."""
    
    title = '__not__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__not__(self.input(0)))
        

class __Or___Node(NodeBase):
    """
    Same as a | b."""
    
    title = '__or__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__or__(self.input(0), self.input(1)))
        

class __Pos___Node(NodeBase):
    """
    Same as +a."""
    
    title = '__pos__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__pos__(self.input(0)))
        

class __Pow___Node(NodeBase):
    """
    Same as a ** b."""
    
    title = '__pow__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__pow__(self.input(0), self.input(1)))
        

class __Rshift___Node(NodeBase):
    """
    Same as a >> b."""
    
    title = '__rshift__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__rshift__(self.input(0), self.input(1)))
        

class __Setitem___Node(NodeBase):
    """
    Same as a[b] = c."""
    
    title = '__setitem__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
        NodeInputBP(label='c'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__setitem__(self.input(0), self.input(1), self.input(2)))
        

class __Sub___Node(NodeBase):
    """
    Same as a - b."""
    
    title = '__sub__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__sub__(self.input(0), self.input(1)))
        

class __Truediv___Node(NodeBase):
    """
    Same as a / b."""
    
    title = '__truediv__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__truediv__(self.input(0), self.input(1)))
        

class __Xor___Node(NodeBase):
    """
    Same as a ^ b."""
    
    title = '__xor__'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.__xor__(self.input(0), self.input(1)))
        

class _Abs_Node(NodeBase):
    """
    Return the absolute value of the argument."""
    
    title = '_abs'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator._abs(self.input(0)))
        

class Abs_Node(NodeBase):
    """
    Same as abs(a)."""
    
    title = 'abs'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.abs(self.input(0)))
        

class Add_Node(NodeBase):
    """
    Same as a + b."""
    
    title = 'add'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.add(self.input(0), self.input(1)))
        

class And__Node(NodeBase):
    """
    Same as a & b."""
    
    title = 'and_'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.and_(self.input(0), self.input(1)))
        

class Concat_Node(NodeBase):
    """
    Same as a + b, for a and b sequences."""
    
    title = 'concat'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.concat(self.input(0), self.input(1)))
        

class Contains_Node(NodeBase):
    """
    Same as b in a (note reversed operands)."""
    
    title = 'contains'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.contains(self.input(0), self.input(1)))
        

class Countof_Node(NodeBase):
    """
    Return the number of times b occurs in a."""
    
    title = 'countOf'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.countOf(self.input(0), self.input(1)))
        

class Delitem_Node(NodeBase):
    """
    Same as del a[b]."""
    
    title = 'delitem'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.delitem(self.input(0), self.input(1)))
        

class Eq_Node(NodeBase):
    """
    Same as a == b."""
    
    title = 'eq'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.eq(self.input(0), self.input(1)))
        

class Floordiv_Node(NodeBase):
    """
    Same as a // b."""
    
    title = 'floordiv'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.floordiv(self.input(0), self.input(1)))
        

class Ge_Node(NodeBase):
    """
    Same as a >= b."""
    
    title = 'ge'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.ge(self.input(0), self.input(1)))
        

class Getitem_Node(NodeBase):
    """
    Same as a[b]."""
    
    title = 'getitem'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.getitem(self.input(0), self.input(1)))
        

class Gt_Node(NodeBase):
    """
    Same as a > b."""
    
    title = 'gt'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.gt(self.input(0), self.input(1)))
        

class Iadd_Node(NodeBase):
    """
    Same as a += b."""
    
    title = 'iadd'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.iadd(self.input(0), self.input(1)))
        

class Iand_Node(NodeBase):
    """
    Same as a &= b."""
    
    title = 'iand'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.iand(self.input(0), self.input(1)))
        

class Iconcat_Node(NodeBase):
    """
    Same as a += b, for a and b sequences."""
    
    title = 'iconcat'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.iconcat(self.input(0), self.input(1)))
        

class Ifloordiv_Node(NodeBase):
    """
    Same as a //= b."""
    
    title = 'ifloordiv'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.ifloordiv(self.input(0), self.input(1)))
        

class Ilshift_Node(NodeBase):
    """
    Same as a <<= b."""
    
    title = 'ilshift'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.ilshift(self.input(0), self.input(1)))
        

class Imatmul_Node(NodeBase):
    """
    Same as a @= b."""
    
    title = 'imatmul'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.imatmul(self.input(0), self.input(1)))
        

class Imod_Node(NodeBase):
    """
    Same as a %= b."""
    
    title = 'imod'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.imod(self.input(0), self.input(1)))
        

class Imul_Node(NodeBase):
    """
    Same as a *= b."""
    
    title = 'imul'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.imul(self.input(0), self.input(1)))
        

class Index_Node(NodeBase):
    """
    Same as a.__index__()"""
    
    title = 'index'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.index(self.input(0)))
        

class Indexof_Node(NodeBase):
    """
    Return the first index of b in a."""
    
    title = 'indexOf'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.indexOf(self.input(0), self.input(1)))
        

class Inv_Node(NodeBase):
    """
    Same as ~a."""
    
    title = 'inv'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.inv(self.input(0)))
        

class Invert_Node(NodeBase):
    """
    Same as ~a."""
    
    title = 'invert'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.invert(self.input(0)))
        

class Ior_Node(NodeBase):
    """
    Same as a |= b."""
    
    title = 'ior'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.ior(self.input(0), self.input(1)))
        

class Ipow_Node(NodeBase):
    """
    Same as a **= b."""
    
    title = 'ipow'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.ipow(self.input(0), self.input(1)))
        

class Irshift_Node(NodeBase):
    """
    Same as a >>= b."""
    
    title = 'irshift'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.irshift(self.input(0), self.input(1)))
        

class Is__Node(NodeBase):
    """
    Same as a is b."""
    
    title = 'is_'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.is_(self.input(0), self.input(1)))
        

class Is_Not_Node(NodeBase):
    """
    Same as a is not b."""
    
    title = 'is_not'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.is_not(self.input(0), self.input(1)))
        

class Isub_Node(NodeBase):
    """
    Same as a -= b."""
    
    title = 'isub'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.isub(self.input(0), self.input(1)))
        

class Itruediv_Node(NodeBase):
    """
    Same as a /= b."""
    
    title = 'itruediv'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.itruediv(self.input(0), self.input(1)))
        

class Ixor_Node(NodeBase):
    """
    Same as a ^= b."""
    
    title = 'ixor'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.ixor(self.input(0), self.input(1)))
        

class Le_Node(NodeBase):
    """
    Same as a <= b."""
    
    title = 'le'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.le(self.input(0), self.input(1)))
        

class Length_Hint_Node(NodeBase):
    """
    Return an estimate of the number of items in obj.

This is useful for presizing containers when building from an iterable.

If the object supports len(), the result will be exact.
Otherwise, it may over- or under-estimate by an arbitrary amount.
The result will be an integer >= 0."""
    
    title = 'length_hint'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='default', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.length_hint(self.input(0), self.input(1)))
        

class Lshift_Node(NodeBase):
    """
    Same as a << b."""
    
    title = 'lshift'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.lshift(self.input(0), self.input(1)))
        

class Lt_Node(NodeBase):
    """
    Same as a < b."""
    
    title = 'lt'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.lt(self.input(0), self.input(1)))
        

class Matmul_Node(NodeBase):
    """
    Same as a @ b."""
    
    title = 'matmul'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.matmul(self.input(0), self.input(1)))
        

class Mod_Node(NodeBase):
    """
    Same as a % b."""
    
    title = 'mod'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.mod(self.input(0), self.input(1)))
        

class Mul_Node(NodeBase):
    """
    Same as a * b."""
    
    title = 'mul'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.mul(self.input(0), self.input(1)))
        

class Ne_Node(NodeBase):
    """
    Same as a != b."""
    
    title = 'ne'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.ne(self.input(0), self.input(1)))
        

class Neg_Node(NodeBase):
    """
    Same as -a."""
    
    title = 'neg'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.neg(self.input(0)))
        

class Not__Node(NodeBase):
    """
    Same as not a."""
    
    title = 'not_'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.not_(self.input(0)))
        

class Or__Node(NodeBase):
    """
    Same as a | b."""
    
    title = 'or_'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.or_(self.input(0), self.input(1)))
        

class Pos_Node(NodeBase):
    """
    Same as +a."""
    
    title = 'pos'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.pos(self.input(0)))
        

class Pow_Node(NodeBase):
    """
    Same as a ** b."""
    
    title = 'pow'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.pow(self.input(0), self.input(1)))
        

class Rshift_Node(NodeBase):
    """
    Same as a >> b."""
    
    title = 'rshift'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.rshift(self.input(0), self.input(1)))
        

class Setitem_Node(NodeBase):
    """
    Same as a[b] = c."""
    
    title = 'setitem'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
        NodeInputBP(label='c'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.setitem(self.input(0), self.input(1), self.input(2)))
        

class Sub_Node(NodeBase):
    """
    Same as a - b."""
    
    title = 'sub'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.sub(self.input(0), self.input(1)))
        

class Truediv_Node(NodeBase):
    """
    Same as a / b."""
    
    title = 'truediv'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.truediv(self.input(0), self.input(1)))
        

class Truth_Node(NodeBase):
    """
    Return True if a is true, False otherwise."""
    
    title = 'truth'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.truth(self.input(0)))
        

class Xor_Node(NodeBase):
    """
    Same as a ^ b."""
    
    title = 'xor'
    type_ = 'operator'
    init_inputs = [
        NodeInputBP(label='a'),
        NodeInputBP(label='b'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, operator.xor(self.input(0), self.input(1)))
        


export_nodes(
    __Abs___Node,
    __Add___Node,
    __And___Node,
    __Concat___Node,
    __Contains___Node,
    __Delitem___Node,
    __Eq___Node,
    __Floordiv___Node,
    __Ge___Node,
    __Getitem___Node,
    __Gt___Node,
    __Iadd___Node,
    __Iand___Node,
    __Iconcat___Node,
    __Ifloordiv___Node,
    __Ilshift___Node,
    __Imatmul___Node,
    __Imod___Node,
    __Imul___Node,
    __Index___Node,
    __Inv___Node,
    __Invert___Node,
    __Ior___Node,
    __Ipow___Node,
    __Irshift___Node,
    __Isub___Node,
    __Itruediv___Node,
    __Ixor___Node,
    __Le___Node,
    __Lshift___Node,
    __Lt___Node,
    __Matmul___Node,
    __Mod___Node,
    __Mul___Node,
    __Ne___Node,
    __Neg___Node,
    __Not___Node,
    __Or___Node,
    __Pos___Node,
    __Pow___Node,
    __Rshift___Node,
    __Setitem___Node,
    __Sub___Node,
    __Truediv___Node,
    __Xor___Node,
    _Abs_Node,
    Abs_Node,
    Add_Node,
    And__Node,
    Concat_Node,
    Contains_Node,
    Countof_Node,
    Delitem_Node,
    Eq_Node,
    Floordiv_Node,
    Ge_Node,
    Getitem_Node,
    Gt_Node,
    Iadd_Node,
    Iand_Node,
    Iconcat_Node,
    Ifloordiv_Node,
    Ilshift_Node,
    Imatmul_Node,
    Imod_Node,
    Imul_Node,
    Index_Node,
    Indexof_Node,
    Inv_Node,
    Invert_Node,
    Ior_Node,
    Ipow_Node,
    Irshift_Node,
    Is__Node,
    Is_Not_Node,
    Isub_Node,
    Itruediv_Node,
    Ixor_Node,
    Le_Node,
    Length_Hint_Node,
    Lshift_Node,
    Lt_Node,
    Matmul_Node,
    Mod_Node,
    Mul_Node,
    Ne_Node,
    Neg_Node,
    Not__Node,
    Or__Node,
    Pos_Node,
    Pow_Node,
    Rshift_Node,
    Setitem_Node,
    Sub_Node,
    Truediv_Node,
    Truth_Node,
    Xor_Node,
)
