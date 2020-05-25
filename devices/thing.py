import clientwrapper
class Thing:
    dev_id = None # Dispositivos > Dispositivo > Copiar
    wrap_instance = None

    def __init__(self,dev_id):
        self.dev_id = dev_id

    def set_wrapper(self,wrap_instance):
        self.wrap_instance = wrap_instance

    def setcallback(self, event_name, params):
        pass

    def get_dev_id(self):
        return self.dev_id

    def subscribe_event(self, event_name, func):
        self.wrap_instance.inscribe(self, event_name, func)


        