import pickle
import base64


class Variable:
    """Represents a variable. Unfortunately, I can't accomplish the same with a simple dict ({name: val}) in Script,
    because I need a ref to an object in VarsList_VarWidget to always show the current value and stuff"""

    def __init__(self, name='', val=None):
        super(Variable, self).__init__()

        self.name = name
        self.val = None
        if type(val) != dict:  # backwards compatibility
            try:
                self.val = pickle.loads(base64.b64decode(val))
            except Exception:
                self.val = val
        else:
            # if val.keys().__contains__('json'):
            #     self.val = val['json']
            if val.keys().__contains__('serialized'):
                self.val = pickle.loads(base64.b64decode(val['serialized']))

