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

def el(speed, megt, target=g.angle, multiplier = 0.8, brek = True, stop = True):
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
    if stop == True:
        print("Motors turning off") 
        ms.off(brake=brek)
    return 0

def hel(speed, megt, target=g.angle, multiplier =0.8, brek = True):
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
    
el(60, 1100, 0, multiplier=0.3)
hel(-30, -400, 0)
fordulas(-45,)
hel(-50, -550, -45)
g.reset()
time.sleep(0.5)
el(60, 800, 0, multiplier=0.3, stop=False)
el(60, 485, 30, 0.3)
fordulas(-45, 0.5) 
el(30, 400, -45, multiplier=0.3,)

kr.on_for_degrees(-30, 300)
kl.on_for_degrees(-30, 700)
hel(-60, -19, -45, 1.5)
hel(-60, -750, 0)
hel(-100, -900, 45)
'''
hel(-30, -300)
fordulas(0)
hel(-60, -1500, multiplier=0.3)
el(60, 500, stop=False)
el(60, 500, target=30)
'''