from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import QFontDatabase

from ryvencore.Node import Node
from ryvencore.Script import Script
from ryvencore.global_tools.Debugger import Debugger
from ryvencore.Design import Design


class Session(QObject):
    """The Session class represents a project and holds all project-level
    data such as nodes."""

    new_script_created = Signal(Script)
    script_renamed = Signal(Script)
    script_deleted = Signal(Script)


    def __init__(self):
        super().__init__()

        self.__register_fonts()

        self.scripts: [Script] = []
        self.nodes: [Node] = []

        self.design = Design()

        self.design.set_flow_theme()
        self.design.set_flow_theme()  # temporary
        #   the double call is just a temporary fix for an issue I will address in a future release.
        #   Problem: because the signal emitted when setting a flow theme is directly connected to the according slots
        #   in NodeInstance as well as NodeInstance_TitleLabel, the NodeInstance's slot (which starts an animation which
        #   uses the title label's current and theme dependent color) could get called before the title
        #   label's slot has been called to reinitialize this color. This results in wrong color end points for the
        #   title label when activating animations.
        #   This is pretty nasty since I cannot think of a nice fix for this issue other that not letting the slot
        #   methods be called directly from the emitted signal but instead through a defined procedure like before.


    def __register_fonts(self):
        QFontDatabase.addApplicationFont('ryvencore/fonts/poppins/Poppins-Medium.ttf')
        QFontDatabase.addApplicationFont('ryvencore/fonts/source code pro/SourceCodePro-Regular.ttf')
        QFontDatabase.addApplicationFont('ryvencore/fonts/asap/Asap-Regular.ttf')


    def register_nodes(self, nodes: [Node]) -> [Node]:
        """Registers a list of Nodes which you then can access in all scripts"""

        for n in nodes:
            self.register_node(n)

        return nodes


    def register_node(self, node: Node) -> Node:
        """Registers a Node which then can be accessed in all scripts"""

        self.nodes.append(node)
        return node


    def create_script(self, title: str, flow_size: list = None) -> Script:
        """Creates and returns a new script"""

        script = Script(session=self, title=title, flow_size=flow_size)
        self.scripts.append(script)
        self.new_script_created.emit(script)
        return script


    def __load_script(self, config: dict):
        """Loads a script from a project dict"""

        script = Script(session=self, config=config)
        self.scripts.append(script)
        self.new_script_created.emit(script)


    def rename_script(self, script: Script, title: str):
        """Renames an existing script"""
        script.title = title
        self.script_renamed.emit(script)


    def check_new_script_title_validity(self, title: str) -> bool:
        if len(title) == 0:
            return False
        for s in self.scripts:
            if s.title == title:
                return False

        return True


    def delete_script(self, script: Script):
        """Deletes an existing script"""

        self.scripts.remove(script)
        self.script_deleted.emit(script)


    def debugger(self) -> Debugger:
        """Returns the session's debugger"""
        pass


    def load(self, project: dict) -> bool:
        """Loads a project and raises an error if required nodes are missing"""
        if 'scripts' not in project:
            return False

        for s in project['scripts']:
            self.__load_script(config=s)


    def serialize(self) -> list:
        """Returns a list with 'config data' of all scripts for saving the project"""

        scripts_data = []
        for script in self.scripts:
            scripts_data.append(script.config_data())
        return scripts_data


    def all_node_instances(self):
        """Returns a list containing all NodeInstance objects used in any flow which is useful for
        advanced project analysis"""

        node_insts = []
        for s in self.scripts:
            for ni in s.flow.all_node_instances:
                node_insts.append(ni)
        return node_insts


    def save_as_project(self, fpath: str):
        """Convenience method for directly saving the the all content as project to a file"""
        pass


    def set_stylesheet(self, s: str):
        """Sets the session's stylesheet"""

        self.design.global_stylesheet = s
