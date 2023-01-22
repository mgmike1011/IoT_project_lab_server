#!/bin/sh
###
#******************************************************************************
# * @author  Miłosz Gajewski
# * @version V1.0
# * @date    01.2023
# * @brief   Bash script for initializing daemons.
# ******************************************************************************
###
sense_emu_gui &
python3 /home/pi/server/IoT/joystick_data.py &
python3 /home/pi/server/IoT/get_all_data_automated.py &
echo "Server ready!";