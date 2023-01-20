#!/usr/bin/python3
"""
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get joystick info: gets data from joystick and saves it to joystick.dat. While True loop!
 ******************************************************************************
"""
import sys
import getopt
from sense_emu import SenseHat
import json
from time import sleep
import select
import os
sense = SenseHat()
x = 0
y = 0
middle = 0
timeout = 0.1

while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if event.direction == "up":
                y += 1
            elif event.direction == "down":
                y -= 1
            elif event.direction == "left": 
                x -= 1
            elif event.direction == "right":
                x += 1
            elif event.direction == "middle":
                middle += 1
    dict_json = {"x":x,"y":y,"middle":middle}
    result = json.dumps(dict_json)
    plik = open("/home/pi/server/IoT/joystick.dat", "w" ,os.O_NONBLOCK)
    plik.write(result)
    plik.close()
    sleep(1)
