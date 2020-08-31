class NodeInstance_MainWidgetPlaceholder:
    def __getattr__(self, item):
        def method(*args):
            pass
        return method

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            return
        super(NodeInstance_MainWidgetPlaceholder, self).__setattr__(key, value)