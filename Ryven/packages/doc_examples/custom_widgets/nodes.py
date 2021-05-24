from NENV import *
widgets = import_widgets(__file__)  # this loads all exported widgets from widgets.py into the object


class MyNode(Node):
    title = 'my node'

    # this one gets automatically created once for each object
    main_widget_class = widgets.MyMainWidget
    main_widget_pos = 'below ports'  # or 'between ports'

    # you can use those for your data inputs
    input_widget_classes = {
        'my inp widget': widgets.MyInputWidget
    }
    # for example:
    init_inputs = [
        NodeInputBP(label='more data', add_config={'widget name': 'my inp widget', 'widget pos': 'below'})
    ]

    # or:
    def __init__(self, params):
        super().__init__(params)

        # note that this happens *before* init_inputs are being built
        self.create_input(label='some data', add_config={'widget name': 'my inp widget', 'widget pos': 'besides'})
        # the widget name must match your registered alias/key in the dict above
        # the widget pos can be 'besides' (the port pin) or 'below' (the port pin)

    def update_event(self, inp=-1):
        print('I have been updated!!')
        print(self.input(0), self.input(1))


export_nodes(
    MyNode,
)
