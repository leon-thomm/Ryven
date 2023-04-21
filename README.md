> This project is looking for new/additional maintainers, as I will have very limited time available to work on it in the future. I am still reviewing PRs and contributions but won't make significant changes myself.

<p align="center">
  <img src="./docs/img/logo.png" alt="drawing" width="70%"/>
</p>

Ryven is an experimental node editor. In other words, Ryven implements a Qt-based visual interface for flow-based programming in Python. It provides a simple system for developing nodes executing any Python code, and an editor for building graphs using those nodes. Ryven enables GUI customizations and features a headless mode for running graphs without any GUI. Some relevant GitHub repos:

* [ryvencore](https://github.com/leon-thomm/ryvencore): backend / core framework
* [ryvencore-qt](https://github.com/leon-thomm/ryvencore-qt): Qt frontend library
* [ryven-blender](https://github.com/leon-thomm/ryven-blender), [ryven-unreal](https://github.com/leon-thomm/ryven-unreal): Ryven plugins for Blender and UE4
  * _not actively maintained_
* [PythonOCC nodes for Ryven](https://github.com/Tanneguydv/Pythonocc-nodes-for-Ryven): Ryven nodes for PythonOCC (CAD)
* [ironflow](https://github.com/pyiron/ironflow): A WIP node interface in jupyter for [pyiron](https://github.com/pyiron) based on ryvencore

## Installation and Configuration

Once you have Python and pip installed, Ryven is available on PyPI via

```
pip install ryven
```

There is also a [conda-forge package](https://anaconda.org/conda-forge/ryven) (`conda install -c conda-forge ryven`).

Ryven itself only comes with some small example nodes! You should use Ryven either to develop nodes, or use a third-party nodes package for your use case if there is one.

When installed, ryven will create a directory `~/.ryven` with the following structure:

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

Ryven can be launched from the command line with `ryven`. If you installed Ryven into a Python virtual environment, the environment needs to be activated first.

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
            Data(random() * self.input(0).payload)
        )
```

and another one which prints them

```python
class PrintNode(Node):
    title = 'Print'
    init_inputs = [NodeInputType()]

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
    """a standard Qt slider widget, which updates the node
    input it is attached to, every time the slider value changes"""
    
    def __init__(self, params):
        NodeInputWidget.__init__(self, params)
        QSlider.__init__(self)
        
        self.setOrientation(Qt.Horizontal)
        self.setMinimumWidth(100)
        self.setMinimum(0)
        self.setMaximum(100)
        self.setValue(50)
        self.valueChanged.connect(self.value_changed)
    
    def value_changed(self, val):
        # updates the node input this widget is attached to
        self.update_node_input(Data(val))
    
    def get_state(self) -> dict:
        # return the state of the widget
        return {'value': self.value()}
    
    def set_state(self, state: dict):
        # set the state of the widget
        self.setValue(state['value'])
    

class RandNodeGui(NodeGUI):
    color = '#fcba03'
    
    # register the input widget class
    input_widget_classes = { 'slider': RandSliderWidget }
    
    # attach the slider widget to the first node input
    # display it _below_ the input pin
    init_input_widgets = {
        0: {'name': 'slider', 'pos': 'below'}
    }

export_guis([
    RandNodeGui,
])
```

and you now just need to reference the `RandNodeGUI` in `nodes.py`:

```python
guis = import_guis(__file__)

class RandNode(Node):
    ...
    GUI = guis.RandNodeGui
```

The value provided by an input widget (through `self.update_node_input(val)`) will be returned in `Node` by `self.input(0)` only when the corresponding input is _not_ connected. Otherwise the value of the connected output will be returned.

So now we can reconstruct the previous example, but we don't need to connect the `val` node to the `Rand` node anymore. Change the slider and see how many different random values are printed.


***

This covered the basic setup for developing nodes. For more information, look at the guide, which covers the details necessary to develop more complex node packages.

## Features

A (possibly incomplete) list of features:

- **headless mode** to run projects without GUI dependencies at high performance
- **sophisticated nodes system** allowing for stateful nodes and widgets
- **cross-platform**; running anywhere where Qt runs (for GUI), or simply Python (headless)
- **rendering flow images** into PNGs
- built-in **exec flow support** (like [UE BluePrints](https://docs.unrealengine.com/5.0/en-US/blueprints-visual-scripting-in-unreal-engine/)) unlike most other node editors
- **custom Qt widgets support**
- various **themes**, including light
- **right-click operations system for nodes**
- **variables add-on** with observer mechanism, to build nodes that automatically adapt to change of data
- very basic **logging support**
- primitive, very experimental **stylus support** for adding handwritten notes on touch devices

## License

* This repository is licensed under the MIT license (LICENSE-MIT or http://opensource.org/licenses/MIT)
* The underlying library ryvencore is licensed under LGPL-2.1 (LICENSE-LGPL-2.1 or https://www.gnu.org/licenses/lgpl-2.1.html)


## Contributions

Contributions are welcome. Notice also the *discussions* area in this repo.

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you shall be licensed as above, without any additional terms or conditions.

The guide on the website is made with [Docsify](https://github.com/docsifyjs/docsify/), you can improve it by simply editing the markdown, you can find the [sources on GitHub](https://github.com/leon-thomm/ryven-website-guide) as well.

Cheers.
