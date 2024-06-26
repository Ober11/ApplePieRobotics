#!/usr/bin/env micropython
from ev3dev2.motor import *
from ev3dev2.sensor.lego import *
from ev3dev2.button import *
from ev3dev2.console import Console
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

g.reset()
time.sleep(0.2)
global blocked
global x, y, nextstartposition, firstnavloop
firstnavloop = True

# 100 cordinate units == 5.08 cm
# 1 cordinate unit = 0.0508 cm

console = Console()
console.set_font(font='Lat15-Terminus20x10', reset_console=False)

class Navigation():
    def GetNumberInCordinates(centimeters):
        cordinates = centimeters / 0.0508
        return cordinates
    def CordinateUpdates():
        global x, y, nextstartposition, firstnavloop
        print("a")
        while True:
            if firstnavloop:
                motorpositionstart = (ml.position*mr.position)/2
                firstnavloop = False
            elif not firstnavloop:
                motorpositionstart = nextstartposition
            motorpositionfinish = (ml.position*mr.position)/2
            robotangle = GyroSensor("in2").angle
            nextstartposition = (ml.position*mr.position)/2
            motorpositionchange = motorpositionfinish - motorpositionstart
            xcordinatechange = motorpositionchange * math.sin(robotangle)
            ycordinatechange = motorpositionchange * math.cos(robotangle)

            x += xcordinatechange
            y += ycordinatechange
               
    def MoveTo(X, Y, enddegrees, force=False):
        print("a")
        start_point = [x, y]
        end_point = [X, Y]

        delta_x = end_point[0] - start_point[0]
        delta_y = end_point[1] - start_point[1]
        
        distance = Navigation.dist(start_point, end_point)
        angle_radians = math.atan2(delta_y, delta_x)
        angle_degrees = math.degrees(angle_radians)
        
        turn(angle_degrees-90)
        forandbackward(30, distance, angle_degrees)
        turn(enddegrees+90)
            
def forandbackward(speed, distance, target=None, multiplier = 0.8, stop = True,):
    #checking if the target is manually set, if not it will be the current angle of the gyrosensor. This is needed because pythons default value stays the same as when it was initialized
    if target == None:
        target = g.angle
    #assigning a variable to the position of the motors at the start
    start_degrees = (ml.position+mr.position)/2
    #calculating the target motor position compared to the current starting position
    target_distance = start_degrees + distance
    #assigning the original full speed to a variable
    originalspeed = speed
    #calculating the remaining motor degrees to the target
    remaining_degrees = target_distance - start_degrees
    #assigning a variable to the remaining degrees that remain unchanged for later calculations
    original_remaining_degrees = remaining_degrees
    #looping until the target is reached
    while remaining_degrees * (1 if distance >= 0 else -1) > 0:
        #calculating how much of the distance is already covered
        iteration_completed_degrees = (ml.position+mr.position)/2-start_degrees
        #calculating the remaining distance to the target
        remaining_degrees = original_remaining_degrees - iteration_completed_degrees
        #linear acceleration, this is where the variably originalspeed is used, by using linear scaling until its fully reached
        if abs(iteration_completed_degrees) < 50:
            speed = max(abs(iteration_completed_degrees) * (originalspeed*0.02), 10)
        #calculating the gyro angle compared to the target angle, for correcting the angle so we don't stray off path, or to turn while moving
        remaining = target-g.angle
        #using a multiplier to control the speed of turning
        correction = remaining*multiplier
        #completely limiting the speed of turning
        correction = min(max(correction, -100), 100)
        #linear deceleration
        if stop == True and abs(remaining_degrees) < 100:
            speed = max(originalspeed*(abs(remaining_degrees)*0.01), 10)
        #turning on the motors
        ms.on(correction if distance >= 0 else -correction, speed if distance >= 0 else -speed)
        #printing debugging variables
        print(remaining, g.angle, (ml.position+mr.position)/2<target_distance, ml.position, mr.position)
    #stopping the motors after the target is reached
    if stop == True:
        print("Motors turning off") 
        ms.off()



