from ryvencore_qt import Node as RC_Node


class NodeBase(RC_Node):
    """
    This class extends the ryvencore-qt Node definition to add some new and support existing
    commonly used features from ryvencore-qt. Parts of this might get moved to ryvencore-qt
    at some point, but for now this is purely part of Ryven to make the usage more intuitive.
    """

    # CONSOLE

    main_console = None

    # CODE

    __class_codes__: dict = None  # used by the src code preview

    def __init__(self, params):
        super().__init__(params)

        self.__obj_codes__ = {}  # gets set by src code preview


    def init_default_actions(self) -> dict:
        actions = super().init_default_actions()
        actions['console ref'] = {'method': self.add_to_console}
        return actions

    def add_to_console(self):
        self.main_console.add_obj_context(self)
