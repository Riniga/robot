from gpiozero import LED
from time import sleep
from Controller import Controller

class LedController(Controller):
    def __init__(self, gpio_pin, *args, **kwargs):
        super(LedController).__init__(*args, **kwargs)
        self.led   = LED(gpio_pin)

    def Action(self, sensor):
        if (sensor.id==1):
            self.led.on()
        else:
            self.led.off()