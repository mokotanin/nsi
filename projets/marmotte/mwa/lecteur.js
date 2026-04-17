const jeu = {
  0: {
    t: "vous êtes dans la campagne.",
    c: [{ t: "et ?", next: 1 }],
  },
  1: {
    t: "vous allez marcher.",
    video: "rg/video.mov",
    c: [{ t: "mhm...", next: 2 }],
  },
  2: {
    t: "vous trouvez un arbre pendant votre marche. vous voyez un trou dans la terre.",
    video: "rg/video3.mov",
    c: [{ t: "je regarde dedans", next: 3 }],
  },
  3: {
    t: "de long escaliers se trouvent dans ce trou",
    mute: true,
    c: [
      { t: "descendre", next: 4 },
      { t: "ne pas y descendre", next: 99999 },
    ],
  },
  4: {
    t: "ces escaliers sont très longs...",
    video: "rg/video4.mov",
    c: [{ t: "c'est suspect", next: 2 }],
  },
  5: {
    t: "et ils continuent",
    video: "rg/video5.mov",
    c: [{ t: "wow", next: 6 }],
  },
  6: {
    t: "une porte ???",
    video: "rg/video6.mov",
    c: [{ t: "ouvrir la porte", next: 7 }],
  },
  7: {
    t: "qu'est-ce que-",
    video: "rg/video7.mov",
    c: [{ t: "une salle délabrée", next: 8 }],
  },
  8: {
    t: "C'est fini. adieu. vos pensées seront retranscrites par ce texte.",
    video: "rg/video8.mov",
    c: [{ t: "entrez", next: 9 }],
  },
  9: {
    t: "en avançant encore, j'ai trouvé une demi grille qui donnait sur un bureau",
    video: "rg/video9.mov",
    c: [{ t: "ramper", next: 10 }],
  },
  10: {
    t: "c'est quand même fou de trouver un bureau dans cet endroit...",
    video: "rg/video10.mov",
    c: [{ t: "observer", next: 11 }],
  },
  11: {
    video: "rg/video11.mov",
    c: [{ t: "...", next: 12 }],
  },
  12: {
    video: "rg/video12.mov", //! fonctionnement pas testé
    c: [{ next: 13 }],
  },
  13: {
    t: "",
    video: "rg/video13.mov",
    c: [{ t: "avancer", next: 14 }],
  },
  14: {
    t: "...",
    video: "rg/video14.mov",
    c: [{ t: "ouvrir", next: 15 }],
  },
}

let scenarioActuel = 0
const volumeUniforme = 0.4
const transitionNoirMs = 240
let transitionEnCours = false

const videoLecteur = document.getElementById("locked-video")
const storyDiv = document.getElementById("story")
const buttonsDiv = document.querySelector(".buttons")
const playerDiv = document.querySelector(".player")
const experienceDiv = document.querySelector(".experience")

function optionsDuScenario(scenario) {
  return Array.isArray(scenario.c) ? scenario.c : scenario.c ? [scenario.c] : []
}

function afficherChoix(scenario) {
  experienceDiv.classList.remove("is-playing")
  experienceDiv.classList.remove("is-transitioning")
  experienceDiv.classList.toggle("is-menu", scenarioActuel === 0)
  const options = optionsDuScenario(scenario)
  buttonsDiv.innerHTML = ""

  options.forEach((choixOption, index) => {
    const button = document.createElement("button")
    button.id = "btn" + (index + 1)
    button.textContent = choixOption.t
    button.onclick = () => {
      const continuer = choixOption.action ? choixOption.action(button) : true
      if (continuer !== false) {
        choix(choixOption.next)
      }
    }
    buttonsDiv.appendChild(button)
  })
}

function cacherVideo() {
  playerDiv.classList.add("is-hidden")
  videoLecteur.pause()
  videoLecteur.removeAttribute("src")
  videoLecteur.load()
}

function transitionVersChoix(scenario) {
  if (transitionEnCours) {
    return
  }

  transitionEnCours = true
  experienceDiv.classList.add("is-transitioning")

  window.setTimeout(() => {
    cacherVideo()
    afficherChoix(scenario)

    window.requestAnimationFrame(() => {
      experienceDiv.classList.remove("is-transitioning")
      transitionEnCours = false
    })
  }, transitionNoirMs)
}

function lancerVideo(scenario) {
  if (!scenario.video) {
    cacherVideo()
    afficherChoix(scenario)
    return
  }

  experienceDiv.classList.remove("is-arming")
  experienceDiv.classList.add("is-playing")
  playerDiv.classList.remove("is-hidden")
  buttonsDiv.innerHTML = ""

  videoLecteur.onended = null
  videoLecteur.src = scenario.video
  videoLecteur.currentTime = 0
  videoLecteur.controls = false
  videoLecteur.muted = scenario.mute === true
  videoLecteur.volume = volumeUniforme
  videoLecteur.playsInline = true
  videoLecteur.load()

  const lecture = videoLecteur.play()
  if (lecture && typeof lecture.catch === "function") {
    lecture.catch(() => {
      buttonsDiv.innerHTML = ""
      const button = document.createElement("button")
      button.textContent = "Démarrer la vidéo avec le son"
      button.onclick = () => lancerVideo(scenario)
      buttonsDiv.appendChild(button)
    })
  }

  videoLecteur.addEventListener(
    "ended",
    () => {
      transitionVersChoix(scenario)
    },
    { once: true },
  )

  videoLecteur.addEventListener(
    "error",
    () => {
      buttonsDiv.innerHTML = ""
      const message = document.createElement("button")
      message.disabled = true
      message.textContent = "Vidéo introuvable ou illisible"
      buttonsDiv.appendChild(message)
    },
    { once: true },
  )
}

function afficherScenario() {
  const scenario = jeu[scenarioActuel]
  if (!scenario) {
    return
  }

  experienceDiv.classList.toggle("is-menu", scenarioActuel === 0 && !scenario.video)

  storyDiv.textContent = scenario.t

  if (scenario.bg) {
    document.documentElement.style.setProperty("--bodybg", scenario.bg)
  }

  if (scenario.border) {
    document.documentElement.style.setProperty("--border", scenario.border)
  }

  if (scenario.boxbg) {
    document.documentElement.style.setProperty("--boxbg", scenario.boxbg)
  }

  if (scenario.url) {
    document.documentElement.style.setProperty("--defaulturl", `url("${scenario.url}")`)
  } else {
    document.documentElement.style.setProperty("--defaulturl", "none")
  }

  if (scenario.action) {
    scenario.action()
  }

  lancerVideo(scenario)
}

function choix(numeroScenario) {
  scenarioActuel = numeroScenario
  afficherScenario()
}

window.addEventListener("load", afficherScenario)
