<?php
	include("pipo.php");
	
	function adapterLiaison($str)
	{
		//
		// ici on modifie $str, à compléter
		//
		return $str;
	}
	
	// variable qui va contenir la conclusion à afficher
	$conclusion = ""; 
	for ($i = 0; $i < 8; $i++) {
		// génération d'un nombrea aléatoire
		$alea = ...
		// construction de la conclusion
		$conclusion = ...
	}
	
	// on utilise la fonction adapterLiaison() pour supprimer le problème de liaison
	$conclusion = ... 
?>

<htmp>
	<head>
		<title>Le pipotron</title>
	</head>
	<body>
		<h1>Le pipotron</h1>
		<?php echo($conclusion); ?>
	<body>
<html>
