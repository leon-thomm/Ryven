
from ryven.NENV import *

import cgi


class NodeBase(Node):
    pass


class _Parseparam_Node(NodeBase):
    """
    """
    
    title = '_parseparam'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi._parseparam(self.input(0)))
        

class Closelog_Node(NodeBase):
    """
    Close the log file."""
    
    title = 'closelog'
    type_ = 'cgi'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.closelog())
        

class Dolog_Node(NodeBase):
    """
    Write a log message to the log file.  See initlog() for docs."""
    
    title = 'dolog'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='fmt'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.dolog(self.input(0)))
        

class Initlog_Node(NodeBase):
    """
    Write a log message, if there is a log file.

    Even though this function is called initlog(), you should always
    use log(); log is a variable that is set either to initlog
    (initially), to dolog (once the log file has been opened), or to
    nolog (when logging is disabled).

    The first argument is a format string; the remaining arguments (if
    any) are arguments to the % operator, so e.g.
        log("%s: %s", "a", "b")
    will write "a: b" to the log file, followed by a newline.

    If the global logfp is not None, it should be a file object to
    which log data is written.

    If the global logfp is None, the global logfile may be a string
    giving a filename to open, in append mode.  This file should be
    world writable!!!  If the file can't be opened, logging is
    silently disabled (since there is no safe place where we could
    send an error message).

    """
    
    title = 'initlog'
    type_ = 'cgi'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.initlog())
        

class Log_Node(NodeBase):
    """
    Write a log message, if there is a log file.

    Even though this function is called initlog(), you should always
    use log(); log is a variable that is set either to initlog
    (initially), to dolog (once the log file has been opened), or to
    nolog (when logging is disabled).

    The first argument is a format string; the remaining arguments (if
    any) are arguments to the % operator, so e.g.
        log("%s: %s", "a", "b")
    will write "a: b" to the log file, followed by a newline.

    If the global logfp is not None, it should be a file object to
    which log data is written.

    If the global logfp is None, the global logfile may be a string
    giving a filename to open, in append mode.  This file should be
    world writable!!!  If the file can't be opened, logging is
    silently disabled (since there is no safe place where we could
    send an error message).

    """
    
    title = 'log'
    type_ = 'cgi'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.log())
        

class Nolog_Node(NodeBase):
    """
    Dummy function, assigned to log when logging is disabled."""
    
    title = 'nolog'
    type_ = 'cgi'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.nolog())
        

class Parse_Node(NodeBase):
    """
    Parse a query in the environment or from a file (default stdin)

        Arguments, all optional:

        fp              : file pointer; default: sys.stdin.buffer

        environ         : environment dictionary; default: os.environ

        keep_blank_values: flag indicating whether blank values in
            percent-encoded forms should be treated as blank strings.
            A true value indicates that blanks should be retained as
            blank strings.  The default false value indicates that
            blank values are to be ignored and treated as if they were
            not included.

        strict_parsing: flag indicating what to do with parsing errors.
            If false (the default), errors are silently ignored.
            If true, errors raise a ValueError exception.

        separator: str. The symbol to use for separating the query arguments.
            Defaults to &.
    """
    
    title = 'parse'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='fp', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='environ', dtype=dtypes.Data(default=environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\nutri\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-0N3SJ6C', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\nutri', 'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\bin', 'LOCALAPPDATA': 'C:\\Users\\nutri\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-0N3SJ6C', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\nutri\\OneDrive - ETH Zurich', 'ONEDRIVECOMMERCIAL': 'C:\\Users\\nutri\\OneDrive - ETH Zurich', 'ONEDRIVECONSUMER': 'C:\\Users\\nutri\\OneDrive', 'ONLINESERVICES': 'Online Services', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\nutri\\projects\\ryven projects\\venv\\Scripts;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Git\\cmd;C:\\Program Files\\Wolfram Research\\WolframScript\\;C:\\Users\\nutri\\AppData\\Local\\programs\\nodejs\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Users\\nutri\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\nutri\\AppData\\Local\\GitHubDesktop\\bin;C:\\Users\\nutri\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\;C:\\Users\\nutri\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PLATFORMCODE': 'KV', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 126 Stepping 5, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '7e05', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\nutri\\projects\\ryven projects\\Ryven\\Ryven;C:\\Users\\nutri\\projects\\ryven projects\\Ryven\\Ryven\\src;C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend;C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'REGIONCODE': 'EMEA', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\nutri\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\nutri\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-0N3SJ6C', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-0N3SJ6C', 'USERNAME': 'nutri', 'USERPROFILE': 'C:\\Users\\nutri', 'VIRTUAL_ENV': 'C:\\Users\\nutri\\projects\\ryven projects\\venv', 'WINDIR': 'C:\\WINDOWS', 'ZES_ENABLE_SYSMAN': '1', '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Git\\cmd;C:\\Program Files\\Wolfram Research\\WolframScript\\;C:\\Users\\nutri\\AppData\\Local\\programs\\nodejs\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Users\\nutri\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\nutri\\AppData\\Local\\GitHubDesktop\\bin;C:\\Users\\nutri\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\;C:\\Users\\nutri\\AppData\\Roaming\\npm', '_OLD_VIRTUAL_PROMPT': '$P$G'}), size='s')),
        NodeInputBP(label='keep_blank_values', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='strict_parsing', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='separator', dtype=dtypes.Data(default='&', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.parse(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Parse_Header_Node(NodeBase):
    """
    Parse a Content-type like header.

    Return the main content-type and a dictionary of options.

    """
    
    title = 'parse_header'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='line'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.parse_header(self.input(0)))
        

class Parse_Multipart_Node(NodeBase):
    """
    Parse multipart input.

    Arguments:
    fp   : input file
    pdict: dictionary containing other parameters of content-type header
    encoding, errors: request encoding and error handler, passed to
        FieldStorage

    Returns a dictionary just like parse_qs(): keys are the field names, each
    value is a list of values for that field. For non-file fields, the value
    is a list of strings.
    """
    
    title = 'parse_multipart'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='fp'),
        NodeInputBP(label='pdict'),
        NodeInputBP(label='encoding', dtype=dtypes.Data(default='utf-8', size='s')),
        NodeInputBP(label='errors', dtype=dtypes.Data(default='replace', size='s')),
        NodeInputBP(label='separator', dtype=dtypes.Data(default='&', size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.parse_multipart(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4)))
        

class Print_Arguments_Node(NodeBase):
    """
    """
    
    title = 'print_arguments'
    type_ = 'cgi'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.print_arguments())
        

