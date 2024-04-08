# Setting Up Raspberry Pi Pico and Writing Scripts

This guide provides step-by-step instructions for setting up a Raspberry Pi Pico microcontroller board and writing scripts to run on it.

## 1. Hardware Setup

### Materials Needed
- Raspberry Pi Pico board
- Micro USB cable
- Computer with USB port

### Steps
1. **Connect Raspberry Pi Pico to Computer**:
   - Plug one end of the micro USB cable into the Raspberry Pi Pico's USB port.
   - Connect the other end of the cable to a USB port on your computer.

2. **Prepare Development Environment**:
   - Download and install the latest version of Thonny IDE from [thonny.org](https://thonny.org).
   - Launch Thonny IDE on your computer.

## 2. Software Setup

### Installing MicroPython Firmware
1. **Download MicroPython Firmware**:
   - Go to [raspberrypi.org/software](https://www.raspberrypi.org/software/) and download the latest MicroPython firmware for Raspberry Pi Pico.

2. **Flash MicroPython Firmware**:
   - Open Thonny IDE.
   - Go to `Tools` > `Options` > `Interpreter`.
   - Select `MicroPython (Raspberry Pi Pico)` as the interpreter.
   - Click `Install or update firmware`.
   - Follow the prompts to flash the MicroPython firmware onto the Raspberry Pi Pico.
# Raspberry_pi_pico
![raspberry](https://github.com/purushottam54/Firewall-Breaker/assets/116374245/56eb95d2-bdca-45c4-9b00-95051472314c)

## 3. Writing and Running Scripts

### Example LED Blink Script
1. **Open New Script**:
   - In Thonny IDE, click `File` > `New`.

2. **Write the Script**:
   ```python
   from machine import Pin
   import time

   led = Pin(25, Pin.OUT)

   while True:
       led.toggle()
       time.sleep(0.5)
### Example FIREWALL BREAKER
1. **Open New Script**:
   - In Thonny IDE, click `File` > `New`.
2. **Write the Script**:
   ```python
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

 # Firewall breaker video

https://github.com/purushottam54/Firewall-Breaker/assets/116374245/f2b09a3a-0a61-4786-88c4-292020a3b85b



 # Working of Raspberry Pi Pico Keyboard Automation Script

This Python script demonstrates keyboard automation using a Raspberry Pi Pico microcontroller board. The script utilizes the `adafruit_hid` library to emulate keypresses and interact with the host computer.

## Script Overview

The script performs the following actions:

1. **Imports**:
   - Imports necessary modules including `time`, `os`, `usb_hid`, `Keycode`, `Keyboard`, and `KeyboardLayoutUS` from the `adafruit_hid` library.

2. **Initial Delay**:
   - Waits for 3 seconds (`time.sleep(3)`) to allow time for USB enumeration after connecting the Raspberry Pi Pico to the computer.

3. **File Check**:
   - Checks if a file named `network.txt` does not exist in the current directory using `os.listdir()`.
   - If the file does not exist, it waits for an additional 1.5 seconds (`time.sleep(1.5)`).

4. **Keyboard Initialization**:
   - Initializes a virtual keyboard (`keyboard`) and sets the keyboard layout to US (`layout = KeyboardLayoutUS(keyboard)`).

5. **Keyboard Actions**:
   - Emulates keyboard actions to interact with the host computer:
     - Presses the `Windows` key (`Keycode.WINDOWS`) to open the Start menu.
     - Types `powershell` followed by pressing `Enter` to launch PowerShell (`layout.write("powershell\n")`).
     - Navigates to the `Run as Administrator` option in the PowerShell menu by sending `ARROW_RIGHT` key and then `ENTER`.
     - Executes the command `powershell -Command Start-Process powershell -Verb RunAs` to start a new PowerShell instance with administrative privileges.
     - Presses `ENTER` and `ARROW_DOWN` keys to confirm the action and proceed.

6. **Script Termination**:
   - Exits the script (`exit()`) and sends `ALT + F4` key combination to close the PowerShell window (`keyboard.send(Keycode.ALT, Keycode.F4)`).

## Running the Script

1. **Setup**:
   - Connect the Raspberry Pi Pico to your computer using a micro USB cable.

2. **Software Setup**:
   - Install the necessary libraries (`adafruit_hid`) for Raspberry Pi Pico development.
   - Use a compatible IDE like Thonny to edit and run Python scripts on the Raspberry Pi Pico.

3. **Execution**:
   - Copy the provided Python script (`keyboard_automation.py`) onto your Raspberry Pi Pico.
   - Open the script in Thonny IDE and run it to execute the keyboard automation actions.

## Note

- This script demonstrates basic keyboard automation functionalities using Raspberry Pi Pico and `adafruit_hid` library.
- Use caution when running scripts that emulate keyboard actions, especially those that interact with system-level functions like opening PowerShell with administrative privileges.

---

For more information on Raspberry Pi Pico and `adafruit_hid` library, refer to the official documentation and resources available at [raspberrypi.org](https://www.raspberrypi.org) and [Adafruit Learn](https://learn.adafruit.com).


