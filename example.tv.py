from classes.clientwrapper import ClientWrapper
from classes.things import TV

from credentials import appKey,secretKey
from credentials import thing_1


'''
Implemented functions for TV
'''

def tv_powerState(arg):
    print("tv_powerState=",arg)
    return True,arg[0]

def tv_setVolume(arg):
    print("tv_setVolume=",arg)
    return True, arg[0]
    
def tv_adjustVolume(arg):
    print("tv_adjustVolume=",arg)
    return True, arg[0]

def tv_setMute(arg):
    print("tv_setMute=",arg)
    return True, arg[0]

def tv_mediaControl(arg):
    print("tv_mediaControl=",arg)
    return True, arg[0]

def tv_selectInput(arg):
    print("tv_selectInput=",arg)
    return True, arg[0]

def tv_changeChannel(arg):
    print("tv_changeChannel=",arg)
    return True, arg[0]

def tv_skipChannels(arg):
    print("tv_skipChannels=",arg)
    return True, arg[0]


if __name__ == '__main__':

    tv = TV(thing_1)
    tv.powerState(tv_powerState)
    tv.setVolume(tv_setVolume)
    tv.adjustVolume(tv_adjustVolume)
    tv.setMute(tv_setMute)
    tv.mediaControl(tv_mediaControl)
    tv.selectInput(tv_selectInput)
    tv.changeChannel(tv_changeChannel)
    tv.skipChannels(tv_skipChannels)


    devices = [tv]

    wrap = ClientWrapper(devices, appKey, secretKey)
    
    # Do some stuff ...

    wrap.start()