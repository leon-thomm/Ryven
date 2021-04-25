
from NENV import *

import builtins


class NodeBase(Node):
    pass


class AutoNode_builtins_abs(NodeBase):
    title = 'abs'
    type_ = 'builtins'
    doc = """Return the absolute value of the argument."""
    init_inputs = [
        NodeInputBP(label='x'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.abs(self.input(0)))
        

class AutoNode_builtins_all(NodeBase):
    title = 'all'
    type_ = 'builtins'
    doc = """Return True if bool(x) is True for all values x in the iterable.

If the iterable is empty, return True."""
    init_inputs = [
        NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.all(self.input(0)))
        

class AutoNode_builtins_any(NodeBase):
    title = 'any'
    type_ = 'builtins'
    doc = """Return True if bool(x) is True for any x in the iterable.

If the iterable is empty, return False."""
    init_inputs = [
        NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.any(self.input(0)))
        

class AutoNode_builtins_ascii(NodeBase):
    title = 'ascii'
    type_ = 'builtins'
    doc = """Return an ASCII-only representation of an object.

As repr(), return a string containing a printable representation of an
object, but escape the non-ASCII characters in the string returned by
repr() using \\x, \\u or \\U escapes. This generates a string similar
to that returned by repr() in Python 2."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.ascii(self.input(0)))
        

class AutoNode_builtins_bin(NodeBase):
    title = 'bin'
    type_ = 'builtins'
    doc = """Return the binary representation of an integer.

   >>> bin(2796202)
   '0b1010101010101010101010'"""
    init_inputs = [
        NodeInputBP(label='number'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.bin(self.input(0)))
        

class AutoNode_builtins_callable(NodeBase):
    title = 'callable'
    type_ = 'builtins'
    doc = """Return whether the object is callable (i.e., some kind of function).

Note that classes are callable, as are instances of classes with a
__call__() method."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.callable(self.input(0)))
        

class AutoNode_builtins_chr(NodeBase):
    title = 'chr'
    type_ = 'builtins'
    doc = """Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff."""
    init_inputs = [
        NodeInputBP(label='i'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.chr(self.input(0)))
        

class AutoNode_builtins_compile(NodeBase):
    title = 'compile'
    type_ = 'builtins'
    doc = """Compile source into a code object that can be executed by exec() or eval().

The source code may represent a Python module, statement or expression.
The filename will be used for run-time error messages.
The mode must be 'exec' to compile a module, 'single' to compile a
single (interactive) statement, or 'eval' to compile an expression.
The flags argument, if present, controls which future statements influence
the compilation of the code.
The dont_inherit argument, if true, stops the compilation inheriting
the effects of any future statements in effect in the code calling
compile; if absent or false these statements do influence the compilation,
in addition to any features explicitly specified."""
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='filename'),
        NodeInputBP(label='mode'),
        NodeInputBP(label='flags'),
        NodeInputBP(label='dont_inherit'),
        NodeInputBP(label='optimize'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.compile(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        

class AutoNode_builtins_delattr(NodeBase):
    title = 'delattr'
    type_ = 'builtins'
    doc = """Deletes the named attribute from the given object.

delattr(x, 'y') is equivalent to ``del x.y''"""
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.delattr(self.input(0), self.input(1)))
        

class AutoNode_builtins_divmod(NodeBase):
    title = 'divmod'
    type_ = 'builtins'
    doc = """Return the tuple (x//y, x%y).  Invariant: div*y + mod == x."""
    init_inputs = [
        NodeInputBP(label='x'),
        NodeInputBP(label='y'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.divmod(self.input(0), self.input(1)))
        

class AutoNode_builtins_eval(NodeBase):
    title = 'eval'
    type_ = 'builtins'
    doc = """Evaluate the given source in the context of globals and locals.

The source may be a string representing a Python expression
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it."""
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='globals'),
        NodeInputBP(label='locals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.eval(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_builtins_exec(NodeBase):
    title = 'exec'
    type_ = 'builtins'
    doc = """Execute the given source in the context of globals and locals.

The source may be a string representing one or more Python statements
or a code object as returned by compile().
The globals must be a dictionary and locals can be any mapping,
defaulting to the current globals and locals.
If only globals is given, locals defaults to it."""
    init_inputs = [
        NodeInputBP(label='source'),
        NodeInputBP(label='globals'),
        NodeInputBP(label='locals'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.exec(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_builtins_format(NodeBase):
    title = 'format'
    type_ = 'builtins'
    doc = """Return value.__format__(format_spec)

format_spec defaults to the empty string.
See the Format Specification Mini-Language section of help('FORMATTING') for
details."""
    init_inputs = [
        NodeInputBP(label='value'),
        NodeInputBP(label='format_spec'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.format(self.input(0), self.input(1)))
        

class AutoNode_builtins_globals(NodeBase):
    title = 'globals'
    type_ = 'builtins'
    doc = """Return the dictionary containing the current scope's global variables.

NOTE: Updates to this dictionary *will* affect name lookups in the current
global scope and vice-versa."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.globals())
        

class AutoNode_builtins_hasattr(NodeBase):
    title = 'hasattr'
    type_ = 'builtins'
    doc = """Return whether the object has an attribute with the given name.

This is done by calling getattr(obj, name) and catching AttributeError."""
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.hasattr(self.input(0), self.input(1)))
        

class AutoNode_builtins_hash(NodeBase):
    title = 'hash'
    type_ = 'builtins'
    doc = """Return the hash value for the given object.

Two objects that compare equal must also have the same hash value, but the
reverse is not necessarily true."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.hash(self.input(0)))
        

class AutoNode_builtins_hex(NodeBase):
    title = 'hex'
    type_ = 'builtins'
    doc = """Return the hexadecimal representation of an integer.

   >>> hex(12648430)
   '0xc0ffee'"""
    init_inputs = [
        NodeInputBP(label='number'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.hex(self.input(0)))
        

class AutoNode_builtins_id(NodeBase):
    title = 'id'
    type_ = 'builtins'
    doc = """Return the identity of an object.

This is guaranteed to be unique among simultaneously existing objects.
(CPython uses the object's memory address.)"""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.id(self.input(0)))
        

class AutoNode_builtins_input(NodeBase):
    title = 'input'
    type_ = 'builtins'
    doc = """Read a string from standard input.  The trailing newline is stripped.

The prompt string, if given, is printed to standard output without a
trailing newline before reading input.

If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
On *nix systems, readline is used if available."""
    init_inputs = [
        NodeInputBP(label='prompt'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.input(self.input(0)))
        

class AutoNode_builtins_isinstance(NodeBase):
    title = 'isinstance'
    type_ = 'builtins'
    doc = """Return whether an object is an instance of a class or of a subclass thereof.

A tuple, as in ``isinstance(x, (A, B, ...))``, may be given as the target to
check against. This is equivalent to ``isinstance(x, A) or isinstance(x, B)
or ...`` etc."""
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='class_or_tuple'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.isinstance(self.input(0), self.input(1)))
        

class AutoNode_builtins_issubclass(NodeBase):
    title = 'issubclass'
    type_ = 'builtins'
    doc = """Return whether 'cls' is a derived from another class or is the same class.

A tuple, as in ``issubclass(x, (A, B, ...))``, may be given as the target to
check against. This is equivalent to ``issubclass(x, A) or issubclass(x, B)
or ...`` etc."""
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='class_or_tuple'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.issubclass(self.input(0), self.input(1)))
        

class AutoNode_builtins_len(NodeBase):
    title = 'len'
    type_ = 'builtins'
    doc = """Return the number of items in a container."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.len(self.input(0)))
        

class AutoNode_builtins_locals(NodeBase):
    title = 'locals'
    type_ = 'builtins'
    doc = """Return a dictionary containing the current scope's local variables.

NOTE: Whether or not updates to this dictionary will affect name lookups in
the local scope and vice-versa is *implementation dependent* and not
covered by any backwards compatibility guarantees."""
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.locals())
        

class AutoNode_builtins_oct(NodeBase):
    title = 'oct'
    type_ = 'builtins'
    doc = """Return the octal representation of an integer.

   >>> oct(342391)
   '0o1234567'"""
    init_inputs = [
        NodeInputBP(label='number'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.oct(self.input(0)))
        

class AutoNode_builtins_open(NodeBase):
    title = 'open'
    type_ = 'builtins'
    doc = """Open file and return a stream.  Raise OSError upon failure.

file is either a text or byte string giving the name (and the path
if the file isn't in the current working directory) of the file to
be opened or an integer file descriptor of the file to be
wrapped. (If a file descriptor is given, it is closed when the
returned I/O object is closed, unless closefd is set to False.)

mode is an optional string that specifies the mode in which the file
is opened. It defaults to 'r' which means open for reading in text
mode.  Other common values are 'w' for writing (truncating the file if
it already exists), 'x' for creating and writing to a new file, and
'a' for appending (which on some Unix systems, means that all writes
append to the end of the file regardless of the current seek position).
In text mode, if encoding is not specified the encoding used is platform
dependent: locale.getpreferredencoding(False) is called to get the
current locale encoding. (For reading and writing raw bytes use binary
mode and leave encoding unspecified.) The available modes are:

========= ===============================================================
Character Meaning
--------- ---------------------------------------------------------------
'r'       open for reading (default)
'w'       open for writing, truncating the file first
'x'       create a new file and open it for writing
'a'       open for writing, appending to the end of the file if it exists
'b'       binary mode
't'       text mode (default)
'+'       open a disk file for updating (reading and writing)
'U'       universal newline mode (deprecated)
========= ===============================================================

The default mode is 'rt' (open for reading text). For binary random
access, the mode 'w+b' opens and truncates the file to 0 bytes, while
'r+b' opens the file without truncation. The 'x' mode implies 'w' and
raises an `FileExistsError` if the file already exists.

Python distinguishes between files opened in binary and text modes,
even when the underlying operating system doesn't. Files opened in
binary mode (appending 'b' to the mode argument) return contents as
bytes objects without any decoding. In text mode (the default, or when
't' is appended to the mode argument), the contents of the file are
returned as strings, the bytes having been first decoded using a
platform-dependent encoding or using the specified encoding if given.

'U' mode is deprecated and will raise an exception in future versions
of Python.  It has no effect in Python 3.  Use newline to control
universal newlines mode.

buffering is an optional integer used to set the buffering policy.
Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
line buffering (only usable in text mode), and an integer > 1 to indicate
the size of a fixed-size chunk buffer.  When no buffering argument is
given, the default buffering policy works as follows:

* Binary files are buffered in fixed-size chunks; the size of the buffer
  is chosen using a heuristic trying to determine the underlying device's
  "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
  On many systems, the buffer will typically be 4096 or 8192 bytes long.

* "Interactive" text files (files for which isatty() returns True)
  use line buffering.  Other text files use the policy described above
  for binary files.

encoding is the name of the encoding used to decode or encode the
file. This should only be used in text mode. The default encoding is
platform dependent, but any encoding supported by Python can be
passed.  See the codecs module for the list of supported encodings.

errors is an optional string that specifies how encoding errors are to
be handled---this argument should not be used in binary mode. Pass
'strict' to raise a ValueError exception if there is an encoding error
(the default of None has the same effect), or pass 'ignore' to ignore
errors. (Note that ignoring encoding errors can lead to data loss.)
See the documentation for codecs.register or run 'help(codecs.Codec)'
for a list of the permitted encoding error strings.

newline controls how universal newlines works (it only applies to text
mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
follows:

* On input, if newline is None, universal newlines mode is
  enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
  these are translated into '\n' before being returned to the
  caller. If it is '', universal newline mode is enabled, but line
  endings are returned to the caller untranslated. If it has any of
  the other legal values, input lines are only terminated by the given
  string, and the line ending is returned to the caller untranslated.

* On output, if newline is None, any '\n' characters written are
  translated to the system default line separator, os.linesep. If
  newline is '' or '\n', no translation takes place. If newline is any
  of the other legal values, any '\n' characters written are translated
  to the given string.

If closefd is False, the underlying file descriptor will be kept open
when the file is closed. This does not work when a file name is given
and must be True in that case.

A custom opener can be used by passing a callable as *opener*. The
underlying file descriptor for the file object is then obtained by
calling *opener* with (*file*, *flags*). *opener* must return an open
file descriptor (passing os.open as *opener* results in functionality
similar to passing None).

open() returns a file object whose type depends on the mode, and
through which the standard file operations such as reading and writing
are performed. When open() is used to open a file in a text mode ('w',
'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
a file in a binary mode, the returned class varies: in read binary
mode, it returns a BufferedReader; in write binary and append binary
modes, it returns a BufferedWriter, and in read/write mode, it returns
a BufferedRandom.

It is also possible to use a string or bytearray as a file for both
reading and writing. For strings StringIO can be used like a file
opened in a text mode, and for bytes a BytesIO can be used like a file
opened in a binary mode."""
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='mode'),
        NodeInputBP(label='buffering'),
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors'),
        NodeInputBP(label='newline'),
        NodeInputBP(label='closefd'),
        NodeInputBP(label='opener'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.open(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class AutoNode_builtins_ord(NodeBase):
    title = 'ord'
    type_ = 'builtins'
    doc = """Return the Unicode code point for a one-character string."""
    init_inputs = [
        NodeInputBP(label='c'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.ord(self.input(0)))
        

class AutoNode_builtins_pow(NodeBase):
    title = 'pow'
    type_ = 'builtins'
    doc = """Equivalent to base**exp with 2 arguments or base**exp % mod with 3 arguments

Some types, such as ints, are able to use a more efficient algorithm when
invoked using the three argument form."""
    init_inputs = [
        NodeInputBP(label='base'),
        NodeInputBP(label='exp'),
        NodeInputBP(label='mod'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.pow(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_builtins_repr(NodeBase):
    title = 'repr'
    type_ = 'builtins'
    doc = """Return the canonical string representation of the object.

For many object types, including most builtins, eval(repr(obj)) == obj."""
    init_inputs = [
        NodeInputBP(label='obj'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.repr(self.input(0)))
        

class AutoNode_builtins_round(NodeBase):
    title = 'round'
    type_ = 'builtins'
    doc = """Round a number to a given precision in decimal digits.

The return value is an integer if ndigits is omitted or None.  Otherwise
the return value has the same type as the number.  ndigits may be negative."""
    init_inputs = [
        NodeInputBP(label='number'),
        NodeInputBP(label='ndigits'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.round(self.input(0), self.input(1)))
        

class AutoNode_builtins_setattr(NodeBase):
    title = 'setattr'
    type_ = 'builtins'
    doc = """Sets the named attribute on the given object to the specified value.

setattr(x, 'y', v) is equivalent to ``x.y = v''"""
    init_inputs = [
        NodeInputBP(label='obj'),
        NodeInputBP(label='name'),
        NodeInputBP(label='value'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.setattr(self.input(0), self.input(1), self.input(2)))
        

class AutoNode_builtins_sorted(NodeBase):
    title = 'sorted'
    type_ = 'builtins'
    doc = """Return a new list containing all items from the iterable in ascending order.

A custom key function can be supplied to customize the sort order, and the
reverse flag can be set to request the result in descending order."""
    init_inputs = [
        NodeInputBP(label='iterable'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.sorted(self.input(0)))
        

class AutoNode_builtins_sum(NodeBase):
    title = 'sum'
    type_ = 'builtins'
    doc = """Return the sum of a 'start' value (default: 0) plus an iterable of numbers

When the iterable is empty, return the start value.
This function is intended specifically for use with numeric values and may
reject non-numeric types."""
    init_inputs = [
        NodeInputBP(label='iterable'),
        NodeInputBP(label='start'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, builtins.sum(self.input(0), self.input(1)))
        


export_nodes(
    AutoNode_builtins_abs,
    AutoNode_builtins_all,
    AutoNode_builtins_any,
    AutoNode_builtins_ascii,
    AutoNode_builtins_bin,
    AutoNode_builtins_callable,
    AutoNode_builtins_chr,
    AutoNode_builtins_compile,
    AutoNode_builtins_delattr,
    AutoNode_builtins_divmod,
    AutoNode_builtins_eval,
    AutoNode_builtins_exec,
    AutoNode_builtins_format,
    AutoNode_builtins_globals,
    AutoNode_builtins_hasattr,
    AutoNode_builtins_hash,
    AutoNode_builtins_hex,
    AutoNode_builtins_id,
    AutoNode_builtins_input,
    AutoNode_builtins_isinstance,
    AutoNode_builtins_issubclass,
    AutoNode_builtins_len,
    AutoNode_builtins_locals,
    AutoNode_builtins_oct,
    AutoNode_builtins_open,
    AutoNode_builtins_ord,
    AutoNode_builtins_pow,
    AutoNode_builtins_repr,
    AutoNode_builtins_round,
    AutoNode_builtins_setattr,
    AutoNode_builtins_sorted,
    AutoNode_builtins_sum,
)
