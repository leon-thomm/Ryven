
from NENV import *

import contextlib


class NodeBase(Node):
    pass


class Asynccontextmanager_Node(NodeBase):
    """
    @asynccontextmanager decorator.

    Typical usage:

        @asynccontextmanager
        async def some_async_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        async with some_async_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
    """
    
    title = 'asynccontextmanager'
    type_ = 'contextlib'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, contextlib.asynccontextmanager(self.input(0)))
        

class Contextmanager_Node(NodeBase):
    """
    @contextmanager decorator.

    Typical usage:

        @contextmanager
        def some_generator(<arguments>):
            <setup>
            try:
                yield <value>
            finally:
                <cleanup>

    This makes this:

        with some_generator(<arguments>) as <variable>:
            <body>

    equivalent to this:

        <setup>
        try:
            <variable> = <value>
            <body>
        finally:
            <cleanup>
    """
    
    title = 'contextmanager'
    type_ = 'contextlib'
    init_inputs = [
        NodeInputBP(label='func'),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, contextlib.contextmanager(self.input(0)))
        

class Wraps_Node(NodeBase):
    """
    Decorator factory to apply update_wrapper() to a wrapper function

       Returns a decorator that invokes update_wrapper() with the decorated
       function as the wrapper argument and the arguments to wraps() as the
       remaining arguments. Default arguments are as for update_wrapper().
       This is a convenience function to simplify applying partial() to
       update_wrapper().
    """
    
    title = 'wraps'
    type_ = 'contextlib'
    init_inputs = [
        NodeInputBP(label='wrapped'),
        NodeInputBP(label='assigned', dtype=dtypes.Data(default=('__module__', '__name__', '__qualname__', '__doc__', '__annotations__'), size='s')),
        NodeInputBP(label='updated', dtype=dtypes.Data(default=('__dict__',), size='s')),
    ]
    init_outputs = [
        NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, inp=-1):
        self.set_output_val(0, contextlib.wraps(self.input(0), self.input(1), self.input(2)))
        


export_nodes(
    Asynccontextmanager_Node,
    Contextmanager_Node,
    Wraps_Node,
)
