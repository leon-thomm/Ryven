# when updating the version make sure to update it in setup.cfg as well!
__version_info__ = (3, 2, 0)
__version__ = '.'.join([str(n) for n in __version_info__])

from ryven.NENV import *
from ryven.NWENV import *

import ryven.main.utils as utils

# expose loading nodes package functionality for manual deployment
from .main.utils import import_nodes_package
from .main.nodes_package import NodesPackage

from .main.Ryven import run as run_ryven
from .main.RyvenConsole import run as run_ryven_console
