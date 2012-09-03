<?php

function getlargestdev($nummm){
  $x = ceil($nummm/2);
  while($x > 2){
	$x--;
	if($nummm % $x == 0){
	  getlargestdev($nummm/$x);
	  getlargestdev($x);
	  return;
	}
   }
   print("Prime? $nummm");
}
//getlargestdev(600851475143);
tryagain(array(555555555,1));

function tryagain($bothnums){
	$xtest = true;
	$ytest = true;
	$x = ceil($bothnums[0]/2);
	$y = ceil($bothnums[1]/2);
  while($x > 2){
	$x--;
	if($bothnums[0] % $x == 0){
		tryagain(array($bothnums[0]/$x, $x));
		$xtest = false;
	}
  }
  while($y > 2){
	$y--;
	if($bothnums[1] % $y == 0){
 		tryagain(array($bothnums[1]/$y, $y));
		$ytest = false;
	}
  }
  if($ytest == true){
 	echo("Prime: {$bothnums[1]}");
  }
  if($xtest == true){
	echo("Prime: {$bothnums[0]}");
  }
}
?>
