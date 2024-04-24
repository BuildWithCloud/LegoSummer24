from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Gary:
    #Hub
    hub = PrimeHub()
    hub.display.orientation(Side.LEFT)

    #Sensors
    LCol = ColorSensor(Port.A)
    RCol = ColorSensor(Port.E)

    #Motors
    LAttach = Motor(Port.B)
    RAttach = Motor(Port.D)
    LDrive = Motor(Port.C, Direction.COUNTERCLOCKWISE, profile=2)
    RDrive = Motor(Port.F, Direction.CLOCKWISE, profile=2)

    #Drive
    Drive = DriveBase(LDrive, RDrive, diameter, axle track )
    #TODO, add the wheelbase and diameter 
    Drive.use_gyro(True)
