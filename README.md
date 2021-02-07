# A simple flow-based visual scripting runtime environment for Python

Ey, what's up! Please visit the [website](https://ryven.org)

### Basic Requirements

- Python 3 (3.8+ recommended)
- PySide2 (2.14+ recommended)

### Installation

- please use the lastest release
- a complete requirements file is in the root folder
- If you experiment a lot, you maybe should set up a virtual env, like this (Windows example):
```
<open cmd>
cd <to your Ryven folder (the outer one)>
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
```

### Ideas and TODOs
- visual content: logos, splash screen, industrial flow theme (and more?)
- hide/show unconnected inputs and outputs action
- code node, interpreter node
- reload imported packages
- modifiable display title for nodes
- tutorials

rather long term:
- subgraphs
- advanced source code editor widget, with syntax highlighting and autocomplete for Ryven, the NodeManager and a *code* node
- Jupyter integration (the native Jupyter QtConsole I seems kinda sketchy)
- better touch controls (not gonna happen until the [guys at QtCompany finally fix this](https://bugreports.qt.io/browse/PYSIDE-287))

![](/docs/images/ryven_screenshot2.png)

![](/docs/images/ui.png)

![](/docs/images/ryven1.png)

![](/docs/images/matrices1.png)

![](/docs/images/checkpoints.png)

![](/docs/images/matplotlib.jpeg)

![](/docs/images/opencv_1.png)

![](/docs/images/matrices2.png)

![](/docs/images/extract_property_1.png)

![](/docs/images/random.png)
