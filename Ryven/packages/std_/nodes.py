from NENV import *
widgets = import_widgets()


# ButtonNode_MainWidget, \
#  = load_from_file(file='widgets.py', caller_file=__file__, components_list=[
#         'ButtonNode_MainWidget',
#     ], gui=True)




class ButtonNode(Node):
    title = 'Button'
    main_widget_class = widgets.ButtonNode_MainWidget
    main_widget_pos = 'between ports'
    init_inputs = [

    ]
    init_outputs = [
        NodeOutputBP('exec')
    ]
    color = '#3344ff'

    def update_event(self, input_called=-1):
        self.exec_output(0)


export_nodes(
    ButtonNode,
)
