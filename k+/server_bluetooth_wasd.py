import socket, keyboard, sys
#importálod a dolgokat
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#megcsinálod a szerver alapját (ahogyan a tutoriálban is)
bind_ip = "169.254.152.201"
#ipconfig /all
#cmd-ben ha ezt beírod, akkor kiírja a különfèle ip címeidet és van valami bluetooth cím, ami egy ehhez hasonló számsor
s.bind((bind_ip, 1234))
#kb megcsinálja a szervert
s.listen(1)
#asszem mennyi vendégnek van hely
clientsocket, addr = s.accept()
print(f"connected{addr}")
#ezek érthetőek
b = 0
s = 0
#az s dolog nemtudom, hogy mi
while True:
    a = "_"
    if keyboard.is_pressed('a'):
        a += 'a'
    if keyboard.is_pressed('s'):
        a += 's'
    if keyboard.is_pressed('w'):
        a += 'w'
    if keyboard.is_pressed('d'):
        a += 'd'
      #érzékeli a keyboardot
    if True:#a != b:
        clientsocket.send(bytes(a, "utf-8"))
        print(f"""[{a}]""")
    b = a
    #ez sufás volt jobban majd meg tudod csinálni, emlékszel hogyan működött szeptemberben
    if "p" in a:
        sys.exit()
        #kilèp ha a crtl+p nyomsz