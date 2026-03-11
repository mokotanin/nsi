let prenom = "Zoé", nom = "Dollé";
let age = 17;
let anniversaire = "30 juillet"
let homme = true;
let sexe = "un homme"
let n = null;
let u = undefined;
let na = NaN;
let v = "";
let heure = prompt("Heure entière")
//let adresse = prompt("Merci de taper votre adresse :")
//let x = prompt("x")
//let y = prompt("y")
//alert("Je m'appelle " + prenom + " " + nom);
//alert("J'ai " + age + " ans et l'année prochaine j'aurai " + (age+1) + " ans le " + anniversaire)
//alert("IMAGINE t'habite au " + adresse)

if (heure>0 && heure<12)
    alert("c'est la matin")
else if (heure>12 && heure<18)
    alert("c'est l'après-midi")
else if (heure>18)
    alert("c'est le soir")
else if (heure<0 && heure>24)
    alert("invalide (ET PAS LA RUE HAHAHAHAHAHAHA")