def turn(target, multiplier=0.6, timeout=None):
    #modulo modifiers for efficiency
    if target < 0:
        target=target*-1
        target=target%360
        target=target*-1
    elif target >= 0: 
        target=target%360  
    #starting timeout if needed
    start_time = time.time() if timeout else None

    #looping until the target is reached
    while target != g.angle:
        # Check for timeout
        if timeout:
            elapsed_time = time.time() - start_time
            if elapsed_time > timeout:
                print("Timeout reached. Exiting the loop.")
                break
        # Calculating the difference between the target and the current angle
        diff = target - g.angle
        #multiplier for the speed of the motors
        diff *= multiplier
        #limiting the speed of the motors
        if diff > 100:
            diff = 100
        elif diff < -100: 
            diff = -100
        #turning the motors
        mt.on(diff, -diff)
        #print test
        print(diff, target, g.angle)
    #stopping the motors
    mt.stop()
    time.sleep(0.3)

def force_on_for_degrees(motor, speed, degrees):
    motor.position = 0
    direction = 1 if degrees >= 0 else -1
    speed *= direction
    start_time = time.time()
    if direction == 1:
        while motor.position < degrees:
            if start_time+2 < time.time():
                break
            motor.on(speed)
            if motor.is_stalled:
                motor.off()
                time.sleep(0.1)
    elif direction == -1:
        while motor.position > degrees:
            if start_time+2 < time.time():
                break
            motor.on(speed)
            if motor.is_stalled:
                motor.off()
                time.sleep(0.1)
    motor.off()
    
def tokiodrift():
    #3,5 sec
    g.reset()
    time.sleep(0.1)
    forandbackward(80, -230)
    turn(-17, 1)
    forandbackward(80, -645)
    turn(-80, timeout=1)
    forandbackward(80, 1000, 0)

    
