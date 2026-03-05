<?php
	include("pipo.php");

	$conclusion ="";
	for ($i = 0; $i < 8; $i++) {
		$alea = rand(0,9);
		$conclusion = $conclusion . $pipo[$i][$alea];
	}
?>

<html>
	<head>
		<title>Le Pipotron</title>
	</head>
	<body>
		<h1>Le pipotron</h1>
		<?php echo($conclusion); ?>
	</body>
</html>