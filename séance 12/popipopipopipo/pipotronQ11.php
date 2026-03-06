<?php
	include("pipo.php");
	
	var_dump($_POST);
	if (isset($_POST['conclusion_no'])) {
		$str_no = $_POST['conclusion_no'];
	} else {
		$str_no = '00000000';
	}
	
	while (strlen($str_no) < 8) {
		$str_no = '0' . $str_no;
	}
	
	function adapterLiaison($str)
	{
		$str = str_replace(" de e", " d'e", $str);
		$str = str_replace(" de é", " d'é", $str);
		$str = str_replace(" de a", " d'a", $str);
		$str = str_replace(" de i", " d'i", $str);
		return $str;
	}
	
	// variable qui va contenir la conclusion à afficher
	$conclusion = ""; 
	for ($i = 0; $i < 8; $i++) {
		// $j <- premier caractère de $str_no converti en nombre (de 0 à 9)
		$j = intval($str_no[0]);
		// Supprimer le 1er caractère de $str_no
		$str_no = substr($str_no,1);
		// $conclusion <- $conclusion + $pipo[$i][$j]
		$conclusion .= $pipo[$i][$j];
	}
	
	$conclusion = adapterLiaison($conclusion);
?>

<htmp>
	<head>
		<title>Le pipotron</title>
	</head>
	<body>
		<h1>Le pipotron</h1>
		<form method="post" action="pipotronQ11.php">
			<label>Entrez un nombre de 8 chiffres</label>
			<input name="conclusion_no" type="number" min="0" max ="99999999"/>
			<input type="submit" value="Générer" />
		</form>
		<?php echo($conclusion); ?>
	<body>
<html>
