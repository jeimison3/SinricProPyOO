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

def light1_setBrightness(arg):
    print("light1 setBrightness=",arg)
    return True, arg[0]

def light1_setColor(arg):
    print("light1 onSetColor=",arg)
    return True, arg[0]

def light1_setColorTemperature(arg):
    print("light1 setColorTemperature=",arg)
    return True, arg[0]


if __name__ == '__main__':
    powerPlug1 = DimmerSwitch(thing_1)
    powerPlug1.setPowerLevel(plug1_setPowerLevel)
    powerPlug1.setPowerState(plug1_powerState)

    light1 = Light(thing_2)
    light1.powerState(light1_powerState)
    light1.setColor(light1_setColor)
    light1.setColorTemperature(light1_setColorTemperature)
    light1.setBrightness(light1_setBrightness)


    devices = [powerPlug1, light1]

    wrap = ClientWrapper(devices, appKey, secretKey)
    
    # Do some stuff ...

    wrap.start()