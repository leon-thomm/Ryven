class Design:
    flow_style = 'dark std'
    ryven_stylesheet = None
    node_instance_shadows_shown = False
    animations_enabled = True


class Algorithm:
    """gen_data_on_request is used by data OutputPortInstances. This (normally unnecessary) feature allows the user to
    define how the data of the graph is being updated. If gen_data_on_request is set to True, a request of a data
    output's value (from a connected input) causes an update_event in the data output's parent NodeInstance.
    If it is set to False, the output value will directly be returned.
    The difference is important when comparing pure data-flows with execution flows.
    Normally, however, this isn't of the essence."""
    gen_data_on_request = False


class PerformanceMode:
    mode = 'fast'  # fast or pretty