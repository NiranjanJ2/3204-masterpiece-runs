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
dt.straight(215)
dt.settings(turn_rate=30)
dt.curve(-42,-43)

dt.straight(-420)
arm.run_angle(700,-180)
arm.run_angle(700,180)
dt.settings(turn_rate=150)
dt.turn(45)
dt.straight(310)
dt.turn(-45)
dt.straight(390)
camarm.run_angle(750,1000)
dt.straight(-250)
dt.straight(150)
dt.turn(-35)
camarm.run_angle(-750,100)
dt.straight(-150)
dt.turn(35)
dt.straight(-500)
