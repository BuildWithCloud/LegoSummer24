from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Gary:
    LCol = ColorSensor(Port.A)
    RCol = ColorSensor(Port.B)
    LAttach = Motor(Port.C)
    RAttach = Motor(Port.D)
    LDrive = Motor(Port.E, Direction.COUNTERCLOCKWISE, profile=2)
    RDrive = Motor(Port.F, Direction.CLOCKWISE, profile=2)