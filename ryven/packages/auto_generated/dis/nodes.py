
from NENV import *

import dis


class NodeBase(Node):
    pass


class _Disassemble_Bytes_Node(NodeBase):
    """
    """
    
    title = '_disassemble_bytes'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='lasti', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='varnames', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='names', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='constants', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='cells', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='linestarts', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._disassemble_bytes(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class _Disassemble_Recursive_Node(NodeBase):
    """
    """
    
    title = '_disassemble_recursive'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='co'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._disassemble_recursive(self.input(0)))
        

class _Disassemble_Str_Node(NodeBase):
    """
    Compile the source string, then disassemble the code object."""
    
    title = '_disassemble_str'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._disassemble_str(self.input(0)))
        

class _Format_Code_Info_Node(NodeBase):
    """
    """
    
    title = '_format_code_info'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='co'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._format_code_info(self.input(0)))
        

class _Get_Code_Object_Node(NodeBase):
    """
    Helper to handle methods, compiled or raw code objects, and strings."""
    
    title = '_get_code_object'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._get_code_object(self.input(0)))
        

class _Get_Const_Info_Node(NodeBase):
    """
    Helper to get optional details about const references

       Returns the dereferenced constant and its repr if the constant
       list is defined.
       Otherwise returns the constant index and its repr().
    """
    
    title = '_get_const_info'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='const_index'),
        NodeInputBP(label='const_list'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._get_const_info(self.input(0), self.input(1)))
        

class _Get_Instructions_Bytes_Node(NodeBase):
    """
    Iterate over the instructions in a bytecode string.

    Generates a sequence of Instruction namedtuples giving the details of each
    opcode.  Additional information about the code's runtime environment
    (e.g. variable names, constants) can be specified using optional
    arguments.

    """
    
    title = '_get_instructions_bytes'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='code'),
        NodeInputBP(label='varnames', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='names', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='constants', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='cells', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='linestarts', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='line_offset', dtype=dtypes.Data(default=0, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._get_instructions_bytes(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        

class _Get_Name_Info_Node(NodeBase):
    """
    Helper to get optional details about named references

       Returns the dereferenced name as both value and repr if the name
       list is defined.
       Otherwise returns the name index and its repr().
    """
    
    title = '_get_name_info'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='name_index'),
        NodeInputBP(label='name_list'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._get_name_info(self.input(0), self.input(1)))
        

class _Test_Node(NodeBase):
    """
    Simple test program to disassemble a file."""
    
    title = '_test'
    type_ = 'dis'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._test())
        

class _Try_Compile_Node(NodeBase):
    """
    Attempts to compile the given source, first as an expression and
       then as a statement if the first approach fails.

       Utility function to accept strings in functions that otherwise
       expect code objects
    """
    
    title = '_try_compile'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._try_compile(self.input(0), self.input(1)))
        

class _Unpack_Opargs_Node(NodeBase):
    """
    """
    
    title = '_unpack_opargs'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis._unpack_opargs(self.input(0)))
        

class Code_Info_Node(NodeBase):
    """
    Formatted details of methods, functions, or code."""
    
    title = 'code_info'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.code_info(self.input(0)))
        

class Dis_Node(NodeBase):
    """
    Disassemble classes, methods, functions, and other compiled objects.

    With no argument, disassemble the last traceback.

    Compiled objects currently include generator objects, async generator
    objects, and coroutine objects, all of which store their code object
    in a special attribute.
    """
    
    title = 'dis'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='x', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.dis(self.input(0)))
        

class Disassemble_Node(NodeBase):
    """
    Disassemble a code object."""
    
    title = 'disassemble'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='co'),
        NodeInputBP(label='lasti', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.disassemble(self.input(0), self.input(1)))
        

class Disco_Node(NodeBase):
    """
    Disassemble a code object."""
    
    title = 'disco'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='co'),
        NodeInputBP(label='lasti', dtype=dtypes.Data(default=-1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.disco(self.input(0), self.input(1)))
        

class Distb_Node(NodeBase):
    """
    Disassemble a traceback (default: last traceback)."""
    
    title = 'distb'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='tb', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.distb(self.input(0)))
        

class Findlabels_Node(NodeBase):
    """
    Detect all offsets in a byte code which are jump targets.

    Return the list of offsets.

    """
    
    title = 'findlabels'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.findlabels(self.input(0)))
        

class Findlinestarts_Node(NodeBase):
    """
    Find the offsets in a byte code which are start of lines in the source.

    Generate pairs (offset, lineno) as described in Python/compile.c.

    """
    
    title = 'findlinestarts'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='code'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.findlinestarts(self.input(0)))
        

class Get_Instructions_Node(NodeBase):
    """
    Iterator for the opcodes in methods, functions or code

    Generates a series of Instruction named tuples giving the details of
    each operations in the supplied code.

    If *first_line* is not None, it indicates the line number that should
    be reported for the first source line in the disassembled code.
    Otherwise, the source line information (if any) is taken directly from
    the disassembled code object.
    """
    
    title = 'get_instructions'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.get_instructions(self.input(0)))
        

class Pretty_Flags_Node(NodeBase):
    """
    Return pretty representation of code flags."""
    
    title = 'pretty_flags'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='flags'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.pretty_flags(self.input(0)))
        

class Show_Code_Node(NodeBase):
    """
    Print details of methods, functions, or code to *file*.

    If *file* is not provided, the output is printed on stdout.
    """
    
    title = 'show_code'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='co'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.show_code(self.input(0)))
        

class Stack_Effect_Node(NodeBase):
    """
    Compute the stack effect of the opcode."""
    
    title = 'stack_effect'
    type_ = 'dis'
    init_inputs = [
        NodeInputBP(label='opcode'),
        NodeInputBP(label='oparg', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, dis.stack_effect(self.input(0), self.input(1)))
        


export_nodes(
    _Disassemble_Bytes_Node,
    _Disassemble_Recursive_Node,
    _Disassemble_Str_Node,
    _Format_Code_Info_Node,
    _Get_Code_Object_Node,
    _Get_Const_Info_Node,
    _Get_Instructions_Bytes_Node,
    _Get_Name_Info_Node,
    _Test_Node,
    _Try_Compile_Node,
    _Unpack_Opargs_Node,
    Code_Info_Node,
    Dis_Node,
    Disassemble_Node,
    Disco_Node,
    Distb_Node,
    Findlabels_Node,
    Findlinestarts_Node,
    Get_Instructions_Node,
    Pretty_Flags_Node,
    Show_Code_Node,
    Stack_Effect_Node,
)
