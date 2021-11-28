from Operator import Operator 
class BasicOperator(Operator):

    def Report(self, sensor):
        for controller in self.controllers:
            controller.Action(sensor)