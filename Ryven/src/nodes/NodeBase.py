from ryvencore_qt import Node as RC_Node


class NodeBase(RC_Node):
    """
    This class extends the ryvencore-qt Node definition to add some new and support existing
    commonly used features from ryvencore-qt. Parts of this might get moved to ryvencore-qt
    at some point, but for now this is purely part of Ryven to make the usage more intuitive.
    """

    # CONSOLE

    main_console = None

    def init_default_actions(self) -> dict:
        actions = super().init_default_actions()
        actions['console ref'] = {'method': self.add_to_console}
        return actions

    def add_to_console(self):
        self.main_console.add_obj_context(self)

    # --------------

    # # DATA INPUT WIDGET NOTATION
    #
    # def create_input_cw(self, label: str = '', widget_name: str = None, widget_pos: str = 'besides', pos=-1):
    #     super().create_input(
    #         type_='data', label=label,
    #         add_config={'widget name': widget_name, 'widget pos': widget_pos} if widget_name else None,
    #         pos=pos
    #     )
    #
    # # --------------
