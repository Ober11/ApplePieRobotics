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

g.reset()

def el(speed, megt, target=g.angle, multiplier = 0.8, brek = True):
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
    ms.off(brake=brek)
    return 0

def hel(speed, megt, target=g.angle, multiplier = 1.5, brek = True):
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
        ms.on(-correction, speed,)
        print(remaining, g.angle, (ml.position+mr.position)/2<megt)
    print("Motors turning off")
    ms.off(brake=brek)
    return 0

def fordulas(target, multiplier=0.8):
    target = target*-1
    if target < 0:
        target=target*-1
        target=target%360
        target=target*-1
    elif target >= 0: 
        target=target%360  
    while target != g.angle:
        diff = target - g.angle
        diff*multiplier
        if diff > 100:
            diff = 100
        elif diff < -100: 
            diff = -100
        mt.on(diff, -diff)
        print(diff, target, g.angle)
    mt.stop()
    
    
kl.on_for_degrees(-30, 400)