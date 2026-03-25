const jeu = {
  0: {
    t: "_w4x.2",
    c: [
      {
        get t() {
          return badEnding9 ? "Oubliez mes salutations..." : "Bonjour";
        },
        next: 1,
      },
    ],
  },
  1: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Non merci, je fais sans", next: 3 },
    ],
  },
  2: {
    t: "Voudriez-vous bien vérifier cela ?",
    c: [
      { t: "Oui", next: 7 },
      {
        t: "Non merci",
        action: (button) => {
          deplacerBouton(button);
          return false;
        },
      },
    ],
  },
  3: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Vous êtes sûr de vous ?", next: 4 },
    ],
  },
  4: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "Vraiment sûr ??", next: 5 },
    ],
  },
  5: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [
      { t: "J'ai augmenté le son", next: 2 },
      { t: "VRAIMENT SÛR ?", next: 6 },
    ],
  },
  6: {
    t: "Pour une expérience complète, montez le volume à environ 35%.",
    c: [{ t: "J'ai augmenté le son", next: 2 }],
  },
  7: {
    t: "Quel animal produit ce son ?",
    audio: "meu.mp3",
    c: [
      { t: "Un chat", next: 9 },
      { t: "Un orang-outan", next: 9 },
      { t: "Un canard", next: 9 },
      { t: "Une vache", next: 8 },
      { t: "Un mammouth", next: 9 },
    ],
  },
  8: {
    t: "Merci pour votre confiance.",
    music: "intro",
    bg: "#c4c4c4",
    boxbg: "#c6c6c6d8",
    border: "#c4c4c4",
    c: [{ t: "Avec plaisir", next: 10 }],
  },
  9: {
    t: "Vous mentez ?",
    c: [
      { t: "Oui", next: 3 },
      {
        t: "Non",
        next: 0,
        action: () => {
          badEnding9 = true;
        },
      },
    ],
  },
  10: {
    t: "Bienvenue dans _w4x.2",
    c: [
      { t: "Qu'est-ce donc cela ?", next: 11 },
      { t: "Intriguant...", next: 11 },
      { t: "Pas si surprenant", next: 12 },
    ],
  },
  11: {
    t: "Insérer explication.",
    c: [{ t: "D'accord", next: 13 }],
  },
  12: {
    t: "これは現実じゃない。最初から存在していなかった。",
    c: [{ t: "???", next: 14 }],
    bg: "#59283e",
    border: "#ffc9c5",
    boxbg: "#b94562bd",
    music: "yume",
    url: "./..png",
  },
};

let scenarioActuel = 0;
let badEnding9 = false;

const musiques = {
  intro: { src: "for_the_fans.mp3", volume: 0.05 },
  yume: { src: "きえない_きずあと.mp3", volume: 0.05},
};

const lecteurMusique = new Audio();
lecteurMusique.loop = true;

let musiqueCourante = null;
let audioDebloque = false;

function changerFond(couleur) {
  document.documentElement.style.setProperty("--bodybg", couleur);
}

function changerBordure(couleur) {
  document.documentElement.style.setProperty("--border", couleur);
}

function changerFondBoite(couleur) {
  document.documentElement.style.setProperty("--boxbg", couleur);
}

function changerFondImage(urll) {
  document.documentElement.style.setProperty("--defaulturl", `url("${urll}")`);
}

function debloquerAudio() {
  if (audioDebloque) return;
  audioDebloque = true;
}

function jouerMusique(id) {
  if (!id) return;
  if (musiqueCourante === id) return;

  const piste = musiques[id];
  if (!piste) return;

  musiqueCourante = id;
  lecteurMusique.src = piste.src;
  lecteurMusique.volume = piste.volume ?? 0.2;
  lecteurMusique.play().catch(() => {
    audioDebloque = false;
  });
}

function deplacerBouton(button) {
  button.style.position = "fixed";
  button.style.left = Math.random() * 80 + "vw";
  button.style.top = Math.random() * 80 + "vh";
}

function afficherScenario() {
  const scenario = jeu[scenarioActuel];
  const storyDiv = document.getElementById("story");
  const buttonsDiv = document.querySelector(".buttons");

  storyDiv.textContent = scenario.t;
  buttonsDiv.innerHTML = "";

  // Si un changement de fond existe
  if (scenario.bg) {
    changerFond(scenario.bg);
  }

  if (scenario.border) {
    changerBordure(scenario.border);
  }

  if (scenario.boxbg) {
    changerFondBoite(scenario.boxbg);
  }

  if (scenario.url) {
    changerFondImage(scenario.url);
  } else {
    document.documentElement.style.setProperty("--defaulturl", "none");
  }

  // Si un son existe
  if (scenario.audio) {
    const audio = new Audio(scenario.audio);
    audio.play();
  }

  // Si une musique existe
  if (scenario.music) {
    jouerMusique(scenario.music);
  }

  scenario.c.forEach((choixOption, index) => {
    const button = document.createElement("button");
    button.id = "btn" + (index + 1); // Simplicité pour sélectionner un bouton en CSS
    button.textContent = choixOption.t;
    button.onclick = () => {
      debloquerAudio();

      const continuer = choixOption.action ? choixOption.action(button) : true;
      if (continuer !== false) {
        choix(choixOption.next);
      }
    };
    buttonsDiv.appendChild(button);
  });
}

function choix(numeroScenario) {
  scenarioActuel = numeroScenario;
  afficherScenario();
}

// Initialiser le jeu au chargement
window.onload = afficherScenario;
