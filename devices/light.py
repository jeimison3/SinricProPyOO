import thing
class Light(Thing):
    # https://github.com/sinricpro/python-examples/blob/master/pro_light_example/app.py
    onPowerState = None
    onAdjustBrightness = None
    onSetColor = None
    onSetColorTemperature = None
    onIncreaseColorTemperature = None
    onDecreaseColorTemperature = None

    def __init__(self,dev_id):
        super().__init__(self,dev_id)

    def setOnPowerState(self,fun):
        self.onPowerState = fun

    def setOnAdjustBrightness(self,fun):
        self.onAdjustBrightness = fun

    def setOnSetColor(self,fun):
        self.onSetColor = fun
    
    def setOnSetColorTemperature(self,fun):
        self.onSetColorTemperature = fun

    def setOnIncreaseColorTemperature(self,fun):
        self.onIncreaseColorTemperature = fun
        
    def setOnDecreaseColorTemperature(self,fun):
        self.onDecreaseColorTemperature = fun

     

