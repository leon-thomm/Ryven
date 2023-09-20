
<p align="center">
  <img src="./img/logo.png" alt="drawing" width="70%"/>
</p>

`ryvencore-qt` provides Qt-based GUI classes for ryvencore, and is itself a Python package. The Ryven editor is built on top of `ryvencore-qt`. `ryvencore-qt` uses the PySide2 Python bindings for Qt. It shouldn't be too much work to get it running with PySide6 but I didn't try it yet. PyQt is not supported (because it doesn't allow for multi-inheritance on QObject derived classes).

### Installation

```
pip install ryvencore-qt
```

or build from sources

```
git clone https://github.com/leon-thomm/ryven
cd ryven/ryvencore-qt
pip install .
```
