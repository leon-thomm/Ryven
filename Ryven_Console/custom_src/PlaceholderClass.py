class PlaceholderClass:
    def __getattr__(self, item):
        def method(*args):
            pass
        return method

    def __setattr__(self, key, value):
        if not hasattr(self, key):
            return
        super(PlaceholderClass, self).__setattr__(key, value)