
from NENV import *

import ast


class NodeBase(Node):
    pass


class _Dims_Getter_Node(NodeBase):
    """
    Deprecated. Use elts instead."""
    
    title = '_dims_getter'
    type_ = 'ast'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast._dims_getter())
        

class _Dims_Setter_Node(NodeBase):
    """
    """
    
    title = '_dims_setter'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast._dims_setter(self.input(0)))
        

class _Getter_Node(NodeBase):
    """
    Deprecated. Use value instead."""
    
    title = '_getter'
    type_ = 'ast'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast._getter())
        

class _New_Node(NodeBase):
    """
    """
    
    title = '_new'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='cls'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast._new(self.input(0)))
        

class _Pad_Whitespace_Node(NodeBase):
    """
    Replace all chars except '\f\t' in a line with spaces."""
    
    title = '_pad_whitespace'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast._pad_whitespace(self.input(0)))
        

class _Setter_Node(NodeBase):
    """
    """
    
    title = '_setter'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast._setter(self.input(0)))
        

class _Splitlines_No_Ff_Node(NodeBase):
    """
    Split a string into lines ignoring form feed and other chars.

    This mimics how the Python parser splits source code.
    """
    
    title = '_splitlines_no_ff'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='source'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast._splitlines_no_ff(self.input(0)))
        

class Contextmanager_Node(NodeBase):
    """
    @contextmanager decorator.

    Typical usage:

        @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        with some_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
    """
    
    title = 'contextmanager'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.contextmanager(self.input(0)))
        

class Copy_Location_Node(NodeBase):
    """
    
    Copy source location (`lineno`, `col_offset`, `end_lineno`, and `end_col_offset`
    attributes) from *old_node* to *new_node* if possible, and return *new_node*.
    """
    
    title = 'copy_location'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='new_node'),
        NodeInputBP(label='old_node'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.copy_location(self.input(0), self.input(1)))
        

class Dump_Node(NodeBase):
    """
    
    Return a formatted dump of the tree in node.  This is mainly useful for
    debugging purposes.  If annotate_fields is true (by default),
    the returned string will show the names and the values for fields.
    If annotate_fields is false, the result string will be more compact by
    omitting unambiguous field names.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    include_attributes can be set to true.  If indent is a non-negative
    integer or string, then the tree will be pretty-printed with that indent
    level. None (the default) selects the single line representation.
    """
    
    title = 'dump'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node'),
        NodeInputBP(label='annotate_fields', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='include_attributes', dtype=dtypes.Data(default=False, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.dump(self.input(0), self.input(1), self.input(2)))
        

class Fix_Missing_Locations_Node(NodeBase):
    """
    
    When you compile a node tree with compile(), the compiler expects lineno and
    col_offset attributes for every node that supports them.  This is rather
    tedious to fill in for generated nodes, so this helper adds these attributes
    recursively where not already set, by setting them to the values of the
    parent node.  It works recursively starting at *node*.
    """
    
    title = 'fix_missing_locations'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.fix_missing_locations(self.input(0)))
        

class Get_Docstring_Node(NodeBase):
    """
    
    Return the docstring for the given node or None if no docstring can
    be found.  If the node provided does not have docstrings a TypeError
    will be raised.

    If *clean* is `True`, all tabs are expanded to spaces and any whitespace
    that can be uniformly removed from the second line onwards is removed.
    """
    
    title = 'get_docstring'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node'),
        NodeInputBP(label='clean', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.get_docstring(self.input(0), self.input(1)))
        

class Get_Source_Segment_Node(NodeBase):
    """
    Get source code segment of the *source* that generated *node*.

    If some location information (`lineno`, `end_lineno`, `col_offset`,
    or `end_col_offset`) is missing, return None.

    If *padded* is `True`, the first line of a multi-line statement will
    be padded with spaces to match its original position.
    """
    
    title = 'get_source_segment'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='node'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.get_source_segment(self.input(0), self.input(1)))
        

class Increment_Lineno_Node(NodeBase):
    """
    
    Increment the line number and end line number of each node in the tree
    starting at *node* by *n*. This is useful to "move code" to a different
    location in a file.
    """
    
    title = 'increment_lineno'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node'),
        NodeInputBP(label='n', dtype=dtypes.Data(default=1, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.increment_lineno(self.input(0), self.input(1)))
        

class Iter_Child_Nodes_Node(NodeBase):
    """
    
    Yield all direct child nodes of *node*, that is, all fields that are nodes
    and all items of fields that are lists of nodes.
    """
    
    title = 'iter_child_nodes'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.iter_child_nodes(self.input(0)))
        

class Iter_Fields_Node(NodeBase):
    """
    
    Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
    that is present on *node*.
    """
    
    title = 'iter_fields'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.iter_fields(self.input(0)))
        

class Literal_Eval_Node(NodeBase):
    """
    
    Safely evaluate an expression node or a string containing a Python
    expression.  The string or node provided may only consist of the following
    Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
    sets, booleans, and None.
    """
    
    title = 'literal_eval'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node_or_string'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.literal_eval(self.input(0)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'ast'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.main())
        

class Parse_Node(NodeBase):
    """
    
    Parse the source into an AST node.
    Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
    Pass type_comments=True to get back type comments where the syntax allows.
    """
    
    title = 'parse'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='filename', dtype=dtypes.Data(default='<unknown>', size='s')),
        NodeInputBP(label='mode', dtype=dtypes.Data(default='exec', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.parse(self.input(0), self.input(1), self.input(2)))
        

class Unparse_Node(NodeBase):
    """
    """
    
    title = 'unparse'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='ast_obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.unparse(self.input(0)))
        

class Walk_Node(NodeBase):
    """
    
    Recursively yield all descendant nodes in the tree starting at *node*
    (including *node* itself), in no specified order.  This is useful if you
    only want to modify nodes in place and don't care about the context.
    """
    
    title = 'walk'
    type_ = 'ast'
    init_inputs = [
        NodeInputBP(label='node'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, ast.walk(self.input(0)))
        


export_nodes(
    _Dims_Getter_Node,
    _Dims_Setter_Node,
    _Getter_Node,
    _New_Node,
    _Pad_Whitespace_Node,
    _Setter_Node,
    _Splitlines_No_Ff_Node,
    Contextmanager_Node,
    Copy_Location_Node,
    Dump_Node,
    Fix_Missing_Locations_Node,
    Get_Docstring_Node,
    Get_Source_Segment_Node,
    Increment_Lineno_Node,
    Iter_Child_Nodes_Node,
    Iter_Fields_Node,
    Literal_Eval_Node,
    Main_Node,
    Parse_Node,
    Unparse_Node,
    Walk_Node,
)
