let nb = prompt("Entrer la numerooooooooooooo de la table de MULT1pL11c4110n que vous souhaitez afficher:");
document.getElementById("tab").innerText =
  "La table de multiplication de  " + nb + " est : ";
let resultat_a_afficher = "";
for (let i = 1; i <= 10; i++) {
  resultat_a_afficher =
    resultat_a_afficher + i + " * " + nb + " = " + i * nb + "\n";
}
document.getElementById("resultat").innerText = resultat_a_afficher;
