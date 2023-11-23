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
dt.settings(750,300)
spin=Motor(Port.E)
dt.straight(50)
dt.turn(-55)
dt.straight(480)
spin.run_time(-10000,4000)
dt.straight(-480)
dt.straight(-50)
dt.turn()

