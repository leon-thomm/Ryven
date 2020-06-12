class Debugger:
    enabled = False

    def enable():
        Debugger.enabled = True

    def disable():
        Debugger.enabled = False

    def debug(*args):
        s = ''
        for arg in args:
            s += ' '+str(arg)
        if Debugger.enabled:
            print('        --> DEBUG:', s)