# Getting Started

This site provides info about using Ryven and programming nodes. It is not a complete documentation on the API, for that please visit the [ryvencore-qt API documentation]().

## Project Idea

Ryven is an editor for flow-based visual scripting in Python. It is easy to create new and use existing nodes executing any python code. I developed an underlying Python framework for building editors like Ryven. `ryvencore` is the backend, implementing the abstract functionality, while `ryvencore-qt` uses `ryvencore` and provides a Qt-based frontend. The Ryven editor is now based on `ryvencore-qt` and implements most of its features (excluding threading compatibility so far). While Ryven is supposed to be general purpose, `ryvencore-qt` can be used to create fundamentally similar but specialized editors. Nodes developed for Ryven are usually easily migratable to other editors made with `ryvencore-qt`. When programming nodes, you are using the framework's API. This API is easy to use but quite powerful, so you can build quite sophisticated nodes. `ryvencore` might be the base for implementing different frontends some day, including web.

Flows you made in Ryven can be deployed directly on `ryvencore` (via *Ryven Console*, simply run `ryven console`) without any frontend related dependencies (including Qt).

## Flows

PICTURE

In Ryven a **Flow** is part of a **Script**. A **Script** contains a **Flow**, a **Logger**, and a **Variables Manager**. There are normal **Scripts** as well as **Function Scripts** which additionally have an input and output node representing parameters and returns, and are registered as node themselves (just like functions in UE4 BluePrints).

Unlike most other flow-based visual scripting editors, Ryven supports 'data connections' *and* 'exec connections'. Data connections transmit data from one node to another, and exec connections only transmit a 'trigger' signal. Pure data flows (only data connections) are like the UE4 Material Editor, while exec flows (some exec connections) are more like the UE4 BluePrints.

