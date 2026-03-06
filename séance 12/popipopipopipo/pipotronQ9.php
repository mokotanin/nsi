<?php
include("pipo.php");
function adapterliaison($str)
{
	$str = str_replace("de e", "d'e", $str);
	$str = str_replace("de é", "d'é", $str);
	$str = str_replace("de i", "d'i", $str);
	$str = str_replace("de a", "d'a", $str);
	return $str;
}


$conclusion = "";
for ($i = 0; $i < 8; $i++) {
	$alea = rand(0, 9);
	$conclusion = $conclusion . $pipo[$i][$alea];
}
$conclusion = adapterliaison($conclusion)

?>
<html>

<head>
	<title> le pipotron </title>
</head>

<body>
	<h1> Le pipotron </h1>
	<?php
	echo ($conclusion);
	?>
</body>

</html>