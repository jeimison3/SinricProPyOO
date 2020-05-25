from clientwrapper import ClientWrapper
from devices.thing import Thing

from credentials import appKey,secretKey
from credentials import thing_1


def onSetBrightness(did, state):
    # Alexa, ligar Device a VALUE%
    print(did, 'BrightnessLevel : ', state)
    return True, state

def onAdjustBrightness(did, state):
    # Alexa increase/decrease device brightness by 44
    print(did, 'AdjustBrightnessLevel : ', state)
    return True, state
    
def onSetPowerLevel(did, powerLevel):
    # Alexa set power level device by 44
    print(did, 'SetPowerLevel : ', powerLevel)
    return True,50



callbacks = {
'powerState': onPowerState,
'setBrightness': onSetBrightness,
'adjustBrightness': onAdjustBrightness,
'setPowerLevel' : onSetPowerLevel,
}

''' 
Implemented functions for dimming light
'''

def light1_setPowerLevel(arg):
    print("setPowerLevel=",arg)
    return True,arg[0]

def light1_powerState(arg):
    print("powerState=",arg)
    return True,arg[0]


if __name__ == '__main__':
    th1 = Thing(thing_1)
    wrap = ClientWrapper([th1], appKey, secretKey)

    th1.subscribe_event("setPowerLevel", light1_setPowerLevel)
    th1.subscribe_event("powerState", light1_powerState)
    

    wrap.setup()