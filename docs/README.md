# Welcome to the documentation page of pyScript!

pyScript is a standalone software based on Python and Qt for runtime flow-based visual programming in Python. Please keep in mind that this is not a professional piece of software and it shouldn't be seen like that.
It is currently not yet in a state of large package varieties of usable nodes. One of the most important concepts however is the process of creation of new nodes which is fairly easy while restrictions are kept very low (see 'Creating new nodes'). However if people keep creating new nodes, this might look very different in the future. For now, this is more for vp-enthusiasts who intend to create their nodes themselves.

# Idea

The idea is basically to have a runtime flow-based visual programming environment for Python. The runtime part means that you don't export any code, everything gets executed within the editor as you go, at runtime. Beside the main pyScript application (the editor), the pyScript NodeManager lets you manage your existing and create new nodes which you can then program using any code editor for use in your visual scripts. I built this system with the focus on enabling a not too complicated routine for creating new nodes while keeping restrictions far away regarding what can be processed and executed. So you can literally throw any Python code into these nodes and pyScript provides you with the platform to use them in combination with others. There are two types of connections (execution and data connections) but if you are searching for a pure data flow sofware, you can absolutely do normal pure dataflows which opens plenty of possibilities for data manipulations.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=8aOn9OsvlXY
" target="_blank"><img src="http://img.youtube.com/vi/8aOn9OsvlXY/0.jpg" 
alt="Prototype Demonstration Video" /></a>

# Getting Started

## Installation

You need to have **Python 3 and PySide2** installed plus all the packages that you may want to use in the nodes. Some example packages are in the 'packages' folder. And you can find example projects in the 'saves' folder that use these packages. **The start the editor simply run 'pyScript.py'**. To start the NodeManager run 'pyScript NodeManager.py' in the 'pyScript_NodeManager' folder.

## Overview

![](/resources/images/pyScript1.PNG)

When you open pyScript, you will notice, there are different scripts. Every script has variables and a flow (or 'graph'). You can right click on scripts, variables and many other components to perform actions like 'remove' on them.

### Placing Nodes

Just left click on a flow to see what nodes you can place. You can also press 'Shift'+'P' to place a new node besides the last one and move it around with 'Shift'+Arrow.

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

# Creating New Nodes (whatever comes before alpha)

Creating new nodes is not very difficult. However, you do need to get the whole system into your head which is not a matter of seconds.

The overall process looks like this:

- First, you open NodeManager, import the node package that you want to edit or expand (or not if you want to create a completely new package).
- Then, you do your stuff there (changing names, adding new nodes, specifying their colors - all that kind of stuff)
- You save them by exporting them as a package
- Then you open the package folder with a file browser
- You edit the 'metacode' files of the nodes and widgets that you want to program
- You program them, first with a very basic implementation
- You open pyScript
- Import the nodes
- And test them
- And from there you constantly switch between all these stages, making adjustments to improve your nodes

New nodes or actually new node packages are created using the pyScript NodeManager. To really dive into this, it needs a little deeper understanding of how the software works.

What you see when you placed a node in the flow is actually not a node but a node _instance_ which comes from a class for itself (a _NodeInstance_, not the _Node_ class). 

![](/resources/images/pyScript_docs_Node-NodeInstance2.PNG)

Every nodeinstance has a so-called _parent node_ which is a node. But we can instanciate every node as often as we want to as node instances. Furthermore, nodeinstances indeed start in a pre-defined state but they can individually dynamically change. Two nodeinstances having the same parent node (for example 'Print') can look different and do different things when being executed. That is important in order to understand why we will be programming node _instances_ not nodes later on. A node just holds all meta information that applies on all of the nodeinstances either constantly (like title, description, color etc.) or at creation of the nodeinstance (like inputs and outputs which then can be individually modified, added, and deleted in nodeinstances).
A node's configuration is defined using the NodeManager. The actual program that runs when a node _instance_ is being executed gets written manually outside of the NodeManager but the NodeManager generates the files neccessary for the pyScript editor to generate the actual source code.

## NodeManager Overview

This section provides information about the creation of new nodes using the NodeManager. Plase be aware that this application is not extremely intuitive just yet, there are quite a few features still missing. I will work on that :)

![pyScript NodeManager screenshot](/resources/images/Qt 70.png)

