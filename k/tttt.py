#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.button import *
import time
from threading import Thread
mt = MoveTank("outA", "outD",)
ms = MoveSteering("outA", "outD",)
mr = LargeMotor("outA")
ml = LargeMotor("outD")
kr = MediumMotor("outB")
kl = MediumMotor("outC")
g = GyroSensor("in2")
#c1 = ColorSensor("in1")
c2 = ColorSensor("in4")

def test(speed, distance, target=None, multiplier=0.7, stop=True):
    if target == None:
            target = g.angle
    if distance < 0:
        distance *= -1
        distance = (ml.position+mr.position)/2 + distance
        distance *= -1
    distance = (ml.position+mr.position)/2 + distance
    originalspeed = speed
    required_degrees = (ml.position+mr.position)/2
    remaining_degrees = distance - required_degrees
    if remaining_degrees < 0:
        remaining_degrees *= -1
    print(remaining_degrees, required_degrees)

test(30, -500)
