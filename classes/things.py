
class Thing:
    dev_id = "" # Dispositivos > Dispositivo > Copiar
    wrap_instance = None
    

    def __init__(self, dev_id:str):
        self.dev_id = dev_id
        self.events_list = []

    def get_dev_id(self):
        return self.dev_id

    def subscribe(self, wrapp): # as ClientWrapper
        for event in self.events_list:
            wrapp.inscribe(self, event[0], event[1])

    def enqueue_event(self, event_name:str, func):
        #print(self, " -> ", event_name, ' -> ', func)
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

    def setOnSetBrightness(self,fun):
        self.enqueue_event("setBrightness", fun)
        # self.onAdjustBrightness = fun

    def setOnSetColor(self,fun):
        self.enqueue_event("setColor", fun)
        # self.onSetColor = fun
    
    def setOnSetColorTemperature(self,fun):
        self.enqueue_event("setColorTemperature", fun)
        # self.onSetColorTemperature = fun

    def setOnIncreaseColorTemperature(self,fun):
        self.enqueue_event("increaseColorTemperature", fun)
        # self.onIncreaseColorTemperature = fun
        
    def setOnDecreaseColorTemperature(self,fun):
        self.enqueue_event("decreaseColorTemperature", fun)
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


class TV(Switch):
    ''' Dimmer switch with power level settings.\n
    dev_id -> deviceId
    '''

    def setVolume(self,fun):
        '''
        arg[0]: int 0-100
        '''
        self.enqueue_event("setVolume", fun)

    def adjustVolume(self,fun):
        '''
        arg[0]: int -100 to 100\n
        arg[1]: bool default(false)
        '''
        self.enqueue_event("adjustVolume", fun)
    
    def setMute(self,fun):
        '''
        arg[0]: bool
        '''
        self.enqueue_event("setMute", fun)
    
    def mediaControl(self,fun):
        '''
        arg[0]: str (Play/Pause/FastForward/Rewind/Previous/Next)
        '''
        self.enqueue_event("mediaControl", fun)

    def selectInput(self,fun):
        '''
        arg[0]: str (HDMI/...)
        '''
        self.enqueue_event("selectInput", fun)

    def changeChannel(self,fun):
        '''
        arg[0]: str channel_name
        '''
        self.enqueue_event("changeChannel", fun)

    def skipChannels(self,fun):
        '''
        arg[0]: int channelCount
        '''
        self.enqueue_event("skipChannels", fun)

        


    