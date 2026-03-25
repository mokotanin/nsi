const jeu = {
  0: {
    t: "_w4x.2",
    c: [{ t: "Bonjour", next: 1 }],
  },
  1: {
    t: "Pour une expérience complète, montez le volume.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Non merci, je fais sans", next: 3 },
    ],
  },
  2: {
    t: "Voudriez-vous bien vérifier cela ?",
    c: [
      { t: "Oui", next: 7 },
      { t: "Non merci", next: 8 /* bouger le bouton partout */},
    ],
  },
  3: {
    t: "Pour une expérience complète, montez le volume.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Vous êtes sûr de vous ?", next: 4 },
    ],
  },
  4: {
    t: "Pour une expérience complète, montez le volume.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Vraiment sûr ??", next: 5 },
    ],
  },
  5: {
    t: "Pour une expérience complète, montez le volume.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "VRAIMENT SÛR ?", next: 6 },
    ],
  },
  6: {
    t: "Pour une expérience complète, montez le volume.",
    c: [{ t: "J'ai augmenté le son", next: 2 }],
  },
  7: {
    t: "Quel animal produit ce son ?",
    c: [
      { t: "Un chat", next: 9 },
      { t: "Un orang-outan", next: 9 },
      { t: "Un canard", next: 9 },
      { t: "Une vache", next: 10 },
      { t: "Un mammouth", next: 9 },
    ],
  },
  9: {
    t: "Vous mentez ?",
    c: [
      { t: "Oui", next: 3 },
      { t: "Non", next: 0 },
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

// Initialiser le jeu au chargement
window.onload = afficherScenario;
