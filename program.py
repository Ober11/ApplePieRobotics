#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.button import *
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
    time.sleep(0.3)

def mhdt():
    # mozgókép három dimenziónális térben
    g.reset()
    el(30, 300)
    kr.on_for_degrees(-50, 375)
    time.sleep(0.2)
    fordulas(-33)
    fordulas(10)
    kr.on_for_degrees(50, 375)
    hel(-50, -900, 10)
    fordulas(-35)
    hel(-50, -220, -35)
    g.reset()
    time.sleep(0.2)
    el(60, 1030, 0)
    kl.on_for_degrees(30, 360)
    hel(-60, -1030, 0)
    el(30, 50, 0)
    fordulas(-90)
    el(30, 160, -135)
    fordulas(-90)
    el(30, 405, -90)

    kr.on_for_degrees(-30, 360)
    kr.on_for_degrees(30, 350)
    

def mk():
    #mozgó kamera
    g.reset()
    el(60, 700, 0)
    time.sleep(1)
    hel(-60, -1100, 0)
    time.sleep(2)
    el(60, 1300, 0)
    hel(-60, -1100, 0)

def wb():
    #hangmixer
    g.reset()
    el(50, 630, 3, 0.8, brek=False, stop=False)
    el(30, 200,)
    kr.on_for_degrees(-10, 300)
    hel(-30, -200, -0, 0.8, stop=False)
    hel(-30, -630)

def szp():
    #színpad
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

def pft():
    g.reset()
    time.sleep(0.5)
    el(60, 1200, 0, stop=False)
    el(30, 215, 0,)
    #fordulas(-33)
    #el(60, 190, -33)
    
    kl.on_for_rotations(-30, 3.75)
    hel(-30, -20, 0)
    fordulas(74)
    el(50, 400, 74)
    el(50, 550, 24)
    hel(-80, -400, 24)
    hel(-80, -650, 74)
    hel(-80, -1200, 0)
    #el(50, 400, 54, stop=False)
    #el(40, 600, 14)
    #hel(-40, -150,  54)
    #fordulas(144)
    #el(50, 110, 144, stop=False)
    #el(50, 800, 234)
    
    #hel(-30, -110, 0)
    #fordulas(57, 0.3)
    #el(60, 450, 57, stop=False)
    #el(30, 650, 12, 1.5)
    '''hel(-30, -200, 0)
    fordulas(-90, 0.3)
    el(30, 400, -90)
    fordulas(-45)
    el(30, 170, -45)
    fordulas(-150, 0.3)
    el(60, 150, -150)
    fordulas(-90, 0.3)
    print("cocked")
    el(60, 200, -90)
    '''




valasztas = 0
balra = 0
jobbra = 0
fo = 0
menu = True
while menu == True:
    if valasztas < 0:
        valasztas = 5
    elif valasztas > 5:
        valasztas = 0
    if valasztas == 0:
        balra = "-"
        fo = "exit"
        jobbra = "mozgókép 1. futás"
    elif valasztas == 1:
        balra = "exit"
        fo = "mozgókép 1. futás"
        jobbra = "Mozgókamera"
    elif valasztas == 2:
        balra = "Mozgókép 1. futás"
        fo = "Mozgókamera"
        jobbra = "waterboard"
    elif valasztas == 3:
        balra = "Mozgókamera"
        fo = "waterboard"
        jobbra = "színpad"
    elif valasztas == 4:
        balra = "waterboard"
        fo = "színpad"
        jobbra = "torony"
    elif valasztas == 5:
        balra = "színpad"
        fo = "torony"
        jobbra = "exit"
    print("\033c", end="")
    print("------------------------------------")
    print("Valassz programot (<-, enter, ->) :")
    print("")
    print("<- ", balra, "   up: ", fo, "     ->", jobbra)
    print("------------------------------------")
    btn = Button()
    mongas = True
    while mongas == True:
        if btn.up == True:
            print("a")
            if valasztas == 0:
                menu = False 
                mongas = False
            elif valasztas == 1:
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                mhdt()
            elif valasztas == 2:
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                mk()
            elif valasztas == 3: 
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                wb()
            elif valasztas == 4: 
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                szp()
            elif valasztas == 5: 
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                pft()
        elif btn.left == True:
            print("b")
            valasztas -= 1
            time.sleep(0.2)
            mongas = False
        elif btn.right == True:
            print("c")
            valasztas += 1
            time.sleep(0.2)
            mongas = False
    btn = None
    
