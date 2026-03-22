function clic() {
  compteurClics++;
  document.getElementById("compteurClics").textContent = compteurClics;
}
var compteurClics = 0;
document.getElementById("clic").addEventListener("click", clic);
document.getElementById("desactiver").addEventListener("click", function () {
  document.getElementById("clic").removeEventListener("click", clic);
});
document.getElementById("reactiver").addEventListener("click", function () {
  document.getElementById("clic").addEventListener("click", clic);
});
