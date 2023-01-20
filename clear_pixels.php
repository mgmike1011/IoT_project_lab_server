<?php
/**
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   PHP script that executes python script that clears LED panel.
 ******************************************************************************
 */
$command = escapeshellcmd("sudo python3 clear_pixels.py");
$last_line = exec($command,$all_lines);