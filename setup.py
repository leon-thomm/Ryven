from setuptools import setup

setup()

# create ~/.ryven/ directory
import os
path = os.path.join(os.path.expanduser('~'), '.ryven/')  # == ryven_dir_path() in ryven.main.utils
if not os.path.exists(path):
    os.mkdir(path)
    os.mkdir(os.path.join(path, 'nodes/'))
    os.mkdir(os.path.join(path, 'saves/'))

# generate default config files if not existent yet
cfg_path = os.path.join(path, 'ryven.cfg')
if not os.path.exists(cfg_path):
    with open(cfg_path, 'w') as f:
        f.write("""
# Automatically loaded default Ryven config file

# EXAMPLE:
# the following configuration launches Ryven in 'light' mode with flow theme 'colorful light' and node packages 'std' and 'linalg' preloaded
#     window-theme: light
#     flow-theme: "colorful light"
#     nodes: std
#     nodes: linalg
""")
