/* choix du thème */
function changerTheme(event) {
  const theme = event.target.value;
  document.body.className = theme;
  localStorage.setItem("theme", theme);
}

function chargerTheme() {
  const theme = localStorage.getItem("theme") || "";
  document.body.className = theme;
  if (document.getElementById("theme-selector")) {
    document.getElementById("theme-selector").value = theme;
  }
}

const jeu = {
  0: {
    t: "Tu es dans une forêt. Que fais-tu ?",
    c: [
      { t: "Aller à gauche", next: 1 },
      { t: "Aller à droite", next: 2 },
    ],
  },
  1: {
    t: "Une maison apparaît ! Qu'est-ce que tu fais ?",
    c: [
      { t: "Entrer dans la maison", next: 3 },
      { t: "Continuer tout droit", next: 4 },
    ],
  },
  2: {
    t: "Tu trouves un trésor ! 💰 Bravo, tu as gagné !",
    c: [{ t: "Stylé", next: 5 }],
  },
  3: {
    t: "Tu as été attaqué par un ours ! 🐻 Jeu terminé.",
    c: [{ t: "Recommencer", next: 0 }],
  },
  4: {
    t: "Tu trouves une rivière et tu t'échappes. Tu as gagné ! 🎉",
    c: [{ t: "Recommencer", next: 0 }],
  },
  5: {
    t: "Et maintenant ?",
    c: [
      { t: "Marcher", next: 3 },
      { t: "Stop", next: 2 },
    ],
  },
};

let scenarioActuel = 0;

function choix(numeroScenario) {
  scenarioActuel = numeroScenario;
  afficherScenario();
}

function afficherScenario() {
  const scenario = jeu[scenarioActuel];
  const storyDiv = document.getElementById("story");
  const buttonsDiv = document.querySelector(".buttons");

  storyDiv.textContent = scenario.t;
  buttonsDiv.innerHTML = "";

  scenario.c.forEach((choixOption) => {
    const button = document.createElement("button");
    button.textContent = choixOption.t;
    button.onclick = () => choix(choixOption.next);
    buttonsDiv.appendChild(button);
  });
}

function toggleTheme() {
  const selector = document.getElementById("theme-selector");
  if (selector.style.display === "none") {
    selector.style.display = "block";
  } else {
    selector.style.display = "none";
  }
}

// Initialiser le jeu au chargement
window.onload = function () {
  chargerTheme();
  afficherScenario();
  const selector = document.getElementById("theme-selector");
  if (selector) {
    selector.addEventListener("change", changerTheme);
  }
};
