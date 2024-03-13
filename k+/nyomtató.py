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



class Pen():
    print("a")
    def updown():
        pvmotor.on_for_degrees(80, 180)
        
class Letters():
    print("a")
    def Check(morse):
        if morse == [0, 1]:
            Letters.Write.a()
        elif morse == [1, 0, 0, 0]:
            Letters.Write.b()
        elif morse == [1, 0, 1, 0]:
            Letters.Write.c()
        elif morse == [1, 0, 0]:
            Letters.Write.d()
        elif morse == [0]:
            Letters.Write.e()
        elif morse == [0, 0, 1, 0]:
            Letters.Write.f()
        elif morse == [1, 1, 0]:
            Letters.Write.g()
        elif morse == [0, 0, 0, 0]:
            Letters.Write.h()
        elif morse == [0, 0]:
            Letters.Write.i()
        elif morse == [0, 1, 1, 1]:
            Letters.Write.j()
        elif morse == [1, 0, 1]:
            Letters.Write.k()
        elif morse == [0, 1, 0, 0]:
            Letters.Write.l()
        elif morse == [1, 1]:
            Letters.Write.m()
        elif morse == [1, 0]:
            Letters.Write.n()
        elif morse == [1, 1, 1]:
            Letters.Write.o()
        elif morse == [0, 1, 1, 0]:
            Letters.Write.p()
        elif morse == [1, 1, 0, 1]:
            Letters.Write.q()
        elif morse == [0, 1, 0]:
            Letters.Write.r()
        elif morse == [0, 0, 0]:
            Letters.Write.s()
        elif morse == [1]:
            Letters.Write.t()
        elif morse == [0, 0, 1]:
            Letters.Write.u()
        elif morse == [0, 0, 0, 1]:
            Letters.Write.v()
        elif morse == [0, 1, 1]:
            Letters.Write.w()
        elif morse == [1, 0, 0, 1]:
            Letters.Write.x()
        elif morse == [1, 0, 1, 1]:
            Letters.Write.y()
        elif morse == [1, 1, 0, 0]:
            Letters.Write.z()
        elif morse == [0, 0, 0, 0, 0]:
            Letters.Write.space()
        
    class Write():
        print("a")
        def a():  
            print("a")
        def b():
            print("b")
        def c():
            print("c")
        def d():
            print("d")
        def e():
            print("e")
        def f():
            print("f")
        def g():
            print("g")
        def h():
            print("h")
        def i():
            print("i")
        def j():
            print("j")
        def k():
            print("k")
        def l():
            print("l")
        def m():
            print("m")
        def n():
            print("n")
        def o():
            print("o")
        def p():
            print("p")
        def q():
            print("q")
        def r():
            print("r")
        def s():
            print("s")
        def t():
            print("t")
        def u():
            print("u")
        def v():
            print("v")
        def w():
            print("w")
        def x():
            print("x")
        def y():
            print("y")
        def z():
            print("z")
        def space():
            print("space")
        
   
mode = "morse"
cs.mode = 'COL-AMBIENT'
morse = []
while True:
    while mode == "morse":
        if button1.is_pressed == True:
            Pen.updown()
            while button1.is_pressed == True:
                pass
            Pen.updown()
        if button2.is_pressed == True:
            if inputmotor.is_running == True:
                inputmotor.off()
                outputmotor.off()
                time.sleep(0.2)
            else:
                inputmotor.on(-10, block=False)
                outputmotor.on(10, block=False)
            time.sleep(0.2)
        if button3.is_pressed == True:
            mode = "letter"
            cs.mode = 'COL-REFLECT'
            
                
    while mode == "letter":   
        print(morse)
        morse = []
        speaker.beep()
        
        while button2.is_pressed == False:
            if button1.is_pressed == True:
                start_time = time.time()
                while button1.is_pressed == True:
                    pass
                elapsed_time= time.time() - start_time
                if elapsed_time >= 0.2:
                    print("long")
                    morse.append(1)
                else:
                    print("short")
                    morse.append(0)
            if button3.is_pressed == True:
                mode = "morse"
                cs.mode = 'COL-AMBIENT'
                pass
        if mode == "morse":
                pass
        Letters.Check(morse)
        if mode == "morse":
                pass
        inputmotor.on_for_degrees(50, -85, block=False)
        outputmotor.on_for_degrees(50, 85)
        inputmotor.on_for_degrees(20, 30, block=False)
        outputmotor.on_for_degrees(20, 30)

    