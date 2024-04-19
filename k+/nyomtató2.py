#!/usr/bin/env python3
import sys, time, threading 
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sound import *
import time, sys, socket
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
    def up():
        pvmotor.on_for_degrees(80, 40)
    def down():
        pvmotor.on_for_degrees(-80, 40)
    def move_spaces(spaces, pendown=True):
        if pendown:
            pvmotor.on_for_degrees(30, 60, brake=False)
        time.sleep(0.3)
        inputmotor.on_for_degrees(-30, (spaces*10), block=False)
        outputmotor.on_for_degrees(30, (spaces*12))
        time.sleep(0.3)
        if pendown:
            pvmotor.on_for_degrees(-30, 60, brake=False)


        
class Letters():
    print("a")
    class Write():
        def a():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def b():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def c():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def d():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def e():
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def f():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def g():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def h():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def i():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def j():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def k():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def l():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def m():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def n():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def o():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def p():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def q():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def r():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def s():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def t():
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def u():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def v():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def w():
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def x():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def y():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(2, False)
        def z():
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(3)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(1, False)
            Pen.move_spaces(1)
            Pen.move_spaces(2, False)
        def space():
            Pen.move_spaces(5, False)



print("a")
def checkinput():
    global ainput
    while True:
        ainput = input()
        time.sleep(0.05)

t = threading.Thread(target=checkinput)
t.start()

ainput = None
while True:
    if ainput:
        if ainput == 'escape':
            sys.exit()
        elif hasattr(Letters.Write, ainput):
            print("Calling function for letter {}".format(ainput))
            getattr(Letters.Write, ainput)()
        else:
            print("Unknown letter: {}".format(ainput))
        ainput = None  # Reset ainput after processing