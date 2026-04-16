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
    audioVolume: 0.35,
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
      { t: "Bien", next: 13 },
    ],
  },
  13: {
    t: "Vos réponses sont enregistrées",
    c: [
      { t: "Entendu", next: 18 },
      { t: "Et mes données ?", next: 16 },
    ],
  },
  12: {
    t: "これは現実じゃない。最初から存在していなかった。",
    c: [{ t: "???", next: 19 }],
    bg: "#59283e",
    border: "#ffc9c5",
    boxbg: "#b94562bd",
    music: "yume",
    // url: "./..png",
    action: () => {
      end3 = true;
    },
  },
  16: {
    t: "Vos données sont sécurisées et stockées sur les serveurs de la société hubiC, fournie par ██████.",
    c: [
      { t: "Compris", next: 18 },
      { t: "Cela me semble sûr", next: 18 },
      { t: "Et le RGPD ?", next: 17 },
    ],
  },
  17: {
    t: "Aucune loi n'est en vigueur à ██████.",
    bg: "#7c7c7c",
    boxbg: "#535353d8",
    border: "#c4c4c4",
    c: [{ t: "Ah...", next: 18 }],
    music: "vie_privee",
  },
  18: {
    t: "Merci pour votre compréhension. _w4x.2 peut à présent commencer.",
  },
  19: {
    t: "Vous avez trois choix.",
    get c() {
      return [
        ...(end1 ? [] : [{ t: "1", next: 100 }]),
        { t: "2", next: 200 },
        { t: "3", next: 12 },
      ];
    },
  },
  100: {
    t: "Insérer scénario 1",
    action: () => { end1 = true },
    c: { t: "yeu", next: 19}
  },
  200: {
    t: "Insérer scénario 2",
    action: () => { end2 = true },
    c: { t: "yeu", next: 19}
  },
};

let scenarioActuel = 0;
let badEnding9 = false;
let end1 = false;
let end2 = false;
let end3 = false;

const musiques = {
  intro: { src: "for_the_fans.mp3", volume: 0.05 },
  yume: { src: "きえない_きずあと.mp3", volume: 0.05 },
  vie_privee: { src: "どこかへつづくもり〜森の世界〜.mp3", volume: 0.1 },
};

const lecteurMusique = new Audio();
lecteurMusique.loop = true;

let musiqueCourante = null;
let audioDebloque = false;
let progressionInterval = null;
let progressionValeur = 0;
const volumeEffetsDefaut = 0.35;

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

function reinitialiserProgression() {
  if (progressionInterval) {
    clearInterval(progressionInterval);
    progressionInterval = null;
  }

  progressionValeur = 0;
  const barre = document.getElementById("bar");
  const container = document.getElementById("progressContainer");

  if (barre) {
    barre.style.width = "0%";
  }

  if (container) {
    container.style.display = "none";
    container.setAttribute("aria-hidden", "true");
  }
}

function demarrerProgressionScenario18() {
  const barre = document.getElementById("bar");
  const container = document.getElementById("progressContainer");
  if (!barre || !container) return;

  if (progressionInterval) return;

  container.style.display = "flex";
  container.setAttribute("aria-hidden", "false");
  barre.style.width = "0%";
  progressionValeur = 0;

  progressionInterval = setInterval(() => {
    progressionValeur += 25;

    if (progressionValeur >= 100) {
      progressionValeur = 100;
      barre.style.width = `${progressionValeur}%`;
      clearInterval(progressionInterval);
      progressionInterval = null;
      choix(19);
      return;
    }

    barre.style.width = `${progressionValeur}%`;
  }, 1500);
}

function afficherScenario() {
  const scenario = jeu[scenarioActuel];
  const storyDiv = document.getElementById("story");
  const buttonsDiv = document.querySelector(".buttons");

  if (scenario.action) {
    scenario.action();
  }

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
    audio.volume = scenario.audioVolume ?? volumeEffetsDefaut;
    audio.play();
  }

  // Si une musique existe
  if (scenario.music) {
    jouerMusique(scenario.music);
  }

  if (scenarioActuel === 18) {
    demarrerProgressionScenario18();
  } else {
    reinitialiserProgression();
  }

  const options = Array.isArray(scenario.c)
    ? scenario.c
    : scenario.c
      ? [scenario.c]
      : [];

  options.forEach((choixOption, index) => {
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
