# pyScript
All about the pyScript project.

pyScript is a standalone software based on Python and Qt for runtime flow-based visual programming in Python. Please keep in mind that this is not a professional piece of software and it shouldn't be seen like that.
This software is currently not yet in a state of large usable node packages. However if people keep creating new nodes, this might look very different in the future. For now, this is more fore vp-enthusiasts who intend to create their nodes themselves.

# Idea
The idea is basically to have a runtime flow-based visual programming environment for Python. The runtime part means that you don#t export any code, everything gets executed within the editor, at runtime. The core concept of this software is the way new nodes are added/new node packages are created. Beside the main pyScript application (the editor), the pyScript NodeManager lets you manage your existing and create new nodes which you can use in your visual scripts. I built the whole system with the focus on enabling a not too complicated routing for creating new nodes while keeping restrictions regarding what can be processed and executed far away.

# pyScript overview

# Creating new nodes
Creating new nodes is not very difficult. However, you do need to get the whole system into your head which is not a matter of seconds. New nodes or actually new node packages are created using the pyScript NodeManager. To dive into this, it needs a little deeper understanding of how the software works.
A node is not a node. Or what you see when you placed on in the graph is actually not a node but a node _instance_. Every nodeinstance has a so-called _parent node_ which is a node. But we can instanciate every node as often as we want to. Furthermore, nodeinstances indeed start in a pre-defined state but they can actually individually dynamically change. That means two nodeinstances having the same parent node (for example 'Print') can look different and do different things when being executed. That is important to understand why we will be programming node _instances_ not nodes later. So, a node just holds all meta information that applies on all of the nodeinstances either constantly (like title, description, color etc.) or at creation of the nodeinstance (like inputs and outputs which then can be individually modified, added, and deleted in nodeinstances).
A node's configuration is defined using the NodeManager. The actual program that runs when a node _instance_ is being executed gets written manually outside of the NodeManager.

## NodeManager Overview

## Programming Nodes
### Overview

asdf
### API
asdf
### A collection of important notes
