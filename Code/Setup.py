from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class Bary:
    #Hub
    hub = PrimeHub(top_side=Axis.Z, front_side=-Axis.Y)
    hub.display.orientation(Side.LEFT)
    hub.system.set_stop_button(Button.BLUETOOTH)

    #Sensors
    LCol = ColorSensor(Port.A)
    RCol = ColorSensor(Port.B)

    #Motors
    LAttach = Motor(Port.C)
    RAttach = Motor(Port.D)
    LDrive = Motor(Port.E, Direction.COUNTERCLOCKWISE, profile=2)
    RDrive = Motor(Port.F, Direction.CLOCKWISE, profile=2)

    #Drive
    Drive = DriveBase(LDrive, RDrive, wheel_diameter = 55.05, axle_track = 97.5)
    Drive.use_gyro(True)
    Drive.heading_control.pid(kp=500000, kd=1000)
    #TODO, add the wheelbase and diameter 
