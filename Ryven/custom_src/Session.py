from PySide2.QtCore import QObject, Signal
from PySide2.QtGui import QFontDatabase

from custom_src.Node import Node
from custom_src.Script import Script
from custom_src.global_tools.Debugger import Debugger


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


    def __register_fonts(self):
        QFontDatabase.addApplicationFont('../resources/fonts/poppins/Poppins-Medium.ttf')
        QFontDatabase.addApplicationFont('../resources/fonts/source code pro/SourceCodePro-Regular.ttf')
        QFontDatabase.addApplicationFont('../resources/fonts/asap/Asap-Regular.ttf')






    def register_nodes(self, nodes: [Node]) -> [Node]:
        """Registers a list of Nodes which you then can access in all scripts"""

        for n in nodes:
            self.register_node(n)

        return nodes


    def register_node(self, node: Node) -> Node:
        """Registers a Node which then can be accessed in all scripts"""

        self.nodes.append(node)
        return node


    def create_script(self, title: str) -> Script:
        """Creates and returns a new script"""

        script = Script(session=self, title=title)
        self.scripts.append(script)
        self.new_script_created.emit(script)


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
        pass