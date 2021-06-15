from NENV import *
import requests
import json
import time
import logging
#todo remove before flight;)
from ryvencore_qt import *

class Hue_Bridge(Node):
    log = None

    def __init__(self, params):
        super().__init__(params)
        self.ConnectionErrorCount = 0
        self.ConnectionErrorRetries = 1
        self.bridge_ip = None
        self.bridge_id = None
        self.bridge_username = None
        if Hue_Bridge.log is None:
            Hue_Bridge.log = self.new_logger(title='Hue log')
        vm = self.get_vars_manager()
        vm.create_new_var('Hue IP address', "none")
        vm.create_new_var('Hue username', "none")
        self.register_var_receiver('Hue IP address', self.newIP)
        self.register_var_receiver('Hue username', self.newUsername)
        self.log.info("finished Hue_Bridge constructor")

    def updateIP(self):
        """looks for a Hue-Bridge with the same id as the one associated with this Hue_Bridge-object on the local network.
        Then updates the ip address."""
        self.log.info("old IP address: %s", self.bridge_ip)
        # TODO this method is deprecated. Upgrade!
        response = requests.get("https://discovery.meethue.com")  # get a list of all Hue-Bridges on the network
        response = json.loads(response.text)
        self.log.info("found %s bridges on the network", len(response))
        for bridge in response:
            if bridge["id"] == self.bridge_id:  # find the bridge with the correct bridge TODO is the id permanent?
                self.bridge_ip = bridge["internalipaddress"]
                self.get_vars_manager().set_var('Hue IP address', self.bridge_ip)
        self.log.info("new IP address: %s", self.bridge_ip)

    def get_state(self) -> dict:
        return {
            'bridge_ip': self.bridge_ip,
            'bridge_id': self.bridge_id,
            'bridge_username': self.bridge_username
        }

    def set_state(self, data: dict):
        self.bridge_ip = data['bridge_ip']
        self.bridge_id = data['bridge_id']
        self.bridge_username = data['bridge_username']

    def newIP(self, name, val):
        self.bridge_ip = val
        self.log.info("new IP address stored")
        if self.bridge_username is None:
            self.log.warning("no username specified. Cannot get internal id of bridge")
            return
        try:
            self.log.info("getting internal id of the Hue Bridge")
            response = requests.get("http://" + self.bridge_ip + "/api/" + self.bridge_username + "/config")
            config = json.loads(response.text)
            self.bridge_id = config["bridgeid"]
            self.log.info("set bridge id to %s", self.bridge_id)
        except requests.exceptions.ConnectionError as error:
            self.log.warning("could not find bridge with ip %s and username %s", self.bridge_ip, self.bridge_username)

    def newUsername(self, name, val):
        self.bridge_username = val
        self.log.info("new username stored")
        if self.bridge_ip is None:
            self.log.warning("no ip address specified. Cannot get internal id of bridge")
            return
        try:
            self.log.info("getting internal id of the Hue Bridge")
            response = requests.get("http://" + self.bridge_ip + "/api/" + self.bridge_username + "/config")
            config = json.loads(response.text)
            self.bridge_id = config["bridgeid"]
            self.log.info("set bridge id to %s", self.bridge_id)
        except requests.exceptions.ConnectionError as error:
            self.log.warning("could not find bridge with ip %s and username %s", self.bridge_ip, self.bridge_username)


