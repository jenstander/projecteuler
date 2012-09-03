<?php
$handle = @fopen("input.txt", "r");
$tri_array = array();
while (($buffer = fgets($handle)) !== false){
	$tri_array[] = explode(" ", $buffer);
}
$x = count($tri_array)- 1;
$new_row = $tri_array[$x];
while($x>0){
	$x--;
	$row = $tri_array[$x];
	$temp_arr = array();
	foreach($row as $key=>$value){
		$temp_arr[] = $new_row[$key] > $new_row[$key+1] ? $value + $new_row[$key] : $value + $new_row[$key+1];
	}
	$new_row = $temp_arr;
}
var_dump($new_row);
