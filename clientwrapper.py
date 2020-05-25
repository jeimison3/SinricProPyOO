from sinric import SinricPro
from sinric import SinricProUdp

class ClientWrapper:

    events = {}
    deviceIdArr = []
    appKey = ""
    secretKey = ""

    def __init__(self, things, appKey, secretKey):
        for thing in things:
            thing.set_wrapper(self)
            self.deviceIdArr.append(thing.get_dev_id())
        self.appKey = appKey
        self.secretKey = secretKey

    def setup(self):
        client = SinricPro(self.appKey, self.deviceIdArr, self.getCallbacks(), event_callbacks=self.eventsCallbacks, enable_log=False,restore_states=True,secretKey=self.secretKey)
        udp_client = SinricProUdp(self.getCallbacks(), self.deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
        client.handle_all(udp_client)

    def run_match_dev_id(self,dev_id,lista_thing_func,arg):
        #print("dev:",dev_id," | arg:",arg," | lista: ",lista_thing_func)
        for item in lista_thing_func:
            if item['thing'].get_dev_id() == dev_id:
                return item['func'](arg)
        return False


    def getCallbacks(self):
        callbs = {}
        if len(self.events) > 0:
            for key, receivers in self.events.items():
                #print("RECV=",receivers)
                callbs[key] = lambda dev_id, *arg,recv=receivers,: self.run_match_dev_id(dev_id,recv,locals()['arg'])
        
        return callbs
    
    def inscribe(self, thing, event_name, func):
        if not (event_name in self.events):
            self.events[event_name] = list()
        self.events[event_name].append({'thing':thing,'func':func, 'event':event_name})



    def Events():
        while True:
            # client.event_handler.raiseEvent(device1, 'setPowerState',data={'state': 'On'})
            # client.event_handler.raiseEvent(device1, 'setPowerLevel',data={'powerLevel': '95%'})
            #sleep(2)
            pass

    eventsCallbacks={
        "Events": Events
    }
        
