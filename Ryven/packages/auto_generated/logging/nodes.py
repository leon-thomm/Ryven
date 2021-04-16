import ryvencore_qt as rc
import logging


class AutoNode_logging__acquireLock(rc.Node):
    title = '_acquireLock'
    doc = '''
    Acquire the module-level lock for serializing access to shared data.

    This should be released with _releaseLock().
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging._acquireLock())
        


class AutoNode_logging__addHandlerRef(rc.Node):
    title = '_addHandlerRef'
    doc = '''
    Add a handler to the internal cleanup list using a weak reference.
    '''
    init_inputs = [
        rc.NodeInputBP(label='handler'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging._addHandlerRef(self.input(0)))
        


class AutoNode_logging__checkLevel(rc.Node):
    title = '_checkLevel'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='level'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging._checkLevel(self.input(0)))
        


class AutoNode_logging__register_at_fork_reinit_lock(rc.Node):
    title = '_register_at_fork_reinit_lock'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='instance'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging._register_at_fork_reinit_lock(self.input(0)))
        


class AutoNode_logging__releaseLock(rc.Node):
    title = '_releaseLock'
    doc = '''
    Release the module-level lock acquired by calling _acquireLock().
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging._releaseLock())
        


class AutoNode_logging__removeHandlerRef(rc.Node):
    title = '_removeHandlerRef'
    doc = '''
    Remove a handler reference from the internal cleanup list.
    '''
    init_inputs = [
        rc.NodeInputBP(label='wr'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging._removeHandlerRef(self.input(0)))
        


class AutoNode_logging__showwarning(rc.Node):
    title = '_showwarning'
    doc = '''
    Implementation of showwarnings which redirects to logging, which will first
    check to see if the file parameter is None. If a file is specified, it will
    delegate to the original warnings implementation of showwarning. Otherwise,
    it will call warnings.formatwarning and will log the resulting string to a
    warnings logger named "py.warnings" with level logging.WARNING.
    '''
    init_inputs = [
        rc.NodeInputBP(label='message'),
rc.NodeInputBP(label='category'),
rc.NodeInputBP(label='filename'),
rc.NodeInputBP(label='lineno'),
rc.NodeInputBP(label='file'),
rc.NodeInputBP(label='line'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging._showwarning(self.input(0), self.input(1), self.input(2), self.input(3), self.input(4), self.input(5)))
        


class AutoNode_logging_addLevelName(rc.Node):
    title = 'addLevelName'
    doc = '''
    Associate 'levelName' with 'level'.

    This is used when converting levels to text during message formatting.
    '''
    init_inputs = [
        rc.NodeInputBP(label='level'),
rc.NodeInputBP(label='levelName'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.addLevelName(self.input(0), self.input(1)))
        


class AutoNode_logging_basicConfig(rc.Node):
    title = 'basicConfig'
    doc = '''
    Do basic configuration for the logging system.

    This function does nothing if the root logger already has handlers
    configured, unless the keyword argument *force* is set to ``True``.
    It is a convenience method intended for use by simple scripts
    to do one-shot configuration of the logging package.

    The default behaviour is to create a StreamHandler which writes to
    sys.stderr, set a formatter using the BASIC_FORMAT format string, and
    add the handler to the root logger.

    A number of optional keyword arguments may be specified, which can alter
    the default behaviour.

    filename  Specifies that a FileHandler be created, using the specified
              filename, rather than a StreamHandler.
    filemode  Specifies the mode to open the file, if filename is specified
              (if filemode is unspecified, it defaults to 'a').
    format    Use the specified format string for the handler.
    datefmt   Use the specified date/time format.
    style     If a format string is specified, use this to specify the
              type of format string (possible values '%', '{', '$', for
              %-formatting, :meth:`str.format` and :class:`string.Template`
              - defaults to '%').
    level     Set the root logger level to the specified level.
    stream    Use the specified stream to initialize the StreamHandler. Note
              that this argument is incompatible with 'filename' - if both
              are present, 'stream' is ignored.
    handlers  If specified, this should be an iterable of already created
              handlers, which will be added to the root handler. Any handler
              in the list which does not have a formatter assigned will be
              assigned the formatter created in this function.
    force     If this keyword  is specified as true, any existing handlers
              attached to the root logger are removed and closed, before
              carrying out the configuration as specified by the other
              arguments.
    Note that you could specify a stream created using open(filename, mode)
    rather than passing the filename and mode in. However, it should be
    remembered that StreamHandler does not close its stream (since it may be
    using sys.stdout or sys.stderr), whereas FileHandler closes its stream
    when the handler is closed.

    .. versionchanged:: 3.8
       Added the ``force`` parameter.

    .. versionchanged:: 3.2
       Added the ``style`` parameter.

    .. versionchanged:: 3.3
       Added the ``handlers`` parameter. A ``ValueError`` is now thrown for
       incompatible arguments (e.g. ``handlers`` specified together with
       ``filename``/``filemode``, or ``filename``/``filemode`` specified
       together with ``stream``, or ``handlers`` specified together with
       ``stream``.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.basicConfig())
        


class AutoNode_logging_captureWarnings(rc.Node):
    title = 'captureWarnings'
    doc = '''
    If capture is true, redirect all warnings to the logging package.
    If capture is False, ensure that warnings are not redirected to logging
    but to their original destinations.
    '''
    init_inputs = [
        rc.NodeInputBP(label='capture'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.captureWarnings(self.input(0)))
        


class AutoNode_logging_critical(rc.Node):
    title = 'critical'
    doc = '''
    Log a message with severity 'CRITICAL' on the root logger. If the logger
    has no handlers, call basicConfig() to add a console handler with a
    pre-defined format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.critical(self.input(0)))
        


class AutoNode_logging_currentframe(rc.Node):
    title = 'currentframe'
    doc = '''None'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.currentframe())
        


class AutoNode_logging_debug(rc.Node):
    title = 'debug'
    doc = '''
    Log a message with severity 'DEBUG' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.debug(self.input(0)))
        


class AutoNode_logging_disable(rc.Node):
    title = 'disable'
    doc = '''
    Disable all logging calls of severity 'level' and below.
    '''
    init_inputs = [
        rc.NodeInputBP(label='level'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.disable(self.input(0)))
        


class AutoNode_logging_error(rc.Node):
    title = 'error'
    doc = '''
    Log a message with severity 'ERROR' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.error(self.input(0)))
        


class AutoNode_logging_exception(rc.Node):
    title = 'exception'
    doc = '''
    Log a message with severity 'ERROR' on the root logger, with exception
    information. If the logger has no handlers, basicConfig() is called to add
    a console handler with a pre-defined format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.exception(self.input(0)))
        


class AutoNode_logging_fatal(rc.Node):
    title = 'fatal'
    doc = '''
    Log a message with severity 'CRITICAL' on the root logger. If the logger
    has no handlers, call basicConfig() to add a console handler with a
    pre-defined format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.fatal(self.input(0)))
        


class AutoNode_logging_getLevelName(rc.Node):
    title = 'getLevelName'
    doc = '''
    Return the textual representation of logging level 'level'.

    If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
    INFO, DEBUG) then you get the corresponding string. If you have
    associated levels with names using addLevelName then the name you have
    associated with 'level' is returned.

    If a numeric value corresponding to one of the defined levels is passed
    in, the corresponding string representation is returned.

    Otherwise, the string "Level %s" % level is returned.
    '''
    init_inputs = [
        rc.NodeInputBP(label='level'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.getLevelName(self.input(0)))
        


class AutoNode_logging_getLogRecordFactory(rc.Node):
    title = 'getLogRecordFactory'
    doc = '''
    Return the factory to be used when instantiating a log record.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.getLogRecordFactory())
        


