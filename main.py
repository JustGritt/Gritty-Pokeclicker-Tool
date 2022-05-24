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
        
        # Get X & Y position
        x = p.position()[0]
        y = p.position()[1]
        print(x, y)

        # Get RGB color at X & Y position
        r,g,b = p.pixel(x, y)
        print(r, g, b)

    # Start breeding script
    if k.is_pressed('8'):
        print("Start breeding script")
        while True : 
            p.click(x=2621, y=394, clicks=2, interval=0.001)
            t.sleep(0.001)

            # Get the pixel color in the position 
            x, y = 3315, 913
            r,g,b = p.pixel(x, y)

            # If the pixel color is not the same as the color background 
            if r == 68 and g == 68 and b == 68:
                pass
            else :  
                p.click(x=3408, y=639)
                p.click(x=2621, y=394, clicks=1, interval=0.1)

            # Stop the current loop
            if k.is_pressed('9'):
                print("Exit")
                break

    # Start autoclicker
    if k.is_pressed('7'):
        print("Start clicking")
        while True : 
            p.click(p.position(), clicks=6)
            t.sleep(0.1)

            # Stop the current loop
            if k.is_pressed('9'):
                print("Exit")
                break

    # End the program on press 9
    if k.is_pressed('-'):
        print("Exit")
        break

