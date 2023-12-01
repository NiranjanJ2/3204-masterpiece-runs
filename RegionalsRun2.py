# Insert run 2 here
# Insert run 2 here

from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase, DriveBase
from pybricks.tools import wait, StopWatch

dt=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
arm=Motor(Port.E)
camarm=Motor(Port.C, Direction.COUNTERCLOCKWISE)
dt.use_gyro(True)
dt.straight(100)
dt.turn(42)
dt.straight(350)
dt.straight(-200)
dt.turn(6)
dt.straight(205)
dt.settings(turn_rate=30)
dt.curve(-42,-43)

dt.straight(-420)
dt.turn(15)
arm.run_angle(700,-180, wait=False)
wait(500)
dt.turn(20)
# arm.run_angle(800, -15)
dt.turn(10)
arm.run_angle(700,220)
dt.settings(turn_rate=150)
dt.straight(310)
dt.turn(-47)
dt.straight(350)
dt.turn(5)
camarm.run_angle(750,1000)
dt.straight(-250)
dt.straight(150)
dt.turn(-35)
camarm.run_angle(-750,100)
dt.straight(-150)
dt.turn(35)
dt.straight(-500)
