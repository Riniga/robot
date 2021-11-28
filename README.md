# Robotics Environment 
This framework enables a structured environment for robotics development in python. 

## Sensors
A sensor inherrits Sensor and implements the Loop function. This is executed in a separat thread and should call super().Report() to report to all controllers.

## Controllers
A controller inherits Controller and implments the Action function. This is called from the operator with sensor reference

## Operators
An operator contains robotic logic, inherrits Operator and implments Report, this is called from sensors anytime they need to report an update. operators could/should call controllers with sensor data.

## Robot
The robot class contains the structure.

## Main
Startup file, startup command:
python Main.py