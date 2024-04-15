#!/usr/bin/env python3
import socket, sys, time
from ev3dev2.motor import OUTPUT_A, OUTPUT_D, OUTPUT_C, MoveTank, Motor
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#ez a sor fontos így kell a dolgot beírni
HOST = "169.254.152.201"
##megnyitod a cmd
##ipconfig /all
##bluetooth device, a cím mögöt zárójelben preferred
##Berakod azt a számsort a HOST illetve a srver.py-nál a bind_ip
#igen egyet értek a régi csigával ezt kell csinálni le van írva a serverben is már
s.connect((HOST, 1234))
mt = MoveTank(OUTPUT_A, OUTPUT_D)
messg_c = ""
while True:
    msg = s.recv(1024) 
    messg = msg.decode("utf-8")
    if messg_c == messg:
        pass

    left = 0
    right = 0
    speed = 0
    #megkapja az üzenet és dekódolja
    if 'w' in messg:
        left += 70
        right += 70
    if 'a' in messg:
        left -= 30
        right += 30
    if "s" in messg:
        left -= 70
        right -= 70
    if "d" in messg:
        left += 30
        right -= 30

    
    if "l" in messg:
        speed -= 100
    if "f" in messg:
        speed += 100

    if "p" in messg:
        sys.exit()
       #kilép
    if left > 100:
        left = 100
    elif left < -100:
        left = -100
    elif right > 100:
        right = 100
    elif right < -100:
        right = -100

    mt.on(left, right)
    messg_c = messg