def big_lap():
    # mozgókép három dimenziónális térben
    # 51 sec
    #   3d mozi
    mr.reset()
    ml.reset()
    g.reset()
    kl.on_for_seconds(-30, 1, block=False)
    kr.on_for_seconds(-30, 1, block=False)
    forandbackward(60, 500, 0, 0.6)
    turn(44, 0.4)
    g.reset()
    
    #   jelenetváltás
    forandbackward(60, 550, 0)
    kl.on_for_degrees(30, 150)
    #popcorn expert and audience member placed
    forandbackward(50, 400, 0)
    kr.on_for_degrees(30, -200)
    turn(50, 0.5)
    #forandbackward(30, -90)
    #kr.on_for_degrees(60, 900)
    
    #put audience member
    kl.on_for_degrees(30, 125)
    turn(50)
    forandbackward(30, 195, 50)
    kr.on_for_degrees(60, -300)
    forandbackward(30, 145, 50)
    
    force_on_for_degrees(kr, 60, 700)
    time.sleep(0.1)
    forandbackward(30, -100)
    time.sleep(0.1)
    kr.on_for_seconds(-60, 0.5)
    forandbackward(40, -120)
    turn(-49, 0.4,3)
    forandbackward(60, 380, -49)
    kr.on_for_seconds(-60, 0.2)
    #put the expert and audience member down
    forandbackward(60, 245, -40)
    #imerzív tapasztalat lenyomása
    time.sleep(0.1)
    kl.on_for_degrees(60, -100)
    kr.on_for_seconds(100, 2)
    time.sleep(0.1)
    forandbackward(60, -120, -45)
    kr.on_for_seconds(100, 0.4)
    
    kr.on_for_degrees(60, -700)
    #touched imerzív tapasztalat
    forandbackward(60, -120, -40)
    kl.on_for_degrees(30, 200)
    time.sleep(1)
    turn(-100, 0.4)
    forandbackward(60, 460, -100, stop=False,)
    forandbackward(60, 400, -180)
    turn(-150)
    kl.on_for_degrees(30, 130)
    turn(-180)
    forandbackward(60, 685, -180)
    #in front of the rollecoster switch
    turn(-130)
    time.sleep(0.1)
    kr.on_for_degrees(60, 700)
    time.sleep(0.1)
    #switched the rollercoaster switch
    forandbackward(60, -150, -154)
    kr.on_for_seconds(-100, 0.5)
    turn(-90)
    #after this we move the ring into its box
    forandbackward(40, -160, -90)
    kr.on_for_degrees(60, 500)
    
    #putting the rod in the ring
    forandbackward(40, -320, -90)
    turn(-25)
    forandbackward(50, -200, -25)
    kr.on_for_degrees(60, -500)
    #back to base
    forandbackward(100, -800, -90)


    '''forandbackward(60, -60)
    kr.on_for_degrees(40, 375)
    turn(-10)
    forandbackward(50, 300, -10, stop=False)
    forandbackward(50, 500, -45)
    forandbackward(50, 400, 0)
    g.reset()
    
    #   immerzív tapasztaltat
    time.sleep(0.3)í
    forandbackward(60, -325, 30)
    turn(0, timeout=4)
    kl.on_for_degrees(30, 520)
    time.sleep(0.1)
    forandbackward(50, -80, 0)
    forandbackward(50, -350, 60)
    turn(0, 0.6)
    forandbackward(40, 80, 0)
    kr.on_for_degrees(-30, 975)
    time.sleep(0.2)
    kr.on_for_degrees(50, 285)
    
    #mozgókamera karjának felnyitása
    turn(180)
    forandbackward(60, 350, 220)
    kl.on_for_degrees(30, 520)
    time.sleep(0.1)
    forandbackward(70, -240, 225)
    turn(180)
    forandbackward(60, 880, 180)
    turn(224)
    forandbackward(60, 120, 224)
    time.sleep(0.2)
    kr.on_for_degrees(-30, 1200)
    forandbackward(30, -500, 180)
    kr.on_for_degrees(30, 600)
    forandbackward(100, 1400, 112)'''
    
    
def rollercoaster():
    #7 sec
    #mozgó kamera ellökése
    g.reset()
    forandbackward(100, -600, 0)
    time.sleep(0.65)
    forandbackward(100, 1250, 0)
    forandbackward(100, -800, 0)

def soundmixer():
    #hangmixer
    #5 sec
    g.reset()
    forandbackward(70, 650, 0, 0.5, stop=False)
    kr.on_for_degrees(-50, 400, block=False)
    forandbackward(60, 150, 0.5,)
    time.sleep(0.1)
    forandbackward(40, -200, 0, 0.8, stop=False)
    forandbackward(80, -750, -30, 0.4)

def concert():
    #9 sec
    #színpad
    g.reset()
    forandbackward(60, 290, 0, multiplier=0.3)
    turn(-45,  multiplier=0.6)
    
    #színpad
    forandbackward(100, 1050)
    forandbackward(100, 700, -90)
    #forandbackward(60, 430, -45, multiplier=0.3, stop=False)
    #forandbackward(60, 620, -15, 0.3)
    #turn(-90, 0.5) 
    #forandbackward(70, 450, -90, multiplier=0.3,)
    kr.on_for_degrees(-100, 300) 
    kl.on_for_degrees(-100, 700)
    forandbackward(100, -400, -90, 1.5)
    '''forandbackward(60, -750, -45)
    forandbackward(100, -900, 0)'''

