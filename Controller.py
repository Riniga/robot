class Controller():
    counter=0
    def __init__(self):
        Controller.counter += 1
        self.id = Controller.counter

    def Start(self):
        self.on=True