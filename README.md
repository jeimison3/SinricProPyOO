# Alexa reactive interface Python3-OO (w/ SinricPro)
**A virtual device library integrable with Alexa for Python coding.**

## Dependences:
[sinric-pro python-sdk](https://github.com/sinricpro/python-sdk): `pip install sinricpro --user`
## Code implements
### Imports
```python
from classes.clientwrapper import ClientWrapper
from classes.things import Switch # All used classes
```

### In practice
```python

def plug1_powerState(arg):
    print("powerPlug1 powerState=",arg)
    return True,arg[0]
    
powerPlug1 = Switch(thing_1)
powerPlug1.powerState(plug1_powerState)
    
devices = [powerPlug1] # your device objects
wrap = ClientWrapper(devices, appKey, secretKey)
wrap.start()
```

## Implemented classes:

### Switch
| Function | Attributes |
| --- | --- |
| powerState | `str` arg[0]: 'On' or 'Off' |

### DimmerSwitch
| Function | Attributes |
| --- | --- |
| powerState | `str` arg[0]: 'On' or 'Off' |
| powerLevel | `int` arg[0]: 1..100 |

### Light
| Function | Attributes |
| --- | --- |
| setPowerState | `str` arg[0]: 'On' or 'Off' |
| setOnSetBrightness | `int` arg[0]: 1..100 |
| setOnSetColor | `int` arg[0]: 0-255<br>`int` arg[1]: 0-255<br>`int` arg[2]: 0-255  |
| setOnSetColorTemperature | `int` arg[0]: temperature in K |

### TV
| Function | Attributes |
| --- | --- |
| setPowerState | `str` arg[0]: 'On' or 'Off' |
| setVolume | `int` arg[0]: 0..100 |
| adjustVolume | `int` arg[0]: -100..100 |
| setMute | `bool` arg[0]: True/False |
| mediaControl | `str` arg[0]: 'Play','Pause','FastForward','Rewind','Next','Previous' |
| selectInput | `str` arg[0]: 'HDMI', ... |
| changeChannel | `str` arg[0]: channelName |
| skipChannels | `int` arg[0]: N |