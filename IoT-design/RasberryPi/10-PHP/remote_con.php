<?php
    if(isset($_GET['LEDON'])){
        $value = shell_exec("home/pi/PHP/PHP_LEDON");
        echo $value;
    }else if(isset($_GET['LEDOFF'])){
        $value = shell_exec("home/pi/PHP/PHP_LEDOFF");
        echo $value;
    }
?>