This is what the NodeManager can look like. To define a node, you have to specity Name, Type, Description, InputWidgets is used, use of MainWidget, DesignStyle, Color, Inputs and Outputs. If your node has a title that is not class-or file-/foldername conform (like '%'), you need to give a custom 'Internal Name' which then will be used internally instead of the node's title. Caution! You are not getting warned if your node title is not conform and you try to save your nodes. But that's one feature on my list I will try to implement soon.

Input widgets are custom widgets you can program for input ports of the node.

![](/resources/images/pyScript2.PNG)

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

![](/resources/images/pyScript5.PNG)

Background info (not neccessary for the task):

> As you can see, we are actually programming a newly generated class derived by _NodeInstance_. This NodeInstance class is the one that gets instanciated when creating new node instances by placing them in a flow, so every single node instance you see in the editor is an object of this class. That way the class inherits some very useful concepts like the specification of custom actions by right clicking on a node while still enabeling reimplementations of certain methods (like the creation of such a right-click menu if you wanted to customize that).

### Special Actions

_The special actions attribute is a dictionary_ and holds information about accessible right-click operations which then will automatically be created when right clicking on a node instance. A possible entry would be

        self.special_actions['pring something'] = {'method': self.action_print_something}

In this case, a method _action_print_something_ would need to exist

    def action_print_something(self):
        print('Hello World!')

And that's basically it.

### Methods

#### Updating

This is where the magic happens. 

Node instances can be connected using either execution connections or data connections. Execution connections are just to activate something actively. They cause an update event in the on the right side connected node instance. Data connections are to get some data from elsewhere. This data will be requested _after_ the node instance received an execution signal.

There are two types of nodes regarding the architechture of the _updating()_ method. Acitve nodes and passive nodes. An active node has at least one execution input. A passive node doesn't. They are called active and passive, becuase the active node instance only does stuff (including setting values of data outputs) when it received an execution signal (aka an execution input port received a signal -> _input_called_ is the index of an exec input port). Whereas a passive node instance is always supposed to update all output values if any output value was requested from somewhere.

That is convention.

This means, you always have to check for the _input_called_ parameter in active node instances unlike in passive ones. Example:

An If node instance's _updating()_ method (active):

    def updating(self, token, input_called=-1):
        if input_called == 0:
            self.do_if(0, self.else_if_enlargement_state)

A + node instance's _updating()_ method (passive):

    def updating(self, token, input_called=-1):
        try:
            sum_val = sum([self.input(i) for i in range(len(self.inputs))])
            self.outputs[0].set_val(sum_val)
        except Exception as e:
            sum_val = ''
            for i in range(len(self.inputs)):
                sum_val += str(self.input(i))
            self.outputs[0].set_val(sum_val)

If you follow these rules, you should be fine.

One exception: in the case that your node instance executes multiple times the same execution output, like a for loop does, you need to create a new **Token** each time, to clarify everytime that this is a _new_ execution call.

So, the For Each Loops's _updating()_ method should look like this:

    def updating(self, token, input_called=-1):
        if input_called == 0:                # activated
            for obj in self.input(1):
                self.handle_token(None)      # creates a new token
                self.outputs[1].set_val(obj) # setting an output value - not important here
                self.exec_output(0)          # executing loop output

            self.handle_token(token)         # reset to the original token
            self.exec_output(2)              # execute 'finished' output

Another important thing is: if you want to call _self.updating()_, don't do it directly. Always call

> self.update()

The _updating()_ method gets called somewhere in a loger process of method calls internally, so a direct call of _self.updating()_ can cause trouble. You probably don't need that but if you take a look at the 'Minimal Example' below, you see an example where this is important.

![](/resources/images/pyScript8.PNG)

That is important, otherwise some nodes - especially passive nodes - will not be updated and remain in the exact same state. See section 'Tokens' below.

#### Get/Set Data

_get_data()_ is called when a project is being saved or a node instance is copied by the user or similar actions. Contrary to that, _set_data(data)_ gets called when a project gets loaded or a copied node instance is being pasted and stuff like that. Both methods are only important for node instances with **states**. If the behaviour of your node instance is the same as of any other node instance of the same parent node, if everything that happens is dependent on what is being triggered (like an execution input) and not on any internal variables, then you don't have to do anything there. But if your nodes stores some internal data (for example some randomly generated points that should get shown again when loading a project exactly like when it was saved), you have to provide it in _get_data()_ **in JSON compatible format** and you have to set it again in _set_data(data)_.

