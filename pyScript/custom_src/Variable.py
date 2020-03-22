


# unfortunately, I can't accomplish the same with a simple dice ({name: val}) in Script, because I need a ref to an
# object in VarsList_VarWidget to always show the current value and stuff
class Variable:
    def __init__(self, name='', val=None):
        self.name = name
        self.val = val