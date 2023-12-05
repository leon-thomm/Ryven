# set package path (for resources etc.)
import os
from .src.GlobalAttributes import Location
Location.PACKAGE_PATH = os.path.normpath(os.path.dirname(__file__))

os.environ['RC_MODE'] = 'gui'  # set ryvencore gui mode
os.environ['QT_ENABLE_HIGHDPI_SCALING'] = '1'

# expose ryvencore
import ryvencore

from .src.SessionGUI import SessionGUI
from .src.flows.nodes.NodeGUI import NodeGUI

# customer base classes
from ryvencore import Node
from .src.flows.nodes.WidgetBaseClasses import NodeMainWidget, NodeInputWidget, NodeInspectorWidget

# gui classes
from .src.widgets import *
from .src.flows.FlowTheme import flow_themes