class setLightStateNode(Hue_Bridge):
    """sets the state of a set of lights or groups"""

    title = 'set state'

    def __init__(self, params):
        super().__init__(params)
        Hue_Bridge.log.info("created setLightStateNode")

    init_inputs = [
        # NodeInputBP(dtype=dtypes.Choice(default=[], items=[]), label='target'),
        NodeInputBP(dtype=dtypes.String(default="None"), label='target'),
        NodeInputBP(dtype=dtypes.Boolean(default=True), label='on'),
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 6553)), label='transtition time'),
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 254)), label='brightness'),
        # todo: why is the default not acutally -1 (but the lower bound) for all Integer dtypes?
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 65535)), label='hue'),
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 254)), label='saturation'),
        NodeInputBP(dtype=dtypes.Float(default=-1, bounds=(-1, 1)), label='CIE color x-coord.'),
        NodeInputBP(dtype=dtypes.Float(default=-1, bounds=(-1, 1)), label='CIE color y-coord.'),
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 500)), label='color temp.')
    ]

    def update_event(self, input_called=-1):  # todo was macht 'input_called=-1' ?
        Hue_Bridge.log.info('updating setLightState')
        if self.bridge_username is None:
            Hue_Bridge.log.warning("no username specified => abort")
            return
        if self.bridge_ip is None:
            Hue_Bridge.log.warning("no ip address specified => abort")
            return
        try:

            if self.input(0) == 'None':  # todo adapt to dtypes.Choice
                Hue_Bridge.log.warning("no target specified => abort")
                return
            target = [self.input(0)]

            Hue_Bridge.log.debug("creating payload")
            payload = dict()
            payload["on"] = self.input(1)
            if self.input(2) != -1:
                payload["transitiontime"] = self.input(2) * 10
            if self.input(3) != -1:
                payload["bri"] = self.input(3)
            if self.input(4) != -1:
                payload["hue"] = self.input(4)
            if self.input(5) != -1:
                payload["sat"] = self.input(5)
            if self.input(6) != -1 and self.input(7) != -1:
                payload["xy"] = [self.input(6), self.input(7)]
            if self.input(8):
                payload["ct"] = self.input(8)

            Hue_Bridge.log.info("checking arguments")
            if payload.keys().__contains__('transitiontime') and (payload['transitiontime'] < 0 or payload['transitiontime'] > 6553):  # check the arguments
                Hue_Bridge.log.warning("illegal transitiontime (%s)", self.input(2))
                Hue_Bridge.log.warning("removing illegal transitiontime")
                payload.pop('transitiontime')
            else:
                Hue_Bridge.log.debug("transitiontime ok")
            if payload.keys().__contains__('bri') and (payload['bri'] < 0 or payload['bri'] > 254):
                Hue_Bridge.log.warning("illegal brightness (%s)", payload['bri'])
                Hue_Bridge.log.warning("removing illegal brightness")
                payload.pop('bri')
            else:
                Hue_Bridge.log.debug("brightness ok")
            if payload.keys().__contains__('hue') and (payload['hue'] < 0 or payload['hue'] > 65535):
                Hue_Bridge.log.warning("illegal hue (%s)", payload['hue'])
                Hue_Bridge.log.warning("removing illegal hue")
                payload.pop('hue')
            else:
                Hue_Bridge.log.debug("hue ok")
            if payload.keys().__contains__('sat') and (payload['sat'] < 0 or payload['sat'] > 254):
                Hue_Bridge.log.warning("illegal saturation (%s)", payload['sat'])
                Hue_Bridge.log.warning("removing illegal saturation")
                payload.pop('sat')
            else:
                Hue_Bridge.log.debug("saturation ok")
            if payload.keys().__contains__('xy'):
                for color in payload['xy']:
                    if color < 0 or color > 1:
                        Hue_Bridge.log.warning("illegal CIE coordinate (%s)", color)
                        Hue_Bridge.log.warning("removing illegal CIE coordinates")
                        payload.pop('xy')
                    else:
                        Hue_Bridge.log.debug("CIE coordinate ok")
            if payload.keys().__contains__('ct') and (payload['ct'] < 153 or payload['ct'] > 500):
                Hue_Bridge.log.warning("illegal colortemp (%s)", payload['ct'])
                Hue_Bridge.log.warning("removing illegal colortemp")
                payload.pop('ct')
                # TODO find out if there are any boundaries to this (besides that lights are not actually capable of any temperature)
            else:
                Hue_Bridge.log.debug("color temperature ok")
            Hue_Bridge.log.info("finished checking all arguments")

            Hue_Bridge.log.info("changing state on bridge at %s with username %s", self.bridge_ip, self.bridge_username)
            response = requests.get(
                "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups")  # change state of groups
            response = json.loads(response.text)
            for group in response:
                if target.__contains__(response[group]["name"]):
                    Hue_Bridge.log.info("setting state of %s", response[group]["name"])
                    r = requests.put(
                        "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups/" + group + "/action",
                        data=json.dumps(payload), headers={'content-type': 'application/json'})

            response = requests.get(
                "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights")  # change state of lights
            response = json.loads(response.text)
            for light in response:
                if target.__contains__(response[light]["name"]):  # if the state of the light is to be changed
                    Hue_Bridge.log.info("setting state of %s", response[group]["name"])
                    r = requests.put(
                        "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights/" + light + "/state",
                        data=json.dumps(payload), headers={'content-type': 'application/json'})
            self.log.info("finished setLightState")

        except requests.exceptions.ConnectionError:
            Hue_Bridge.log.info("Connection Error => updating IP address")
            self.updateIPaddress()
            if self.ConnectionErrorCount < self.ConnectionErrorRetry:
                self.ConnectionErrorCount += 1
                Hue_Bridge.log.info("retrying setLightState")
                self.update()
            else:
                Hue_Bridge.log.error("setLightState failed. No (more) retries")
                self.ConnectionErrorCount = 0

        finally:  # otherwise, there might for example be one retry, then a success and the counter stays one
            self.ConnectionErrorCount = 0


