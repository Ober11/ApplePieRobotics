#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
import time
button1 = TouchSensor("in1")
button2 = TouchSensor("in4")
button3 = TouchSensor("in3")
cs = ColorSensor("in2")
inputmotor = LargeMotor("outA")
outputmotor = LargeMotor("outD")
pvmotor = LargeMotor("outC")
phmotor = MediumMotor("outB")
speaker = Sound()

#1:1.5 speed/ 1.5:1 fok arány ph:input/output
phmotor.on_for_degrees(11, 300, block=False)
inputmotor.on_for_degrees(16.5, 300, block=False)
outputmotor.on_for_degrees(16.5, 300)
time.sleep(2)
phmotor.on_for_degrees(30, -300)