??? note "More Precisely"

    ### Data Flows

    In a data flow, every change of data (which means that a data output of a node has been changed via `self.set_output_val()`) gets forward propagated and causes an update event in all connected nodes. In the example below, changing the slider value would therefore cause immediate updates and a visible change in the result node on the right.

    ![](img/data_flow_example.png)

    ### Exec Flows

    In execution flows, data isn't forward propagated on change, but generated on request (backwards), only causing update events in affected nodes once the data of an output is requested somewhere (through `self.input()` in a node). In the example above, changing the slider value would not lead to a change in the result node, but if an active node requested this data, like shown below, then the whole expression gets executed.

    ![](img/exec_flow_example.png)

    The data flow paradigm is the more important and fundamental one, and there might be changes for the exec mode in the future.

    While you can choose the according mode for a flow, it turned out to be a use case too to use the data flow mode in combination with few exec connections. This can lead to performance issues, but is very powerful if used in the right way. Ultimately, both paradigms are possible. For more precise definitions on the aspects of flow execution, see [ryvencore-qt features](https://leon-thomm.github.io/ryvencore-qt/features/).

    If you don't have experience with the flow-based programming idea already don't worry, all these differences don't really matter now.

## Editor Overview

### Running Ryven

After installing the application, following the instructions on [GitHub](https://github.com/leon-thomm/Ryven), you can run Ryven by running `ryven` on the console, or by opening `Ryven.py` with Python.

### Flows

The flow supports all usual actions, including undo/redo operations. You can place nodes by right-clicking somewhere into the scene, and also pan around by right clicking and dragging. I would like to add sophisticated touch support, but there are Qt bugs that are not being tackled making this difficult.

There are many different themes for the flows, which you can select in the menu at the top of the window. Furthermore, when nodes update, they "blink" so you can easily see what's going on. There is also a performance mode which you can change to `fast` to significantly simplify the drawing and rendering of the components for "weaker" hardware (or large flows).

### Console

This console runs a Python REPL. Additionally, you can right click on a node to add a reference to it to the console, so you can directly access the node's whole API at any time. This is a really powerful feature, no matter if you would like to quickly access a few intern variables or perform some temporary modifications on the node (like adding/removing inputs/outputs), you have full control there.

Furthermore, the session object (which is basically the project) is already added to the console automatically, so you can type `session` to access it and do pretty much *everything* from there (you can play around with the `ryvencore-qt` API, for example try creating a new script via `session.create_script('hello there!')`).

### Script Variables

The script variables, located on the right, can be modified at any time by right-clicking on them, and when you hover over one, you can see its current value and data type. The values of those variables are usually accessed and changed by your nodes. The API provides a few very simple but really powerful methods for nodes to 'register as variable receivers'. Basically, a node can dynamically register as a receiver for script variables by providing a var name and a method that is supposed to be called whenever a script variable with that name changes (or is created). I particularly like this feature, as you can easily build highly sophisticated nodes using this that automatically adapt to change of data.

!!! example
    In one of the node packages Ryven comes with, there's a *Matrix* node where you can just type a few numbers into a small textedit and it creates a numpy array out of them. But you can also type in `v('')` and the name of a script variable (instead of a number) which makes the matrix node register as a receiver, so it updates and regenerates the matrix every time the value of a script variable with that name changed.

### Logs

The script's logs are hidden at the bottom, just drag the splitter handle. The nodes can access the two default logs via the API, and also request new ones. I think this also is a neat feature, but be aware that there might be changes/improvements in the future.

### Source Code Preview

Next to the logs is the source code area where you can inspect the source code of the last selected node (click into the text field for syntax highlighting), and also edit method implementations of single objects. That's right, you can override method implementations of single objects. All these changes are temporary (they don't get saved) and only apply on the currently selected object, but it's a great way to play around or debug your components, especially when combining this with the console. For example you can just add some output to one of your nodes via the console, and then modify the update event of it to provide some additional data there via the source code preview. This is a really useful feature, however as you might suspect, modifying an object's method implementation is not exactly conventional and doesn't work in all cases. For example, when you created references somewhere else to this modified method, those references will still point to the old implementation of it.

??? note "how to fix this"
    ...

It usually works quite well, but there might be some bugs since the implementation in Ryven 3 hasn't been extensively tested yet.

### Rendering Flow Images

You can render images of the currently displayed flow, also via the top menus. By rendering the viewport, the picture will show what's currently visible of the flow, in the exact same resolution it is currently displayed. For high res pictures render the whole scene and zoom to the top left, the zoom factor will determine the exact resolution of your image. It can take a few seconds to render high resolution picutures.

### Save&Load

You can save via `ctrl+s` and choose to laod a project when starting the applicaiton. To import a nodes package, you can also hit `ctrl+i`.

For programming your own nodes (see below), you only need to follow the rule that all API provided features are saved and reloaded automatically, for example the current inputs and outputs, display title, as well as special actions.

## Programming Nodes

Now comes the technical stuff. Programming new nodes is at the heart of all this. You need basic Python knowledge, but nothing advanced.

A node is defined by its Python class. You basically subclass the `Node` class from Ryven, specify pre-defined attributes and methods and enhance it the way you like. For example:

```python
class MyPrintNode(Node):
    title='print'
    init_inputs=[
        NodeInputBP()
    ]

    def update_event(self, input_called=-1):
        print(self.input(0))
```

This simple node gets updated when data arrives at its only input, causing an update event. Then, we just print this data and that's basically it. The static attributes at the top define basic properties that equally apply on all nodes of this type (all such `print` nodes here), and there are various methods (defined in `Node`) you can reimplement to do more sophisticated stuff.

### Important Methods

If your node has states, which means its behavior depends on the values of internal variables, to be able to reconstruct the current state when loading a project or pasting the node after copying an instance of it, you can use the `get_state()` and `set_state()` methods.

```python
class StoreDataNode(Node):
    title='store'
    init_inputs=[
        NodeInputBP()
    ]

    def __init__(self, params):
        super().__init__(params)

        self.storage = []

    def update_event(self, input_called=-1):
        self.storage.append(self.input(0))
    
    def get_state(self) -> dict:
        # assuming only pickle serializable data is stored in self.storage
        return {
            'data': self.storage
        }
    
    def set_state(self, data: dict):
        self.storage = data['data']
```

By default, nodes are updated, possibly multiple times, while the flow is building up, which is the usual situation for 'combinational' nodes (no states, like a `+` node). However, with sequential nodes you don't want the node's state to change due to the flow building process. You can disable updates on flow building by just setting the attribute `block_init_updates` after calling the parent constructor:

```Python
class StoreDataNode(Node):
    def __init__(self, params):
        super().__init__(params)

        self.block_init_updates = True
```

There are a few more methods that might be important, especially when building complex 'sequential' nodes which need to correctly reconstruct their state.

The `place_event` is called everything the node is added to the flow. Notice that this can happen multiple times, for example when undoing a remove operation in the flow, but also when the node is first constructed and placed in the flow. The `place_event` is called *before* any incident connections are built, so it is sometimes used to trigger updates since setting outputs does not affect any other nodes.

!!! example
    ```python
    class MyNode(Node):
        def place_event(self):
            self.update()
    ```

Just like the `place_event`, there's a `remove_event` called every time the node is removed from the flow (this too can happen multiple times).

!!! example
    ```python
    class MyNode(Node):
        def remove_event(self):
            self.timer.stop()
    ```

In contrast to the `place_event`, the `view_place_event` is called once the whole GUI of the node (including custom widgets) has initialized, which is important when using custom widgets, see below. Only do GUI related work here, as this method of  course is never called when running the node on ryven console since there does not exist any GUI then.

!!! example
    ```python
    class MyNode(Node):
        def view_place_event(self):
            self.main_widget().update()
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
| ``create_input(type_: str = 'data', label: str = '', add_config={}, pos=-1)`| 
| `create_input_dt(dtype: DType, label: str = '', add_config={}, pos=-1)`    | 
| `delete_input(index: int)`, `delete_output(index: int)`                    | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 
| ``                                                 | 

#### `update()`

Causes an `update_event`.

#### `input(index: int)`

Gets the data at the input (has to be a data input) at given index. If the input is connected to another node output, the data that has been provided by this output is used. If the input is not connected but has a widget, that widget value is used. Otherwise `None` is returned.

#### `set_output_val(index: int, val)`

Set the value of the output of given index (has to be a data output) to `val`, causing all outgoing data connections (in the order they were added) to activate (transmitting the `val` to all connected nodes and causing updates there).

#### `exec_output(index: int)`

Emits an exec signal at the output (has to be an exec output) at given index, causing every outgoing exec connection (in the order they were added) to activate (simply causing updates in the receiving nodes).

#### ``

Requests and returns a new script `Log`.

#### 

Disables/enables all previously requested logs. Happens automatically when the node is removed/placed.

#### `

Creates a new input. `type_` can be `'data'` or `'exec'`, `pos` specifies index (negative values allowed).

#### `create_input_dt(dtype: DType, label: str = '', add_config={}, pos=-1)`

*[alpha]*

Create a new data input with 'data type' `dtype`. Those `DTypes` are defined in an abstract manner in `ryvencore` and `ryvencore-qt` creates automatically adds default Qt widgets for them. It is the idea that those `DTypes` are used as much as possible instead of custom widgets, so other eventual frontends (web?) can also just add their own widget implementations for those `DTypes` so the nodes are automatically compatible.

??? example
    ```python
    ...
    ```

Currently available `DTypes` are: `Data` (evaluating the input expression), `String` (-> *line edit*), `Integer` (-> *spin box*), `Float` (-> *slider*), `Boolean` (-> *check box*), `Choice` (-> *drop down menu*). More should be added soon.

#### 

Deletes the input/output at given index and removes all incident connections.

#### `get_var_val(name: str)`

Returns the current value of a script variable with given name and `None` if it doesn't exist.

#### `set_var_val(name: str)`

Sets the value of a script variable with given name.

#### `register_var_receiver(name: str, method)`

Registers the given method as var receiver.

#### `unregister_var_receiver(name: str)`

Unregisters all registered methods as var receivers.

### Node Packages

In Ryven, nodes are organized in *node packages* A node package consists of a package folder, the folder name is the package name, and a file `nodes.py` where you define your node classes. Ryven comes with its own packages folder, but if you installed it via `pip`, you should define another one somewhere on your file system, so your packages dont get lost when you update the ryven installation.

### Example

Below you can see the complete definition of a nodes file in a nodes package called `mypackage`.

```python

```

Simply use `export_nodes()` to define the nodes you want to expose to Ryven. And don't forget to `import NENV`.

After importing the nodes package in Ryven, it looks like this:

PICTURE

### Custom Widgets

#### Example
