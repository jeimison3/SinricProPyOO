from clientwrapper import ClientWrapper
from devices.thing import Thing

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
    th1 = Thing(thing_1)
    wrap = ClientWrapper([th1], appKey, secretKey)

    th1.subscribe_event("setPowerLevel", light1_setPowerLevel)
    th1.subscribe_event("powerState", light1_powerState)
    

    wrap.setup()