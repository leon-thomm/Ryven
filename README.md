<p align="center">
  <img src="./docs/img/logo.png" alt="drawing" width="70%"/>
</p>

Ryven is an experimental node editor. In other words, Ryven implements a Qt-based visual interface for flow-based programming in python. It provides a simple system for developing nodes executing any python code, and an editor for building graphs using those nodes. Ryven enables GUI customizations and features a headless mode for running graphs without any GUI. Some relevant GitHub repos:

* [ryvencore](https://github.com/leon-thomm/ryvencore): backend / core framework
* [ryvencore-qt](https://github.com/leon-thomm/ryvencore-qt): Qt frontend library
* [ryven-blender](https://github.com/leon-thomm/ryven-blender), [ryven-unreal](https://github.com/leon-thomm/ryven-unreal): Ryven plugins for Blender and UE4
  * _not actively maintained_
* [PythonOCC nodes for Ryven](https://github.com/Tanneguydv/Pythonocc-nodes-for-Ryven): Ryven nodes for PythonOCC (CAD)
* [ironflow](https://github.com/pyiron/ironflow): A WIP node interface in jupyter for [pyiron](https://github.com/pyiron) based on ryvencore

The nodes Ryven comes with are just examples, and there's no guarantee that any of them will stay included or compatible in future versions. I'd like to open a repository for maintaining particularly active (frameworks of) nodes once there are more publicly available large node packages.

## Installation and Configuration

Once you have Python and pip installed, Ryven is available on PyPI via

```
pip install ryven
```

There is also a [conda-forge package](https://anaconda.org/conda-forge/ryven) (`conda install -c conda-forge ryven`).

Ryven itself only comes with some small example nodes! You should use Ryven either to develop nodes, or use a third-party nodes package for your use case if there is one.

Once installed, ryven will create a directory `~/.ryven` with the following structure:

```
~/.ryven
├── nodes
│   ├── examples
│   ├── your_nodes_pkg_1
│       ├── nodes.py
│       └── gui.py
│   └── ...
├── saves
│   ├── your_project_1.json
│   └── ...
└── ryven.cfg
```

The `ryven.cfg` file contains global configurations for Ryven.

Ryven can be launched from the command line with `ryven`. If you have installed Ryven from a Python virtual environment, the environment needs to be activated.

Ryven can be configured in four ways:
1. from the command line, e.g. `ryven --nodes your_nodes_pkg_1 --no-animations`
2. from a configuration file, e.g. in `~/.ryven/ryven.cfg`:
   > ```
   > nodes = your_nodes_pkg_1
   > no_animations = True
   > ``` 
3. through arguments when it's integrated in another Python application, e.g.
   > ```python
   > import ryven
   > ryven.run_ryven(nodes=['your_nodes_pkg_1'], no_animations=True)
   > ```
4. using a GUI in the startup dialog
   * you can also convert the manual configuration to cmd line args (or a config file) in the dialog

See `ryven --help` for a list of available options.

## Editor Usage

Quickstart guide:

* open Ryven by running `ryven` from the command line
* you should see the startup dialog
* create a new project
* import some example nodes
  * `File -> Import Example Nodes` and select `~/.ryven/nodes/examples/std/nodes.py`
* you should now see a list of nodes on the left
* drag and drop them into the scene and connect them with your mouse
* everything is being executed at runtime; try this:
  * drag two `val` nodes into the scene
  * wire them together with a `+` node
  * display the result in a `result` node 
  * now replace one of them with a slider node generating real numbers
* by right-clicking, you can also get an interactive nodes list preview inside the scene
* you can pan around also with the right mouse button (hold and drag)
* and zoom via `ctrl + scroll`

## Developing Nodes

Resources to get started on developing nodes:
1. the quick start guide below
2. some tutorials in the `docs/node_tutorials` directory
   * _TODO: outdated_
3. a more detailed [guide on the website](https://ryven.org/guide#/)
   * _TODO: outdated_

Navigate to `~/.ryven/nodes/` and create a sub-directory of the following structure

```
~/.ryven/nodes
└── your_nodes_pkg_1
    ├── nodes.py
    └── gui.py
```

With the following contents:

`nodes.py`

```python
from ryven.node_env import *

# your node definitions go here

export_nodes([
    # list your node classes here
])
```

`gui.py`

```python
from ryven.gui_env import *

# your node gui definitions go here

export_guis([
    # list your node gui classes here
])
```

You can now start defining your own nodes. Let's define two basic nodes. One which generates random numbers

```python
from random import random

class RandNode(Node):
    """Generates scaled random float values"""
    # the docstring will appear as tooltip

    title = 'Rand'  # the display_title is title by default
    tags = ['random', 'numbers']  # for better search
    init_inputs = [NodeInputType()]
    init_outputs = [NodeOutputType()]
    
    def update_event(self, inp=-1):
        self.set_output_val(0, 
            # random float between 0 and value at input
            Data(random() * self.input(0))
        )
```

and another one which prints them

```python
class PrintNode(Node):
    title = 'Print'
    init_inputs = [NodeInputType()]
    # color = '#A9D5EF'

    def update_event(self, inp=-1):
        print(self.input(0))
```

and expose them to Ryven

```python
export_nodes([
    RandNode,
    PrintNode,
])
```

That's it! You can import your nodes package in Ryven (`File -> Import Nodes`), place the nodes in the graph, and wire them up. Now add a `val` node and connect it to the `Rand` node, to feed its input with data. If you type a number into the widget of the `val` node and hit enter, it will send the number to the `Rand` node, which will send a scaled random number to the `Print` node, which will print it to the standard output.

Notice that the standard output is by default the in-editor console, which you can access at the very bottom of the editor window (drag the blue handle up to make it visible).

### Adding GUI

You can now spice up your nodes with some GUI. Ryven runs on Qt, using the [qtpy](https://github.com/spyder-ide/qtpy) library. You can configure the GUI of your nodes in a separate `gui.py` file, and add custom Qt widgets to your nodes. Make sure to always clearly separate the node logic from the GUI. The `nodes.py` file should NOT have any dependency to Qt. One of the central features of Ryven is to run projects headless (on ryvencore) without any GUI dependencies, if your node packages obey the rules.

Let's give them some color and add a slider to the `Rand` node, in `gui.py`:

```python
from ryven.gui_env import *

from qtpy.QtWidgets import QSlider
from qtpy.QtCore import Qt


class RandSliderWidget(NodeInputWidget, QSlider):
    def __init__(self, params):
        NodeInputWidget.__init__(self, params)
        QSlider.__init__(self)
        
        self.setOrientation(Qt.Horizontal)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(50)
        self.valueChanged.connect(self.value_changed)
    
    def value_changed(self, val):
        # updates the node input this widget is attached to
        self.update_node_input(val)
    
    def get_state(self) -> dict:
        # return the state of the widget
        return {'value': self.value()}
    
    def set_state(self, state: dict):
        # set the state of the widget
        self.setValue(state['value'])
    

class RandNodeGUI(NodeGUI):
    color = '#fcba03'
    
    # register the input widget class
    input_widget_classes = { 'slider': RandSliderWidget }
    
    # attach the slider widget to the first node input
    # display it _below_ the input pin
    init_input_widgets = {
        0: {'name': 'slider', 'pos': 'below'}
    }

export_guis([
    RandNodeGUI,
])
```

and you now just need to reference the `RandNodeGUI` in `nodes.py`:

```python
guis = import_guis(__file__)

class RandNode(Node):
    ...
    GUI = guis.RandNodeGUI
```

The value provided by an input widget (through `self.update_node_input(val)`) will be returned in `Node` by `self.input(0)` only when the corresponding input is _not_ connected. Otherwise the value of the connected output will be returned.

So now we can reconstruct the previous example, but we don't need to connect the `val` node to the `Rand` node anymore. Change the slider and see how many different random values are printed.

***

### Further Features

- **themes**, including light
- **actions / right-click operations system for nodes**
- **variables system** with update mechanism for nodes that automatically adapt to change of data
- **logging support**
- **rendering flow images**
- primitive **stylus support** for adding handwritten notes on touch devices
- **exec flow support** like [UnrealEngine BluePrints](https://docs.unrealengine.com/5.0/en-US/blueprints-visual-scripting-in-unreal-engine/)
- **custom Qt widgets support**

and some usage examples:

#### actions / right-click operations system for nodes
```python
class MyNode(Node):
    ...
    def a_method(self):
        self.actions['do something'] = {'method': self.do_sth}

    def do_sth(self):  # with some method
        ...
```
These actions can be edited at any time.

#### custom Qt widgets

see [guide](https://ryven.org/guide)

<!--
#### Qt widgets (TODO: put this in the guide instead)
You can add custom Qt widgets for your nodes. Define a `gui.py` file next to your `nodes.py` with similar structure to `nodes.py`, see the guide for detailed instructions.

`gui.py`
```python
from ryven.NWENV import *
from qtpy.QtWidgets import QWidget

class SomeMainWidget(MWB, QWidget):
    def __init__(self, params):
        MWB.__init__(self, params)
        QWidget.__init__(self)
    ...

class SomeInputWidget(IWB, QWidget):
    def __init__(self, params):
        IWB.__init__(self, params)
        QWidget.__init__(self)
    ...

export_widgets(
    SomeMainWidget,
    SomeInputWidget,
)
```
`nodes.py`
```python
...
widgets = import_widgets(__file__)

class MyNode(Node):
    ...
    main_widget_class = widgets.MyNode_MainWidget  # register main (body) widget
    main_widget_pos = 'below ports'  # alternatively 'between ports'
    input_widget_classes = {  # register input widgets for that node type
        'some input widget': widgets.SomeInputWidget,
    }
    init_inputs = [  # and you can use input widgets like this:
        NodeInputBP(add_data={'widget': 'some input widget'}),
    ]
```
-->

#### stylus support
<p align="center">
  <img src="./docs/img/stylus_dark.png" alt="drawing" width="70%"/>
</p>

#### logging support
```python
import logging

class MyNode(Node):
    def somewhere(self):
        self.logger = self.new_logger('nice log')
    
    def update_event(self, inp=-1):
        self.logger.info('updated!')
```

#### variables system

```python
class MyNode(Node):
    def a_method(self):
        self.register_var_receiver('x', method=self.process)
        
        # set the value of x to 0
        self.set_var_val('x', 0)
        # causes process to be called
    
    def process(self, val_of_x):
        # processing new value of var 'x'
        # the value could have been set by another node as well
        ...
```

## Contributions

Contributing guidelines: [here](https://github.com/leon-thomm/Ryven/blob/dev/CONTRIBUTING.md).

Also notice that there's a *discussions* area in this repo.

The guide on the website is made with [Docsify](https://github.com/docsifyjs/docsify/), so you can improve it by simply editing the markdown, you can find the [sources on GitHub](https://github.com/leon-thomm/ryven-website-guide) as well.

Cheers.
