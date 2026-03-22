let canvas = document.getElementById("c1"); // récupère le canvas
let ctx = canvas.getContext("2d"); // accès au contexte

// Rectangle contour
ctx.strokeStyle = "red";
ctx.strokeRect(20, 10, 200, 100);

// Rectangle rempli
ctx.fillStyle = "rgba(0,0,255,0.3)";
ctx.fillRect(20, 120, 200, 100);

// Effacer zone
ctx.clearRect(100, 50, 100, 100);

// Triangle vert
ctx.beginPath();
ctx.moveTo(20, 250);
ctx.lineTo(20, 350);
ctx.lineTo(120, 350);
ctx.lineTo(20, 250);
ctx.strokeStyle = "#00FF00";
ctx.lineWidth = 3;
ctx.closePath();
ctx.stroke();

// Ligne noire
ctx.beginPath();
ctx.moveTo(140, 250);
ctx.lineTo(140, 350);
ctx.strokeStyle = "black";
ctx.lineWidth = 3;
ctx.closePath();
ctx.stroke();

// Triangle rempli jaune
ctx.beginPath();
ctx.moveTo(160, 350);
ctx.lineTo(260, 350);
ctx.lineTo(260, 250);
ctx.lineTo(160, 350);
ctx.fillStyle = "yellow";
ctx.closePath();
ctx.fill();

// Arc cyan (sens horaire)
ctx.beginPath();
ctx.strokeStyle = "cyan";
ctx.lineWidth = 5;
ctx.arc(60, 420, 35, 0.8 * Math.PI, 2 * Math.PI);
ctx.closePath();
ctx.stroke();

// Arc cyan (sens trigo)
ctx.beginPath();
ctx.strokeStyle = "cyan";
ctx.lineWidth = 5;
ctx.arc(260, 420, 35, 0.2 * Math.PI, Math.PI, true);
ctx.closePath();
ctx.stroke();

// Cercle magenta
ctx.beginPath();
ctx.fillStyle = "magenta";
ctx.arc(160, 480, 40, 0, 2 * Math.PI);
ctx.closePath();
ctx.fill();

// Arc rouge
ctx.beginPath();
ctx.fillStyle = "red";
ctx.lineWidth = 5;
ctx.arc(160, 500, 100, 0.2 * Math.PI, 0.8 * Math.PI);
ctx.closePath();
ctx.fill();

// Dégradé linéaire
let lineaire = ctx.createLinearGradient(20, 600, 120, 700);
lineaire.addColorStop(0, "green");
lineaire.addColorStop(0.5, "blue");
lineaire.addColorStop(1, "red");

ctx.beginPath();
ctx.moveTo(20, 600);
ctx.lineTo(20, 700);
ctx.lineTo(120, 700);
ctx.lineTo(20, 600);
ctx.fillStyle = lineaire;
ctx.closePath();
ctx.fill();

// Dégradé radial
let radial = ctx.createRadialGradient(200, 650, 5, 200, 650, 50);
radial.addColorStop(0, "yellow");
radial.addColorStop(0.5, "magenta");
radial.addColorStop(1, "cyan");

ctx.beginPath();
ctx.fillStyle = radial;
ctx.arc(200, 650, 50, 0, 2 * Math.PI);
ctx.closePath();
ctx.fill();

// Texte
ctx.font = "italic 30px Arial";
ctx.fillStyle = "black";
ctx.fillText("Exemple de dessins en Javascript", 10, 750);
