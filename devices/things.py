import clientwrapper


class Thing:
    dev_id = None # Dispositivos > Dispositivo > Copiar
    wrap_instance = None

    def __init__(self,dev_id):
        self.dev_id = dev_id

    def set_wrapper(self,wrap_instance):
        self.wrap_instance = wrap_instance

    def get_dev_id(self):
        return self.dev_id

    def subscribe_event(self, event_name, func):
        self.wrap_instance.inscribe(self, event_name, func)


class Light(Thing):
    # onPowerState = None
    # onAdjustBrightness = None
    # onSetColor = None
    # onSetColorTemperature = None
    # onIncreaseColorTemperature = None
    # onDecreaseColorTemperature = None

    def __init__(self,dev_id):
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
    
    def __init__(self,dev_id):
        super().__init__(dev_id)

    def setPowerLevel(self,fun):
        self.subscribe_event("setPowerLevel", fun)

    def setPowerState(self,fun):
        self.subscribe_event("powerState", fun)

    