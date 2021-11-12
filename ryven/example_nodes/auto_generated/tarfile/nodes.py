
from ryven.NENV import *

import tarfile


class NodeBase(Node):
    pass


class _Safe_Print_Node(NodeBase):
    """
    """
    
    title = '_safe_print'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile._safe_print(self.input(0)))
        

class Bltn_Open_Node(NodeBase):
    """
    Open file and return a stream.  Raise OSError upon failure.

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
    
    title = 'bltn_open'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='file'),
        NodeInputBP(label='mode', dtype=dtypes.Data(default='r', size='s')),
        NodeInputBP(label='buffering', dtype=dtypes.Data(default=-1, size='s')),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='errors', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='newline', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='closefd', dtype=dtypes.Data(default=True, size='s')),
        NodeInputBP(label='opener', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.bltn_open(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5), self.input(6), self.input(7)))
        

class Calc_Chksums_Node(NodeBase):
    """
    Calculate the checksum for a member's header by summing up all
       characters except for the chksum field which is treated as if
       it was filled with spaces. According to the GNU tar sources,
       some tars (Sun and NeXT) calculate chksum with signed char,
       which will be different if there are chars in the buffer with
       the high bit set. So we calculate two checksums, unsigned and
       signed.
    """
    
    title = 'calc_chksums'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='buf'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.calc_chksums(self.input(0)))
        

class Copyfileobj_Node(NodeBase):
    """
    Copy length bytes from fileobj src to fileobj dst.
       If length is None, copy the entire content.
    """
    
    title = 'copyfileobj'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='src'),
        NodeInputBP(label='dst'),
        NodeInputBP(label='length', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='exception', dtype=dtypes.Data(default=OSError, size='s')),
        NodeInputBP(label='bufsize', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.copyfileobj(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Is_Tarfile_Node(NodeBase):
    """
    Return True if name points to a tar archive that we
       are able to handle, else return False.

       'name' should be a string, file, or file-like object.
    """
    
    title = 'is_tarfile'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='name'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.is_tarfile(self.input(0)))
        

class Itn_Node(NodeBase):
    """
    Convert a python number to a number field.
    """
    
    title = 'itn'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='n'),
        NodeInputBP(label='digits', dtype=dtypes.Data(default=8, size='s')),
        NodeInputBP(label='format', dtype=dtypes.Data(default=2, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.itn(self.input(0), self.input(1), self.input(2)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'tarfile'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.main())
        

class Nti_Node(NodeBase):
    """
    Convert a number field to a python number.
    """
    
    title = 'nti'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.nti(self.input(0)))
        

class Nts_Node(NodeBase):
    """
    Convert a null-terminated bytes object to a string.
    """
    
    title = 'nts'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.nts(self.input(0), self.input(1), self.input(2)))
        

class Open_Node(NodeBase):
    """
    Open a tar archive for reading, writing or appending. Return
           an appropriate TarFile class.

           mode:
           'r' or 'r:*' open for reading with transparent compression
           'r:'         open for reading exclusively uncompressed
           'r:gz'       open for reading with gzip compression
           'r:bz2'      open for reading with bzip2 compression
           'r:xz'       open for reading with lzma compression
           'a' or 'a:'  open for appending, creating the file if necessary
           'w' or 'w:'  open for writing without compression
           'w:gz'       open for writing with gzip compression
           'w:bz2'      open for writing with bzip2 compression
           'w:xz'       open for writing with lzma compression

           'x' or 'x:'  create a tarfile exclusively without compression, raise
                        an exception if the file is already created
           'x:gz'       create a gzip compressed tarfile, raise an exception
                        if the file is already created
           'x:bz2'      create a bzip2 compressed tarfile, raise an exception
                        if the file is already created
           'x:xz'       create an lzma compressed tarfile, raise an exception
                        if the file is already created

           'r|*'        open a stream of tar blocks with transparent compression
           'r|'         open an uncompressed stream of tar blocks for reading
           'r|gz'       open a gzip compressed stream of tar blocks
           'r|bz2'      open a bzip2 compressed stream of tar blocks
           'r|xz'       open an lzma compressed stream of tar blocks
           'w|'         open an uncompressed stream for writing
           'w|gz'       open a gzip compressed stream for writing
           'w|bz2'      open a bzip2 compressed stream for writing
           'w|xz'       open an lzma compressed stream for writing
        """
    
    title = 'open'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='cls'),
        NodeInputBP(label='name', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='mode', dtype=dtypes.Data(default='r', size='s')),
        NodeInputBP(label='fileobj', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='bufsize', dtype=dtypes.Data(default=10240, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.open(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Stn_Node(NodeBase):
    """
    Convert a string to a null-terminated bytes object.
    """
    
    title = 'stn'
    type_ = 'tarfile'
    init_inputs = [
        NodeInputBP(label='s'),
        NodeInputBP(label='length'),
        NodeInputBP(label='encoding'),
        NodeInputBP(label='errors'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, tarfile.stn(self.input(0), self.input(1), self.input(2), self.input(3)))
        


export_nodes(
    _Safe_Print_Node,
    Bltn_Open_Node,
    Calc_Chksums_Node,
    Copyfileobj_Node,
    Is_Tarfile_Node,
    Itn_Node,
    Main_Node,
    Nti_Node,
    Nts_Node,
    Open_Node,
    Stn_Node,
)