class AutoNode_logging_getLogger(rc.Node):
    title = 'getLogger'
    doc = '''
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    '''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.getLogger(self.input(0)))
        


class AutoNode_logging_getLoggerClass(rc.Node):
    title = 'getLoggerClass'
    doc = '''
    Return the class to be used when instantiating a logger.
    '''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.getLoggerClass())
        


class AutoNode_logging_info(rc.Node):
    title = 'info'
    doc = '''
    Log a message with severity 'INFO' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.info(self.input(0)))
        


class AutoNode_logging_log(rc.Node):
    title = 'log'
    doc = '''
    Log 'msg % args' with the integer severity 'level' on the root logger. If
    the logger has no handlers, call basicConfig() to add a console handler
    with a pre-defined format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='level'),
rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.log(self.input(0), self.input(1)))
        


class AutoNode_logging_makeLogRecord(rc.Node):
    title = 'makeLogRecord'
    doc = '''
    Make a LogRecord whose attributes are defined by the specified dictionary,
    This function is useful for converting a logging event received over
    a socket connection (which is sent as a dictionary) into a LogRecord
    instance.
    '''
    init_inputs = [
        rc.NodeInputBP(label='dict'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.makeLogRecord(self.input(0)))
        


class AutoNode_logging_setLogRecordFactory(rc.Node):
    title = 'setLogRecordFactory'
    doc = '''
    Set the factory to be used when instantiating a log record.

    :param factory: A callable which will be called to instantiate
    a log record.
    '''
    init_inputs = [
        rc.NodeInputBP(label='factory'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.setLogRecordFactory(self.input(0)))
        


class AutoNode_logging_setLoggerClass(rc.Node):
    title = 'setLoggerClass'
    doc = '''
    Set the class to be used when instantiating a logger. The class should
    define __init__() such that only a name argument is required, and the
    __init__() should call Logger.__init__()
    '''
    init_inputs = [
        rc.NodeInputBP(label='klass'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.setLoggerClass(self.input(0)))
        


class AutoNode_logging_shutdown(rc.Node):
    title = 'shutdown'
    doc = '''
    Perform any cleanup actions in the logging system (e.g. flushing
    buffers).

    Should be called at application exit.
    '''
    init_inputs = [
        rc.NodeInputBP(label='handlerList'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.shutdown(self.input(0)))
        


class AutoNode_logging_warn(rc.Node):
    title = 'warn'
    doc = '''None'''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.warn(self.input(0)))
        


class AutoNode_logging_warning(rc.Node):
    title = 'warning'
    doc = '''
    Log a message with severity 'WARNING' on the root logger. If the logger has
    no handlers, call basicConfig() to add a console handler with a pre-defined
    format.
    '''
    init_inputs = [
        rc.NodeInputBP(label='msg'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, logging.warning(self.input(0)))
        