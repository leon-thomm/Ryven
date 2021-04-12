from ryvencore_qt import *


class Print_Node(Node):
    title = 'print'
    
    def __init__(self, params):
        super(Print_Node, self).__init__(params)

        self.special_actions['print something 1'] = {'method': self.print_something,
                                                     'data': 'hello!!'}
        self.special_actions['print something 2'] = {'method': self.print_something,
                                                     'data': 'HELLOO!?!?!?'}

    def update_event(self, input_called=-1):
        if input_called == 0:
            print(self.input(1))
            self.exec_output(0)

    def print_something(self, data):
        print(data)


class Button_Node(Node):
    title = 'button'

    def button_clicked(self):
        self.update()

    def update_event(self, input_called=-1):
        self.exec_output(0)
