from classes.clientwrapper import ClientWrapper
from classes.things import Light, DimmerSwitch

from credentials import appKey,secretKey
from credentials import thing_1, thing_2


'''
Implemented functions for bulb dimming
'''

def plug1_setPowerLevel(arg):
    print("powerPlug1 setPowerLevel=",arg)
    return True,arg[0]

def plug1_powerState(arg):
    print("powerPlug1 powerState=",arg)
    return True,arg[0]


'''
Implemented functions for light
'''
def light1_powerState(arg):
    print("light1 powerState=",arg)
    return True,arg[0]

def light1_onSetBrightness(arg):
    print("light1 setBrightness=",arg)
    return True, arg[0]

def light1_onSetColor(arg):
    print("light1 onSetColor=",arg)
    return True, arg[0]

def light1_onSetColorTemperature(arg):
    print("light1 setColorTemperature=",arg)
    return True, arg[0]


if __name__ == '__main__':
    powerPlug1 = DimmerSwitch(thing_1)
    powerPlug1.setPowerLevel(plug1_setPowerLevel)
    powerPlug1.setPowerState(plug1_powerState)

    light1 = Light(thing_2)
    light1.setPowerState(light1_powerState)
    light1.setOnSetColor(light1_onSetColor)
    light1.setOnSetColorTemperature(light1_onSetColorTemperature)
    light1.setOnSetBrightness(light1_onSetBrightness)


    devices = [powerPlug1, light1]

    wrap = ClientWrapper(devices, appKey, secretKey)
    
    # Do some stuff ...

    wrap.start()