<?php
$handle = @fopen("input.txt", "r");
$ass_array = array();
while (($buffer = fgets($handle)) !== false){
	$ass_array[] = explode(" ", $buffer);
}
$x = count($ass_array)- 1;
$new_row = $ass_array[$x];
while($x>0){
	$x--;
	$row = $ass_array[$x];
	$temp_arr = array();
	foreach($row as $key=>$value){
		$temp_arr[] = $new_row[$key] > $new_row[$key+1] ? $value + $new_row[$key] : $value + $new_row[$key+1];
	}
	$new_row = $temp_arr;
}
var_dump($new_row);
