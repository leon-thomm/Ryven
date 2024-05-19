"""
This file contains the implementations of undoable actions for FlowView.
"""

# prevent circular imports
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .FlowView import FlowView

from typing import Tuple

from qtpy.QtCore import QObject, QPointF
from qtpy.QtWidgets import QUndoCommand

from ryvencore import InfoMsgs, Flow


def undo_text_multi(items:list, command: str, to_str=None):
    """Generates a text for an undo command that has zero, one or multiple items"""
    
    if to_str is None:
        to_str = str
    
    if len(items) == 1:
        return f'{command} {to_str(items[0]) if to_str else items[0]}'
    elif len(items) == 0:
        return f'Clear-{command}'
    else:
        return f'Multi-{command}'


class FlowUndoCommand(QObject, QUndoCommand):
    """
    The main difference to normal QUndoCommands is the activate feature. This allows the flow widget to add the
    undo command to the undo stack before redo() is called. This is important since some of these commands can cause
    other commands to be added while they are performing redo(), so to prevent those commands to be added to the
    undo stack before the parent command, it is here blocked at first.
    """

    # prevent recursive calls of redo() and undo()
    _any_cmd_active = False

    def __init__(self, flow_view: FlowView) -> None:
        self.flow_view: FlowView = flow_view
        self.flow: Flow = flow_view.flow
        self._activated: bool = False

        QObject.__init__(self)
        QUndoCommand.__init__(self)

    def activate(self):
        self._activated = True
        self.redo()

    def redo(self) -> None:
        if not self._activated:
            return
        elif FlowUndoCommand._any_cmd_active:
            InfoMsgs.write_err(
                'FlowUndoCommand.redo() called while another FlowUndoCommand is active, '
                'most likely due to a recursive redo. This is not allowed. '
                'The editor is now in an undefined state. Save your work and restart the editor. '
            )
            return
        else:
            FlowUndoCommand._any_cmd_active = True
            self.redo_()
            FlowUndoCommand._any_cmd_active = False

    def undo(self) -> None:
        if FlowUndoCommand._any_cmd_active:
            InfoMsgs.write_err(
                'FlowUndoCommand.undo() called while another FlowUndoCommand is active, '
                'most likely due to a recursive undo. This is not allowed. '
                'The editor is now in an undefined state. Save your work and restart the editor. '
            )
            return
        FlowUndoCommand._any_cmd_active = True
        self.undo_()
        FlowUndoCommand._any_cmd_active = False

    def redo_(self):
        """subclassed"""
        pass

    def undo_(self):
        """subclassed"""
        pass


# (not currently used)
# class Nested_Command(FlowUndoCommand):
#     """Simple undo command nesting."""
#     def __init__(self, flow_view, *args):
#         super().__init__(flow_view)
#         self.commands = [arg for arg in args]
#         self.setText('Nested Command')
# 
#     def undo_(self):
#         for command in self.commands:
#             command.undo_()
#   
#     def redo_(self):
#         for command in self.commands:
#             command.redo_()


class Delegate_Command(FlowUndoCommand):
    """
    Custom undo command that delegates the undo and redo actions to two functions.
    """
    def __init__(self, flow_view, text: str, on_undo, on_redo):
        super().__init__(flow_view)
        self.setText(text)
        self._on_undo = on_undo
        self._on_redo = on_redo
    
    def undo_(self):
        self._on_undo()

    def redo_(self):
        self._on_redo()


class MoveComponents_Command(FlowUndoCommand):
    def __init__(self, flow_view, items_list, p_from, p_to):
        super(MoveComponents_Command, self).__init__(flow_view)

        self.items_list = items_list
        self.p_from = p_from
        self.p_to = p_to
        self.last_item_group_pos = p_to
        self.setText(undo_text_multi(self.items_list, 'Move'))

    def undo_(self):
        items_group = self.items_group()
        items_group.setPos(self.p_from)
        self.last_item_group_pos = items_group.pos()
        self.destroy_items_group(items_group)
        for item in self.items_list:
            item.on_move()

    def redo_(self):
        items_group = self.items_group()
        items_group.setPos(self.p_to - self.last_item_group_pos)
        self.destroy_items_group(items_group)
        for item in self.items_list:
            item.on_move()
        
    def items_group(self):
        return self.flow_view.scene().createItemGroup(self.items_list)

    def destroy_items_group(self, items_group):
        self.flow_view.scene().destroyItemGroup(items_group)