class Print_Directory_Node(NodeBase):
    """
    Dump the current directory as HTML."""
    
    title = 'print_directory'
    type_ = 'cgi'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.print_directory())
        

class Print_Environ_Node(NodeBase):
    """
    Dump the shell environment as HTML."""
    
    title = 'print_environ'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='environ', dtype=dtypes.Data(default=environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\nutri\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-0N3SJ6C', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\nutri', 'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\bin', 'LOCALAPPDATA': 'C:\\Users\\nutri\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-0N3SJ6C', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\nutri\\OneDrive - ETH Zurich', 'ONEDRIVECOMMERCIAL': 'C:\\Users\\nutri\\OneDrive - ETH Zurich', 'ONEDRIVECONSUMER': 'C:\\Users\\nutri\\OneDrive', 'ONLINESERVICES': 'Online Services', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\nutri\\projects\\ryven projects\\venv\\Scripts;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Git\\cmd;C:\\Program Files\\Wolfram Research\\WolframScript\\;C:\\Users\\nutri\\AppData\\Local\\programs\\nodejs\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Users\\nutri\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\nutri\\AppData\\Local\\GitHubDesktop\\bin;C:\\Users\\nutri\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\;C:\\Users\\nutri\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PLATFORMCODE': 'KV', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 126 Stepping 5, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '7e05', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\nutri\\projects\\ryven projects\\Ryven\\Ryven;C:\\Users\\nutri\\projects\\ryven projects\\Ryven\\Ryven\\src;C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend;C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'REGIONCODE': 'EMEA', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\nutri\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\nutri\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-0N3SJ6C', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-0N3SJ6C', 'USERNAME': 'nutri', 'USERPROFILE': 'C:\\Users\\nutri', 'VIRTUAL_ENV': 'C:\\Users\\nutri\\projects\\ryven projects\\venv', 'WINDIR': 'C:\\WINDOWS', 'ZES_ENABLE_SYSMAN': '1', '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Git\\cmd;C:\\Program Files\\Wolfram Research\\WolframScript\\;C:\\Users\\nutri\\AppData\\Local\\programs\\nodejs\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Users\\nutri\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\nutri\\AppData\\Local\\GitHubDesktop\\bin;C:\\Users\\nutri\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\;C:\\Users\\nutri\\AppData\\Roaming\\npm', '_OLD_VIRTUAL_PROMPT': '$P$G'}), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.print_environ(self.input(0)))
        

class Print_Environ_Usage_Node(NodeBase):
    """
    Dump a list of environment variables used by CGI as HTML."""
    
    title = 'print_environ_usage'
    type_ = 'cgi'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.print_environ_usage())
        

class Print_Exception_Node(NodeBase):
    """
    """
    
    title = 'print_exception'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='type', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='value', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='tb', dtype=dtypes.Data(default=None, size='s')),
        NodeInputBP(label='limit', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.print_exception(self.input(0), self.input(1), self.input(2), self.input(3)))
        

class Print_Form_Node(NodeBase):
    """
    Dump the contents of a form as HTML."""
    
    title = 'print_form'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='form'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.print_form(self.input(0)))
        

