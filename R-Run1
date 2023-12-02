from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()

armleft=Motor(Port.E)
armright=Motor(Port.C)
dt=DriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
armleft.run_angle(1000, -550)
dt.straight(390)
armleft.run_angle(1000, -1100)
dt.straight(20)
armleft.run_angle(1000, 600)
dt.straight(100)
armleft.run_angle(1000, 600)
dt.straight(700)
armleft.run_angle(1000,-600)
#dt.straight(30)
#armleft.run_angle(1000,600)
#dt.straight(150)
dt.turn(-45)
dt.straight(200)
dt.turn(45)
dt.straight(300)
