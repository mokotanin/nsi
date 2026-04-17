const jeu = {
  0: {
    t: "Choisissez la video de depart.",
    c: [
      { t: "Video 1", next: 1 },
      { t: "Video 2", next: 2 },
    ],
  },
  1: {
    t: "Vous regardez la premiere video.",
    video: "video.mp4",
    c: [
      { t: "Video 2", next: 2 },
      { t: "Video 3", next: 3 },
    ],
  },
  2: {
    t: "Vous regardez la deuxieme video.",
    video: "video2.mp4",
    c: [
      { t: "Video 1", next: 1 },
      { t: "Video 3", next: 3 },
    ],
  },
  3: {
    t: "Vous regardez la troisieme video.",
    video: "video3.mp4",
    c: [
      { t: "Video 1", next: 1 },
      { t: "Video 2", next: 2 },
    ],
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
  videoLecteur.muted = false
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
