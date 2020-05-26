from clientwrapper import ClientWrapper


class Thing:
    dev_id = "" # Dispositivos > Dispositivo > Copiar
    wrap_instance = None
    events_list = []

    def __init__(self, dev_id:str):
        self.dev_id = dev_id

    def set_wrapper(self, wrap_instance:ClientWrapper):
        self.wrap_instance = wrap_instance

    def get_dev_id(self):
        return self.dev_id

    def subscribe(self):
        for event in self.events_list:
            self.wrap_instance.inscribe(self, event[0], event[1])

    def subscribe_event(self, event_name:str, func):
        self.events_list.append([event_name, func])
        


class Light(Thing):
    # onPowerState = None
    # onAdjustBrightness = None
    # onSetColor = None
    # onSetColorTemperature = None
    # onIncreaseColorTemperature = None
    # onDecreaseColorTemperature = None

    def __init__(self,dev_id:str):
        super().__init__(dev_id)

    def setOnPowerState(self,fun):
        self.subscribe_event("onPowerState", fun)
        # self.onPowerState = fun

    def setOnAdjustBrightness(self,fun):
        self.subscribe_event("onAdjustBrightness", fun)
        # self.onAdjustBrightness = fun

    def setOnSetColor(self,fun):
        self.subscribe_event("onSetColor", fun)
        # self.onSetColor = fun
    
    def setOnSetColorTemperature(self,fun):
        self.subscribe_event("onSetColorTemperature", fun)
        # self.onSetColorTemperature = fun

    def setOnIncreaseColorTemperature(self,fun):
        self.subscribe_event("onIncreaseColorTemperature", fun)
        # self.onIncreaseColorTemperature = fun
        
    def setOnDecreaseColorTemperature(self,fun):
        self.subscribe_event("onDecreaseColorTemperature", fun)
        # self.onDecreaseColorTemperature = fun


class DimmerSwitch(Thing):
    # onPowerState = None
    # onAdjustBrightness = None
    
    def __init__(self,dev_id:str):
        super().__init__(dev_id)

    def setPowerLevel(self,fun):
        self.subscribe_event("setPowerLevel", fun)

    def setPowerState(self,fun):
        self.subscribe_event("powerState", fun)

    