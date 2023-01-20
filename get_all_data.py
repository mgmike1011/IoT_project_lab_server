#!/usr/bin/python3
"""
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get all data standard: gets all available data from SenseHat and prints it.
 ******************************************************************************
"""
import sys
import getopt
from sense_emu import SenseHat
import json

json_dict = []
sense = SenseHat()

tempflag = 0 # Temperature flag -t
tempval = 0 # Temperature value
humflag = 0 # Humidity flag -h
humval = 0 # Humidity value
presflag = 0 #Pressure flag -p
presval = 0 # Pressure value
rollflag = 0 # Roll flag -r
pitchflag = 0 # Pitch flag -i
yawflag = 0 # Yaw flag -y
uflag = 0 # Degree in roll, pitch, yaw flag -u
magnetometer = 0 # Magnetometer flag - indukcja magnetyczna uT -m 
accelerometer = 0 # Accelerometer flag - przyspieszenia liniowe G -a
gyroscope = 0 # Gyroscope flag - przyspieszenia katowe rad/s -g
joystick = 0 # Joystick -j

sysarg = sys.argv[1:]

# #############################
#    ///     Get parameter    ///
# #############################
try:
    opts, args = getopt.getopt(sysarg,':t:h:p:riyumagjl')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for opt, arg in opts:
    if opt in '-t': # Temperature
        tempflag = 1
        tempval = arg
    elif opt in '-h': # Humidity
        humflag = 1
        humval = arg
    elif opt in '-p': # Pressure
        presflag = 1
        presval = arg
    elif opt in '-r': # Roll
        rollflag = 1
    elif opt in '-i': # Pitch
        pitchflag = 1
    elif opt in '-y': # Yawn
        yawflag = 1
    elif opt in '-u': # RPY in deg
        uflag = 1
    elif opt in '-m': # Magnetic induction
        magnetometer = 1
    elif opt in '-a': # Linear accelerations
        accelerometer = 1
    elif opt in '-g': # Angle accelerations
        gyroscope = 1
    elif opt in '-j': # Joystick
        joystick = 1

# #############################
#    ///     Temperature, humidity, pressure     ///
# #############################
if tempflag: # Temperature 
    if tempval == 'C': # C deg
        temp = sense.get_temperature() # HTS221
        temp2 = sense.get_temperature_from_pressure() # LPS25H
        json_dict.append({"id":"temp1","val":temp,"type":"C","sensor":"THS221"})
        json_dict.append({"id":"temp2","val":temp2,"type":"C","sensor":"LPS25H"})
    elif tempval == 'F': # Fahrenheit
        temp = 9/5 * sense.get_temperature() + 32 # HTS221
        temp2 = 9/5 * sense.get_temperature_from_pressure() + 32 # LPS25H
        json_dict.append({"id":"temp1","val":temp,"type":"F","sensor":"THS221"})
        json_dict.append({"id":"temp2","val":temp2,"type":"C","sensor":"LPS25H"})

if humflag: # Humidity
    if humval == 'p': # Percent
        hum = sense.get_humidity() # HTS221
        json_dict.append({"id":"humidity","val":hum,"type":"procent","sensor":"THS221"})
    elif humval == 'l': # Number 0 - 1
        hum = sense.get_humidity()/100 # HTS221
        json_dict.append({"id":"humidity","val":hum,"type":"liczba","sensor":"THS221"})

if presflag: # Pressure
    if presval == "hPa": # hPa
        press = sense.get_pressure() # LPS25H
        json_dict.append({"id":"pressure","val":press,"type":"hPa","sensor":"LPS25H"})
    elif presval == 'mmHg': # mmHg
        press = 0.75 * sense.get_pressure() # LPS25H
        json_dict.append({"id":"pressure","val":press,"type":"mmHg","sensor":"LPS25H"})
# #############################
#    ///     RPY     ///
# #############################
if rollflag: # R - roll
    if uflag == 1:
        roll = sense.get_accelerometer()["roll"] # LSM9DS1
        json_dict.append({"id":"roll","val":roll,"type":"deg","sensor":"LSM9DS1"})
    else:
        roll = sense.get_accelerometer()["roll"]* 0.0174532925 # LSM9DS1
        json_dict.append({"id":"roll","val":roll,"type":"rad","sensor":"LSM9DS1"})

if pitchflag: # P - pitch
    if uflag:
        pitch = sense.get_accelerometer()["pitch"] # LSM9DS1
        json_dict.append({"id":"pitch","val":pitch,"type":"deg","sensor":"LSM9DS1"})
    else:
        pitch = sense.get_accelerometer()["pitch"] * 0.0174532925 # LSM9DS1
        json_dict.append({"id":"pitch","val":pitch,"type":"rad","sensor":"LSM9DS1"})

if yawflag: # Y - yaw
    if uflag:
        yaw = sense.get_accelerometer() # LSM9DS1
        yaw = yaw["yaw"]
        json_dict.append({"id":"yaw","val":yaw,"type":"deg","sensor":"LSM9DS1"})
    else:
        yaw = sense.get_accelerometer() # LSM9DS1
        yaw = yaw["yaw"] * 0.0174532925
        json_dict.append({"id":"yaw","val":yaw,"type":"rad","sensor":"LSM9DS1"})

# #############################
#    ///     Magnetometer, Accelerometer     ///
# #############################
if magnetometer:
    mag = sense.get_compass_raw()
    json_dict.append({"id":"magnetometer_x","val":mag["x"],"type":"uT","sensor":"LSM9DS1"})
    json_dict.append({"id":"magnetometer_y","val":mag["y"],"type":"uT","sensor":"LSM9DS1"})
    json_dict.append({"id":"magnetometer_z","val":mag["z"],"type":"uT","sensor":"LSM9DS1"})

if accelerometer:
    accel = sense.get_accelerometer_raw()
    json_dict.append({"id":"linear_accel_x","val":accel["x"],"type":"G","sensor":"LSM9DS1"})
    json_dict.append({"id":"linear_accel_y","val":accel["y"],"type":"G","sensor":"LSM9DS1"})
    json_dict.append({"id":"linear_accel_z","val":accel["z"],"type":"G","sensor":"LSM9DS1"})

if gyroscope:
    gyr = sense.get_gyroscope_raw()
    json_dict.append({"id":"angular_accel_x","val":gyr["x"],"type":"radps","sensor":"LSM9DS1"})
    json_dict.append({"id":"angular_accel_y","val":gyr["y"],"type":"radps","sensor":"LSM9DS1"})
    json_dict.append({"id":"angular_accel_z","val":gyr["z"],"type":"radps","sensor":"LSM9DS1"})

# #############################
#    ///     Joystick     ///
# #############################
if joystick:
    with open("joystick.dat","r") as plik:
        joystick_position = json.loads(plik.read())
        json_dict.append({"id":"joystick_x","val":joystick_position["x"],"type":"position","sensor":"SKRHABE010"})
        json_dict.append({"id":"joystick_y","val":joystick_position["y"],"type":"position","sensor":"SKRHABE010"})
        json_dict.append({"id":"joystick_m","val":joystick_position["middle"],"type":"position","sensor":"SKRHABE010"})

#Print as json
print(json.dumps(json_dict))
for arg in opts:
    sysarg.remove(arg[0])
    if arg[1]:
        sysarg.remove(arg[1])

index = 1
for arg in sysarg:
    print('Non - option argument # ' , index , " = " , arg , sep = " ")
    index = index + 1
