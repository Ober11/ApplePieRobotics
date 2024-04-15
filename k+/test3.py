#!/usr/bin/env python3
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
import time
import math
button1 = TouchSensor("in1")
button2 = TouchSensor("in4")
button3 = TouchSensor("in3")
cs = ColorSensor("in2")
inputmotor = LargeMotor("outA")
outputmotor = LargeMotor("outD")
pvmotor = LargeMotor("outC")
phmotor = MediumMotor("outB")
speaker = Sound()



class Pen():
    print("a")
    def updown():
        pvmotor.on_for_degrees(80, 160)
    def MovePenVector(direction, distance):
        direction*=-1
        direction+=90
        direction_rad = math.radians(direction)

        delta_x = distance * math.cos(direction_rad)
        delta_y = distance * math.sin(direction_rad)

        print(delta_x, delta_y)
        if delta_y != 0:
            ratio = delta_x / delta_y
            print("Ratio of delta_x / delta_y:", ratio)
        scaling_factor = 1.5 / ratio
        phmotor.on_for_degrees(30*scaling_factor, delta_y, block=False)
        inputmotor.on_for_degrees(-30*scaling_factor, delta_x, block=False)
        outputmotor.on_for_degrees(30*scaling_factor, delta_x)
    
    def reset():
        while phmotor.position != 0:
            phmotor.on(-10)
        phmotor.off()
        
        
Pen.updown()
Pen.MovePenVector(45, 500)
Pen.MovePenVector(-45, 500)
Pen.MovePenVector(45, 250)
Pen.updown()
Pen.MovePenVector(45, 500)
Pen.updown()
print("a")

        