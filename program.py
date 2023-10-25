#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
import time
mt = MoveTank("outA", "outD",)
ms = MoveSteering("outA", "outD",)
mr = LargeMotor("outA")
ml = LargeMotor("outD")
kr = MediumMotor("outB")
kl = MediumMotor("outC")
g = GyroSensor("in2")
c1 = ColorSensor("in1")
c2 = ColorSensor("in4")

g.calibrate()
time.sleep(1)

def el(speed, megt, target=g.angle, multiplier = 0.8):
    target = g.angle
    ml.position = 0
    mr.position = 0
    while (ml.position+mr.position)/2<megt:
        remaining = target-g.angle
        correction = remaining*multiplier
        if correction > 100:
            correction = 100
        elif correction < -100:
            correction = -100
        ms.on(correction, speed)
        print(remaining, g.angle, (ml.position+mr.position)/2<megt)
    print("Motors turning off")
    ms.off()
    return 0

def hel(speed, megt, target=g.angle, multiplier = 1.5):
    target=g.angle
    ml.position = 0
    mr.position = 0
    while (ml.position+mr.position)/2>megt:
        remaining = target-g.angle
        correction = remaining*multiplier
        if correction > 100:
            correction = 100
        elif correction < -100:
            correction = -100
        ms.on(-correction, speed)
        print(remaining, g.angle, (ml.position+mr.position)/2<megt)
    print("Motors turning off")
    ms.off()
    return 0

def fordulas(target, multiplier=0.8):
    if target < 0:
        target=target*-1
        target=target%180
        target=target*-1
    elif target >= 0:
        target=target%180  
    while target != g.angle:
        diff = target-g.angle
        diff*multiplier
        if diff > 100: 
            diff = 100
        elif diff < -100:
            diff = -100
        mt.on(diff, -diff)
        print(diff, target, g.angle)
    mt.stop()

fordulas(70)
time.sleep(3)
fordulas(-80)
time.sleep(3)
fordulas(70)
time.sleep(3)
fordulas(-100)