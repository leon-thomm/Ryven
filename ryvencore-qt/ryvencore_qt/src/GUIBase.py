from ryvencore.Base import Base


class GUIBase:
    """Base class for GUI items that represent specific core components"""

    # every frontend GUI object that represents some specific component from the core
    # is stored there under the the global id of the represented component.
    # used for completing data (serialization)
    FRONTEND_COMPONENT_ASSIGNMENTS = {}  # component global id : GUI object

    @staticmethod
    def get_complete_data_function(session):
        """
        generates a function that searches through generated data by the core and calls
        complete_data() on frontend components that represent them to add frontend data
        """

        def analyze(obj):
            """Searches recursively through obj and calls complete_data(obj) on associated
            frontend components (instances of GUIBase)"""

            if isinstance(obj, dict):
                GID = obj.get('GID')
                if GID is not None:
                    # find representative
                    comp = GUIBase.FRONTEND_COMPONENT_ASSIGNMENTS.get(GID)
                    if comp:
                        obj = comp.complete_data(obj)

                # look for child objects
                for key, value in obj.items():
                    obj[key] = analyze(value)

            elif isinstance(obj, list):
                for i in range(len(obj)):
                    item = obj[i]
                    item = analyze(item)
                    obj[i] = item

            return obj

        return analyze

    def __init__(self, representing_component: Base = None):
        """parameter `representing` indicates representation of a specific core component"""
        if representing_component is not None:
            GUIBase.FRONTEND_COMPONENT_ASSIGNMENTS[representing_component.global_id] = self

    # OVERRIDE
    def complete_data(self, data: dict) -> dict:
        """completes the data dict of the represented core component by adding all frontend data"""
        return data
