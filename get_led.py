#!/usr/bin/python3
"""
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get LED data: gets all LED matrix info and prints it.
 ******************************************************************************
"""
import sys
import getopt
from time import sleep
import os
from sense_emu import SenseHat
import json

sense = SenseHat()
led = sense.get_pixels()
led_message = {"id":"led","val":led,"type":"rgb","sensor":"LED2472G"}
led_message_json = json.dumps(led_message)
print(led_message_json)