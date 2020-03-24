## Welcome to the documentation page of pyScript!

pyScript is a standalone software based on Python and Qt for runtime flow-based visual programming in Python. Please keep in mind that this is not a professional piece of software and it shouldn't be seen like that.
It is currently not yet in a state of large package varieties of usable nodes. One of the most important concepts however is the process of creation of new nodes which is fairly easy while restrictions are kept very low (see 'Creating new nodes'). However if people keep creating new nodes, this might look very different in the future. For now, this is more fore vp-enthusiasts who intend to create their nodes themselves.

# Idea

The idea is basically to have a runtime flow-based visual programming environment for Python. The runtime part means that you don't export any code, everything gets executed within the editor as you go, at runtime. Beside the main pyScript application (the editor), the pyScript NodeManager lets you manage your existing and create new nodes which you can then program using any code editor for use in your visual scripts. I built this system with the focus on enabling a not too complicated routine for creating new nodes while keeping restrictions far away regarding what can be processed and executed. So you can literally throw any Python code into these nodes and pyScript provides you with the platform to use them in combination with others.

# Getting Started

## Installation

You need to have **Python 3 and PySide2** installed plus all the packages that you may want to use in the nodes. Some example packages are in the 'packages' folder. And you can find example projects in the 'saves' folder that use these packages. *The start the editor simply run 'pyScript.py'*. To start the NodeManager run 'pyScript NodeManager.py' in the 'pyScript_NodeManager' folder.

## Overview

![pyScript NodeManager screenshot](/resources/images/pyScript1.PNG)

When you open pyScript, you will notice, there are different scripts. Every script as variables and a flow (or 'graph'). You can right click on scripts, variables and many other components to perform actions like 'remove' on them.

### Placing Nodes

Just left click on a flow to see what nodes you can place.

### Importing Nodes

You need to import nodes before you can use them from node packages (File -> Import Nodes and then choose a nodes package file *.pypac). If the import succeeded, you will then be able to use the imported nodes in all scripts.

### Variables

You can create new variables just like scripts. By right clicking on a variable, you can set the value in the dialog that pops up. Whatever you type into that field will be evaluated by Python using the eval() method, so the datatype will automatically be parsed just like when assigning variables in Python source code. To use a variable, you must use the get var node. As long as your variable does not have a complex tape that will be given by reference when the object is being passed to another node, the original variable's value will not change if you change the value of what's coming out of the get var node. However if the variable does have a referenced type, it will.

If you are not sure about that, dont panic, I did not apply any custom operations on the variables in pyScript according to their types, so everything behaves strictly following the rules of Python, nothing else.

### Load&Save

You can save projects by clicking File -> Save Project. You should do this often. When starting pyScript, you can load such a saved project into the editor. A little dialog will show all the required packages for the project you are trying to load. If you have used packages from special places (not the standard packages folder), you should choose them manually. Normally if you only used packages located in the packages folder, you can use auto import, it will search through all packages in this directory.

### Stylus Support

You can use stylus pens for either editing flows aka programming just like normal or to put notes into your script. In the top right corner, you can spcify that. Be aware, that this feature is not heavily tested, it surely contains some bugs.

### Save Picture

I see a lot of potential for this software at the visualization of algorithms. To support that, you can save pictures of your flow. Besides the option to just get a screenshot of the viewport, you also can get a full image of the scene, so you can cut out the parts that you need for use in your presentation for example. Just remember to zoom in before if you want to create a high resolution image. Be aware that this might take a bit of time.

### Debugging

If you are troubleshooting your nodes, you can turn debugging on. This will print a lot of information in the output window including the following
        
        EXCEPTION IN <NodeInstance Name> NI: <exception>
        
error message whenever the execution of a node returned an error. That is a very useful feature but one of the most things I have to work on most importantly since this is not very intuitive yet. Stay tuned.

# Creating New Nodes

Creating new nodes is not very difficult. However, you do need to get the whole system into your head which is not a matter of seconds. New nodes or actually new node packages are created using the pyScript NodeManager. To dive into this, it needs a little deeper understanding of how the software works.
A node is not a node. Or what you see when you placed on in the graph is actually not a node but a node _instance_. Every nodeinstance has a so-called _parent node_ which is a node. But we can instanciate every node as often as we want to. Furthermore, nodeinstances indeed start in a pre-defined state but they can actually individually dynamically change. That means two nodeinstances having the same parent node (for example 'Print') can look different and do different things when being executed. That is important to understand why we will be programming node _instances_ not nodes later. So, a node just holds all meta information that applies on all of the nodeinstances either constantly (like title, description, color etc.) or at creation of the nodeinstance (like inputs and outputs which then can be individually modified, added, and deleted in nodeinstances).
A node's configuration is defined using the NodeManager. The actual program that runs when a node _instance_ is being executed gets written manually outside of the NodeManager.

## NodeManager Overview

## Programming Nodes

### Overview

![pyScript NodeManager screenshot](/resources/images/Qt 70.png)
asdf
### API

asdf

### A collection of important notes

