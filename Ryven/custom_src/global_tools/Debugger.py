class Debugger:
    enabled = False

    def enable():
        Debugger.enabled = True

    def disable():
        Debugger.enabled = False

    def debug(*args):
        if not Debugger.enabled:
            return

        s = ''
        for arg in args:
            s += ' '+str(arg)
        print('        --> DEBUG:', s)