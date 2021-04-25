from pyqode.core import backend


def run_backend():
    # configure the code completion providers, here we just use a basic one
    backend.CodeCompletionWorker.providers.append(
        backend.DocumentWordsProvider())
    backend.serve_forever()


import sys
# Here, you might want to set the ``QT_API`` to use.
# Valid values are: 'pyqt5', 'pyqt4' or 'pyside'
# See
# import os; os.environ['QT_API'] = 'pyside'
from pyqode.core import api, modes, panels
from qtpy.QtWidgets import QApplication, QMainWindow
import threading


if __name__ == "__main__":
    t = threading.Thread(target=run_backend)
    t.start()

    app = QApplication(sys.argv)

    # create editor and window
    window = QMainWindow()
    editor = api.CodeEdit()
    window.setCentralWidget(editor)

    # start the backend as soon as possible
    editor.backend.start('server.py')

    # append some modes and panels
    editor.modes.append(modes.CodeCompletionMode())
    editor.modes.append(modes.PygmentsSyntaxHighlighter(editor.document()))
    editor.modes.append(modes.CaretLineHighlighterMode())
    editor.panels.append(panels.SearchAndReplacePanel(),
                         api.Panel.Position.BOTTOM)

    # open a file
    editor.file.open(__file__)

    # run
    window.show()
    app.exec_()