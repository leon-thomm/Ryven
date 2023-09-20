# GUI for flows

The frontend for flows mainly consists of the classes

- `FlowView` - representing `ryvencore.Flow`
- `NodeItem` - representing `ryvencore.Node`
- `ConnectionItem` - representing `ryvencore.Connection`

Furthermore, there are drawing objects (which is the stylus drawings in the scene), a nodes list widget with drag&drop support (which can also be used outside of `FlowView`), all the flow themes in `FlowTheme.py` and lots of classes around `NodeItem` implementing specific parts. Notice that, besides `FlowView.py` there is also `Flowcommands.py` where all abstract undoable actions you can perform in the flow are implemented for the `FlowView` in a reactive way.