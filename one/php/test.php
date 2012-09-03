<?

$x=3;
$z=0;

while($x<1000){
  if(is_int($x/3) || is_int($x/5)){
    $z += $x;
  }
  $x++;
}
print $z;
?>
