<?php
/**
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get LED data: gets all LED matrix info and prints it.
 ******************************************************************************
 */
$command = escapeshellcmd("sudo python3 get_led.py");
$last_line = exec($command, $all_lines);

foreach($all_lines as $line){
    print($line);
    print("<br>");
}