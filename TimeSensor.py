import time
from Sensor import Sensor

class TimeSensor(Sensor):
    
    def __init__(self, interval, *args, **kwargs):
        super(TimeSensor, self).__init__(*args, **kwargs)
        self.interval = interval
    
    def Loop(self):
        while self.on:
            time.sleep(self.interval)
            super().Report()
            