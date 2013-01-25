<?php
$months = array(31,28,31,30,31,30,31,31,30,31,30,31);
$months_leap = array(31,29,31,30,31,30,31,31,30,31,30,31);
$sunday_start = 0;
$start_day = 1; // set monday as the start day 1900
$year = 1900;

function countyear ($leap = false){	
	global $year, $months, $months_leap, $sunday_start, $start_day;
	
	$month_array = ($leap == true)?$months_leap:$months;
	foreach ($month_array as $day_count){
        if($start_day == 0 && $year != 1900){
		$sunday_start++;     
	}

	$start_day = ($day_count%7)+$start_day;
	if($start_day > 6){
		$start_day = $start_day - 7;
	}
    }

}

while($year < 2001){
	       if($year % 4 == 0 && !(year % 100 == 0 && year % 400 != 0 )){
			countyear(true);
	       }else{
		       countyear();
	       }
	$year++;
}
echo($sunday_start);
