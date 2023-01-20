<?php
/**
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get all data standard: Gets the latest data from SenseHat using get_all_data.py.
 ******************************************************************************
 */
$arguments = " -t C -h p -p hPa -r -i -y -m -a -g -j";
$command = escapeshellcmd("sudo python3 get_all_data.py");
$last_line = exec($command.$arguments, $all_lines);

foreach($all_lines as $line){
    print($line);
    print("<br>");
}