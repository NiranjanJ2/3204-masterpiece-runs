from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, hub_menu
import run1
import run2
import run3
import run4
hub = PrimeHub()
runs=hub_menu(1,2,3,4)
if runs==1:
    run1()
if runs==2:
    run2()
if runs==3:
    run3()
if runs==4:
    run4()
