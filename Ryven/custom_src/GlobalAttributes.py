class Algorithm:
    """gen_data_on_request is used by data OutputPortInstances. This (normally unnecessary) feature allows the user to
    define how the data of the graph is being updated. If gen_data_on_request is set to True, a request of a data
    output's value (from a connected input) causes an update_event in the data output's parent NodeInstance.
    If it is set to False, the output value will directly be returned.
    The difference is important when comparing pure data-flows with execution flows.
    Normally, however, this isn't of the essence."""
    gen_data_on_request = False

class ViewportUpdateMode:
    """A synchronous viewport update mode means that the viewport of a flow, in case of some node activation, is
    updated once the whole execution is finished (once every affected NodeInstance's update event has returned).
    Asynchronous mode causes the viewport to update the rect of a NodeInstance every time a data output value of this
    NodeInstance is set. I made it that way because this feature is really useful for pure, linear data-flows."""
    sync = True