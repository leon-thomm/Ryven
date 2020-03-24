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
A node is not a node. Or what you see when you placed one in the graph is actually not a node but a node _instance_. Every nodeinstance has a so-called _parent node_ which is a node. But we can instanciate every node as often as we want to as node instances. Furthermore, nodeinstances indeed start in a pre-defined state but they can individually dynamically change. Two nodeinstances having the same parent node (for example 'Print') can look different and do different things when being executed. That is important in order to understand why we will be programming node _instances_ not nodes later on. A node just holds all meta information that applies on all of the nodeinstances either constantly (like title, description, color etc.) or at creation of the nodeinstance (like inputs and outputs which then can be individually modified, added, and deleted in nodeinstances).
A node's configuration is defined using the NodeManager. The actual program that runs when a node _instance_ is being executed gets written manually outside of the NodeManager but the NodeManager generates the files neccessary for the pyScript editor to generate the actual source code.

## NodeManager Overview

This section provides information about the creation of new nodes using the NodeManager. Plase be aware that this application is not extremely intuitive just yet, there are quite a few features still missing. I will work on that :)

![pyScript NodeManager screenshot](/resources/images/Qt 70.png)

This is what the NodeManager can look like. To define a node, you have to specity Name, Type, Description, InputWidgets is used, use of MainWidget, DesignStyle, Color, Inputs and Outputs. If your node has a title that is not class-or file-/foldername conform (like '%'), you need to give a custom 'Internal Name' which then will be used internally instead of the node's title. Caution! You are not getting warned if your node title is not conform and you try to save your nodes. But that's one feature on my list I will try to implement soon.

Input widgets are custom widgets you can program for input ports of the node.

![pyScript NodeManager screenshot](/resources/images/pyScript2.PNG)

When using custom input widgets, you must define them in the 'Input Widgets' area and give the exact name in the 'input widget name' line edit of the input you want to have this widget. Multiple inputs can have the same custom widget. The 'Yes' and 'No' radio buttons specify whether your input has a widget at all or not. Execution inputs do not have custom widgets, so then you can ignore the whole widgets part of the input's indget.

## Updating Packages 

If you want to change the properties of an existing node, you need to start the NodeManager, import the node's package, do the changes that you want to perform and save it again. You can and should choose the original package directory. None of your content will be deleted or edited. Source code files get only created if they do not already exist (see next section) and all your custom files and folders you have put somwhere into the packages directory stay as they are. It is important, that you keep one main name for your package. If you create different versions of it and use different versions in different pyScript projects, you can only use these versions. So if you want to edit an existing package, save it as a new package first, test it and when everything works, overwrite the original package by just saving it in the original package folder in the NodeManager.

## Programming Nodes

And there we are. Programming nodes is not very difficult once you got the idea. The basic concepts are:

- For every node (as well as all it's widget classes, more on that later), the NodeManager creates **METACODE**-files from templates if they are not already existing. All programing is done by editing these METACODE files.
- pyScript will create the actual source code files every time the package is being imported. These get created in the same locations as the metacode files.
- **Do not edit non-metacode source files directly, as these changes will be lost.**

To start programming a node, simply direct into it's folder in the package directory and open the metacode python file with a code editor. **I strongly recommend using the Atom editor to program the metacode files** as compared with oder text-or code editors, Atom supports you with a good code completion which causes your attention if you typed something wrong while not outraging because there are expressions in a .py file that can not be resolved like that by Python. Also I sometimes got spaces-itentation problems when I tried oder editors - for example Notepad++.

If you open the file, you will see something similar to this:

![pyScript NodeManager screenshot](/resources/images/pyScript2.PNG)

Background info (not neccessary for the task):

> As you can see, we are actually programming a newly generated class derived by _NodeInstance_. This NodeInstance class is the one that gets instanciated when creating new node instances by placing them in a flow, so every single node instance you see in the editor is an object of this class. That way the class inherits some very useful concepts like the specification of custom actions by right clicking on a node while still enabeling reimplementations of certain methods (like the creation of such a right-click menu if you wanted to customize that).

### Special Actions

_The special actions attribute is a dictionary_ holds information about accessible right-click operations which then will automatically be created when right clicking on a node instance. A possible entry would be

        self.special_actions['pring something'] = {'method': self.action_print_something}

In this case, a method _action_print_something_ would need to exist

    def actions_print_something(self):
        print('Hello World!')

And that's basically it.

#### Advanced - Storing Data About The Action

You probably will not need this, so don't let yourself get confused if you didn't search for it.

Only if you want to create very dynamic nodes with multiple right click operations representing the same action but for different inputs while having a dynamic number of these inputs - then you will definately run into this, so I had to come up with a solution.

When you have multiple entries in _special_actions_ that point to the same method like that:

        self.special_actions = {'delete input 1': {'method' : self.action_delete_input},
                                'delete input 2': {'method' : self.action_delete_input}}

because the user added an input through another action for example, then how can we determine in the _delete_input_ method which action was pressed?

The solution is another attribute in the action's object in the _special_actions_ dict:

        self.special_actions = {'delete input 1': {'method' : self.action_delete_input,
                                                   'data' : {'input number' : 1}},
                                'delete input 2': {'method' : self.action_delete_input},
                                                   'data' : {'input number' : 2}}

and the extension of the _delete_input_ method by a _data_ parameter

    def action_delete_input(self, data):
        input_number = data['input number']

Full example following soon...

### Methods

#### Updating

This is where the magic happens. 

Nodes can be connected using either execution connections or data connections. Execution connections are just to activate something actively. Data connections are to get some data from elsewhere. This data will be requested _after_ the node received an execution signal.

PICTURE

So, once this Print node received a signal at input 0, it requests data from the + node to know what it is supposed to print. That is being done by calling a 

_updating()_ gets called every time, the node received a signal. It is important, that the parameter _input_called_ specifies the input of the node that received a signal. This value can be -1 if the node updated itself normally because the value of a data _output_ was requested by another node and it has not been set yet in the current execution of the script.

### API

asdf

## Programming Widgets