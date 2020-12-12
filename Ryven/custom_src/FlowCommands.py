from PySide2.QtWidgets import QUndoCommand

from custom_src.global_tools.class_inspection import find_type_in_object
from custom_src.NodeInstance import NodeInstance


class MoveComponents_Command(QUndoCommand):
    def __init__(self, flow, items_list, p_from, p_to):
        super(MoveComponents_Command, self).__init__()

        self.flow = flow
        self.items_list = items_list
        self.p_from = p_from
        self.p_to = p_to
        self.last_item_group_pos = p_to

    def undo(self):
        items_group = self.items_group()
        items_group.setPos(self.p_from)
        self.last_item_group_pos = items_group.pos()
        self.destroy_items_group(items_group)

    def redo(self):
        items_group = self.items_group()
        items_group.setPos(self.p_to - self.last_item_group_pos)
        self.destroy_items_group(items_group)


    def items_group(self):
        return self.flow.scene().createItemGroup(self.items_list)

    def destroy_items_group(self, items_group):
        self.flow.scene().destroyItemGroup(items_group)


class PlaceNodeInstanceInScene_Command(QUndoCommand):
    def __init__(self, flow, node_instance, pos):
        super(PlaceNodeInstanceInScene_Command, self).__init__()

        self.flow = flow
        self.node_instance = node_instance
        self.NI_pos = pos

    def undo(self):
        self.flow.remove_node_instance(self.node_instance)

    def redo(self):
        self.flow.add_node_instance(self.node_instance, self.NI_pos)


class PlaceDrawingObject_Command(QUndoCommand):
    def __init__(self, flow, posF, drawing_obj):
        super(PlaceDrawingObject_Command, self).__init__()

        self.flow = flow

        self.drawing_obj = drawing_obj
        self.drawing_obj_place_pos = posF
        self.drawing_obj_pos = self.drawing_obj_place_pos

    def undo(self):
        """Important: The drawing_obj_pos is not anymore the drawing_obj_place_pos here anymore because after the
        drawing object was completed, it's actual position got recalculated according to all points and differs from
        the initial pen press pos (=drawing_obj_place_pos). See DrawingObject.finished()."""

        self.drawing_obj_pos = self.drawing_obj.pos()

        self.flow.remove_component(self.drawing_obj)

    def redo(self):
        self.flow.add_drawing(self.drawing_obj, self.drawing_obj_pos)


class RemoveComponents_Command(QUndoCommand):
    def __init__(self, flow, items):
        super(RemoveComponents_Command, self).__init__()

        self.flow = flow
        self.items = items
        self.broken_connections = []  # the connections that go beyond the removed ports and need to be restored in undo

        self.node_instances = []
        for i in self.items:
            if find_type_in_object(i, NodeInstance):
                self.node_instances.append(i)

        self.connected_node_instances_indices_not_in_del_selection = []
        for n in self.node_instances:
            for i in n.inputs:
                for cpi in i.connected_port_instances:
                    cni = cpi.parent_node_instance
                    if cni not in self.node_instances:
                        self.broken_connections.append({
                            cpi: i
                        })
            for o in n.outputs:
                for cpi in o.connected_port_instances:
                    cni = cpi.parent_node_instance
                    if cni not in self.node_instances:
                        self.broken_connections.append({
                            o: cpi
                        })

    def undo(self):
        for i in self.items:
            self.flow.add_component(i)
        self.connect_gates()
        self.flow.select_components(self.items)

    def redo(self):
        self.connect_gates()
        for i in self.items:
            self.flow.remove_component(i)

    def connect_gates(self):
        for b_c in self.broken_connections:
            self.flow.connect_gates(list(b_c.keys())[0].gate, list(b_c.values())[0].gate)


class ConnectGates_Command(QUndoCommand):
    def __init__(self, flow, parent_port, child_port):
        super(ConnectGates_Command, self).__init__()

        self.flow = flow
        self.parent_port = parent_port
        self.child_port = child_port

    def undo(self):
        self.flow.connect_gates(self.parent_port.gate, self.child_port.gate)

    def redo(self):
        self.flow.connect_gates(self.parent_port.gate, self.child_port.gate)


class Paste_Command(QUndoCommand):
    def __init__(self, flow, data, offset_for_middle_pos):
        super(Paste_Command, self).__init__()

        self.flow = flow
        self.data = data
        self.offset_for_middle_pos = offset_for_middle_pos
        self.pasted_items = None
        self.pasted_node_instances = None
        self.pasted_drawing_objects = None

    def undo(self):
        for i in self.pasted_items:
            self.flow.remove_component(i)

    def redo(self):
        if self.pasted_items is None:
            new_node_instances = self.flow.place_nodes_from_config(self.data['nodes'],
                                                                   offset_pos=self.offset_for_middle_pos.toPoint())

            self.flow.connect_nodes_from_config(new_node_instances, self.data['connections'])

            new_drawing_objects = self.flow.place_drawings_from_config(self.data['drawings'],
                                                                       offset_pos=self.offset_for_middle_pos.toPoint())

            self.pasted_items = new_node_instances + new_drawing_objects
            self.pasted_node_instances = new_node_instances
            self.pasted_drawing_objects = new_drawing_objects
        else:
            self.flow.add_node_instances(self.pasted_node_instances)
            self.flow.add_drawings(self.pasted_drawing_objects)

        self.flow.select_components(self.pasted_items)