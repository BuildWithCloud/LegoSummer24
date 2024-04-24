from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import Setup

def DriveBaseTest():
    Setup.Bary.Drive.settings(200, 100)
    Setup.Bary.Drive.straight(1000, wait = True)
    while Setup.Bary.hub.buttons.pressed() == None:
        pass
    Setup.Bary.Drive.turn(360, wait = True)