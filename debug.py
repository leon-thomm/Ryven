#!/usr/bin/env python3

# manually debug ryven; ensure that the following packages are 
# not installed in the current environment:
#   * ryven
#   * ryvencore-qt'
#   * ryvencore

RYVEN_PATH = './ryven-editor'
RYVEN_QT_PATH = './ryvencore-qt'
RYVENCORE_PATH = '../ryvencore'

import sys

sys.path.insert(0, RYVEN_PATH)
sys.path.insert(0, RYVEN_QT_PATH)
sys.path.insert(0, RYVENCORE_PATH)

from ryven import run_ryven

if __name__ == '__main__':
    run_ryven(
        f"{RYVEN_PATH}/ryven/example_projects/matrices.json",
        nodes=[
            f"{RYVEN_PATH}/ryven/example_nodes/examples",
            f"{RYVEN_PATH}/ryven/example_nodes/linalg",
        ],
        qt_api='pyside6',
        show_dialog=False,
    )
