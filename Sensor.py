import random
class Sensor:
    counter=0
    def __init__(self):
        Sensor.counter += 1
        self.id = Sensor.counter
        self.operators = []

    def Start(self):
        self.on=True
        self.Loop()
        
    def Report(self):
        for operator in self.operators:
                operator.Report(self)