class Variable:
    """Represents a variable. Unfortunately, I can't accomplish the same with a simple dict ({name: val}) in Script,
    because I need a ref to an object in VarsList_VarWidget to always show the current value and stuff"""
    def __init__(self, name='', val=None):
        self.name = name
        self.val = val