#### Removing

The _removing()_ method is being called when a node instance gets removed from the flow. This is only important for node instances that autonomously run independent computations like threads or timers. These should all be stopped in this method.

## API

To access the node instance's contents there is a small 'API' that you can use inside the node instance class.

#### Logging

You can log mesasges to the script's logs via

> self.log_message(message: str, target='global')

_target_ can be _global_ or _error_ which addresses the global messages log or the error log.

A node instance can also request new logs using

> self.new_log(title: str)

One node instance can hold mutliple personal logs. When using logs, don't forget to add

> mylog.removing()

for every log in the _removing()_ method. This will cause the log widget in the script's logging area to change appearance.

#### Shape

You can cause a recomputation of the shape of the node instance including the positions of all contents using the

> self.update_shape()

command. Every time you add, remove, rename (whatever) an input or output, resize a widget - anything -, after you completed that, you should call _self.update_shape()_ once at the end.

#### Ports

Adding a new input port:

> self.create_new_input(type_: str, label: str, append=True, widget_type='', widget_name='', widget_pos='under', pos=-1)

- _type__ refers to the input's type ('exec' or 'data')
- _label_ is the shown name of the port
after these two I recommend only using unpositional identifiers
- (I do not recommend using _append_, it will be removed soon; use _pos_) _append=True_ **and** _pos=-1_ means, the input will be appended at the end. Setting _append_ with _pos=-1_ inserts the points at the first position. By setting the _pos_, you can specify an index at which the new input shall be inserted. -1 means append.
All widget related arguments are only important for data inputs:
- The _widget_type_ is the type of the input widget that will be created. Possible values are:
    - 'std line edit'
    - 'std spin box'
    - 'custom'
- If _widget_type_ is 'custom', you must give a _widget_name_ which must refer to an already programmed input widget.
- _widget_pos_ determines whether the input widget will be 'besides' or 'under' the the Port

Adding a new output port:

> self.create_new_output(type_, label, append=True, pos=-1)

see 'Adding a new input port'.

Deleting input port:

> self.delete_input(index)

Deleting output port:

> self.delete_output(index)

Renaming input port:

> ...

Renaming output port:

> ...

## Programming Widgets

The possibility to program custom widgets for the node instances is one of the corea concepts. It is not very different from programming the node instance itself. Widgets are being created by programming a class that derives from QWidget, so everything that you can do with a QWidget can be done in the node's custom widgets - which is pretty amazing, you could throw whole programs into nodes if you wanted to. There are two types of widgets. A node instance can have a main widget which sits either between or under the ports, and every data input of a node instance can have a widget too. All widget classes must be stated in the NodeManager (whether it has a main widget and every custom input widget in the 'Input Widgets' area). When saving the node in a package, the NodeManager will then create template files (_METACODE_) for all these widgets (just like for the node intance class) which you can find in the 'widgets' folder in the node's directory. To program the widgets, simply edit these metacode files.

### Main Widget

The metacode for a main widget looks somehow like this:

    from PySide2.QtWidgets import ...
    # from PySide2.QtCore import ...
    # from PySide2.QtGui import ...

    import os


    class %NODE_TITLE%_NodeInstance_MainWidget(...):
        def __init__(self, parent_node_instance):
            super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

            # leave these lines ------------------------------
            self.parent_node_instance = parent_node_instance
            self.package_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../../')
            # ------------------------------------------------

            self.setStyleSheet('''

            ''')

            # ...


        def get_data(self):
            data = {}
            # ...
            return data

        def set_data(self, data):
            pass



        # optional - important for threading - stop everything here
        def removing(self):
            pass

You can either let the class derive directly from QWidget (just import it in the first like and put it in the parantheses behind the class name), or from a specified one like QLineEdit (same process).

#### Access Parent Node Instance

You can access the parent node instance via

> self.parent_node_instance

#### Using Custom Content - Package Path

As you can see there is a package path which is the path to the package the node instance is a part of. This is very useful if you want to use resources laying on your file system, images for example. You can put them anywhere you want into the package directory, they will not be removed by the NodeManager when overwriting the package.

