from pkg_resources import resource_string
import os

if __name__ == '__main__':
    print(os.path.abspath(os.path.dirname(resource_string(__name__, 'tests.py'))))
