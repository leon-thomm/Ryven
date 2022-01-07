from setuptools import setup

setup()

# create ~/.ryven/ directory
import os
path = os.path.join(os.path.expanduser('~'), '.ryven/')  # == ryven_dir_path() in ryven.main.utils
if not os.path.exists(path):
    os.mkdir(path)
    os.mkdir(os.path.join(path, 'nodes/'))
    os.mkdir(os.path.join(path, 'saves/'))
