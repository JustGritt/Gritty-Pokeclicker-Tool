import pyautogui as p
import keyboard as k
import time as t

# PyAutoGUI parameters
p.FAILSAFE = True
p.PAUSE = 0

while True :
    t.sleep(0.1)

    # Get position on 1
    if k.is_pressed('1'): 
        p.position()
        print(p.position())

    if k.is_pressed('2'):
        while True : 
            p.click(p.position(), interval=0, clicks=5)
            t.sleep(0.001)
            print("click")

            # Stop the current loop
            if k.is_pressed('3'):
                print("Exit")
                break

    # End the program on press 9
    if k.is_pressed('9'):
        print("Exit")
        break

