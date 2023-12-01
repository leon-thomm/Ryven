from random import random, Random
from ryvencore import Node, NodeInputType, NodeOutputType, Data
from ryven.node_env import export_nodes, on_gui_load
from traits.api import HasTraits, Str, Int, Range, Enum, observe, Any, File, Instance, Float, Bool, Event


class RandNode(Node):
    """Generates scaled random float values"""

    class RandNodeConfig(HasTraits):
        # auto_set, enter_set allow the any_trait_changed to be called only when pressing enter
        # to play nicely with undo / redo
        scale: float = Float(1, auto_set=False, enter_set=True)
        use_seed: bool = Bool
        seed: int = Int(0, auto_set=False, enter_set=True)
        generate = Event
        
        _node = Instance(klass=Node, visible=False)
        traits_view = None  # must be included if one wants to use the observe decorator
        on_trait: list = []
        on_val: list = []
        ran_gen: Random = Random()

        # @observe('*') the decorator doesn't allow removal of notifications
        def any_trait_changed(self, event):
            node: RandNode = self._node
            # generates a new random when pressing the button
            if event.name == 'generate':
                prev = node.val
                node.generate_new_val()
                for e in self.on_val:
                    e(prev, node.val)
            
            # state change events (scale, use_seed, seed)
            else:
                for e in self.on_trait:
                    e(event)

        def allow_notifications(self):
            self.observe(self.any_trait_changed, '*')

        def block_notifications(self):
            self.observe(self.any_trait_changed, '*', remove=True)

    title = 'Rand'
    tags = ['random', 'numbers']
    init_outputs = [NodeOutputType(label='out')]

    def __init__(self, params):
        self.config = RandNode.RandNodeConfig()
        self.config._node = self
        self.config.allow_notifications()
        self.val = None
        super().__init__(params)
    
    def place_event(self): # must be here (there should be one output value)
        self.update()
        
    def update_event(self, inp=-1):
        self.generate_new_val()
        self.set_output_val(0, Data(self.val))

    def generate_new_val(self):
        self.val = self.config.scale * (
            random() if self.config.use_seed else self.config.ran_gen.random()
        )

class PrintNode(Node):
    title = 'Print'
    init_inputs = [NodeInputType()]

    def update_event(self, inp=-1):
        data = self.input(0)
        if not data:
            return
        print(data.payload)


export_nodes([RandNode, PrintNode])


@on_gui_load
def load_gui():
    from . import gui
