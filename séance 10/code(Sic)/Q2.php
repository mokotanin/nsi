<?php
// déclaration de constante
define('NSI', 'Numérique et Sciences Informatique');
// déclaration de variables
$nom = "Beltran";
$prenom = "Tristan";
$age = 17; // modifiez si nécessaire
?>
<html>
    <head>
        <meta charset="utf-8"/>
    <title>TP PHP NSI</title>
    </head>
    <body>
        <p>Je m'appelle <?php echo($prenom . " " . $nom); ?>.</p>
        <p>J'ai <?php echo($age); ?> ans.</p>
        <p>L'année prochaine, j'aurais <?php echo($age + 1); ?>.</p>
        <p>Je suis en cours de <?php echo(NSI); ?>.</p>
    </body>
</html>