class Flow_AlgorithmMode:
    """ Owned by a flow.
    This mode is used by data OutputPortInstances in the flow that holds the AlgorithmMode object.
    This feature allows the user to define how changes of data in the graph get updated/propagated.
    If mode_data_flow is set to True, a request of a data
    output's value (from a connected input) causes an update_event in the data output's parent NodeInstance.
    If it is set to False, the output value will directly be returned.
    The difference is important when comparing pure data-flows with execution flows."""
    mode_data_flow = True