#### Get/Set Data

Exactly the same idea as in the node instance class (see above). The widget of course also only gets exactly the data in _set_data()_ which it previously provided in _get_data()_.

#### Removing

Exactly the same idea as in the node instance class (see above). Stop all autonomously running element there (threads, timers etc).

#### Minimal Example

The following code is an example for a button node. Once you press the button, the first and only execution output should get executed. Because all the connecting is done in the node instance class, this is pretty simple:

    from PySide2.QtWidgets import QPushButton


    class %NODE_TITLE%_NodeInstance_MainWidget(QPushButton):
        def __init__(self, parent_node_instance):
            super(%NODE_TITLE%_NodeInstance_MainWidget, self).__init__()

            # leave these lines ------------------------------
            self.parent_node_instance = parent_node_instance
            # ------------------------------------------------
            self.setStyleSheet('''
                background-color: #36383B;
                padding-top: 5px;
                padding-bottom: 5px;
                padding-left: 22px;
                padding-right: 22px;
                border: 1px solid #666666;
                border-radius: 5px;
            ''')

        def get_data(self):
            return {}

        def set_data(self, data):
            pass



        # optional - important for threading - stop everything here
        def removing(self):
            pass

![](/resources/images/pyScript9.PNG)

In the node instance class, we need to connect this button like that:

    # ...

    class %NODE_TITLE%_NodeInstance(NodeInstance):
        def __init__(self, parent_node: Node, flow, configuration=None):
            super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

            self.main_widget.clicked.connect(self.button_clicked)

            if configuration:
                self.set_data(configuration['state data'])

        def button_clicked(self):
            self.update()

        def updating(self, token, input_called=-1):
            self.exec_output(0)

    # ...

### Data Input Widgets

There are standard widgets for data inputs which you can select in the NodeManager for the pre defined ports, or you can also use them when programatically adding new inputs (see section 'Ports' above). But you can also program custom widgets for inputs.

After you stated the existence of the custom input widget in the NodeManager and saved the node in a package, the metacode files that you can edit should be in the 'widgets' folder of you node. Programming a custom widget does not differ from programming a main widget at all.

# Advanced

## Tokens

A so-called _token_ is created when an execution 'impulse' is created. It tells the node instance receiving an update event call whether the script is still executing the same execution string.

![](/resources/images/pyScript6.PNG)

The + node instance does not have to update again when the set var b node instance causes a request for the output value through the / node instance, because the + already updated when the set var a node instance requested data. That is a performance measure. It might seem a little overpowered but if this + node instance would depend on a few other passive node instances which themselves depend on event more passive node instances, we would run very quickly into serious performance issues.

I'm actually proud of that. I just got the idea very spontaniously one sunday morning and for my conditions this is working way too well :)


## Storing Data In Actions

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

## Updating Algorithm

![](/resources/images/pyScript4.PNG)

Assuming the If node received a signal at input 0 (execution) - maybe by the richtig click actions menu by the user - this is what happens here:

> 1. The the If's _updating()_ method is being called with _input_called_ == 0
> 2. The If's _input(1)_ method is called because the If needs the data from this input to continue
> 3. The If's second input sees that it is connected (the user could also type something directly into the input widget), so it requestes the data from the output of the ==
> 4. The =='s _updating()_ method is called with _input_called_ == -1
> 5. The == calls self.input(0)
> 6. The =='s first input port has no connections, so it returns what is typed into the input witget (the number 1)
> 7. The == calls self.input(1)
> 8. The =='s second input port returns 2
> 9. The == sets it's output port's value to 3 and returns
> 10. The =='s output port returns
> 11. The If's second input port returns 2
> 12. The If executes output 1 (second output)
> 13. The Print B's _updating()_ method is called with _input_called_ == 0
> 14. The Print calls self.input(1)
> 15. The Print's second input requests data from the =='s output
> 16. The =='s output sees, that it already updated in this execution task, so it instantly returns 3
> 17. The Print's second input returns 3
> 18. The Print prints 3

_updating()_ gets called every time, the node received a signal. It is important, that the parameter _input_called_ specifies the input of the node that received a signal. This value can be -1 if the node updated itself normally because the value of a data _output_ was requested by another node and it has not been set yet in the current execution of the script.