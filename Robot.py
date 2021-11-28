from BasicOperator import BasicOperator
from TimeSensor import TimeSensor
from PrintController import PrintController
from LedController import LedController

class Robot:
    operators=[]

    def __init__(self):
        self.name ='R1'
        operator = BasicOperator()

        operator.AddSensor(TimeSensor(5))
        operator.AddSensor(TimeSensor(3))

        operator.AddController(PrintController())
        operator.AddController(LedController(18))

        self.operators.append(operator)

    def Start(self):
        for operator in self.operators:
            operator.Start()