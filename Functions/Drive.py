from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import Setup

#Basic Drive
drive_base.straight(500)
#number in mm
#Drive With Turn
drive_base.turn(180)
#number in degrees
#Gyro Drive
drive_base.use_gyro(True)
#put before first movement
#Acceleration Drive
