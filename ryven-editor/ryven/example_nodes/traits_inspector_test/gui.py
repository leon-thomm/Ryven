from .nodes import *
from ryven.gui_env import inspector_gui
from ryvencore_qt.src.flows.nodes.InspectorGUI import NodeInspector
from traitsui.api import View, Item, ButtonEditor, Group
from ryvencore_qt.src.flows.FlowCommands import Delegate_Command
from collections import deque

@inspector_gui(RandNode)
class RandNodeInspector(NodeInspector):
    @property
    def config(self):
        return self.node.config

    def attach_inspector(self, parent):
        self.node: RandNode = self.node  # help with auto-complete

        view = self.config.trait_view()
        # This could be None, but wanted to a label and a border
        view = View(
            Group(
                *tuple(Item(name) for name in self.config.visible_traits()),
                Item("generate", show_label=False, editor=ButtonEditor(label="Generate!")),
                label="Config",
                show_border=True,
            )
        )
        self.ui = self.config.edit_traits(
            parent=parent.layout(), kind='subpanel', view=view
        ).control
        self.config.on_trait.append(self.on_trait_changed)
        self.config.on_val.append(self.on_val_changed)
        parent.layout().addWidget(self.ui)

    def unload(self):
        self.config.on_trait.remove(self.on_trait_changed)
        self.config.on_val.remove(self.on_val_changed)
        self.ui.setParent(None)
        super().unload()

    def on_val_changed(self, prev_val, new_val):
        def undo_redo(value):
            def _undo_redo():
                self.node.set_output_val(0, Data(value))
            return _undo_redo
        
        self.flow_view._push_undo(
            Delegate_Command(self.flow_view, f'Update {prev_val} -> {new_val}', undo_redo(prev_val), undo_redo(new_val))
        )
    
    def on_trait_changed(self, trait_event):
        print(f'Trait "{trait_event.name}" changed from {trait_event.old} to {trait_event.new}')
        # otherwise an enter event for a text editor wouldn't stop text editing
        self.flow_view.setFocus()
        if trait_event.name == trait_event.new:
            return

        def undo_redo(value):
            def _undo_redo():
                self.config.block_notifications()
                setattr(self.config, trait_event.name, value)
                if trait_event.name == 'seed':
                        self.config.ran_gen.seed = value
                self.config.allow_notifications()

            return _undo_redo

        self.flow_view._push_undo(
            Delegate_Command(self.flow_view, f'Config Change {trait_event.name} {trait_event.old} -> {trait_event.new}', undo_redo(trait_event.old), undo_redo(trait_event.new))
        )

    # def create_inspector(self, parent: QWidget):
    #    node: RandNode = self.node
    #
    #    ui = node.config.edit_traits(parent=parent.layout(), kind = 'subpanel').control
    #    parent.layout().addWidget(ui) # or simply return ui
