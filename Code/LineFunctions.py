from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#import math
import Setup
#def LineSquare():

def AngleToLine():
    Setup.Bary.Drive.drive(100,0)
    while Setup.Bary.LCol.reflection() > 25 and Setup.Bary.RCol.reflection() > 25:
        pass
    dIstance = Setup.Bary.Drive.distance()
    if Setup.Bary.LCol.reflection() < 25:
        Setup.Bary.hub.display.pixel(1, 1, 100)
        while Setup.Bary.RCol.reflection() > 25:
            pass
        move = Setup.Bary.Drive.distance() - distance
    else:
        pass
    Setup.Bary.Drive.stop()
    wait(1000)
    Setup.Bary.Drive.straight(distance=dIstance)
    return (math.atan(dIstance/Setup.Bary.ColDistance))
