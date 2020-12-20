from ryvencore.Node import Node, NodePort
from ryvencore.NodeInstance import NodeInstance
from ryvencore.Session import Session
from ryvencore.WidgetBaseClasses import MWB, IWB
from ryvencore.global_tools.Debugger import Debugger


# CONVENIENCE CLASSES

class ConvUI:
    from ryvencore.custom_list_widgets.ScriptsListWidget import ScriptsListWidget
    from ryvencore.custom_list_widgets.VariablesListWidget import VariablesListWidget
    from ryvencore.logging.LogWidget import LogWidget

    ScriptsList = ScriptsListWidget
    VarsList = VariablesListWidget
    LogWidget = LogWidget


class Retain:
    from ryvencore.retain import M
    M = M
