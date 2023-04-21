import json
import unittest

import ryvencore as rc
from ryven.main.RyvenConsole import load_project_and_nodes


class RyvenConsoleTestCase(unittest.TestCase):
    # This class tests the working of the underlying methods used by RyvenConsole, i.e. that do not use
    # the GUI elements of Ryven.

    def test_load_empty_flow(self):
        # Create empty flow
        rc.Base.Base._global_id_ctr.ctr = -1
        session = rc.Session()
        session.create_flow('main')
        serialize = session.serialize()
        json_string = json.dumps(serialize)
        del session

        test_data_path = ".\\data\\test.json"
        with open(test_data_path, "w") as f:
            # Writing data to a file
            f.write(json_string)

        # Given how the Global IDs work (they are re-generated every time an object is created)
        # we reset the counter manually to ensure the IDs are the same
        rc.Base.Base._global_id_ctr.ctr = -1

        # Reload file
        session = rc.Session()
        load_project_and_nodes(test_data_path, [], None, session)

        self.assertEqual(serialize, session.serialize())


if __name__ == '__main__':
    unittest.main()
