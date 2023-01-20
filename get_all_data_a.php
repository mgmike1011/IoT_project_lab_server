<?php
/**
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get all data automated: Gets the latest data from SenseHat using get_all_data_automated.py.
 ******************************************************************************
 */
$myfile = fopen("alldata.dat", "r") or die("Unable to open file!");
echo fread($myfile,filesize("alldata.dat"));
fclose($myfile);
