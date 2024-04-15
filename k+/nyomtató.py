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
        pvmotor.on_for_degrees(80, 180)
    def MovePenVector(direction, distance):
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
        elif morse == [0, 0, 0, 0, 0] or []:
            Letters.Write.space()
        
    class Write():
        print("a")
        def a():  
            Pen.updown()
            Pen.MovePenVector(45, 500)
            Pen.MovePenVector(-45, -500)
            Pen.updown
            Pen.MovePenVector(45, 250)
            Pen.updown
            Pen.MovePenVector(0, 500)
            Pen.updown
            print("a")
            #FONTOS hogy a görbék NEM voltak tesztelve így nem biztos hogy jól működnek
            phmotor.reset
        def b():
            print("b")
        def c():
            print("c")
        def d():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            phmotor.on_for_degrees(-20, -250, Blokc=False)
            inputmotor.on_for_degrees(30, 200, Block=False)
            outputmotor.on_for_degrees(30, 200, Block=False)
            time.sleep(0,2)
            phmotor.on_for_degrees(-20, -250, Block=False)
            inputmotor.on_for_degrees(-20, -200, Block=False)
            outputmotor.on_for_degrees(-20, -200, Block=False)
            Pen.updown
            print("d")
            phmotor.reset
        def e():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 500)
            Pen.updown
            phmotor.on_for_degrees(-30, -250)
            Pen.updown
            Pen.MovePenVector(-0, -500)
            Pen.updown
            phmotor.on_for_degrees(-30, -250)
            Pen.updown
            Pen.MovePenVector(0, 500)
            print("e")
            phmotor.reset
        def f():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 500)
            Pen.updown
            phmotor.on_for_degrees(-30, -200)
            Pen.updown
            Pen.MovePenVector(-0, -500)
            Pen.updown
            print("f")
            phmotor.reset
        def g():
            print("g")
        def h():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            phmotor.on_for_degrees(30, 250)
            Pen.updown
            Pen.MovePenVector(0, 250)
            phmotor.on_for_degrees(-30, -250)
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            print("h")
            phmotor.reset
        def i():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            print("i")
            phmotor.reset
        def j():
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            Pen.MovePenVector(0, 300)
            Pen.MovePenVector(-0, -150)
            phmotor.on_for_degrees(30, 400)
            phmotor.on_for_degrees(30, 100, Block=False)
            inputmotor.on_for_degrees(-30, -100, Block=False)
            outputmotor.on_for_degrees(-30, -100, Block=True)
            inputmotor.on_for_degrees(30, 100, Block=False)
            outputmotor.on_for_degrees(30, 100, Block=True)
            Pen.updown
            print("j")
            phmotor.reset
        def k():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            phmotor.on_for_degrees(30, 250)
            Pen.updown
            Pen.MovePenVector(45, 200)
            Pen.updown
            phmotor.on_for_degrees(30, 300)
            Pen.updown
            Pen.MovePenVector(-45,-500)
            Pen.updown
            print("k")
            phmotor.reset
        def l():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            phmotor.on_for_degrees(-30, -500)
            Pen.updown
            Pen.MovePenVector(0, 200)
            print("l")
            phmotor.reset
        def m():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(-45, -500)
            Pen.MovePenVector(45, 500)
            phmotor.on_for_degrees(-30, -500)
            Pen.updown
            print("m")
            phmotor.reset
        def n():
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(-45, -500)
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            print("n")
            phmotor.reset
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
            Pen.updown
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(-0, -250)
            Pen.MovePenVector(0, 500)
            Pen.updown
            print("t")
            phmotor.reset
        def u():
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            phmotor.on_for_degrees(-30, -400, Block=True)
            phmotor.on_for_degrees(-20, -100, Block=False)
            inputmotor.on_for_degrees(30, 100, Block=False)
            outputmotor.on_for_degrees(30, 100, Block=False)
            phmotor.on_for_degrees(-20, -100, Block=False)
            inputmotor.on_for_degrees(30, 100, Block=False)
            outputmotor.on_for_degrees(30, 100, Block=False)
            phmotor.on_for_degrees(30, 400, Block=True)
            Pen.updown
            print("u")
            phmotor.reset
        def v():
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            Pen.MovePenVector(-30, -500)
            Pen.MovePenVector(30, 500)
            Pen.updown
            print("v")
            phmotor.reset
        def w():
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            Pen.MovePenVector(-30, -500)
            Pen.MovePenVector(30, 500)
            Pen.MovePenVector(-30, -500)
            Pen.MovePenVector(30, 500)
            Pen.updown
            print("w")
            phmotor.reset
        def x():
            Pen.updown()
            Pen.MovePenVector(45, 500)
            Pen.updown()
            phmotor.on_for_degrees(30, 200)
            Pen.updown
            Pen.MovePenVector(-45, -500)
            Pen.updown
            print("x")
            phmotor.reset()
        def y():
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            Pen.MovePenVector(-45, -250)
            Pen.MovePenVector(45, 250)
            Pen.MovePenVector(225, 500)
            Pen.updown
            print("y")
            phmotor.reset
        def z():
            phmotor.on_for_degrees(30, 500)
            Pen.updown
            Pen.MovePenVector(0, 500)
            Pen.MovePenVector(-45, -500)
            Pen.MovePenVector(0, 500)
            Pen.updown
            print("z")
            phmotor.reset
        def space():
            print("space")

phmotor.position = 0
phstartpos = phmotor.position
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
        time.sleep(5)
        inputmotor.on_for_degrees(50, -85, block=False)
        outputmotor.on_for_degrees(50, 85)
        inputmotor.on_for_degrees(20, 30, block=False)
        outputmotor.on_for_degrees(20, 30)

    