# A simple flow-based visual scripting runtime environment for Python

![](/docs/resources/images/ryven_screenshot2.png)

Ey, what's up!

Please be aware that this whole project is a proof of concept. It is primarily meant to show the idea and the source code is not developed with highest focus on readability. However its working surprisingly well so far and I think this has the potential to become something really intuitive and practical. How it is going to evolve will depend on the resonance it gets.

### Requirements
- Python 3
- PySide2

# Idea

The idea is a dynamic runtime flow-based visual programming environment for Python, with visual flows serving as a diagram-like representation of your script while being executable at the same time (useful for presentations for examle). The runtime part means that you don't export any code, everything gets executed within the editor as you go, at runtime. 
<a href="http://www.youtube.com/watch?feature=player_embedded&v=8aOn9OsvlXY" target="_blank">
    <img src="docs/resources/images/thumbnail7.png" alt="Prototype Demonstration Video" width="300" border="10" align="right" />
</a>
Beside the main Ryven application (the editor), the Ryven NodeManager lets you manage your existing nodes and the creation of new ones which you can then program for use in your visual scripts. The focus is on enabling an easy process of creating new nodes and giving them intuitive GUI elements. **You can throw any Python code into these nodes and Ryven provides you with the platform to use them in combination with others.** Keep in mind that the intention is not to 'replace' textual coding - there is a lot you can do in textual programming which doesn't make sense being represented that way at all. But there is also the opposite.

There are two types of connections (execution and data connections) but if you are searching for a pure data flow sofware, you can absolutely do normal pure dataflows which opens plenty of possibilities for data manipulation applications.

Ryven is currently not yet in a state of large package varieties of usable nodes. Creating nodes, however, is fairly easy while restrictions are kept very low (see _Creating new nodes_ on the [GitHub page](https://leon-thomm.github.io/Ryven/)). However if people keep creating new nodes, this might look very different in the future. For now, this is primarily for vp-enthusiasts who intend to create their nodes themselves and are looking for some inspiration.

# Getting Started

**To start the editor simply run _Ryven.py_**. Some example packages are in the _packages_ folder. And you may find example projects in the _saves_ folder that uses these packages. **To start the NodeManager run _Ryven NodeManager.py_**, located in the folder _Ryven_NodeManager_.

## Ryven Overview

![](docs/resources/images/pyScript1.PNG)

When you open Ryven, you will notice, there are different scripts. Every script has variables, a flow (or _graph_) and logs. You can right click on scripts, variables and many other components to perform actions like _remove_ on them.

### Importing Nodes

You need to import nodes before you can use them from node packages (File -> Import Nodes and then choose a nodes package file *.rypac). If the import succeeded, you will then be able to use the imported nodes in all scripts.

### Controls


#### Stylus Support
Note that Ryven is also optimized for use with convertible notebooks/tablets using a stylus pen. You can use stylus pens for either editing your flows or to add handwritten notes. In the top right corner, you can spcify your actions. Be aware, that there may be bugs.

#### Zoom

Strg+Mouse Wheel

#### Pan

Middlee mouse button

#### Placing Nodes

Right click. You can then also press 'Shift'+'P' to place a new node next to the selected one and move it around with 'Shift'+Arrow.

#### Selecting, Dragging, Connecting

Left Mouse

### Variables

You can create new variables just like scripts. By right clicking on a variable, you can set the value in the dialog that pops up. Whatever you type into that field will be evaluated by Python using the _eval()_ method, so the datatype will automatically be parsed just like when assigning variables in Python source code. To use a variable, you must use the _get var_ node, which returns its _value_ (without copying it!). You can press Ctrl+s in the value edit dialog.

[//]: # (As long as your variable does not have a complex tape that will be given by reference when the object is being passed to another node, the original variable's value will not change if you change the value of what's coming out of the get var node. However if the variable does have a referenced type, it will. If you are not sure about that, dont panic, I did not apply any custom operations on the variables in Ryven according to their types, so everything behaves strictly following the rules of Python, nothing else.)

### Load&Save

You can save projects by clicking File -> Save Project. You should do this often. When starting Ryven, you can load such a saved project into the editor. A little dialog will show all the required packages for the project you are trying to load. If you have used packages from special places (not the standard packages folder), you should choose them manually. If not, you can use auto import, it will search through all packages in the standard packages directory.

### Save Picture

I see a lot of potential for this software at the visualization of algorithms. To support that, you can save pictures of your flow (View -> Save Pic ...).

#### Viewport Picture
Makes a picture of exactly what you see in the editor.

#### Whole Scene Picture
You also can get a full image of the scene, so you can cut out the parts that you need for use in your presentation for example. The zoom factor determines the resolution.

# Screenshots

![](/docs/resources/images/pyScript14.PNG)

![](/docs/resources/images/ryven_screenshot1.png)
