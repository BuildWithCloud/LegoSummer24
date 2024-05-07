from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import umath
import Setup
#def LineSquare():

def AngleToLine():
    Setup.Bary.Drive.drive(100,0)
    while Setup.Bary.LCol.reflection() > Setup.Bary.ColTolerance and Setup.Bary.RCol.reflection() > Setup.Bary.ColTolerance:
        pass
    dIstance = Setup.Bary.Drive.distance()
    if Setup.Bary.LCol.reflection() < Setup.Bary.ColTolerance:
        Setup.Bary.hub.display.pixel(1, 1, 100)
        while Setup.Bary.RCol.reflection() > Setup.Bary.ColTolerance:
            pass
        move = Setup.Bary.Drive.distance() - dIstance
    else:
        Setup.Bary.hub.display.pixel(1, 1, 100)
        while Setup.Bary.LCol.reflection() > Setup.Bary.ColTolerance:
            pass
        move = -Setup.Bary.Drive.distance() + dIstance
    Setup.Bary.Drive.stop()
    
    return umath.degrees(umath.atan(move/Setup.Bary.ColDistance))
