import ryvencore_qt as rc
import dis


class AutoNode_dis__disassemble_bytes(rc.Node):
    title = '_disassemble_bytes'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='lasti'),
rc.NodeInputBP(label='varnames'),
rc.NodeInputBP(label='names'),
rc.NodeInputBP(label='constants'),
rc.NodeInputBP(label='cells'),
rc.NodeInputBP(label='linestarts'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._disassemble_bytes(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        


class AutoNode_dis__disassemble_recursive(rc.Node):
    title = '_disassemble_recursive'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='co'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._disassemble_recursive(self.input(0)))
        


class AutoNode_dis__disassemble_str(rc.Node):
    title = '_disassemble_str'
    description = '''Compile the source string, then disassemble the code object.'''
    init_inputs = [
        rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._disassemble_str(self.input(0)))
        


class AutoNode_dis__format_code_info(rc.Node):
    title = '_format_code_info'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='co'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._format_code_info(self.input(0)))
        


class AutoNode_dis__get_code_object(rc.Node):
    title = '_get_code_object'
    description = '''Helper to handle methods, compiled or raw code objects, and strings.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._get_code_object(self.input(0)))
        


class AutoNode_dis__get_const_info(rc.Node):
    title = '_get_const_info'
    description = '''Helper to get optional details about const references

       Returns the dereferenced constant and its repr if the constant
       list is defined.
       Otherwise returns the constant index and its repr().
    '''
    init_inputs = [
        rc.NodeInputBP(label='const_index'),
rc.NodeInputBP(label='const_list'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._get_const_info(self.input(0), self.input(1)))
        


class AutoNode_dis__get_instructions_bytes(rc.Node):
    title = '_get_instructions_bytes'
    description = '''Iterate over the instructions in a bytecode string.

    Generates a sequence of Instruction namedtuples giving the details of each
    opcode.  Additional information about the code's runtime environment
    (e.g. variable names, constants) can be specified using optional
    arguments.

    '''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='varnames'),
rc.NodeInputBP(label='names'),
rc.NodeInputBP(label='constants'),
rc.NodeInputBP(label='cells'),
rc.NodeInputBP(label='linestarts'),
rc.NodeInputBP(label='line_offset'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._get_instructions_bytes(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6)))
        


class AutoNode_dis__get_name_info(rc.Node):
    title = '_get_name_info'
    description = '''Helper to get optional details about named references

       Returns the dereferenced name as both value and repr if the name
       list is defined.
       Otherwise returns the name index and its repr().
    '''
    init_inputs = [
        rc.NodeInputBP(label='name_index'),
rc.NodeInputBP(label='name_list'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._get_name_info(self.input(0), self.input(1)))
        


class AutoNode_dis__test(rc.Node):
    title = '_test'
    description = '''Simple test program to disassemble a file.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._test())
        


class AutoNode_dis__try_compile(rc.Node):
    title = '_try_compile'
    description = '''Attempts to compile the given source, first as an expression and
       then as a statement if the first approach fails.

       Utility function to accept strings in functions that otherwise
       expect code objects
    '''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._try_compile(self.input(0), self.input(1)))
        


class AutoNode_dis__unpack_opargs(rc.Node):
    title = '_unpack_opargs'
    description = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis._unpack_opargs(self.input(0)))
        


class AutoNode_dis_code_info(rc.Node):
    title = 'code_info'
    description = '''Formatted details of methods, functions, or code.'''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.code_info(self.input(0)))
        


class AutoNode_dis_dis(rc.Node):
    title = 'dis'
    description = '''Disassemble classes, methods, functions, and other compiled objects.

    With no argument, disassemble the last traceback.

    Compiled objects currently include generator objects, async generator
    objects, and coroutine objects, all of which store their code object
    in a special attribute.
    '''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.dis(self.input(0)))
        


class AutoNode_dis_disassemble(rc.Node):
    title = 'disassemble'
    description = '''Disassemble a code object.'''
    init_inputs = [
        rc.NodeInputBP(label='co'),
rc.NodeInputBP(label='lasti'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.disassemble(self.input(0), self.input(1)))
        


class AutoNode_dis_disco(rc.Node):
    title = 'disco'
    description = '''Disassemble a code object.'''
    init_inputs = [
        rc.NodeInputBP(label='co'),
rc.NodeInputBP(label='lasti'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.disco(self.input(0), self.input(1)))
        


class AutoNode_dis_distb(rc.Node):
    title = 'distb'
    description = '''Disassemble a traceback (default: last traceback).'''
    init_inputs = [
        rc.NodeInputBP(label='tb'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.distb(self.input(0)))
        


class AutoNode_dis_findlabels(rc.Node):
    title = 'findlabels'
    description = '''Detect all offsets in a byte code which are jump targets.

    Return the list of offsets.

    '''
    init_inputs = [
        rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.findlabels(self.input(0)))
        


class AutoNode_dis_findlinestarts(rc.Node):
    title = 'findlinestarts'
    description = '''Find the offsets in a byte code which are start of lines in the source.

    Generate pairs (offset, lineno) as described in Python/compile.c.

    '''
    init_inputs = [
        rc.NodeInputBP(label='code'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.findlinestarts(self.input(0)))
        


class AutoNode_dis_get_instructions(rc.Node):
    title = 'get_instructions'
    description = '''Iterator for the opcodes in methods, functions or code

    Generates a series of Instruction named tuples giving the details of
    each operations in the supplied code.

    If *first_line* is not None, it indicates the line number that should
    be reported for the first source line in the disassembled code.
    Otherwise, the source line information (if any) is taken directly from
    the disassembled code object.
    '''
    init_inputs = [
        rc.NodeInputBP(label='x'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.get_instructions(self.input(0)))
        


class AutoNode_dis_pretty_flags(rc.Node):
    title = 'pretty_flags'
    description = '''Return pretty representation of code flags.'''
    init_inputs = [
        rc.NodeInputBP(label='flags'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.pretty_flags(self.input(0)))
        


class AutoNode_dis_show_code(rc.Node):
    title = 'show_code'
    description = '''Print details of methods, functions, or code to *file*.

    If *file* is not provided, the output is printed on stdout.
    '''
    init_inputs = [
        rc.NodeInputBP(label='co'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.show_code(self.input(0)))
        


class AutoNode_dis_stack_effect(rc.Node):
    title = 'stack_effect'
    description = '''Compute the stack effect of the opcode.'''
    init_inputs = [
        rc.NodeInputBP(label='opcode'),
rc.NodeInputBP(label='oparg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, dis.stack_effect(self.input(0), self.input(1)))
        