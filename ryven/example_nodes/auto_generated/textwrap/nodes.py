
from ryven.NENV import *

import textwrap


class NodeBase(Node):
    pass


class Dedent_Node(NodeBase):
    """
    Remove any common leading whitespace from every line in `text`.

    This can be used to make triple-quoted strings line up with the left
    edge of the display, while still presenting them in the source code
    in indented form.

    Note that tabs and spaces are both treated as whitespace, but they
    are not equal: the lines "  hello" and "\thello" are
    considered to have no common leading whitespace.

    Entirely blank lines are normalized to a newline character.
    """
    
    title = 'dedent'
    type_ = 'textwrap'
    init_inputs = [
        NodeInputBP(label='text'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, textwrap.dedent(self.input(0)))
        

class Fill_Node(NodeBase):
    """
    Fill a single paragraph of text, returning a new string.

    Reformat the single paragraph in 'text' to fit in lines of no more
    than 'width' columns, and return a new string containing the entire
    wrapped paragraph.  As with wrap(), tabs are expanded and other
    whitespace characters converted to space.  See TextWrapper class for
    available keyword args to customize wrapping behaviour.
    """
    
    title = 'fill'
    type_ = 'textwrap'
    init_inputs = [
        NodeInputBP(label='text'),
        NodeInputBP(label='width', dtype=dtypes.Data(default=70, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, textwrap.fill(self.input(0), self.input(1)))
        

class Indent_Node(NodeBase):
    """
    Adds 'prefix' to the beginning of selected lines in 'text'.

    If 'predicate' is provided, 'prefix' will only be added to the lines
    where 'predicate(line)' is True. If 'predicate' is not provided,
    it will default to adding 'prefix' to all non-empty lines that do not
    consist solely of whitespace characters.
    """
    
    title = 'indent'
    type_ = 'textwrap'
    init_inputs = [
        NodeInputBP(label='text'),
        NodeInputBP(label='prefix'),
        NodeInputBP(label='predicate', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, textwrap.indent(self.input(0), self.input(1), self.input(2)))
        

class Shorten_Node(NodeBase):
    """
    Collapse and truncate the given text to fit in the given width.

    The text first has its whitespace collapsed.  If it then fits in
    the *width*, it is returned as is.  Otherwise, as many words
    as possible are joined and then the placeholder is appended::

        >>> textwrap.shorten("Hello  world!", width=12)
        'Hello world!'
        >>> textwrap.shorten("Hello  world!", width=11)
        'Hello [...]'
    """
    
    title = 'shorten'
    type_ = 'textwrap'
    init_inputs = [
        NodeInputBP(label='text'),
        NodeInputBP(label='width'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, textwrap.shorten(self.input(0), self.input(1)))
        

class Wrap_Node(NodeBase):
    """
    Wrap a single paragraph of text, returning a list of wrapped lines.

    Reformat the single paragraph in 'text' so it fits in lines of no
    more than 'width' columns, and return a list of wrapped lines.  By
    default, tabs in 'text' are expanded with string.expandtabs(), and
    all other whitespace characters (including newline) are converted to
    space.  See TextWrapper class for available keyword args to customize
    wrapping behaviour.
    """
    
    title = 'wrap'
    type_ = 'textwrap'
    init_inputs = [
        NodeInputBP(label='text'),
        NodeInputBP(label='width', dtype=dtypes.Data(default=70, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, textwrap.wrap(self.input(0), self.input(1)))
        


export_nodes(
    Dedent_Node,
    Fill_Node,
    Indent_Node,
    Shorten_Node,
    Wrap_Node,
)
