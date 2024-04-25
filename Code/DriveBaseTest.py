from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop, Axis
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import Setup

def DriveBaseTest():
    Setup.Bary.Drive.settings(straight_speed=400, straight_acceleration=200, turn_rate = 90, turn_acceleration = 90)
  #  Setup.Bary.Drive.straight(distance=1000, wait = True)
    Setup.Bary.Drive.turn(angle=0, wait = True)
    #Setup.Bary.Drive.curve()
    
    
