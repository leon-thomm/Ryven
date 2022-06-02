<p align="center">
  <img src="./docs/img/logo.png" alt="drawing" width="70%"/>
</p>

**Ryven combines flow-based visual scripting with Python. It's a platform for developing nodes executing any python code, for building graphs using those nodes, and for deploying them.**

 *While there are some example node packages, you will most likely rely mostly on your own nodes.*

Ryven features configuration options from the command-line, from configuration files, or directly from code so you can also embed it into other applications. Using RyvenConsole you can also deploy graphs directly on the backend through a tiny command-line interface, with not a single dependency other than what libraries your nodes use.

| Ryven repos on GitHub | -------------------------------------------------------------------------------- |
|---|---|
| [ryvencore](https://github.com/leon-thomm/ryvencore) | backend / core framework |
| [ryvencore-qt](https://github.com/leon-thomm/ryvencore-qt) | Qt frontend |
| [ryven-blender](https://github.com/leon-thomm/ryven-blender) | Ryven plugin for Blender |
| [ryven-unreal](https://github.com/leon-thomm/ryven-unreal) | Ryven plugin for Unreal Engine |
| [PythonOCC nodes for Ryven](https://github.com/Tanneguydv/Pythonocc-nodes-for-Ryven) | Ryven nodes for PythonOCC |

![](./docs/img/themes_with_logo.png)

To get started, these are the resources that guide you through the process (in order):
1. the quick start guide below
2. the tutorials in the `docs/node_tutorials` directory
3. a longer [guide on the website](https://ryven.org/guide#/) for details

Ryven comes with some example nodes, but these are, indeed, just examples, and there's no guarantee that all of them will stay. I want to open a repository for maintaining particularly maintained frameworks of nodes once there are more publicly available large node packages.

### Installation

```
pip install ryven
```

There is also a [conda-forge package](https://anaconda.org/conda-forge/ryven), so on Anaconda you can run
```
 conda install -c conda-forge ryven 
 ```

#### Launching

Run `ryven -s` on your terminal to launch Ryven and `ryven_console` for RyvenConsole. 

#### Integration

For running Ryven from Python, simply `import ryven; ryven.run_ryven()` and pass keyword arguments for configuration analogous to the command line options, see `ryven --help`.

### quick start

**editor usage**

Open Ryven by typing `ryven -s` in your terminal, you will see the startup dialog. For now simply create a new project.

Import some example nodes via `File -> Import Example Nodes` and select `std/nodes.py`.

> In case Ryven cannot automatically open the file dialog in the user's nodes directory, navigate manually to `<your_home_dir>/.ryven/nodes/`.

You should now see a long list of nodes on the left. Drag and drop them into the scene and connect them, everything is being executed at runtime. For instance, drag two `val` nodes into the scene, wire them together with a `+` node and display the result in a `result` node. Now replace one of them with a slider node generating real numbers. You can also get an interactive nodes list preview inside the scene by right-clicking. You can pan around also with the right mouse button, and zoom via `ctrl + scroll`. 

You can also create new scripts, rename and delete them. Now let's check out the small example projects: open a new Ryven window and load one of them by selecting it in the dialog from the beginning. Take a closer look, you can play around and understand what it does.

**defining nodes**

Now it's time to build our own nodes. Navigate to the `~/.ryven/packages/` directory and create a new folder `<your_package_name>`. Inside this folder create a python file `nodes.py` and fill it with the following content:

```python
from ryven.NENV import *

# your node definitions go here

export_nodes(
    # list your node classes here, as tuple
)
```

and now you can define your own node classes. Reference the ones you want to expose to Ryven in the `export_nodes` function (for example `export_nodes(MyNode, )` or `export_nodes(Node1, Node2, )`). Let's define two basic nodes:

one which generates random numbers

```python
from random import random

class RandNode(Node):
    """Generates scaled random float values"""
    # the docstring will be shown as tooltip in the editor

    title = 'Rand'  # the display_title is title by default
    tags = ['random', 'numbers']  # for better search
    
    init_inputs = [  # one input
        NodeInputBP(dtype=dtypes.Data(default=1))
        # the dtype will automatically provide a suitable widget
    ]
    init_outputs = [  # and one output
        NodeOutputBP()
    ]
    color = '#fcba03'

    def update_event(self, inp=-1):
        # update first output
        self.set_output_val(0, 
            random() * self.input(0)  # random float between 0 and value at input
        )
```

and another one which prints them

```python
class PrintNode(Node):
    title = 'Print'
    init_inputs = [
        NodeInputBP(),
    ]
    color = '#A9D5EF'

    def update_event(self, inp=-1):
        print(self.input(0))
```

and expose them to Ryven

```python
export_nodes(
    Rand_node,
    Print_Node,
)
```

and that's it! Go ahead and import your custom nodes package in Ryven (`File -> Import Nodes`). Place both nodes in the scene, connect the `Rand` node to your `Print` node, and give your `Rand` node instance some data by clicking into the input widget and typing some numbers and hitting enter.

***

More features:

- **many themes**, including light themes
- **actions / right-click operations system for nodes**
- **variables system** with update mechanism for nodes that automatically adapt to change of data
- **logging support**
- **rendering flow images**
- **stylus support** for adding handwritten notes on touch devices
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
You can add custom Qt widgets for your nodes. Define a `widgets.py` file next to your `nodes.py` with similar structure to `nodes.py`, see the guide for detailed instructions.

`widgets.py`
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
