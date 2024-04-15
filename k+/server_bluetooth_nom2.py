import keyboard, sys, time
from pybricks.messaging import BluetoothMailboxClient, TextMailbox

SERVER = 'ev3dev2'

client = BluetoothMailboxClient()
mbox = TextMailbox('tunnel', client)

print('establishing connection...')
client.connect(SERVER)
print('connected!')

b = 0


while True:
    keypressed = ""
    if keyboard.is_pressed('a'):
        keypressed += 'a'
        print("a")
        time.sleep(3)
    if keyboard.is_pressed('b'):
        keypressed += 'b'
        print("b")
        time.sleep(3)
    if keyboard.is_pressed('c'):
        keypressed += 'c'
        print("c")
        time.sleep(3)
    if keyboard.is_pressed('d'):
        keypressed += 'd'
        print("d")
        time.sleep(3)
    if keyboard.is_pressed('e'):
        keypressed += 'e'
        print("e")
        time.sleep(3)
    if keyboard.is_pressed('f'):
        keypressed += 'f'
        print('f')
        time.sleep(3)
    if keyboard.is_pressed('g'):
        keypressed += 'g'
        print("g")
        time.sleep(3)
    if keyboard.is_pressed('h'):
        keypressed += 'h'
        print("h")
        time.sleep(3)
    if keyboard.is_pressed('i'):
        keypressed += 'i'
        print("i")
        time.sleep(3)
    if keyboard.is_pressed('j'):
        keypressed += 'j'
        print("j")
        time.sleep(3)
    if keyboard.is_pressed('k'):
        keypressed += 'k'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('l'):
        keypressed += 'l'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('m'):
        keypressed += 'm'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('n'):
        keypressed += 'n'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('o'):
        keypressed += 'o'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('p'):
        keypressed += 'p'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('q'):
        keypressed += 'q'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('r'):
        keypressed += 'r'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('s'):
        keypressed += 's'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('t'):
        keypressed += 't'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('u'):
        keypressed += 'u'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('v'):
        keypressed += 'v'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('w'):
        keypressed += 'w'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('x'):
        keypressed += 'x'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('y'):
        keypressed += 'y'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('z'):
        keypressed += 'z'
        print(keypressed)
        time.sleep(3)
    if keyboard.is_pressed('space'):
        keypressed += 'spc'
        print(keypressed)
    if keyboard.is_pressed('escape'):
        keypressed += 'esc'
        print(keypressed)
      #érzékeli a keyboardot
    if True:#a != b:
        mbox.send(keypressed)
        print(f"""[{keypressed}]""")
    b = keypressed
    #ez sufás volt jobban majd meg tudod csinálni, emlékszel hogyan működött szeptemberben
    if "esc" in keypressed:
        sys.exit()
        #kilèp ha a crtl+p nyomsz