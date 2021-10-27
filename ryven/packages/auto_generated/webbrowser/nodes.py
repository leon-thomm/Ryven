
from NENV import *

import webbrowser


class NodeBase(Node):
    pass


class _Synthesize_Node(NodeBase):
    """
    Attempt to synthesize a controller based on existing controllers.

    This is useful to create a controller when a user specifies a path to
    an entry in the BROWSER environment variable -- we can copy a general
    controller to operate using a specific installation of the desired
    browser in this way.

    If we can't create a controller in this way, or if there is no
    executable for the requested browser, return [None, None].

    """
    
    title = '_synthesize'
    type_ = 'webbrowser'
    init_inputs = [
        NodeInputBP(label='browser'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser._synthesize(self.input(0)))
        

class Get_Node(NodeBase):
    """
    Return a browser launcher instance appropriate for the environment."""
    
    title = 'get'
    type_ = 'webbrowser'
    init_inputs = [
        NodeInputBP(label='using', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.get(self.input(0)))
        

class Main_Node(NodeBase):
    """
    """
    
    title = 'main'
    type_ = 'webbrowser'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.main())
        

class Open_Node(NodeBase):
    """
    Display url using the default browser.

    If possible, open url in a location determined by new.
    - 0: the same browser window (the default).
    - 1: a new browser window.
    - 2: a new browser page ("tab").
    If possible, autoraise raises the window (the default) or not.
    """
    
    title = 'open'
    type_ = 'webbrowser'
    init_inputs = [
        NodeInputBP(label='url'),
        NodeInputBP(label='new', dtype=dtypes.Data(default=0, size='s')),
        NodeInputBP(label='autoraise', dtype=dtypes.Data(default=True, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.open(self.input(0), self.input(1), self.input(2)))
        

class Open_New_Node(NodeBase):
    """
    Open url in a new window of the default browser.

    If not possible, then open url in the only browser window.
    """
    
    title = 'open_new'
    type_ = 'webbrowser'
    init_inputs = [
        NodeInputBP(label='url'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.open_new(self.input(0)))
        

class Open_New_Tab_Node(NodeBase):
    """
    Open url in a new page ("tab") of the default browser.

    If not possible, then the behavior becomes equivalent to open_new().
    """
    
    title = 'open_new_tab'
    type_ = 'webbrowser'
    init_inputs = [
        NodeInputBP(label='url'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.open_new_tab(self.input(0)))
        

class Register_Node(NodeBase):
    """
    Register a browser connector."""
    
    title = 'register'
    type_ = 'webbrowser'
    init_inputs = [
        NodeInputBP(label='name'),
        NodeInputBP(label='klass'),
        NodeInputBP(label='instance', dtype=dtypes.Data(default=None, size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.register(self.input(0), self.input(1), self.input(2)))
        

class Register_X_Browsers_Node(NodeBase):
    """
    """
    
    title = 'register_X_browsers'
    type_ = 'webbrowser'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.register_X_browsers())
        

class Register_Standard_Browsers_Node(NodeBase):
    """
    """
    
    title = 'register_standard_browsers'
    type_ = 'webbrowser'
    init_inputs = [
        
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, webbrowser.register_standard_browsers())
        


export_nodes(
    _Synthesize_Node,
    Get_Node,
    Main_Node,
    Open_Node,
    Open_New_Node,
    Open_New_Tab_Node,
    Register_Node,
    Register_X_Browsers_Node,
    Register_Standard_Browsers_Node,
)
