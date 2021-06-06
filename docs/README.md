<center><img src="./img/logo.png" style="max-width: 500px" /></center>

## Project Idea

Ryven is an editor for flow-based visual scripting in Python. It is easy to create new and use existing nodes executing any python code. I developed an underlying Python framework for building editors like Ryven. `ryvencore` is the backend, implementing the abstract functionality, while `ryvencore-qt` uses `ryvencore` and provides a Qt-based frontend. The Ryven editor is now based on `ryvencore-qt` and implements most of its features (excluding threading compatibility so far). While Ryven is supposed to be general purpose, `ryvencore-qt` can be used to create fundamentally similar but specialized editors. Nodes developed for Ryven are usually easily migratable to other editors made with `ryvencore-qt`. When programming nodes, you are using the framework's API. This API is easy to use but quite powerful, so you can build quite sophisticated nodes. `ryvencore` might be the base for implementing different frontends some day, including web.

Flows you made in Ryven can be deployed directly on `ryvencore` (via *Ryven Console*, simply run `ryven console`) without any frontend related dependencies (including Qt).

![](img/screenshot1.png)

## Differences to Ryven 2

Ryven 3 is a complete remake, now based on the framework, where many internal implementations have drastically changed. I completely removed the former *NodeManager* since the new nodes system makes it pretty much useless. There is no such thing as a *NodeInstance* anymore, everything is just nodes. All information about a node is now part of its class, so there is no need for .rpc files anymore, a node package is simply defined by the node definitions in `nodes.py`, see below. Ryven 3 is a much more consistent piece of software with focus on ease of use and scalability. You probably won't be able to port your old projects, because there's too much that changed. The future of Ryven 3 will also depend on contributions.

## Flows

A **Script** contains a **Flow**, a **Logger**, and a **Variables Manager**. A special type of script is a **Macro** which additionally has an input and output node representing parameters and returns, which can be called by using the node that is automatically registered for it.

Unlike most other flow-based visual scripting editors, Ryven supports *data connections* **and** *exec connections*. Data connections transmit data from one node to another, and exec connections only transmit a trigger signal. Pure data flows (only data connections) are like the UE4 Material Editor, while exec flows (some exec connections) are more like the UE4 BluePrints. You can choose the appropriate algorithm (*data flow* or *exec flow*) in every script.

