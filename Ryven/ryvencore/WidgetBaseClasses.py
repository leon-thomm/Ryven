class MWB:
    """MainWidgetBase"""
    def __init__(self, params):
        self.parent_node_instance = params

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass


class IWB:
    """InputWidgetBase"""
    def __init__(self, params):
        self.parent_port_instance, self.parent_node_instance = params

    def get_data(self):
        data = {}
        return data

    def set_data(self, data):
        pass

    def remove_event(self):
        pass
