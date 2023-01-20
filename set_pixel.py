#!/usr/bin/python3
"""
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Set pixel: Sets the pixel on LED matrix - require x y r g b params.
 ******************************************************************************
"""
import sys
import getopt
from sense_emu import SenseHat
import json

sense = SenseHat()

xflag = 0
xval = 0
yflag = 0
yval = 0
rflag = 0
rval = 0
gflag = 0
gval = 0
bflag = 0
bval = 0

json_dict = {}

sysarg = sys.argv[1:]

try:
    opts, args = getopt.getopt(sysarg,':x:y:r:g:b:')
except getopt.GetoptError as err:
    print(err)
    sys.exit(1)

for opt, arg in opts:
    if opt in '-x':
        xflag = 1
        xval = int(arg)
    elif opt in '-y':
        yflag = 1
        yval = int(arg)
    elif opt in '-r':
        rflag = 1
        rval = int(arg)
    elif opt in '-g':
        gflag = 1
        gval = int(arg)
    elif opt in '-b':
        bflag = 1
        bval = int(arg)

json_dict.update({"x":xval})
json_dict.update({"y":yval})
json_dict.update({"r":rval})
json_dict.update({"g":gval})
json_dict.update({"b":bval})

sense.set_pixel(xval,yval,rval,gval,bval)
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
