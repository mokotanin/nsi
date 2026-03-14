function persona(prenom,nom,age)
{
    this.prenom=prenom;
    this.nom=nom;
    this.age=age;
}
let nom = new persona("jean-jaques","hilst","480");
let paul=nom;
paul.prenom="paul";
alert(nom.prenom);