class Test_Node(NodeBase):
    """
    Robust test CGI script, usable as main program.

    Write minimal HTTP headers and dump all information provided to
    the script in HTML form.

    """
    
    title = 'test'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='environ', dtype=dtypes.Data(default=environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'APPDATA': 'C:\\Users\\nutri\\AppData\\Roaming', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'DESKTOP-0N3SJ6C', 'COMSPEC': 'C:\\WINDOWS\\system32\\cmd.exe', 'DRIVERDATA': 'C:\\Windows\\System32\\Drivers\\DriverData', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\nutri', 'IDEA_INITIAL_DIRECTORY': 'C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\bin', 'LOCALAPPDATA': 'C:\\Users\\nutri\\AppData\\Local', 'LOGONSERVER': '\\\\DESKTOP-0N3SJ6C', 'NUMBER_OF_PROCESSORS': '8', 'ONEDRIVE': 'C:\\Users\\nutri\\OneDrive - ETH Zurich', 'ONEDRIVECOMMERCIAL': 'C:\\Users\\nutri\\OneDrive - ETH Zurich', 'ONEDRIVECONSUMER': 'C:\\Users\\nutri\\OneDrive', 'ONLINESERVICES': 'Online Services', 'OS': 'Windows_NT', 'PATH': 'C:\\Users\\nutri\\projects\\ryven projects\\venv\\Scripts;C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Git\\cmd;C:\\Program Files\\Wolfram Research\\WolframScript\\;C:\\Users\\nutri\\AppData\\Local\\programs\\nodejs\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Users\\nutri\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\nutri\\AppData\\Local\\GitHubDesktop\\bin;C:\\Users\\nutri\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\;C:\\Users\\nutri\\AppData\\Roaming\\npm', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PLATFORMCODE': 'KV', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 126 Stepping 5, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '7e05', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PROMPT': '(venv) $P$G', 'PSMODULEPATH': 'C:\\Program Files\\WindowsPowerShell\\Modules;C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\Modules', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_DISPLAY_PORT': '63342', 'PYCHARM_HOSTED': '1', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'C:\\Users\\nutri\\projects\\ryven projects\\Ryven\\Ryven;C:\\Users\\nutri\\projects\\ryven projects\\Ryven\\Ryven\\src;C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_matplotlib_backend;C:\\Users\\nutri\\AppData\\Local\\programs\\JetBrains\\PyCharm 2021.1.1\\plugins\\python\\helpers\\pycharm_display', 'PYTHONUNBUFFERED': '1', 'REGIONCODE': 'EMEA', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\WINDOWS', 'TEMP': 'C:\\Users\\nutri\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\nutri\\AppData\\Local\\Temp', 'USERDOMAIN': 'DESKTOP-0N3SJ6C', 'USERDOMAIN_ROAMINGPROFILE': 'DESKTOP-0N3SJ6C', 'USERNAME': 'nutri', 'USERPROFILE': 'C:\\Users\\nutri', 'VIRTUAL_ENV': 'C:\\Users\\nutri\\projects\\ryven projects\\venv', 'WINDIR': 'C:\\WINDOWS', 'ZES_ENABLE_SYSMAN': '1', '_OLD_VIRTUAL_PATH': 'C:\\Program Files\\Common Files\\Oracle\\Java\\javapath;C:\\WINDOWS\\system32;C:\\WINDOWS;C:\\WINDOWS\\System32\\Wbem;C:\\WINDOWS\\System32\\WindowsPowerShell\\v1.0\\;C:\\WINDOWS\\System32\\OpenSSH\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Git\\cmd;C:\\Program Files\\Wolfram Research\\WolframScript\\;C:\\Users\\nutri\\AppData\\Local\\programs\\nodejs\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\Scripts\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Python39\\;C:\\Users\\nutri\\AppData\\Local\\Programs\\Python\\Launcher\\;C:\\Users\\nutri\\AppData\\Local\\Microsoft\\WindowsApps;C:\\Users\\nutri\\AppData\\Local\\GitHubDesktop\\bin;C:\\Users\\nutri\\AppData\\Local\\Programs\\MiKTeX\\miktex\\bin\\x64\\;C:\\Users\\nutri\\AppData\\Roaming\\npm', '_OLD_VIRTUAL_PROMPT': '$P$G'}), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.test(self.input(0)))
        

class Valid_Boundary_Node(NodeBase):
    """
    """
    
    title = 'valid_boundary'
    type_ = 'cgi'
    init_inputs = [
        NodeInputBP(label='s'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, cgi.valid_boundary(self.input(0)))
        


export_nodes(
    _Parseparam_Node,
    Closelog_Node,
    Dolog_Node,
    Initlog_Node,
    Log_Node,
    Nolog_Node,
    Parse_Node,
    Parse_Header_Node,
    Parse_Multipart_Node,
    Print_Arguments_Node,
    Print_Directory_Node,
    Print_Environ_Node,
    Print_Environ_Usage_Node,
    Print_Exception_Node,
    Print_Form_Node,
    Test_Node,
    Valid_Boundary_Node,
)
