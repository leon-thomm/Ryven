from custom_src.GlobalAttributes import Flow_AlgorithmMode


class PortInstance:
    def __init__(self, parent_node_instance, type_, label):
        self.parent_node_instance = parent_node_instance
        self.type_ = type_
        self.label = label
        self.connected_port_instances = []


    def get_val(self):
        pass


class OutputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_, label):
        super(OutputPortInstance, self).__init__(parent_node_instance, type_, label)

        self.val = None

    def exec(self):
        for cpi in self.connected_port_instances:
            cpi.update()

    def set_val(self, val):
        self.val = val

        if Flow_AlgorithmMode.mode_data_flow and not self.parent_node_instance.initializing:
            for cpi in self.connected_port_instances:
                cpi.update()

    def get_val(self):
        if not Flow_AlgorithmMode.mode_data_flow:
            self.parent_node_instance.update()
        return self.val


class InputPortInstance(PortInstance):
    def __init__(self, parent_node_instance, type_: str, label: str, widget_data: str):
        super(InputPortInstance, self).__init__(parent_node_instance, type_, label)

        self.val = None
        try:
            self.val = eval(widget_data)
        except Exception as e:
            self.val = widget_data

    def get_val(self):
        if len(self.connected_port_instances) == 0:
            return self.val
        else:
            return self.connected_port_instances[0].get_val()

    def update(self):
        if (self.parent_node_instance.is_active() and self.type_ == 'exec') or not self.parent_node_instance.is_active():
            self.parent_node_instance.update(self.parent_node_instance.inputs.index(self))