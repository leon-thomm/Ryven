from NENV import *


# 
#  = load_from_file(file='widgets.py', callee_file=__file__, components_list=[
#         ''
#     ], gui=True)


import threading



class ThreadSplitter(Node):
    title = 't_split'
    description = 'Controls thread execution branches'

    init_inputs = [
        NodeInputBP(),
    ]
    init_outputs = [
        NodeOutputBP(),
        NodeOutputBP(),
    ]

    def update(self, input_called=-1):
        threads = []
        data = self.input(0)
        for out in self.outputs:
            for c in out.connections:
                threads.append(
                    threading.Thread(target=c.activate, args=(data, ))
                )

        for th in threads:
            th.start()





nodes = [
    ThreadSplitter,
]