class activateSceneNode(Hue_Bridge):
    """activates a scene stored in the bridge for a set of lights or groups"""

    title = 'activate Scene'

    def __init__(self, params):
        super().__init__(params)
        Hue_Bridge.log.info("created activate Scene node")

    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="None"), label='scene'),
        NodeInputBP(dtype=dtypes.String(default="None"), label='groups'),
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 6553)), label='transition time')
    ]

    def update_event(self, input_called=-1):
        Hue_Bridge.log.info("activate scene")
        try:
            if input(0) == "None" or input(0) == "":    # wouldn't cause problems if this check would not be made
                Hue_Bridge.log.warning("no scene specified => abort")
                return
            if type(input(1)) == str:  # make sure groups is a set
                groups = {input(0)}
            else:
                groups = input(0)

            scenes = requests.get(
                "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/scenes")  # get json of all scenes on Hue Bridge
            scenes = json.loads(scenes.text)  # make json a dict

            sceneid = None  # find the internal ID of the scene
            for entry in scenes:
                if scenes[entry]["name"] == input(0):
                    sceneid = entry
                    break
            if sceneid is None:
                Hue_Bridge.log.warning("no such scene (%s)", input(0))
                return

            Hue_Bridge.log.debug("creating payload")
            payload = dict
            payload["scene"] = sceneid
            if self.input(2) != -1:
                payload["transitiontime"] = self.input(2) * 10
            Hue_Bridge.log.info("checking arguments")
            if payload.keys().__contains__('transitiontime') and (
                    payload['transitiontime'] < 0 or payload['transitiontime'] > 6553):  # check the arguments
                Hue_Bridge.log.warning("illegal transitiontime (%s)", self.input(2))
                Hue_Bridge.log.warning("removing illegal transitiontime")
                payload.pop('transitiontime')
            else:
                Hue_Bridge.log.debug("transitiontime ok")

            Hue_Bridge.log.info("getting groups from bridge at %s with username %s", self.bridge_ip, self.bridge_username)
            allGroups = requests.get(
                "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups")  # get json of all groups from Bridge
            allGroups = json.loads(allGroups.text)

            for group in allGroups:  # activate scene for every group listed in groups
                if groups.__contains__(allGroups[group]["name"]):
                    Hue_Bridge.log.info("activating scene for group %s", allGroups[group]["name"])
                    requests.put(
                        "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups/" + group + "/action",
                        data=json.dumps(payload), headers={'content-type': 'application/json'})

        except requests.exceptions.ConnectionError as exception:
            Hue_Bridge.log.info("Connection Error => updating IP address")
            self.updateIPaddress()
            if self.ConnectionErrorCount < self.ConnectionErrorRetry:
                self.ConnectionErrorCount += 1
                Hue_Bridge.log.info("retrying activateScene")
                self.update()
            else:
                self.ConnectionErrorCount = 0
                Hue_Bridge.log.warning("activateScene failed. No (more) retries")
                Hue_Bridge.log.warning(exception)

        finally:  # otherwise, there might be one retry, then a success and the counter stays one
            self.ConnectionErrorCount = 0


