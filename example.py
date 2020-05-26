from classes.clientwrapper import ClientWrapper
from classes.things import Thing, Light, DimmerSwitch

from credentials import appKey,secretKey
from credentials import thing_1


'''
Implemented functions for dimming light
'''

def plug1_setPowerLevel(arg):
    print("setPowerLevel=",arg)
    return True,arg[0]

def plug1_powerState(arg):
    print("powerState=",arg)
    return True,arg[0]


if __name__ == '__main__':
    powerPlug1 = DimmerSwitch(thing_1)
    powerPlug1.setPowerLevel(plug1_setPowerLevel)
    powerPlug1.setPowerState(plug1_powerState)

    devices = [powerPlug1]

    wrap = ClientWrapper(devices, appKey, secretKey)
    
    # Do some stuff ...

    wrap.start()