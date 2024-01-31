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
#c1 = ColorSensor("in1")
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

def hel(speed, megt, target=g.angle, multiplier =0.8, brek = True, stop=True):
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
    if stop == True:
        print("Motors turning off") 
        ms.off(brake=brek)
    return 0

def fordulas_with_timeout(target, multiplier=0.7, timeout=5):
    start_time = time.time()  # Record the start time
    while target != g.angle:
        # Check for timeout
        elapsed_time = time.time() - start_time
        if elapsed_time > timeout:
            print("Timeout reached. Exiting the loop.")
            break

        # Rest of the existing code
        diff = target - g.angle
        diff *= multiplier
        if diff > 100:
            diff = 100
        elif diff < -100: 
            diff = -100
        mt.on(diff, -diff)
        print(diff, target, g.angle)

    mt.stop()
    time.sleep(0.3)
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
    #   3d mozi
    g.reset()
    el(50, 300)
    kr.on_for_degrees(-30, 450)
    time.sleep(0.2)
    fordulas_with_timeout(-31, 0.7, 2.5)
    kr.on_for_degrees(30, 600)
    fordulas(10)
    kr.on_for_degrees(-50, 200)
    hel(-70, -900, 10)
    fordulas(-35)
    hel(-50, -275, -30)
    g.reset()
    
    #   jelenetváltás
    time.sleep(0.2)
    el(60, 1030, 0)
    kl.on_for_degrees(30, 480)
    time.sleep(0.2)
    el(50, 230)
    fordulas(60)
    hel(-10, -170, 60, 1.5)
    time.sleep(0.4)
    fordulas(60)
    el(45, 73, 60)
    kr.on_for_degrees(-60, 975)
    el(45, 3, 60)
    time.sleep(1)
    hel(-50, -60)
    kr.on_for_degrees(40, 375)
    fordulas(-10)
    el(40, 300, -10, stop=False)
    el(40, 500, -45)
    el(40, 400, 0)
    g.reset()
    
    #   immerzív tapasztaltat
    time.sleep(0.3)
    hel(-50, -325, 45)
    fordulas(0)
    kl.on_for_degrees(30, 520)
    time.sleep(0.1)
    hel(-50, -80, 0)
    hel(-50, -350, 60)
    fordulas(0, 0.3)
    el(40, 40, 0)
    kr.on_for_degrees(-30, 975)
    time.sleep(0.2)
    kr.on_for_degrees(50, 375)
    
    #mozgókamera karjának felnyitása
    fordulas(180)
    el(30, 290, 180)
    kl.on_for_degrees(30, 520)
    time.sleep(0.1)
    hel(-50, -150, 225)
    fordulas(180)
    el(50, 800, 180)
    fordulas(218)
    el(40, 70, 218)
    time.sleep(0.2)
    kr.on_for_degrees(-30, 1200)
    hel(-30, -500, 180)
    kr.on_for_degrees(30, 600)
    el(50, 1400, 120)
    
def mk():
    #mozgó kamera ellökése
    g.reset()
    el(60, 700, 0)
    time.sleep(1)
    #közönségtag kiszállítása
    hel(-30, -1250, 0)
    time.sleep(2)
    el(60, 1450, 0)
    hel(-30, -700, 0)

def wb():
    #hangmixer
    g.reset()
    el(30, 630, 0, 0.5, brek=False, stop=False)
    el(50, 200, 0.5)
    time.sleep(0.1)
    hel(-20           , -200, -0, 0.8, stop=False)
    hel(-60, -630)

def szp():
    #nyomtató betolása
    g.reset()
    el(60, 1100, 0, multiplier=0.3)
    hel(-30, -400, 0)
    fordulas(-45,)
    hel(-50, -550, -45)
    
    #színpad
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
    #fényjáték
    g.reset()
    time.sleep(0.5)
    el(60, 1200, 0, stop=False)
    el(30, 215, 0,)
    kl.on_for_rotations(-30, 3.75)
    #Masterpiece(Tm)
    hel(-30, -20, 0)
    print("hel1")
    fordulas(74)
    print("fordulas2")
    el(50, 525, 74)
    print("el1")
    el(23, 500, 19)
    print("el2")
    hel(-30, -300, 74, 0.4)
    #visszamenetel a bázisba
    print("hel2")
    fordulas(-16, 0.3)
    print("fordulas3")
    el(60, 1200, -16, stop=False)
    el(60, 500, -76, stop=False)
    el(60, 700, -96, stop=False)
    el(60, 500, -56)
    print("el3")
     
#---- jelenleg nem használt kód ----    
def csirke():
    g.reset()
    el(50, 1000, 0)
    hel(-40, -1000, 0)
#-----------------------------------

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
        fo = "futas1"
        jobbra = "mozgókép 1. futás"
    elif valasztas == 1:
        balra = "exit"
        fo = "hangmixer"
        jobbra = "Mozgókamera"
    elif valasztas == 2:
        balra = "Mozgókép 1. futás"
        fo = "torony"
        jobbra = "waterboard"
    elif valasztas == 3:
        balra = "Mozgókamera"
        fo = "mozgókamera"
        jobbra = "színpad"
    elif valasztas == 4:
        balra = "waterboard"
        fo = "színpad"
        jobbra = "torony"
    elif valasztas == 5:
        balra = "színpad"
        fo = "vége"
        jobbra = "exit"
    print("\033c", end="")
    print("------------------------------------")
    print("Nyomj egy felfelét a következő futáshoz")
    print("")
    print("-------------- " + fo + " ----------------")
    print("------------------------------------")
    btn = Button()
    mongas = True
    while mongas == True:
        if btn.up == True:
            print("a")
            if valasztas == 0:
                mongas = False
                mhdt()
                valasztas += 1 
            elif valasztas == 1:
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                valasztas += 1
                wb()
            elif valasztas == 2:
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                valasztas += 1
                pft()
            elif valasztas == 3: 
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                mk()
                valasztas += 1
            elif valasztas == 4: 
                print("Program elinditva")
                mongas = False
                time.sleep(0.3)
                valasztas += 1
                szp()
            elif valasztas == 5: 
                print("Program elinditva")
                mongas = False
                menu=False
    btn = None
