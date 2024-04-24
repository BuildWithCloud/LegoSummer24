from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
import Setup

#straight drive
drive_base.straight(500)
#number in mm

#turn drive
drive_base.turn(180)
#number in degrees negative for ant-clockwise

#straight speed
straight_speed(num)
#number in mm/s 40% of max speed (based on wheel diameter and axle track) is default for nothing

#turn rate
turn_rate(num)
#number on deg/s

#Gyro Drive
#drive_base.use_gyro(True)
#put before first movement

#Straight Acceleration Drive
straight_acceleration(num)
#number in mm/s² use normal drive after this to apply acceleration.

#Turn Acceleration Drive
turn_acceleration(num)
#number on deg/s² use normal turn after this to apply acceleration.

