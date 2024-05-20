# statically stores source codes of nodes and their widgets
from dataclasses import dataclass
from typing import Type, Optional, Dict, no_type_check
import inspect

from ryvencore import Node
from ryven.main.config import instance


def register_node_type(n: Type[Node]):
    """
    Registers a node type and loads its source code directly if deferred 
    source code loading is disabled.
    """

    assert instance is not None, 'Ryven instance not initialized.'

    if not instance.defer_code_loading:
        load_src_code(n)
    else:
        class_codes[n] = None


@no_type_check
def load_src_code(n: Type[Node]):
    # check for custom GUI and main widget
    has_gui = hasattr(n, 'GUI')
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
    custom_input_widget_clss: Dict[str, str]


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


class_codes: Dict[Type[Node], Optional[NodeTypeCodes]] = {}
# {
#     Type[Node]: NodeTypeCodeInfo
# }


#
# below fields are only used when src code edits are enabled
#


# maps node- or widget classes to their full module source code
mod_codes: Dict[Type, str] = {}

# maps node- or widget objects to their modified source code
modif_codes: Dict[object, str] = {}
