# statically stores source codes of nodes and their widgets
from dataclasses import dataclass
from typing import Type, Optional
import inspect

from ryvencore import Node
from ryven.main.config import instance


def register_node_type(n: Type[Node]):
    """
    Inspects and stores source code of a node type.
    """

    has_gui = hasattr(n, 'GUI')  # check if node type has custom gui
    has_mw = has_gui and n.GUI.main_widget_class is not None

    src = inspect.getsource(n)
    mw_src = inspect.getsource(n.GUI.main_widget_class) if has_mw else None
    inp_src = {
        name: inspect.getsource(cls)
        for name, cls in n.GUI.input_widget_classes.items()
    } if has_gui else None

    class_codes[n] = NodeTypeCodes(
        node_cls=src,
        main_widget_cls=mw_src,
        custom_input_widget_clss=inp_src,
    )

    if instance.src_code_edits_enabled:
        # store full module source code
        mod_codes[n] = inspect.getsource(inspect.getmodule(n))
        if has_mw:
            mod_codes[n.GUI.main_widget_class] = \
                inspect.getsource(inspect.getmodule(n.GUI.main_widget_class))
            for inp_cls in n.GUI.input_widget_classes.values():
                mod_codes[inp_cls] = inspect.getsource(inspect.getmodule(inp_cls))


@dataclass
class NodeTypeCodes:
    node_cls: str
    main_widget_cls: Optional[str]
    custom_input_widget_clss: {str: str}


class Inspectable:
    """
    Represents an object whose source code can be inspected.
    This is either a node or some node widget.
    Used by the code editor to store polymorphic references to
    objects which can be inspected.
    """
    def __init__(self, node, obj, code):
        self.node = node
        self.obj = obj
        self.code = code


class NodeInspectable(Inspectable):
    def __init__(self, node, code):
        super().__init__(node, node, code)


class MainWidgetInspectable(Inspectable):
    pass


class CustomInputWidgetInspectable(Inspectable):
    pass


class_codes: {Type[Node]: {}} = {}
# {
#     Type[Node]: NodeTypeCodeInfo
# }


#
# below fields are only used when src code edits are enabled
#


# maps node- or widget classes to their full module source code
mod_codes: {Type: str} = {}

# maps node- or widget objects to their modified source code
modif_codes: {object: str} = {}
