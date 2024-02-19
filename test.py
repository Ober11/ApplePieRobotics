#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.button import *
import time
mt = MoveTank("outA", "outD",)
ms = MoveSteering("outA", "outD",)
mr = LargeMotor("outA")
ml = LargeMotor("outD")
kr = MediumMotor("outB")
kl = MediumMotor("outC")
g = GyroSensor("in2")
#c1 = ColorSensor("in1")
c2 = ColorSensor("in4")

g.reset()

def el(speed, megt, target=g.angle, multiplier = 0.8, stop = True):
    ml.position = 0
    mr.position = 0
    originalspeed = speed
    megtfok = (ml.position+mr.position)/2
    remfok = megt - megtfok
    while remfok > 0:
        megtfok = (ml.position+mr.position)/2
        remfok = megt - megtfok
        if megtfok < 51:
            speed = max(megtfok * (originalspeed*0.02), 5)
        remaining = target-g.angle
        correction = remaining*multiplier
        if correction > 100:
            correction = 100
        elif correction < -100:
            correction = -100
        if remfok < 200:
            speed = max(originalspeed*(remfok*0.005), 5)
            
        ms.on(correction, speed)
        print(remaining, g.angle, (ml.position+mr.position)/2<megt)
    if stop == True:
        print("Motors turning off") 
        ms.off()
    return 0 

def hel(speed, megt, target=g.angle, multiplier =0.8, stop=True):
    ml.position = 0
    mr.position = 0
    while (ml.position+mr.position)/2>megt:
        remaining = target-g.angle
        correction = remaining*multiplier
        if correction > 100:
            correction = 100
        elif correction < -100:
            correction = -100
        ms.on(-correction, speed,)
        print(remaining, g.angle, (ml.position+mr.position)/2<megt)
    if stop == True:
        print("Motors turning off") 
        ms.off()
    return 0

def fordulas_with_timeout(target, multiplier=0.7, timeout=5):
    start_time = time.time()  # Record the start time
    while target != g.angle:
        # Check for timeout
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            print("Timeout reached. Exiting the loop.")
            break

        # Rest of the existing code
        diff = target - g.angle
        diff *= multiplier
        if diff > 100:
            diff = 100
        elif diff < -100: 
            diff = -100
        mt.on(diff, -diff)
        print(diff, target, g.angle)

    mt.stop()
    time.sleep(0.3)
def fordulas(target, multiplier=0.7):
    if target < 0:
        target=target*-1
        target=target%360
        target=target*-1
    elif target >= 0: 
        target=target%360  
    while target != g.angle:
        diff = target - g.angle
        diff*=multiplier
        if diff > 100:
            diff = 100
        elif diff < -100: 
            diff = -100
        mt.on(diff, -diff)
        print(diff, target, g.angle)
    mt.stop()
    time.sleep(0.3)

el(60, 1000)