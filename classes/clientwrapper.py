from sinric import SinricPro
from sinric import SinricProUdp

class ClientWrapper:
    """ ClientWrapper for comunicate classes and things.\n
    things -> [DimmerSwitch, Switch...] \n
    appKey -> d89f1***-****-****-****-************ \n
    secretKey -> 44d1d31-1c19-****-****-9bc96c34b5bb-d19f42dd-****-****-****-************"""
    
    logger = None
    events = {}
    deviceIdArr = []
    appKey = ""
    secretKey = ""

    def __init__(self, things : list, appKey : str, secretKey : str):
        for thing in things:
            thing.subscribe(self)
            self.deviceIdArr.append(thing.get_dev_id())
        self.appKey = appKey
        self.secretKey = secretKey
        
    
    def start(self):
        ''' Start clients and setup connection '''
        # Request callbacks
        callbs = {}
        if len(self.events) > 0:
            for key, receivers in self.events.items():
                callbs[key] = lambda dev_id, *arg, recv=receivers: self.run_match_dev_id(dev_id,recv,locals()['arg'])
        
        # Instantiate client (setup connections)
        client = SinricPro(self.appKey, self.deviceIdArr, callbs, event_callbacks=self.eventsCallbacks, enable_log=False,restore_states=True,secretKey=self.secretKey)
        udp_client = SinricProUdp(callbs, self.deviceIdArr,enable_trace=False)  # Set it to True to start logging request Offline Request/Response
        client.handle_all(udp_client)
        self.logger = client.logger
        self.logger.success("SinricProOO started!")

    def run_match_dev_id(self,dev_id,lista_thing_func,arg):
        #print("dev:",dev_id," | arg:",arg," | lista: ",lista_thing_func)
        for item in lista_thing_func:
            if item['thing'].get_dev_id() == dev_id:
                return item['func'](arg)
        return False
    
    def inscribe(self, thing, event_name, func):
        if not (event_name in self.events):
            self.events[event_name] = list()
        self.events[event_name].append({'thing':thing,'func':func})



    def Events():
        while True:
            # client.event_handler.raiseEvent(device1, 'setPowerState',data={'state': 'On'})
            # client.event_handler.raiseEvent(device1, 'setPowerLevel',data={'powerLevel': '95%'})
            #sleep(2)
            pass

    eventsCallbacks={
        "Events": Events
    }
        
