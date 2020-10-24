import os

def package_path():
    return os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../'))
