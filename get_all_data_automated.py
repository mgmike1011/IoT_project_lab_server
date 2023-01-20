#!/usr/bin/python3
"""
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get all data automated: gets all available data from SenseHat and saves it to alldata.dat. While True loop!.
 ******************************************************************************
"""
import sys
import getopt
from time import sleep
import os
from sense_emu import SenseHat
import json

sense = SenseHat()

while True:
    json_dict = []
    temp = sense.get_temperature() # HTS221
    temp2 = sense.get_temperature_from_pressure() #LPS25H
    json_dict.append({"id":"temp1","val":temp,"type":"C","sensor":"THS221"})
    json_dict.append({"id":"temp2","val":temp2,"type":"C","sensor":"LPS25H"})
    hum = sense.get_humidity() # HTS221
    json_dict.append({"id":"humidity","val":hum,"type":"procent","sensor":"THS221"})
    press = sense.get_pressure() #LPS25H
    json_dict.append({"id":"pressure","val":press,"type":"hPa","sensor":"LPS25H"})
    roll = sense.get_accelerometer()["roll"] # LSM9DS1
    json_dict.append({"id":"roll","val":roll,"type":"deg","sensor":"LSM9DS1"})
    pitch = sense.get_accelerometer()["pitch"] # LSM9DS1
    json_dict.append({"id":"pitch","val":pitch,"type":"deg","sensor":"LSM9DS1"})
    yaw = sense.get_accelerometer() # LSM9DS1
    yaw = yaw["yaw"]
    json_dict.append({"id":"yaw","val":yaw,"type":"deg","sensor":"LSM9DS1"})
    mag = sense.get_compass_raw()
    json_dict.append({"id":"magnetometer_x","val":mag["x"],"type":"uT","sensor":"LSM9DS1"})
    json_dict.append({"id":"magnetometer_y","val":mag["y"],"type":"uT","sensor":"LSM9DS1"})
    json_dict.append({"id":"magnetometer_z","val":mag["z"],"type":"uT","sensor":"LSM9DS1"})
    accel = sense.get_accelerometer_raw()
    json_dict.append({"id":"linear_accel_x","val":accel["x"],"type":"G","sensor":"LSM9DS1"})
    json_dict.append({"id":"linear_accel_y","val":accel["y"],"type":"G","sensor":"LSM9DS1"})
    json_dict.append({"id":"linear_accel_z","val":accel["z"],"type":"G","sensor":"LSM9DS1"})
    gyr = sense.get_gyroscope_raw()
    json_dict.append({"id":"angular_accel_x","val":gyr["x"],"type":"radps","sensor":"LSM9DS1"})
    json_dict.append({"id":"angular_accel_y","val":gyr["y"],"type":"radps","sensor":"LSM9DS1"})
    json_dict.append({"id":"angular_accel_z","val":gyr["z"],"type":"radps","sensor":"LSM9DS1"})
    with open("/home/pi/server/IoT/joystick.dat","r") as plik:
        joystick_position = json.loads(plik.read())
        json_dict.append({"id":"joystick_x","val":joystick_position["x"],"type":"position","sensor":"SKRHABE010"})
        json_dict.append({"id":"joystick_y","val":joystick_position["y"],"type":"position","sensor":"SKRHABE010"})
        json_dict.append({"id":"joystick_m","val":joystick_position["middle"],"type":"position","sensor":"SKRHABE010"})
    message_to_save = json.dumps(json_dict)
    plik = open("/home/pi/server/IoT/alldata.dat", "w", os.O_NONBLOCK)
    plik.write(message_to_save)
    plik.close()
    led = sense.get_pixels()
    led_message = {"id":"led","val":led,"type":"rgb","sensor":"LED2472G"}
    led_message_json = json.dumps(led_message)
    plik_led = open("/home/pi/server/IoT/leddata.dat", "w", os.O_NONBLOCK)
    plik_led.write(led_message_json)
    plik_led.close()
    sleep(0.1)