import sys


class Debugger:
    enabled = False

    @staticmethod
    def enable():
        Debugger.enabled = True

    @staticmethod
    def disable():
        Debugger.enabled = False

    def debug(*args):
        if not Debugger.enabled:
            return

        s = ''
        for arg in args:
            s += ' '+str(arg)
        print('--> DEBUG:', s)

    def debugerr(*args):
        if not Debugger.enabled:
            return

        s = ''
        for arg in args:
            s += ' '+str(arg)

        sys.stderr.write(s)

        # print(DEBUG_COLORS.WARNING + s + DEBUG_COLORS.ENDC)


class DEBUG_COLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
