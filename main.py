from clientwrapper import ClientWrapper
from devices.things import Thing, Light, DimmerSwitch

from credentials import appKey,secretKey
from credentials import thing_1


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

    light1 = DimmerSwitch(thing_1)
    wrap = ClientWrapper([light1], appKey, secretKey)

    light1.setPowerLevel(light1_setPowerLevel)
    light1.setPowerState(light1_powerState)
    
    wrap.setup()