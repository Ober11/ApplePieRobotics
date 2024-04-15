import threading
import time

def randomshit():
    time.sleep(10)
    print("Thread is done")

thread = threading.Thread(target=randomshit)
thread.start()

while thread.is_alive():
    print("Thread is still running")
    time.sleep(1)