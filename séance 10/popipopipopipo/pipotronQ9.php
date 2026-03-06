<?php
    include("pipo.php");
    var_dump($_POST);
    if(isset($_POST["conclusion_no"])){
        $conclusion_no = $_POST["conclusion_no"];
    }
    function adapterliaison($str)
{$str=str_replace("de e","d'e",$str);
$str=str_replace("de é","d'é",$str);
$str=str_replace("de i","d'i",$str);
$str=str_replace("de a","d'a",$str);
return $str;}
    $conclusion="";
    for ($i = 0; $i < 8; $i++) {
    $alea = rand(0,9); 
    $conclusion=$conclusion. $pipo[$i][$alea];}
    $conclusion=adapterliaison($conclusion);

?>
<html>
    <head>
        <title>Le pipotron</title>
    </head>
    <body>
        <h1>Le pipotron</h1>
        <form method="post" action="pipotronQ6.php">
        <label>Entrer un nombre de 8 chiffres</label>
        <input name="conclusion_no" type="number" min="0" max="99999999"/>
        <input type="submit" value="Générer"/>
        </form>
        <?php
        echo($conclusion);
        ?>
    </body>
</html>