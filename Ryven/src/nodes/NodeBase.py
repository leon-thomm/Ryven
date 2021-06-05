from ryvencore_qt import Node as RC_Node


class NodeBase(RC_Node):

    # CONSOLE

    main_console = None

    # CODE

    __class_codes__: dict = None  # used by the src code preview

    # def __init__(self, params):
    #     super().__init__(params)
    #
    #     self.__obj_codes__ = {}  # gets set by src code preview


    def init_default_actions(self) -> dict:
        actions = super().init_default_actions()
        actions['console ref'] = {'method': self.add_to_console}
        return actions

    def add_to_console(self):
        # from MainConsole import MainConsole
        # MainConsole.instance.add_obj_context(self)
        self.main_console.add_obj_context(self)