class PlaceNode_Command(FlowUndoCommand):
    def __init__(self, flow_view, node_class, pos):
        super().__init__(flow_view)

        self.node_class = node_class
        self.node = None
        self.item_pos = pos
        self._prev_selected = flow_view._current_selected

    def undo_(self):
        self.flow.remove_node(self.node)
        self.flow_view.select_items(self._prev_selected)

    def redo_(self):
        if self.node:
            self.flow.add_node(self.node)
        else:
            self.node = self.flow.create_node(self.node_class)
        self.setText(f'Create {self.node.gui.item}')


class PlaceDrawing_Command(FlowUndoCommand):
    def __init__(self, flow_view, posF, drawing):
        super().__init__(flow_view)

        self.drawing = drawing
        self.drawing_obj_place_pos = posF
        self.drawing_obj_pos = self.drawing_obj_place_pos
        self._prev_selected = flow_view._current_selected

    def undo_(self):
        # The drawing_obj_pos is not anymore the drawing_obj_place_pos because after the
        # drawing object was completed, its actual position got recalculated according to all points and differs from
        # the initial pen press pos (=drawing_obj_place_pos). See DrawingObject.finished().

        self.drawing_obj_pos = self.drawing.pos()

        self.flow_view.remove_component(self.drawing)
        self.flow_view.select_items(self._prev_selected)

    def redo_(self):
        self.flow_view.add_drawing(self.drawing, self.drawing_obj_pos)
        self.setText(self.drawing(True))


class SelectComponents_Command(FlowUndoCommand):
    def __init__(self, flow_view, new_items, prev_items):
        super().__init__(flow_view)
        self.items = new_items
        self.prev_items = prev_items
        self.setText(undo_text_multi(self.items, 'Select'))
        
    def redo_(self):
        self.flow_view.select_items(self.items)
    
    def undo_(self):
        self.flow_view.select_items(self.prev_items)


class RemoveComponents_Command(FlowUndoCommand):
    def __init__(self, flow_view, items):
        super().__init__(flow_view)
        self.items = items
        self.selection = flow_view._current_selected
        self.setText(undo_text_multi(self.items, 'Delete'))
        
        self.broken_connections = (
            set()
        )  # the connections that go beyond the removed nodes and need to be restored in undo
        self.internal_connections = set()

        self.node_items = []
        self.nodes = []
        self.drawings = []

        # importing here to prevent circular imports
        from .nodes.NodeItem import NodeItem
        from .connections.ConnectionItem import ConnectionItem
        from .drawings.DrawingObject import DrawingObject
        
        for i in self.items:
            if isinstance(i, NodeItem):
                self.node_items.append(i)
                self.nodes.append(i.node)
            elif isinstance(i, DrawingObject):
                self.drawings.append(i)

        # for connections
        for i in self.items:
            if not isinstance(i, ConnectionItem):
                continue
            out_port, _ = i.connection
            if out_port.node not in self.nodes:
                self.broken_connections.add(i.connection)

        for n in self.nodes:
            for i in n.inputs:
                cp = n.flow.connected_output(i)
                if cp is not None:
                    cn = cp.node
                    if cn not in self.nodes:
                        self.broken_connections.add((cp, i))
                    else:
                        self.internal_connections.add((cp, i))
            for o in n.outputs:
                for cp in n.flow.connected_inputs(o):
                    cn = cp.node
                    if cn not in self.nodes:
                        self.broken_connections.add((o, cp))
                    else:
                        self.internal_connections.add((o, cp))

    def undo_(self):
        # add nodes
        for n in self.nodes:
            self.flow.add_node(n)

        # add drawings
        for d in self.drawings:
            self.flow_view.add_drawing(d)

        # add connections
        self.restore_broken_connections()
        self.restore_internal_connections()
        
        # removing the items means something was probably selected
        # restore the selection
        self.flow_view.select_items(self.selection)

    def redo_(self):
        # remove connections
        self.remove_broken_connections()
        self.remove_internal_connections()

        # remove nodes
        for n in self.nodes:
            self.flow.remove_node(n)

        # remove drawings
        for d in self.drawings:
            self.flow_view.remove_drawing(d)

    def restore_internal_connections(self):
        for c in self.internal_connections:
            self.flow.add_connection(c)

    def remove_internal_connections(self):
        for c in self.internal_connections:
            self.flow.remove_connection(c)

    def restore_broken_connections(self):
        for c in self.broken_connections:
            self.flow.add_connection(c)

    def remove_broken_connections(self):
        for c in self.broken_connections:
            self.flow.remove_connection(c)


