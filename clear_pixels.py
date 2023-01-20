#!/usr/bin/python3
"""
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Python script that clears LED display panel on SenseHat.
 ******************************************************************************
"""
import sys
import getopt
from sense_emu import SenseHat
import json

sense = SenseHat()

for x in range(0,8):
    for y in range(0,8):
        sense.set_pixel(x, y, 255, 255, 255)