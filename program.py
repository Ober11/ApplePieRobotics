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

def el(speed, megt, target=g.angle, multiplier = 0.8, stop = True):
    ml.position = 0
    mr.position = 0
    originalspeed = speed
    megtfok = (ml.position+mr.position)/2
    remfok = megt - megtfok
    while remfok > 0:
        megtfok = (ml.position+mr.position)/2
        remfok = megt - megtfok
        if megtfok < 50:
            speed = max(megtfok * (originalspeed*0.02), 10)
        remaining = target-g.angle
        correction = remaining*multiplier
        if correction > 100:
            correction = 100
        elif correction < -100:
            correction = -100
        if stop == True:
            if remfok < 100:
                speed = max(originalspeed*(remfok*0.01), 10)
            
        ms.on(correction, speed)
        print(remaining, g.angle, (ml.position+mr.position)/2<megt)
    if stop == True:
        print("Motors turning off") 
        ms.off()
    return 0 

def hel(speed, megt, target=g.angle, multiplier =0.8, stop=True):
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
        ms.off()
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
    el(50, 345)
    kr.on_for_degrees(-30, 450)
    time.sleep(0.2)
    fordulas_with_timeout(-31, 1.2, 1.75)
    kr.on_for_degrees(30, 600)
    fordulas(10)
    kr.on_for_degrees(-50, 200)
    hel(-70, -920, 10)
    fordulas(-35)
    hel(-70, -320  , -30)
    g.reset()
    
    #   jelenetváltás
    time.sleep(0.2)
    el(60, 1030, 0)
    kl.on_for_degrees(30, 480)
    time.sleep(0.2)
    el(50, 250)
    fordulas(60)
    hel(-10, -175, 60, 1.5)
    time.sleep(0.4)
    fordulas(60)
    el(45, 79, 60)
    kr.on_for_degrees(-60, 975)
    el(45, 3, 60)
    time.sleep(1)
    hel(-60, -60)
    kr.on_for_degrees(40, 375)
    fordulas(-10)
    el(50, 300, -10, stop=False)
    el(50, 500, -45)
    el(50, 400, 0)
    g.reset()
    
    #   immerzív tapasztaltat
    time.sleep(0.3)
    hel(-60, -325, 45)
    fordulas(0)
    kl.on_for_degrees(30, 520)
    time.sleep(0.1)
    hel(-50, -80, 0)
    hel(-50, -350, 60)
    fordulas(0, 0.6)
    el(40, 40, 0)
    kr.on_for_degrees(-30, 975)
    time.sleep(0.2)
    kr.on_for_degrees(50, 285)
    
    #mozgókamera karjának felnyitása
    fordulas(180)
    el(60, 350, 220)
    kl.on_for_degrees(30, 520)
    time.sleep(0.1)
    hel(-70, -240, 225)
    fordulas(180)
    el(60, 880, 180)
    fordulas(224)
    el(60, 120, 224)
    time.sleep(0.2)
    kr.on_for_degrees(-30, 1200)
    hel(-30, -500, 180)
    kr.on_for_degrees(30, 600)
    el(100, 1400, 110)
    
def mk():
    #mozgó kamera ellökése
    g.reset()
    el(60, 700, 0)
    time.sleep(1)
    #közönségtag kiszállítása
    hel(-30, -1250, 0)
    time.sleep(2)
    el(60, 1450, 0)
    hel(-75, -800, 0)

def wb():
    #hangmixer
    g.reset()
    el(40, 630, 0, 0.5, stop=False)
    el(50, 200, 0.5)
    time.sleep(0.1)
    hel(-20, -200, -0, 0.8, stop=False)
    hel(-60, -630)

def szp():
    #színpad
    g.reset()
    el(60, 460, 0, multiplier=0.3)
    fordulas(-45,)
    
    #színpad
    time.sleep(0.5)
    el(60, 300, -45, multiplier=0.3, stop=False)
    el(60, 650, -15, 0.3)
    fordulas(-90, 0.5) 
    el(70, 400, -90, multiplier=0.3,)
    kr.on_for_degrees(-30, 300) 
    kl.on_for_degrees(-30, 700)
    hel(-60, -200, -90, 1.5)
    '''hel(-60, -750, -45)
    hel(-100, -900, 0)'''

def pft():
    #fényjáték
    g.reset()
    time.sleep(0.5)
    el(60, 1200, 0, stop=False)
    el(45, 220, 0,)
    kl.on_for_rotations(-30, 3.75)
    #Masterpiece(Tm)
    hel(-50, -20, 0, 0.5)
    print("hel1")
    fordulas(74, 0.6)
    print("fordulas2")
    el(60, 425, 74)
    print("el1")
    el(30, 575, 19)
    print("el2")
    hel(-30, -300, 74, 0.4)
    #visszamenetel a bázisba
    print("hel2")
    fordulas(-16, 0.6)
    print("fordulas3")
    el(60, 1200, -16, stop=False)
    el(60, 500, -76, stop=False)
    el(60, 700, -96, stop=False)
    el(60, 500, -56)
    print("el3")
     
   
def csirke():
    g.reset()
    el(60, 640, 0)
    fordulas(60)
    fordulas(0, 0.6)
    el(70, 470)
    kl.on_for_degrees(100, 4000)
    hel(-60, -1000)

valasztas = 0
balra = 0
jobbra = 0
fo = 0
menu = True
while menu == True:
    if valasztas < 0:
        valasztas = 6
    elif valasztas > 6:
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
        fo = "csirke"
        jobbra = "torony"
    elif valasztas == 5:
        fo = "színpad"
    elif valasztas == 6:
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
    try:
        while mongas == True:
            if btn.enter == True:
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
                    valasztas += 1
                    mk()
                elif valasztas == 4: 
                    print("Program elinditva")
                    mongas = False
                    time.sleep(0.3)
                    valasztas += 1
                    csirke()
                elif valasztas == 5: 
                    print("Program elinditva")
                    mongas = False
                    time.sleep(0.3)
                    valasztas += 1
                    szp()
                elif valasztas == 6: 
                    print("Program elinditva")
                    mongas = False
                    menu=False
            if btn.right == True:
                valasztas+=1
                mongas=False
                time.sleep(0.2)
            if btn.left == True:
                valasztas-=1
                mongas=False
                time.sleep(0.2)
            if btn.down == True:
                
                for i in range(0, 4):
                    kr.on_for_degrees(80, 90, block=False)
                    kl.on_for_degrees(80, 90, )
                    kr.on_for_degrees(-80, 90, block=False)
                    kl.on_for_degrees(-80, 90, )
    except KeyboardInterrupt:
        mt.off()
        print("a")
        ms.off()
        print("b")
        mr.off()
        ml.off()
        kl.off()
        print("c")
        kr.off()
        print("d")
        pass
    btn = None

