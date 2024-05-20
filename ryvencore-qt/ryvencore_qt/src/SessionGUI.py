from typing import List, Dict

from qtpy.QtCore import QObject, Signal, Qt
from qtpy.QtWidgets import QWidget, QApplication

import ryvencore

from .flows.FlowView import FlowView
from .Design import Design
from .GUIBase import GUIBase


class SessionGUI(GUIBase, QObject):
    """
    ryvencore-qt's Session wrapper class, implementing the GUI.
    Any session with a GUI must be created through this class.
    Access the ryvencore session through the :code:`session`
    attribute, and the GUI from the ryvencore session through the
    :code:`gui` attribute. Once instantiated, you can simply use
    the :code:`session` directly to create, rename, delete flows,
    register nodes, etc.
    """

    flow_created = Signal(object)
    flow_deleted = Signal(object)
    flow_renamed = Signal(object, str)
    flow_view_created = Signal(object, object)

    def __init__(self, gui_parent: QWidget):
        GUIBase.__init__(self)
        QObject.__init__(self)

        self.core_session = ryvencore.Session(gui=True, load_addons=True)
        setattr(self.core_session, 'gui', self)

        self.gui_parent = gui_parent

        # flow views
        self.flow_views: Dict[ryvencore.Flow, FlowView] = {}

        # register complete_data function
        ryvencore.set_complete_data_func(self.get_complete_data_function(self))

        # load design
        app = QApplication.instance()
        app.setAttribute(Qt.AA_UseHighDpiPixmaps)
        Design.register_fonts()
        self.design = Design()

        # connect to session
        self.core_session.flow_created.sub(self._flow_created)
        self.core_session.flow_deleted.sub(self._flow_deleted)
        self.core_session.flow_renamed.sub(self._flow_renamed)

    def _flow_created(self, flow: ryvencore.Flow):
        """
        Builds the flow view for a newly created flow, saves it in
        self.flow_views, and emits the flow_view_created signal.
        """
        self.flow_created.emit(flow)

        self.flow_views[flow] = FlowView(
            session_gui=self,
            flow=flow,
            parent=self.gui_parent,
        )
        self.flow_view_created.emit(flow, self.flow_views[flow])

        return flow

    def _flow_deleted(self, flow: ryvencore.Flow):
        """
        Removes the flow view for a deleted flow from self.flow_views.
        """
        self.flow_views.pop(flow)
        self.flow_deleted.emit(flow)

    def _flow_renamed(self, flow: ryvencore.Flow, new_name: str):
        """
        Renames the flow view for a renamed flow.
        """
        self.flow_renamed.emit(flow, new_name)