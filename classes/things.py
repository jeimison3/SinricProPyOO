from classes.clientwrapper import ClientWrapper


class Thing:
    dev_id = "" # Dispositivos > Dispositivo > Copiar
    wrap_instance = None
    events_list = []

    def __init__(self, dev_id:str):
        self.dev_id = dev_id

    def get_dev_id(self):
        return self.dev_id

    def subscribe(self, wrapp:ClientWrapper):
        for event in self.events_list:
            wrapp.inscribe(self, event[0], event[1])

    def enqueue_event(self, event_name:str, func):
        self.events_list.append([event_name, func])
        

class Switch(Thing):
    ''' Switch on/off state.\n
    dev_id -> deviceId
    '''
    def setPowerState(self,fun):
        '''
        arg[0]: str 'On'-'Off'
        '''
        self.enqueue_event("powerState", fun)

class Light(Switch):
    ''' Light with colors and temperature settings.\n
    dev_id -> deviceId
    '''

    def setOnAdjustBrightness(self,fun):
        self.enqueue_event("onAdjustBrightness", fun)
        # self.onAdjustBrightness = fun

    def setOnSetColor(self,fun):
        self.enqueue_event("onSetColor", fun)
        # self.onSetColor = fun
    
    def setOnSetColorTemperature(self,fun):
        self.enqueue_event("onSetColorTemperature", fun)
        # self.onSetColorTemperature = fun

    def setOnIncreaseColorTemperature(self,fun):
        self.enqueue_event("onIncreaseColorTemperature", fun)
        # self.onIncreaseColorTemperature = fun
        
    def setOnDecreaseColorTemperature(self,fun):
        self.enqueue_event("onDecreaseColorTemperature", fun)
        # self.onDecreaseColorTemperature = fun


class DimmerSwitch(Switch):
    ''' Dimmer switch with power level settings.\n
    dev_id -> deviceId
    '''

    def setPowerLevel(self,fun):
        '''
        arg[0]: int 1-100
        '''
        self.enqueue_event("setPowerLevel", fun)

    