from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch
#arm - up position from 0 is 330
#arm - placing position from 0 is 100-135
hub = PrimeHub()
#max degree for forklift is 380
dt=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
dt.settings(925,925)
spin=Motor(Port.E)
arm=Motor(Port.C)
dt.turn(-55)
dt.straight(520)
wait(200)
dt.straight(50)
arm.run_angle(200,260,wait=False)
spin.run_time(-10000,3500)
dt.straight(-100)
arm.run_angle(1200,-260)
dt.straight(-480)#arm.run_angle(1200, 260)
