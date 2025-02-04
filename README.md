> This project is not receiving substantial updates, and I'll have limited time for it in the future. With the latest release the project became quite accurately what I want it to be: an easy and flexible editor and framework to explore use cases of flow-based visual scripting in Python. If you have questions or further ideas feel free to open issues or fork the project and try it yourself.

<p align="center">
  <img src="./docs/img/logo.png" alt="drawing" width="70%"/>
</p>

Ryven is an experimental node editor written in Python. It implements a Qt-based visual interface for flow-based visual scripting in Python. It provides a powerful system for developing nodes executing any Python code, and an editor for building graphs using those nodes. Ryven features a bunch of configuration options and a headless mode for running graphs without any GUI. Some relevant GitHub repos:

* [ryvencore](https://github.com/leon-thomm/ryvencore): backend / core library
* [ryven-blender](https://github.com/leon-thomm/ryven-blender), [ryven-unreal](https://github.com/leon-thomm/ryven-unreal): Ryven plugins for Blender and UE4 (_deprecated_)
* [PythonOCC nodes for Ryven](https://github.com/Tanneguydv/Pythonocc-nodes-for-Ryven): WIP Ryven nodes for PythonOCC (3D CAD) (_deprecated_)
* [ironflow](https://github.com/pyiron/ironflow): WIP node interface in jupyter for [pyiron](https://github.com/pyiron) based on ryvencore

The `ryvencore-qt` library adds Qt-based GUI classes for ryvencore (`./ryvencore-qt/`), and the Ryven editor assembles them into a fully-featured cross-platform application (`./ryven-editor/`).

## Installation and Configuration

Once you have Python and pip installed, Ryven is available on PyPI via

```
pip install ryven
```

There is also a [conda-forge package](https://anaconda.org/conda-forge/ryven) (`conda install -c conda-forge ryven`).

Ryven can be launched from the command line by typing `ryven`. If you installed Ryven into a Python virtual environment (or a conda environment), the environment needs to be activated first.

Ryven itself only comes with some small example nodes. You should use Ryven either to develop nodes, or use a third-party nodes package for your use case if there is one. The example nodes are - indeed - just examples, and not stable in any way, so you should not depend on them.

When installed, ryven will create a directory `~/.ryven/` in your user home with the following structure:

```
~/.ryven
├── nodes
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
   > import pathlib
   > ryven.run_ryven(nodes=pathlib.Path(['your_nodes_pkg_1']), no_animations=True)
   > ```
4. using a GUI in the startup dialog
   * you can also convert the manual configuration to cmd line args (or a config file) in the dialog

Type `ryven --help` for a list of available options.

To deploy a Ryven project headless (without any GUI) use the `ryven-console` command.

<details>
<summary>Example: headless deployment with REPL access</summary>

```bash
> ryven-console /home/leon/.ryven/saves/basics.json
Welcome to the Ryven Console! Your project has been loaded.
You can access the ryvencore session by typing `session`.
For more information, visit https://leon-thomm.github.io/ryvencore/

>>> f = session.flows[0]
>>> ctr_var_result_node = f.nodes[2]
>>> ctr_set_var_node = f.nodes[8]
>>> ctr_var_result_node.val
3738
>>> ctr_set_var_node.update(0)
>>> ctr_var_result_node.val
3739
```

</details>

## Editor Usage
<details>
<summary>quick start guide</summary>

* open Ryven by running `ryven` from the command line
* you should see the startup dialog
* create a new project
* import some example nodes
  * `File -> Import Example Nodes` and select `<installation_dir>/example_nodes/std/nodes.py`
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

</details>

## Developing Nodes

<details>
<summary>quick start into to developing node packages</summary>

A Ryven nodes package is simply a typical Python package which contains at least a `nodes.py` file, and calls the Ryven node API to expose node definitions.

Navigate to `~/.ryven/nodes/` and create a sub-directory of the following structure

```
~/.ryven/nodes
└── your_nodes_pkg_1
    ├── __init__.py
    ├── nodes.py
    └── gui.py
```

with the following contents:

`nodes.py`:

```python
from ryven.node_env import *

# your node definitions go here

export_nodes([
    # list your node classes here
])


@on_gui_load
def load_gui():
    # import gui sources here only
    from . import gui
```

and `gui.py`:

```python
from ryven.gui_env import *

from . import nodes

# your node gui definitions go here
```

You can now start defining your own nodes. Let's define two basic nodes. One which generates random numbers...

```python
from random import random

class RandNode(Node):
    """Generates scaled random float values"""

    title = 'Rand'
    tags = ['random', 'numbers']
    init_inputs = [NodeInputType()]
    init_outputs = [NodeOutputType()]

    def update_event(self, inp=-1):
        self.set_output_val(0, 
            Data(random() * self.input(0).payload)
        )
```

...and another one which prints them

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

That's it! You can import your nodes package in Ryven (`File -> Import Nodes`), place the nodes in the graph, and wire them up. Add a `val` node and connect it to the `Rand` node, to feed its input with data. If you type a number into the widget of the `val` node and hit enter, it will send the number to the `Rand` node, which will send a scaled random number to the `Print` node, which will print it to the standard output.

Notice that the standard output is by default the in-editor console, which you can access at the very bottom of the editor window (drag the blue handle up to make it visible).

### Adding GUI

You can now spice up your nodes with some GUI. Ryven runs on Qt, using either PySide2 or PySide6 (through the [qtpy](https://github.com/spyder-ide/qtpy) library). You can configure the GUI of your nodes in a separate file, and add custom Qt widgets to your nodes. Make sure to always clearly separate the node logic from the GUI components. One of the central features of Ryven is to run projects headless (on ryvencore) without any GUI dependencies. In order for this to work, your `nodes.py` files should never depend on Qt directly. Instead, you can attach custom GUI to your nodes from the GUI files as shown below.

Let's give them some color and add a slider to the `Rand` node, in `gui.py`:

```python
from qtpy.QtWidgets import QSlider
from qtpy.QtCore import Qt

from ryven.gui_env import *

from . import nodes


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
    

@node_gui(nodes.RandNode)
class RandNodeGui(NodeGUI):
    color = '#fcba03'
    
    # register the input widget class
    input_widget_classes = { 'slider': RandSliderWidget }
    
    # attach the slider widget to the first node input
    # display it _below_ the input pin
    init_input_widgets = {
        0: {'name': 'slider', 'pos': 'below'}
    }
```

and this is it! Ryven will now register `RandNodeGui` as "GUI class" of the `RandNode` class, which serves as a container for all UI things. Your can add custom primary ("main") widgets to your nodes, input widgets, and further customize the look of the nodes.

The value provided by an input widget (e.g. `self.update_node_input(val)` above) will be returned in the node, when calling `input()` (e.g. `self.input(0)` in the `RandNode`), but only when the corresponding input is _not connected_. Otherwise, the value of the connected output will be returned.

</details>

Please find further resources on the GitHub wiki page in this repository.

## Features

- **headless mode** to run projects without GUI dependencies at high performance
- **sophisticated nodes system** allowing for stateful nodes and widgets
- **cross-platform**; running anywhere where Qt runs (for GUI), or simply Python (headless)
- **rendering flow images** into PNGs
- built-in **exec flow support** (like [UE BluePrints](https://docs.unrealengine.com/5.0/en-US/blueprints-visual-scripting-in-unreal-engine/)) unlike most other node editors
- **custom Qt widgets support**
- various **themes**, including light
- **right-click operations system for nodes**
- **variables system** with observer mechanism, to build nodes that automatically adapt to change of data
- basic Python **logging support**
<!-- - primitive, very experimental **stylus support** for adding handwritten notes on touch devices -->

## License

* This repository is licensed under the MIT license (LICENSE-MIT or http://opensource.org/licenses/MIT)
* The underlying library ryvencore is licensed under LGPL-2.1 (LICENSE-LGPL-2.1 or https://www.gnu.org/licenses/lgpl-2.1.html)

Unless you explicitly state otherwise, any contribution intentionally submitted for inclusion in the work by you shall be licensed as above, without any additional terms or conditions.

## Credits

Contributions are highly appreciated. This project does not exist without the open-source community. I want to particularly thank the people listed in the `CREDITS.md` file.
