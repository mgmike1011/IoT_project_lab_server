<?php
/**
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Get led data from file.
 ******************************************************************************
 */
$myfile = fopen("leddata.dat", "r") or die("Unable to open file!");
echo fread($myfile,filesize("alldata.dat"));
fclose($myfile);