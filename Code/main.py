from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task
import Setup
import DriveBaseTest
import LineFunctions

def main():
    #DriveBaseTest.DriveBaseTest()
    Setup.Bary.Drive.turn(-LineFunctions.AngleToLine())

main()
wait(100000)
