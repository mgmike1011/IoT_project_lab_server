<?php
/**
 ******************************************************************************
 * @author  Miłosz Gajewski
 * @version V1.0
 * @date    01.2023
 * @brief   Set pixel: Executes the set_pixel.py, requires x y r g b params.
 ******************************************************************************
 */
$x=0; $y=0; $r=0; $g=0; $b=0;
if(isset($_GET['x']) And isset($_GET['y']) And isset($_GET['r']) And isset($_GET['g']) And isset($_GET['b'])){
    $x = (int)$_GET['x'];
    $y = (int)$_GET['y'];
    $r = (int)$_GET['r'];
    $g = (int)$_GET['g'];
    $b = (int)$_GET['b'];

    $arguments = " -x $x -y $y -r $r -g $g -b $b";
    $command = escapeshellcmd("sudo python3 set_pixel.py");
    $last_line = exec($command.$arguments,$all_lines);

    foreach($all_lines as $line){
        print($line);
        print("<br>");
    }
}else{
    print("Error: Not enough parameters.");
}