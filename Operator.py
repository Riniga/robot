import threading
class Operator():
    sensors = []
    controllers = []

    def AddSensor(self, sensor):
        self.sensors.append(sensor)
        self.sensors[-1].operators.append(self)
        
    def AddController(self, controller):
        self.controllers.append(controller)

    def Start(self):
        for sensor in self.sensors:
            sensorLoop = threading.Thread(target=sensor.Start)
            sensorLoop.start()
        for  controller in self.controllers:
            controller.Start()