def lightshow():
    #fényjáték
    #24 sec
    g.reset()
    time.sleep(0.1)
    forandbackward(60, 1200, 0, stop=False)
    forandbackward(45, 200, 0,)
    kl.on_for_rotations(-100, 3.75)
    #Masterpiece(Tm)
    forandbackward(50, -20, 0, 0.5)
    print("el1")
    turn(74, 0.6)
    print("fordulas2")
    forandbackward(60, 425, 74)
    print("el1")
    forandbackward(30, 575, 54)
    print("el2")
    forandbackward(30, -300, 74, 0.4)
    #visszamenetel a bázisba
    print("el2")
    turn(-16, 0.6)
    print("fordulas3")
    forandbackward(60, 510, -16)
    turn(74)
    forandbackward(60, 400, 74)
    turn(-106)
    forandbackward(60, 70, -106, stop=False)
    forandbackward(60, 150, -71, stop=False)
    forandbackward(60, 340, -16)
    forandbackward(60, 500, 14)
    
    '''
    forandbackward(60, 1200, -16, stop=False)
    forandbackward(60, 500, -76, stop=False)
    forandbackward(60, 700, -96, stop=False)
    forandbackward(60, 500, -56)
    print("el3")'''


def chicken():
    #17,6 sec
    g.reset()
    forandbackward(60, 640, 1)
    turn(60)
    turn(0, 0.6)
    forandbackward(100, 470, 1)
    kl.on_for_degrees(100, 3000)
    forandbackward(30, -500)
    turn(40)
    forandbackward(100, 500, 39, 1, stop=False)
    forandbackward(100, 700, 40, stop=False)
    forandbackward(100, 1000, 40, stop=False)
    forandbackward(100, 1000, 91)



x=0
y=0
navt = Thread(target=Navigation.CordinateUpdates)
#navt.start()
choice = 0
left = 0
right = 0
fo = 0
menu = True
menu_select = True
while menu == True:
    if choice < 0:
        choice = 7
    elif choice > 7:
        choice = 0
    if choice == 0:
        left = "-"
        fo = "chicken"
        right = "tokiodrift"
    if choice == 1:
        left = "chicken"
        fo = "tokiodrift"
        right = "sound mixer"
    elif choice == 2:
        left = "tokiodrift"
        fo = "sound mixer"
        right = "big lap"
    elif choice == 3:
        left = "sound mixer"
        fo = "big lap"
        right = "tower"
    elif choice == 4:
        left = "big lap"
        fo = "tower"
        right = "roller coaster"
    elif choice == 5:
        left = "tower"
        fo = "roller coaster"
        right = "hologram"
    elif choice == 6:
        fo = "hologram"
    elif choice == 7:
        left = "hologram"
        fo = "exit"
        right = "chicken"
    #print("\033c", end="")
    print("---------------")
    print("")
    print(fo)
    print("---------------")
    btn = Button()
    time.sleep(0.2)
    menu_select = True
    try:
        while menu_select == True:
            if btn.enter == True:
                print("a")
                if choice == 0:
                    menu_select = False
                    choice += 1 
                    chicken()
                elif choice == 1:
                    print("Program elinditva")
                    menu_select = False
                    time.sleep(0.3)
                    choice += 1
                    tokiodrift()
                elif choice == 2:
                    print("Program elinditva")
                    menu_select = False
                    time.sleep(0.3)
                    choice += 1
                    soundmixer()
                elif choice == 3: 
                    print("Program elinditva")
                    menu_select = False
                    time.sleep(0.3)
                    choice += 1
                    big_lap()
                elif choice == 4: 
                    print("Program elinditva")
                    menu_select = False
                    time.sleep(0.3)
                    choice += 1
                    lightshow()
                elif choice == 5: 
                    print("Program elinditva")
                    menu_select = False
                    time.sleep(0.3)
                    choice += 1
                    rollercoaster()
                elif choice == 6: 
                    print("Program elinditva")
                    menu_select = False
                    time.sleep(0.3)
                    choice+=1
                    concert()
                elif choice == 7:
                    print("program befejezve")
                    menu_select=False
                    menu=False
            if btn.right == True:
                choice+=1
                menu_select=False
                time.sleep(0.2)
            if btn.left == True:
                choice-=1
                menu_select=False
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