class ConnectPorts_Command(FlowUndoCommand):
    def __init__(self, flow_view, out, inp):
        super().__init__(flow_view)

        # CAN ALSO LEAD TO DISCONNECT INSTEAD OF CONNECT!!

        self.out = out
        self.inp = inp
        self.connection = None
        self.connecting = True

        for i in flow_view.flow.connected_inputs(out):
            if i == self.inp:
                self.connection = (out, i)
                self.connecting = False

    def undo_(self):
        if self.connecting:
            # remove connection
            self.flow.remove_connection(self.connection)
        else:
            # recreate former connection
            self.flow.add_connection(self.connection)

    def redo_(self):
        if self.connecting:
            if self.connection:
                self.flow.add_connection(self.connection)
            else:
                # connection hasn't been created yet
                self.connection = self.flow.connect_nodes(self.out, self.inp)
            self.setText(f'Connect {self.flow_view.connection_items[self.connection]}')
            
        else:
            # remove existing connection
            self.setText(f'Disconnect {self.flow_view.connection_items[self.connection]}')
            self.flow.remove_connection(self.connection)
        

class Paste_Command(FlowUndoCommand):
    def __init__(self, flow_view, data, offset_for_middle_pos):
        super().__init__(flow_view)

        self.data = data
        self.modify_data_positions(offset_for_middle_pos)
        self.pasted_components = None
        self.setText('Paste')

    def modify_data_positions(self, offset):
        """adds the offset to the components' positions in data"""

        for node in self.data['nodes']:
            node['pos x'] = node['pos x'] + offset.x()
            node['pos y'] = node['pos y'] + offset.y()
        for drawing in self.data['drawings']:
            drawing['pos x'] = drawing['pos x'] + offset.x()
            drawing['pos y'] = drawing['pos y'] + offset.y()

    def redo_(self):
        if self.pasted_components is None:
            self.pasted_components = {}

            # create components
            self.create_drawings()

            (
                self.pasted_components['nodes'],
                self.pasted_components['connections'],
            ) = self.flow.load_components(
                nodes_data=self.data['nodes'],
                conns_data=self.data['connections'],
                output_data=self.data['output data'],
            )

            self.select_new_components_in_view()
        else:
            self.add_existing_components()

    def undo_(self):
        # remove components and their items from flow
        for c in self.pasted_components['connections']:
            self.flow.remove_connection(c)
        for n in self.pasted_components['nodes']:
            self.flow.remove_node(n)
        for d in self.pasted_components['drawings']:
            self.flow_view.remove_drawing(d)

    def add_existing_components(self):
        # add existing components and items to flow
        for n in self.pasted_components['nodes']:
            self.flow.add_node(n)
        for c in self.pasted_components['connections']:
            self.flow.add_connection(c)
        for d in self.pasted_components['drawings']:
            self.flow_view.add_drawing(d)

        self.select_new_components_in_view()

    def select_new_components_in_view(self):
        self.flow_view.clear_selection()
        for d in self.pasted_components['drawings']:
            d.setSelected(True)
        for n in self.pasted_components['nodes']:
            node_item = self.flow_view.node_items[n]
            node_item.setSelected(True)

    def create_drawings(self):
        drawings = []
        for d in self.data['drawings']:
            new_drawing = self.flow_view.create_drawing(d)
            self.flow_view.add_drawing(
                new_drawing, posF=QPointF(d['pos x'], d['pos y'])
            )
            drawings.append(new_drawing)
        self.pasted_components['drawings'] = drawings
