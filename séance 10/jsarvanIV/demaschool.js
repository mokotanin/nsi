let noms=[];
let prenoms=[];
let notes=[];
let i=0;
noms[i]=prompt("Entrer le nom de l'élève");
while(noms[i]!="fin"){
    prenoms.push(prompt("Entrer le prénom de l'élève"))
    notes[i]=prompt("Entrer le nom de l'élève")
}
let moy=0.0
for (let j=0;j<prenoms.length;j++){
    document.getElementById("eleves").innerHTML+=noms[j]+'\t'+prenoms[j]+'\t'+notes[j]+' /20'+'<br>';
}
for (let valeur of notes){
    moy= Number(moy)+Number(valeur)
}
moy=moy/notes.length;
document.getElementById("moyenne").innerHTML='Moyenne de la classe = '+moy.toFixed(2)+' /20'