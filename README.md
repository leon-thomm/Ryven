<p align="center">
  <img src="./Ryven/resources/pics/logo.png" alt="drawing" height="200"/>
</p>

# A simple flow-based visual scripting env for Python

## Intro

Hello there! Ryven is an editor combining flow-based visual scripting with Python. It provides an easy to use system for programming nodes executing any Python code.

*Be aware that all the all new Ryven 3, and particularly the new underlying framework, haven't been tested extensively yet, so there might be some further changes incoming.*

## Installation

```
pip install ryven
```

or from sources
```
git clone https://github.com/leon-thomm/ryven
cd Ryven
python setup.py install
```

If you're using the master branch, make sure to also use the master branch of [ryvencore-qt](https://github.com/leon-thomm/ryvencore-qt) instead of the the pip version.

## Features

- **simple nodes system**  
All information about a node is part of its class. A minimal node definition can be as simple as this

    ```python
    class PrintNode(Node):
        """Prints your data."""

        title = 'Print'
        init_inputs = [
            NodeInputBP()
        ]
        color = '#A9D5EF'
    
        def update_event(self, inp=-1):
            print(self.input(0))
    ```
- **macros aka subgraphs**  
You can define *macros* which get registered as nodes themselves

    ![](./docs/img/macro.png)
    Macros are like all other scripts, so they have their own flow, plus input and output node
    ![](./docs/img/macro2.png)
- **right click operations system for nodes**  
which can be edited through the API at any time.
    ```python
    self.special_actions[f'remove input {i}'] = {
        'method': self.rem_input,
        'data': i,
    }

    # with some method...
    def rem_input(self, index):
        self.delete_input(index)
        del self.special_actions[f'remove input {len(self.inputs)}']
    ```
- **Qt widgets**  
You can add custom QWidgets for your nodes, so you can also easily integrate your existing Python-Qt widgets.
    ```python
    class MyNode(Node):
        main_widget_class = MyNode_MainWidget
        main_widget_pos = 'below ports'  # alternatively 'between ports'
        # ...
    ```
<!-- - **convenience GUI classes** -->
- **many different modifiable themes**  
![](./docs/img/themes_1_merged.png)
- **exec flow support**  
While data flows are the most common use case, exec flows (like [UnrealEngine BluePrints](https://docs.unrealengine.com/4.26/en-US/ProgrammingAndScripting/Blueprints/)) are also supported.
- **stylus support for adding handwritten notes**  
![](./docs/img/stylus_light.png)
- **rendering flow images**  
- **logging support**  
    ```python
    import logging
    class MyNode(rc.Node):
        def __init__(self, params):
            super().__init__(params)

            self.my_logger = self.new_logger(title='nice log')
        
        def update_event(self, inp=-1):
            self.my_logger.log(logging.INFO, 'updated!')
    ```
- **variables system**  
with an update mechanism to build nodes that automatically adapt to change of variables.

    ```python
    import logging
    class MyNode(Node):
        ...
        def __init__(self, params):
            super().__init__(params)
            self.my_logger = self.new_logger(title='nice log')
            # assuming a 'messages' var exists in the script
            self.register_var_receiver(name='messages', method=self.new_msg)
            # causes new_msg() to trigger when var 'messages' updates
        
        def new_msg(self, msgs: list):
            self.my_logger.log(logging.INFO, f'received msg: {msgs[-1]}')
    ```

Also visit the [website](https://ryven.org) if you haven't been there already.

Ryven is now built on top of [ryvencore-qt](https://github.com/leon-thomm/ryvencore-qt), a framework for building Ryven-like editors. Nodes from Ryven are easily migratable to other ryvencore-qt editors.

## Contributions

To support the development of this project, which will decide its future, check out the [ryvencore-qt](https://github.com/leon-thomm/ryvencore-qt) repo where the main development is happening.

Feel free to open discussions here (there's a discussions area in this repo) also regarding the frameworks.
