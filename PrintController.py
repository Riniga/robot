from Controller import Controller
class PrintController(Controller):
    def Action(self, sensor):
        print("Controller triggered by sensor: "+ str(sensor.id))        