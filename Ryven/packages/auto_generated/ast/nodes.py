import ryvencore_qt as rc
import ast


class AutoNode_ast__getter(rc.Node):
    title = '_getter'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast._getter(self.input(0)))
        


class AutoNode_ast__new(rc.Node):
    title = '_new'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='cls'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast._new(self.input(0)))
        


class AutoNode_ast__pad_whitespace(rc.Node):
    title = '_pad_whitespace'
    doc = '''Replace all chars except '\f\t' in a line with spaces.'''
    init_inputs = [
        rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast._pad_whitespace(self.input(0)))
        


class AutoNode_ast__setter(rc.Node):
    title = '_setter'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='self'),
rc.NodeInputBP(label='value'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast._setter(self.input(0), self.input(1)))
        


class AutoNode_ast__splitlines_no_ff(rc.Node):
    title = '_splitlines_no_ff'
    doc = '''Split a string into lines ignoring form feed and other chars.

    This mimics how the Python parser splits source code.
    '''
    init_inputs = [
        rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast._splitlines_no_ff(self.input(0)))
        


class AutoNode_ast_copy_location(rc.Node):
    title = 'copy_location'
    doc = '''
    Copy source location (`lineno`, `col_offset`, `end_lineno`, and `end_col_offset`
    attributes) from *old_node* to *new_node* if possible, and return *new_node*.
    '''
    init_inputs = [
        rc.NodeInputBP(label='new_node'),
rc.NodeInputBP(label='old_node'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.copy_location(self.input(0), self.input(1)))
        


class AutoNode_ast_dump(rc.Node):
    title = 'dump'
    doc = '''
    Return a formatted dump of the tree in node.  This is mainly useful for
    debugging purposes.  If annotate_fields is true (by default),
    the returned string will show the names and the values for fields.
    If annotate_fields is false, the result string will be more compact by
    omitting unambiguous field names.  Attributes such as line
    numbers and column offsets are not dumped by default.  If this is wanted,
    include_attributes can be set to true.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node'),
rc.NodeInputBP(label='annotate_fields'),
rc.NodeInputBP(label='include_attributes'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.dump(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_ast_fix_missing_locations(rc.Node):
    title = 'fix_missing_locations'
    doc = '''
    When you compile a node tree with compile(), the compiler expects lineno and
    col_offset attributes for every node that supports them.  This is rather
    tedious to fill in for generated nodes, so this helper adds these attributes
    recursively where not already set, by setting them to the values of the
    parent node.  It works recursively starting at *node*.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.fix_missing_locations(self.input(0)))
        


class AutoNode_ast_get_docstring(rc.Node):
    title = 'get_docstring'
    doc = '''
    Return the docstring for the given node or None if no docstring can
    be found.  If the node provided does not have docstrings a TypeError
    will be raised.

    If *clean* is `True`, all tabs are expanded to spaces and any whitespace
    that can be uniformly removed from the second line onwards is removed.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node'),
rc.NodeInputBP(label='clean'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.get_docstring(self.input(0), self.input(1)))
        


class AutoNode_ast_get_source_segment(rc.Node):
    title = 'get_source_segment'
    doc = '''Get source code segment of the *source* that generated *node*.

    If some location information (`lineno`, `end_lineno`, `col_offset`,
    or `end_col_offset`) is missing, return None.

    If *padded* is `True`, the first line of a multi-line statement will
    be padded with spaces to match its original position.
    '''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='node'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.get_source_segment(self.input(0), self.input(1)))
        


class AutoNode_ast_increment_lineno(rc.Node):
    title = 'increment_lineno'
    doc = '''
    Increment the line number and end line number of each node in the tree
    starting at *node* by *n*. This is useful to "move code" to a different
    location in a file.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node'),
rc.NodeInputBP(label='n'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.increment_lineno(self.input(0), self.input(1)))
        


class AutoNode_ast_iter_child_nodes(rc.Node):
    title = 'iter_child_nodes'
    doc = '''
    Yield all direct child nodes of *node*, that is, all fields that are nodes
    and all items of fields that are lists of nodes.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.iter_child_nodes(self.input(0)))
        


class AutoNode_ast_iter_fields(rc.Node):
    title = 'iter_fields'
    doc = '''
    Yield a tuple of ``(fieldname, value)`` for each field in ``node._fields``
    that is present on *node*.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.iter_fields(self.input(0)))
        


class AutoNode_ast_literal_eval(rc.Node):
    title = 'literal_eval'
    doc = '''
    Safely evaluate an expression node or a string containing a Python
    expression.  The string or node provided may only consist of the following
    Python literal structures: strings, bytes, numbers, tuples, lists, dicts,
    sets, booleans, and None.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node_or_string'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.literal_eval(self.input(0)))
        


class AutoNode_ast_parse(rc.Node):
    title = 'parse'
    doc = '''
    Parse the source into an AST node.
    Equivalent to compile(source, filename, mode, PyCF_ONLY_AST).
    Pass type_comments=True to get back type comments where the syntax allows.
    '''
    init_inputs = [
        rc.NodeInputBP(label='source'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='mode'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.parse(self.input(0), self.input(1), self.input(2)))
        


class AutoNode_ast_walk(rc.Node):
    title = 'walk'
    doc = '''
    Recursively yield all descendant nodes in the tree starting at *node*
    (including *node* itself), in no specified order.  This is useful if you
    only want to modify nodes in place and don't care about the context.
    '''
    init_inputs = [
        rc.NodeInputBP(label='node'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, ast.walk(self.input(0)))
        