class blinkNode(Hue_Bridge):
    """makes lights / groups blink for duration. Not supported by all lights"""

    title = 'blink'

    def __init__(self, params):
        super().__init__(params)
        Hue_Bridge.log.info("created blink node")

    init_inputs = [
        NodeInputBP(dtype=dtypes.String(default="None"), label='target'),
        NodeInputBP(dtype=dtypes.Integer(default=-1), label='duration'),
        NodeInputBP(dtype=dtypes.Integer(default=-1, bounds=(-1, 254)), label='brightness')
    ]

    def update_event(self, input_called=-1):
        print("blink")
        Hue_Bridge.log.info("blink")
        print("checkpoint")
        try:
            Hue_Bridge.log.info("checking and preparing arguments")
            print("checking and preparing arguments")
            if input(0) == "None" or input(0) == "":
                Hue_Bridge.log.warning("no target (group(s) and/or light(s)) specified => abort")
                print("no target (group(s) and/or light(s)) specified => abort")
                return
            if type(input(0)) == str:
                target = {input(0)}
            else:
                target = input(0)

            duration = 0
            payload = dict
            if input(1) < -1:
                Hue_Bridge.log.warning("illegal duration (%s) => abort", input(1))
                print("illegal duration (%s) => abort", input(1))
                return
            elif input(1) != -1:
                duration = input(1)
            if input(2) < -1 or input(2) > 254:
                Hue_Bridge.log.warning("illegal brightness (%s) => removing argument", input(2))
                print("illegal brightness (%s) => removing argument", input(2))
            elif input(2) != -1:
                payload['bri'] = input(2)

            lights = requests.get(
                "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights")  # store the original states of the lights / groups for later restoration of brightness
            lights = json.loads(lights.text)
            groups = requests.get("http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups")
            groups = json.loads(groups.text)

            while duration >= 15:  # repeatedly make lights blink for 15 seconds until less then 15s are left
                payload["alert"] = "lselect"
                Hue_Bridge.log.info("remaining duration: %s", duration)
                print("remaining duration: %s", duration)
                for light in lights:
                    if target.__contains__(lights[light]["name"]):
                        Hue_Bridge.log.info("initiating 15 seconds of blinking for %s", lights[light]["name"])
                        print("initiating 15 seconds of blinking for %s", lights[light]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights/" + light + "/state",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})
                for group in groups:
                    if target.__contains__(groups[group]["name"]):
                        logging.info("initiating 15 seconds of blinking for %s", groups[group]["name"])
                        print("initiating 15 seconds of blinking for %s", groups[group]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups/" + group + "/action",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})
                Hue_Bridge.log.info("sleeping for 15s")
                time.sleep(15)
                duration -= 15

            if duration > 0:
                payload["alert"] = "lselect"
                Hue_Bridge.log.info("remaining duration: %s", duration)
                print("remaining duration: %s", duration)
                for light in lights:  # start a cycle of 15 seconds of blinking
                    if target.__contains__(lights[light]["name"]):
                        Hue_Bridge.log.info("initiating 15 seconds of blinking for %s", lights[light]["name"])
                        print("initiating 15 seconds of blinking for %s", lights[light]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights/" + light + "/state",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})
                for group in groups:
                    if target.__contains__(groups[group]["name"]):
                        Hue_Bridge.log.info("initiating 15 seconds of blinking for %s", groups[group]["name"])
                        print("initiating 15 seconds of blinking for %s", groups[group]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups/" + group + "/action",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})
                Hue_Bridge.log.info("sleeping for %s seconds", duration)
                time.sleep(duration)  # after the remaining duration
                payload["alert"] = "none"
                for light in lights:  # end the blinking
                    if target.__contains__(lights[light]["name"]):
                        Hue_Bridge.log.info("stop blinking for %s", lights[light]["name"])
                        print("stop blinking for %s", lights[light]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights/" + light + "/state",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})
                for group in groups:
                    if target.__contains__(groups[group]["name"]):
                        Hue_Bridge.log.info("stop blinking for %s", group[group]["name"])
                        print("stop blinking for %s", group[group]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups/" + group + "/action",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})

            if duration == 0:
                payload["alert"] = "select"
                for light in lights:  # have the lights flash once
                    if target.__contains__(lights[light]["name"]):
                        Hue_Bridge.log.info("making %s flash once", lights[light]["name"])
                        print("making %s flash once", lights[light]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights/" + light + "/state",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})
                for group in groups:
                    if target.__contains__(groups[group]["name"]):
                        Hue_Bridge.log.info("making %s flash once", groups[group]["name"])
                        print("making %s flash once", groups[group]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups/" + group + "/action",
                            data=json.dumps(payload), headers={'content-type': 'application/json'})

            if payload.keys().__contains__("bri"):
                payload["alert"] = "none"
                for light in lights:  # have the lights flash once
                    if target.__contains__(lights[light]["name"]):
                        Hue_Bridge.log.info("restoring brighness of %s", lights[light]["name"])
                        print("restoring brighness of %s", lights[light]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/lights/" + light + "/state",
                            data=json.dumps({"bri": lights[light]["state"]["bri"]}), headers={'content-type': 'application/json'})
                for group in groups:
                    if target.__contains__(groups[group]["name"]):
                        Hue_Bridge.log.info("restoring brightness of %s", groups[group]["name"])
                        print("restoring brightness of %s", groups[group]["name"])
                        r = requests.put(
                            "http://" + self.bridge_ip + "/api/" + self.bridge_username + "/groups/" + group + "/action",
                            data=json.dumps({"bri": groups[group]["action"]["bri"]}), headers={'content-type': 'application/json'})

        except requests.exceptions.ConnectionError as exception:
            Hue_Bridge.log.info("Connection Error => updating IP address")
            print("Connection Error => updating IP address")
            self.updateIPaddress()
            if self.ConnectionErrorCount < self.ConnectionErrorRetry:
                self.ConnectionErrorCount += 1
                Hue_Bridge.log.info("retrying blinking")
                print("retrying blinking")
                self.update()
            else:
                self.ConnectionErrorCount = 0
                Hue_Bridge.log.warning("blinking failed because of the following Error. No (more) retries")
                print("blinking failed because of the following Error. No (more) retries")
                Hue_Bridge.log.warning(exception)

        finally:  # otherwise, there might be one retry, then a success and the counter stays one
            self.ConnectionErrorCount = 0


class routineOnOfNode(Hue_Bridge):
    """activates or deactivates the specified routine(s) (pass one routine as a String or >= 1 routine(s) as a set"""

    title = 'routine On/Of'

    def __init__(self, params):
        super().__init__(params)
        Hue_Bridge.log.info("created routine On/Of node")

    init_inputs = [
        NodeInputBP(dtype=dtypes.String(), label='routine(s)'),
        NodeInputBP(dtype=dtypes.Boolean(default=True), label='On')
    ]

    def update_event(self, input_called=-1):

        try:
            # check the arguments
            if input(0) == "":
                Hue_Bridge.log.warning("no target (group(s) and/or light(s)) specified => abort")
                return
            routines = input(0)       # todo find out if it makes sense to check for non-iterable types
            if type(routines) == str:
                routines = {routines}

            schedules = requests.get("http://" + self.bridge_ip + "/api/" + self.bridge_username + "/schedules")  # get all schedules from the bridge
            schedules = json.loads(schedules.text)
                # schedules are synonymous to routines (as far as I see), but routines is the name used in the app, which is why I used that in the method name

            payload = dict()
            if input(1):
                payload = {"status": "enabled"}
            else:
                payload = {"status": "disabled"}

            for schedule in schedules:
                if routines.__contains__(schedules[schedule]["name"]):
                    r = requests.put("http://" + self.bridge_ip + "/api/" + self.bridge_username + "/schedules/" + schedule,
                                     data=json.dumps(payload), headers={'content-type': 'application/json'})

        except requests.exceptions.ConnectionError as exception:
            Hue_Bridge.log.info("Connection Error => updating IP address")
            self.updateIPaddress()
            if self.ConnectionErrorCount < self.ConnectionErrorRetry:
                self.ConnectionErrorCount += 1
                Hue_Bridge.log.info("retrying routineOnOf")
                self.update()
            else:
                self.ConnectionErrorCount = 0
                Hue_Bridge.log.warning("routineOnOf failed because of the following Error. No (more) retries")
                Hue_Bridge.log.warning(exception)

        finally:  # otherwise, there might be one retry, then a success and the counter stays one
            self.ConnectionErrorCount = 0


export_nodes(
    setLightStateNode,
    activateSceneNode,
    blinkNode,
    routineOnOfNode
)
