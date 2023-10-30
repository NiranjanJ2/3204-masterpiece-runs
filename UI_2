from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
def run1():
    dt=GyroDriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
    print("We are a team! -Joseph Yoon")
    dt.straight(540, then=Stop.COAST) #goes forward to push in printer
    dt.straight(-92) #backs out to turn
    dt.turn(45.7) # turns to go to stage
    dt.straight(243) #goes to stage
    dt.turn(44) # turns to position to stage
    dt.straight(255, then=Stop.COAST) #pushes in stage
    dt.straight(-240) #backs out
    dt.turn(-95)# turns to go to aug
    dt.straight(160)
    dt.turn(-42.5)
    #dt.turn(-45)
    dt.straight(735)
    dt.curve(-40, -90)
    dt.straight(280)
    dt.straight(-200)
    dt.turn(-50)
    dt.straight(150)
    dt.turn(-35)
    dt.straight(150)
    dt.turn(52.5)
    dt.straight(230)
    dt.straight(-200)
    dt.straight(230)
    dt.straight(-180)    
    dt.turn(-85)
    dt.straight(120)
    dt.turn(-25)
    dt.straight(450)
    dt.reset()
def run2():
    dt=GyroDriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
    #example_motor.dc(-70)
    dt.straight(525)
    dt.straight(-250)
    dt.turn(7)
    dt.straight(300)
    wait(500)
    dt.straight(-300)
    dt.turn(38)
    dt.straight(1200)
    dt.turn(30)
    dt.straight(200)
    dt.reset()
def run3():
    dt=GyroDriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
    dt.straight(230)
    dt.turn(45)
    dt.turn(-45)
    dt.straight(-230)
    dt.reset()
def run4():
    dt=GyroDriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
    dt.settings(750,300,45)
    arm=Motor(Port.E, Direction.CLOCKWISE,gears=[12,28])
    dt.straight(320)
    arm.run_angle(1000,135)
    dt.straight(320)
    arm.run_angle(-1000,130)
    dt.turn(-12)
    dt.straight(-650)
    dt.reset()
def run5():
    dt=GyroDriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
    spinnythingy=Motor(Port.C,Direction.CLOCKWISE)
    dt.straight(412)
    spinnythingy.run_time(-1000,7500)
    dt.straight(-412)
    dt.reset()
def run6():
    dt=GyroDriveBase(Motor(Port.F, Direction.COUNTERCLOCKWISE), Motor(Port.B),56,84)
    dt.settings(500,250,45)
    dt.straight(550)
    dt.turn(-70)
    dt.straight(600)
    dt.turn(-20)
    dt.reset()
run1()
wait(7500)
run2()
wait(7500)
run3()
wait(7500)
run4()
wait(7500)
run5()
wait(7500)
run6()
