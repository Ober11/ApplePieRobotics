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
    def up():
        pvmotor.on_for_degrees(80, 140)
    def down():
        pvmotor.on_for_degrees(-80, 140)
    def MovePenVector(direction, distance):
        if direction == 0 or -0:
            phmotor.on_for_degrees(30, distance)
        else:    
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
            Pen.down()
            Pen.MovePenVector(45, 500)
            Pen.MovePenVector(-45, 500)
            Pen.up()
            Pen.MovePenVector(45, 250)
            Pen.down()
            Pen.MovePenVector(0, 450)
            Pen.up()
            print("a")
            Pen.reset()

        def b():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 200)
            phmotor.on_for_degrees(30, 200)
            Pen.MovePenVector(-0, -200)
            Pen.up()
            Pen.MovePenVector(0, 300)
            phmotor.on_for_degrees(30, 300)
            Pen.MovePenVector(-0, -300)
            Pen.down()
            print("b")
            Pen.up()
            Pen.reset()
        def c():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 450)
            phmotor.on_for_degrees(-0, -500)
            Pen.MovePenVector(-0, -450)
            Pen.up()
            print("c")
            Pen.reset()
        def d():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(-45, 50)
            Pen.MovePenVector(-70, 50)
            phmotor.on_for_degrees(-30, -250)
            Pen.MovePenVector(110,50)
            Pen.MovePenVector(135, 50)
            Pen.up()
            print("d")
            Pen.reset()
        def e():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 500)
            Pen.up()
            phmotor.on_for_degrees(-30, -250)
            Pen.down()
            Pen.MovePenVector(-0, -500)
            Pen.up()
            phmotor.on_for_degrees(-30, -250)
            Pen.down()
            Pen.MovePenVector(0, 500)
            Pen.up()
            print("e")
            Pen.reset()
        def f():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 500)
            Pen.up()
            phmotor.on_for_degrees(-30, -200)
            Pen.down()
            Pen.MovePenVector(-0, -500)
            Pen.up()
            print("f")
            Pen.reset()
        def g():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 300)
            Pen.up()
            Pen.MovePenVector(-0, -300)
            phmotor.on_for_degrees(-30, -500)
            Pen.down()
            Pen.MovePenVector(0, 250)
            phmotor.on_for_degrees(30, 200)
            Pen.MovePenVector(-0, -100)
            Pen.MovePenVector(0, 200)
            Pen.up()
            print("g")
            Pen.reset()
        def h():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.up()
            phmotor.on_for_degrees(30, 250)
            Pen.down()
            Pen.MovePenVector(0, 250)
            phmotor.on_for_degrees(-30, -250)
            phmotor.on_for_degrees(30, 500)
            Pen.up()
            print("h")
            Pen.reset()
        def i():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.updown()()
            print("i")
            Pen.reset()
        def j():
            phmotor.on_for_degrees(30, 500)
            Pen.down()
            Pen.MovePenVector(0, 300)
            Pen.MovePenVector(-0, -150)
            phmotor.on_for_degrees(30, 400)
            phmotor.on_for_degrees(30, 100, Block=False)
            inputmotor.on_for_degrees(-30, -100, Block=False)
            outputmotor.on_for_degrees(-30, -100, Block=True)
            inputmotor.on_for_degrees(30, 100, Block=False)
            outputmotor.on_for_degrees(30, 100, )
            Pen.up()
            print("j")
            Pen.reset()
        def k():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.up()
            phmotor.on_for_degrees(30, 250)
            Pen.down()
            Pen.MovePenVector(45, 200)
            Pen.up()
            phmotor.on_for_degrees(30, 300)
            Pen.down()
            Pen.MovePenVector(-45,-500)
            Pen.up()
            print("k")
            Pen.reset()
        def l():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.up()
            phmotor.on_for_degrees(-30, -500)
            Pen.down()
            Pen.MovePenVector(0, 200)
            Pen.up()
            print("l")
            Pen.reset()
        def m():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(-45, -500)
            Pen.MovePenVector(45, 500)
            phmotor.on_for_degrees(-30, -500)
            Pen.up()
            print("m")
            Pen.reset()
        def n():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(-45, -500)
            phmotor.on_for_degrees(30, 500)
            Pen.up()
            print("n")
            Pen.reset()
        def o():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 500)
            phmotor.on_for_degrees(-30, -500)
            Pen.MovePenVector(180, 500)
            Pen.up()
            print("o")
            Pen.reset()
        def p():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            phmotor.on_for_degrees(-30, -100, Block=False)
            inputmotor.on_for_degrees(-30, -150, Block=False)
            outputmotor.on_for_degrees(-30, -150)
            time.sleep(0,5)
            phmotor.on_for_degrees(-30, -100, Block=False)
            inputmotor.on_for_degrees(30, 150, Block=False)
            outputmotor.on_for_degrees(30, 150)
            Pen.up()
            print("p")
            Pen.reset()
        def q():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 500)
            phmotor.on_for_degrees(-30, -500)
            Pen.MovePenVector(-0, -500)
            Pen.up()
            Pen.MovePenVector(0, 250)
            phmotor.on_for_degrees(30, 250)
            Pen.down()
            Pen.MovePenVector(50, 400)
            Pen.up()
            print("q")
            Pen.reset()
        def r():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(0, 200)
            phmotor.on_for_degrees(30, 200)
            Pen.MovePenVector(-0, -200)
            Pen.MovePenVector(-45, -300)
            Pen.up()
            print("r")
            Pen.reset()
        def s():
            Pen.down()
            Pen.MovePenVector(0, 250)
            phmotor.on_for_degrees(30, 250)
            Pen.MovePenVector(180, 250)
            phmotor.on_for_degrees(30, 250)
            Pen.MovePenVector(0, 250)
            Pen.up()
            print("s")
            Pen.reset()
        def t():
            Pen.down()
            phmotor.on_for_degrees(30, 500)
            Pen.MovePenVector(-0, -250)
            Pen.MovePenVector(0, 500)
            Pen.up()
            print("t")
            Pen.reset()
        def u():
            phmotor.on_for_degrees(30, 500)
            Pen.down()
            phmotor.on_for_degrees(-30, -400, Block=True)
            phmotor.on_for_degrees(-20, -100, Block=False)
            inputmotor.on_for_degrees(30, 100, Block=False)
            outputmotor.on_for_degrees(30, 100, Block=False)
            phmotor.on_for_degrees(-20, -100, Block=False)
            inputmotor.on_for_degrees(30, 100, Block=False)
            outputmotor.on_for_degrees(30, 100, Block=False)
            phmotor.on_for_degrees(30, 400, Block=True)
            Pen.up()
            print("u")
            Pen.reset()
        def v():
            phmotor.on_for_degrees(30, 500)
            Pen.down()
            Pen.MovePenVector(-30, -500)
            Pen.MovePenVector(30, 500)
            Pen.up()
            print("v")
            Pen.reset()
        def w():
            phmotor.on_for_degrees(30, 500)
            Pen.down()
            Pen.MovePenVector(-30, -500)
            Pen.MovePenVector(30, 500)
            Pen.MovePenVector(-30, -500)
            Pen.MovePenVector(30, 500)
            Pen.up()
            print("w")
            Pen.reset()
        def x():
            Pen.down()
            Pen.MovePenVector(45, 500)
            Pen.up()
            phmotor.on_for_degrees(30, 200)
            Pen.down()
            Pen.MovePenVector(-45, -500)
            Pen.up()
            print("x")
            Pen.reset()
        def y():
            phmotor.on_for_degrees(30, 500)
            Pen.down()
            Pen.MovePenVector(-45, -250)
            Pen.MovePenVector(45, 250)
            Pen.MovePenVector(225, 500)
            Pen.up()
            print("y")
            Pen.reset()
        def z():
            phmotor.on_for_degrees(30, 500)
            Pen.down()
            Pen.MovePenVector(0, 500)
            Pen.MovePenVector(-45, -500)
            Pen.MovePenVector(0, 500)
            Pen.up()
            print("z")
            Pen.reset()
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
            start_time = time.time()
            while button1.is_pressed == True:
                pass
            elapsed_time= time.time() - start_time
            if elapsed_time >= 0.2:
                Pen.down()
                inputmotor.on_for_degrees(-30, 50, block=False)
                outputmotor.on_for_degrees(30, 50)
                Pen.up()
            else:
                Pen.down()
                inputmotor.on_for_degrees(-30, 150, block=False)
                outputmotor.on_for_degrees(30, 150)
                Pen.up()
                    
        if button2.is_pressed == True:
            inputmotor.on_for_degrees(-30, 150, block=False)
            outputmotor.on_for_degrees(30, 150)
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

    
    