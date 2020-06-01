# Python Object Oriented for SinricPro
**A virtual device library integrable with Alexa for Python coding.**

## Code implements
### Imports
```python
from classes.clientwrapper import ClientWrapper
from classes.things import ... #[used classes]
```

### In practice
```python

def plug1_setPowerLevel(arg):
    print("powerPlug1 setPowerLevel=",arg)
    return True,arg[0]
    
powerPlug1 = Switch(thing_1)
powerPlug1.setPowerState(plug1_powerState)
    
devices = [powerPlug1] # your instanced devices class
wrap = ClientWrapper(devices, appKey, secretKey)
wrap.start()
```

## Implemented classes:

### Switch
| Function | Attributes |
| --- | --- |
| setPowerState | `str` arg[0]: 'On' or 'Off' |

### DimmerSwitch
| Function | Attributes |
| --- | --- |
| setPowerState | `str` arg[0]: 'On' or 'Off' |
| setPowerLevel | `int` arg[0]: 1..100 |


### Light
| Function | Attributes |
| --- | --- |
| setPowerState | `str` arg[0]: 'On' or 'Off' |
| setOnSetBrightness | `int` arg[0]: 1..100 |
| setOnSetColor | `int` arg[0]: 0-255; `int` arg[1]: 0-255; `int` arg[2]: 0-255  |
| setOnSetColorTemperature | `int` arg[0]: temperature in K |
