def retain(foo):
    """This method is very important for live source code manipulation. It ensures, that every reference to an object's
    method is going to change when the method has been edited (and therefore been overridden). If a reference to a
    method is made by providing the method object without calling retain(self.mymethod) or M(self.mymethod), changing
    this method in Ryven will not result in different behavior when the previously created reference is being called."""

    return lambda *args, **kwargs: getattr(foo.__self__, foo.__name__)(*args, **kwargs)


class M:
    def __init__(self, method):
        self.method_name = method.__name__
        self.method = retain(method)

    def __call__(self, *args, **kwargs):
        self.method(*args, **kwargs)