> [!NOTE|label:The Differences in Detail]
> *If you don't have experience with the flow-based programming idea already you can skip this, these differences don't really matter for now.*
> 
> ### Data Flows
> 
> In a data flow, every change of data (which means that a data output of a node has been changed via `self.set_output_val()`) gets forward propagated and causes an update event in all connected nodes. In the example below, changing the slider value would therefore cause immediate updates and a visible change in the result node on the right.
> 
> <center><img src="./img/data_flow_example.png" style="max-width: 900px" /></center>
> 
> ### Exec Flows
> 
> In execution flows, data isn't forward propagated on change, but generated on request (backwards), only causing update events in affected nodes once the data of an output is requested somewhere (through `Node.input()`). In the example above, changing the slider value would not lead to a change in the result node in an exec flow, but if an active node requests this data, like shown below, then the whole expression gets executed.
> 
> <center><img src="./img/exec_flow_example.png" style="max-width: 900px" /></center>
> 
> The data flow paradigm is the more fundamental one, and there might be changes for the exec mode in the future.
> 
> While you can choose the according mode for a flow, it turned out to be a use case too to use the data flow mode in combination with few exec connections. This can lead to performance issues, but is quite powerful if used in the right way. Ultimately, both paradigms are possible. For more precise definitions on the aspects of flow execution, see [ryvencore-qt features](https://leon-thomm.github.io/ryvencore-qt/#/features).

## Editor Overview

### Running Ryven

After installing the application, following the instructions on [GitHub](https://github.com/leon-thomm/Ryven), you can run Ryven by running `ryven` on the console, or by opening `Ryven.py` with Python.

### Flows

The flow supports all usual actions, including undo/redo operations. You can place nodes by right-clicking and pan around by right clicking and dragging the scene.

> [!NOTE]
> I would like to add sophisticated touch support, but there are Qt bugs that are not being tackled making this difficult, at least with PySide2.

There are many different themes for the flows, which you can select in the menu at the top of the window. Furthermore, when nodes update, they blink so you can easily see what's going on. There is also a performance mode which you can change to `fast` to significantly simplify the rendering of the components for weaker hardware or large flows. I already introduced some caching, but the performance is usually still not so great in `pretty` mode.

### Console

The console, located at the bottom of the window, runs a Python REPL. Additionally, you can right click on a node to add a reference to it to the console scope, so you can directly access the node's whole API at any time. This is a really powerful feature, no matter if you would like to quickly access a few intern variables or perform some temporary modifications on the node (like adding/removing inputs/outputs), you have full control there.

> [!TIP|label:Session Access]
> The session object (which is basically the project) is added to the console automatically, so you can type `session` to access it and do pretty much *everything* from there. You can play around with the `ryvencore-qt` API, for example try creating a new script via `session.create_script('hello there!')`. Due to the fully signals-based communication between `ryvencore` and `ryvencore-qt`, the frontend will react accordingly to everything you do in the console.

### Script Variables

The script variables, located on the right, can be modified at any time by right-clicking on them, and when you hover over one, you can see its current value and data type. The values of those variables are usually accessed and changed by your nodes. The API provides a few very simple but really powerful methods for nodes to register as *variable receivers*. Basically, a node can dynamically register as a receiver for script variables by providing a var name and a method that is supposed to be called whenever a script variable with that name changes (or is created). I particularly like this feature, as you can easily build highly sophisticated nodes using this that automatically adapt to change of data.

> [!TIP|label:Example]
> In one of the node packages Ryven comes with, there's a *Matrix* node where you can just type a few numbers into a small textedit and it creates a numpy array out of them. But you can also type in `v('')` and the name of a script variable (instead of a number) which makes the matrix node register as a receiver, so it updates and regenerates the matrix every time the value of a script variable with that name changed. You can see this in action in the big screenshot above. In the console you can see I manually changed the variable's value which caused the matrix node to update.

### Logs

Every script has logs of type `logging.Logger` of python's builtin `logging` module. The script's logs are located at the bottom, above the console. The nodes can access default logs via the API, and also instanciate new ones.

### Source Code Preview

Next to the logs is the source code area where you can inspect the source code of the last selected node (click into the text field for syntax highlighting), and also edit method implementations of single objects. That's right, you can override method implementations of single objects. All these changes are temporary (they don't get saved) and only apply on the currently selected object. It's a great way to play around or debug your components, especially when combining this with the console. For example you can just add some output to one of your nodes via the console, and then modify the update event of it to provide some additional data there via the source code preview. This is a really useful feature, however as you might suspect, modifying an object's method implementation is not exactly conventional and doesn't work in all cases. For example, when you created references somewhere else to this modified method, those references will still point to the old implementation of it.

> [!TIP|label:How to fix this]
> If you need to reference methods directly somewhere (for example when passing them as 'variable receiver'), you could use a workaround by, instead of passing the actual method reference, passing a lambda causing a new search for the newest version whenever the method is called, like this
> ```python
def retain(foo):
    return lambda *args, **kwargs: getattr(foo.__self__, foo.__name__)(*args, **kwargs)
> ```
> And when referencing, for example:
> ```python
self.register_var_receiver('x', retain(self.my_method))
> ```

It usually works quite well, but there might be some bugs since the implementation in Ryven 3 hasn't been extensively tested yet.

### Rendering Flow Images

You can render images of the currently displayed flow, also via the top menus. By rendering the viewport, the picture will show what's currently visible of the flow, in the exact same resolution it is currently displayed. For high res pictures render the whole scene and zoom to the top left, the zoom factor will determine the exact resolution of your image. It can take a few seconds to render high resolution images.

### Save&Load

You can save via `ctrl+s` and choose to load a project when starting the application. To import a nodes package, you can also hit `ctrl+i`.

For programming your own nodes (see below), you only need to follow the rule that all API provided features are saved and reloaded automatically, for example the current inputs and outputs, display title, as well as special actions.

## Programming Nodes

And there we go. Programming new nodes is at the heart of all this, you need basic Python knowledge but nothing advanced.

> [!NOTE|label:Overview]
> In Ryven, nodes are organized in *node packages*. A node package consists of a package folder (its name is the name of the package), and a file `nodes.py` where you define your node classes. Ryven comes with its own packages folder, but if you installed it via `pip` you should define another one somewhere on your file system, so your packages don't get lost when you update the Ryven installation. For additional custom widgets you create a file `widgets.py` in the same dir which has a similar structure to `nodes.py`. In `nodes.py` you define subclasses of `Node`, set basic properties by editing static class attributes and add functionality mainly through using event methods from `Node`. You can find an example package in the Example section below.

> [!NOTE]
> There is no requirement to have only one level of `Node` class inheritance and file locality. When packages get larger it's usually better to define your own `NodeBase` class(es), decentralize your node definitions into multiple modules, and just import them in `nodes.py`. You will specify all the exact nodes that you want to expose in `export_nodes()`, see below.

A node is defined by its Python class. You basically subclass the `Node` class from Ryven, specify pre-defined attributes and methods and enhance it the way you like. For example:

```python
class MyPrintNode(Node):
    title = 'print'
    init_inputs = [
        NodeInputBP()
    ]

    def update_event(self, inp=-1):
        print(self.input(0))
```

This simple node gets updated when data arrives at its only input, causing an update event. Then, we just print this data and that's basically it. The static attributes at the top define basic properties that equally apply on all nodes of this type (all such `print` nodes here), and there are various methods (defined in `Node`) you can reimplement to do more sophisticated stuff.

### Important Methods

<!-- There are a few more methods that might be important, especially when building complex 'sequential' nodes which need to correctly reconstruct their state. -->

The `place_event` is called every time the node is added to the flow. Notice that this can happen multiple times, for example when undoing a remove operation in the flow, but also when the node is first constructed and placed in the flow. The `place_event` is called *before* any incident connections are built, so it is sometimes used to trigger updates since setting outputs does not affect any other nodes.


> [!TIP|label:Example]
> ```python
class MyNode(Node):
    def place_event(self):
        self.update()
> ```

Just like the `place_event`, there's a `remove_event` called every time the node is removed from the flow (this too can happen multiple times).


> [!TIP|label:Example]
> ```python
class MyNode(Node):
    def remove_event(self):
        self.timer.stop()
> ```

In contrast to the `place_event`, the `view_place_event` is called once the whole GUI of the node (including custom widgets) has initialized, which is important when using custom widgets, see below. Only do GUI related work here, as this method of  course is never called when running the node on ryven console since there does not exist any GUI then.


> [!TIP|label:Example]
> ```python
class MyNode(Node):
    def view_place_event(self):
        self.main_widget().update()
> ```

#### Nodes with States

If your node has states, which means its behavior depends on the values of internal variables, to be able to reconstruct the current state when loading a project or pasting the node after copying an instance of it, use the `get_state()` and `set_state()` methods.

```python
class StoreDataNode(Node):
    title='store'
    init_inputs=[
        NodeInputBP()
    ]

    def __init__(self, params):
        super().__init__(params)

        self.storage = []

    def update_event(self, inp=-1):
        self.storage.append(self.input(0))
    
    def get_state(self) -> dict:
        # assuming only pickle serializable data is stored in self.storage
        return {
            'data': self.storage
        }
    
    def set_state(self, data: dict):
        self.storage = data['data']
```

By default nodes are updated possibly multiple times while the flow is building up, which is the usual situation for 'combinational' nodes (no states, like a `+` node). However, with sequential nodes you don't want the node's state to change due to the flow building process. You can disable updates on flow building by just setting the attribute `block_init_updates` after calling the parent constructor:

```python
class StoreDataNode(Node):
    def __init__(self, params):
        super().__init__(params)

        self.block_init_updates = True
```

### Important API Methods

Here I'll just informally present most of the important API methods for nodes you might want to use. Refer to the [ryvencore-qt API documentation](https://leon-thomm.github.io/ryvencore-qt/api/) for a complete list.

| Method                                                                     | Description                          |
| -------------------------------------------------------------------------- | ------------------------------------ |
| `update()`                                                                 | Causes an `update_event`.
| `input(index: int)`                                                        | Gets the data at the input (has to be a data input) at given index. If the input is connected to another node output, the data that has been provided by this output is used. If the input is not connected but has a widget, that widget value is used. Otherwise `None` is returned.
| `set_output_val(index: int, val)`                                          | Set the value of the output of given index (has to be a data output) to `val`, causing all outgoing data connections (in the order they were added) to activate (transmitting the `val` to all connected nodes and causing updates there).
| `exec_output(index: int)`                                                  | Emits an exec signal at the output (has to be an exec output) at given index, causing every outgoing exec connection (in the order they were added) to activate (simply causing updates in the receiving nodes).
| `new_log(title: str) -> Log`                                               | Requests and returns a new script `Log`.
| `disable_logs()`, `enable_logs()`                                          | Disables/enables all previously requested logs. Happens automatically when the node is removed/placed.
| `create_input(`<br>`type_: str = 'data', label: str = '', add_config={}, pos=-1)`| Creates an new input at index `pos` (negative values allowed).
| `create_input_dt(`<br>`dtype: DType, label: str = '', add_config={}, pos=-1)`    | *[alpha]* Create a new data input with 'data type' `dtype`, see below.
| `delete_input(index: int)`, `delete_output(index: int)`                    | Deletes the input/output at given index and removes all incident connections.
| `get_var_val(name: str)`                                                 | Returns the current value of a script variable with given name and `None` if it doesn't exist.
| `set_var_val(name: str)`                                                 | Sets the value of a script variable with given name.
| `register_var_receiver(name: str, method)`                                                 | Registers the given method as var receiver.
| `unregister_var_receiver(name: str)`                                                 | Unregisters all registered methods as var receivers.
<!-- 
| ``                                                 | 
| ``                                                 | 
| ``                                                 |  
-->

#### `DType` Inputs

Those `DTypes` are defined in an abstract way in `ryvencore` and `ryvencore-qt` automatically adds default Qt widgets for them. It's the idea that those `DTypes` are used as much as possible instead of custom widgets, so other eventual frontends could just add their own widget implementations for those `DTypes` so the nodes are automatically compatible.

> [!TIP|label:Example]
> ```python
class MyNode(Node):
    ...
    init_inputs = [
        NodeInputBP(
            dtype=dtypes.Integer(default=1, bounds=(1, 100)), 
            label='scale'
        ),
    ]
> ```
> or
> ```python
self.create_input_dt(
    dtype=dtypes.Integer(default=1, bounds=(1, 100)),
    label='scale')
> ```

Currently available `DTypes` are:

| DType                                       | widget
| ------------------------------------------- | ------------------------------------------------------------|
| `Data`                                      | line edit (*evaluating* the input expression)
| `String`                                    | line edit
| `Integer`                                   | spin box
| `Float`                                     | slider
| `Boolean`                                   | check box
| `Choice`                                    | drop down menu

### Example

Below you can see a complete node file in some nodes package 'mypackage'.

`mypackage/nodes.py`
```python
from NENV import *


class NodeBase(Node):

    def __init__(self, params):
        super().__init__(params)
        
        # here we could add some stuff for all nodes below...


import random

class Rand_Node(NodeBase):
    """Generate a random number in a given range"""
    # this __doc__ string will be displayed as tooltip in the editor

    title = 'random'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Integer(default=1, bounds=(1, 100)), label='scale'),
    ]
    init_outputs = [
        NodeOutputBP(),
    ]
    color = '#aabb44'

    def update_event(self, inp=-1):
        self.set_output_val(0, round(random.random() * self.input(0), 3))


class Print_Node(NodeBase):
    title = 'print'
    doc = 'prints data'
    init_inputs = [
        NodeInputBP(dtype=dtypes.Data(size='s')),
    ]
    color = '#3355dd'

    def update_event(self, inp=-1):
        print(self.input(0))


export_nodes(
    Rand_Node,
    Print_Node,
)
```

Simply use `export_nodes()` to define the nodes you want to expose to Ryven. And don't forget to import `NENV`.

> [!ATTENTION]
> `export_nodes()` expects an unpacked tuple of arguments, so writing `export_nodes(MyNode)` will not work, instead write `export_nodes(MyNode, )`.

After importing the nodes package in Ryven, it looks like this:

<center><img src="./img/mypackage_flow.png" style="max-width: 800px" /></center>

### Further Features

There are a few more features for which you can find instructions in the [ryvencore-qt docs](https://leon-thomm.github.io/ryvencore-qt/#/features).

#### Special Actions

For example: you can use a node's `actions` dict to easily add dynamic right-click operations to your nodes which you can change at any time. Almost all of the example nodes make use of this feature, it's super useful.

### Custom Widgets

For building nodes with sophisticated UI you can implement custom Qt widgets for your nodes. A node can have to types of widgets.

1. data input widgets, which are used for data inputs and provide an interface for the user to input data
2. a main widget, which is usually a larger widget displayed below or between the ports

Custom input widget sources should always be strictly separated from the actual node sources in `nodes.py` since those widgets are not supposed to exist when running ryven console. For the same reason, you should always program your nodes s.t. they do not depend on their widgets in order to run. The widgets should just provide an interface for the user but not perform any node functionality. To achieve this, you can always check the boolean attribute `self.session.gui` in your node to determine whether the session is running with a frontend or not.

The system for them is pretty much the same as for nodes, you define a file `widgets.py` in the same directory as your `nodes.py`, define your widgets there and export them to make them accessible for your nodes. For example:

Defining some basic custom Qt widgets:

`widgets.py`
```python
from NWENV import *

from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit


class MyMainWidget(MWB, QWidget):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)

        self.setLayout(QVBoxLayout())
        self.layout().addWidget(QLabel('click it!'))
        b = QPushButton('click me')
        b.clicked.connect(self.button_clicked)
        self.layout().addWidget(b)

    def button_clicked(self):
        print('I have been clicked!!')
        self.update_node()


class MyInputWidget(IWB, QLineEdit):
    def __init__(self, params):
        IWB.__init__(self, params)
        QLineEdit.__init__(self)

        self.setPlaceholderText('type something...')
        self.editingFinished.connect(self.update_node)

    # override this from IWB
    def get_val(self):
        return self.text()

    # triggered when the input is connected and it received some data
    def val_update_event(self, val):
        self.setText(str(val))


export_widgets(
    MyMainWidget,
    MyInputWidget,
)
```

And now we can access them like this:

`nodes.py`
```python
from NENV import *
widgets = import_widgets(__file__)  # this loads all exported widgets from widgets.py into the object


class MyNode(Node):
    title = 'my node'

    # this one gets automatically created once for each object
    main_widget_class = widgets.MyMainWidget
    main_widget_pos = 'below ports'  # alternatively 'between ports'

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
```

<center><img src="./img/custom_widgets_example.png" style="max-width: 800px" /></center>

When importing the nodes package in ryven console, `import_widgets(__file__)` does not actually import anything, so the widget classes don't get parsed at all so there is no Qt dependency then, and when trying to access them in the `widgets` object, it just just responds with `None`.

An input widget must subclass `IWB` (InputWidgetBase) and main widgets must subclass `MWB` (MainWidgetBase). When a data input with a widget is connected (which means that the widget does not function as input, the connection is prioritized), the input widget is disabled, otherwise it's enabled.

#### `MWB` Methods

The `MWB` class has `get_state`, `set_state`, and `remove_event` methods to subclass, similar to `Node`. API methods:

| method                | description            |
| --------------------- | ---------------------- |
| `update_node`         | causes an `update_event` in the node object
| `update_node_shape`   | causes the GUI item of the node to update its shape, which you should use when the size of your widget changed.

#### `IWB` Methods

Similar to `MWB`, `IWB` has `get_state`, `set_state`, and `remove_event`. Additionally there is a `val_update_event(val)` which is called when the input is connected and new data arrived. So you can use this to then display the data appropriately in your widget, just like in the example above.

API methods: (*same as above*)

| method                | description            |
| --------------------- | ---------------------- |
| `update_node`         | causes an `update_event` in the node object
| `update_node_shape`   | causes the GUI item of the node to update its shape, which you should use when the size of your widget changed.

***

For getting more examples on how to make nodes and node packages, make sure to take a look at the implementations of the node packages Ryven comes with.
