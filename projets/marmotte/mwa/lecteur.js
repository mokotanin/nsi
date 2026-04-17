document.addEventListener("DOMContentLoaded", () => {
	const video = document.getElementById("locked-video");
	if (!video) {
		return;
	}

	let safeTime = 0;

	const forcePlay = () => {
		video.controls = false;
		video.muted = true;
		const playPromise = video.play();
		if (playPromise && typeof playPromise.catch === "function") {
			playPromise.catch(() => {
				// If autoplay is blocked by browser policy, it will retry on next allowed event.
			});
		}
	};

	const blockEvent = (event) => {
		event.preventDefault();
		event.stopPropagation();
		forcePlay();
	};

	document.addEventListener("keydown", blockEvent, true);
	document.addEventListener("keyup", blockEvent, true);
	document.addEventListener("keypress", blockEvent, true);

	[
		"click",
		"dblclick",
		"mousedown",
		"mouseup",
		"pointerdown",
		"pointerup",
		"touchstart",
		"touchend",
		"wheel",
		"contextmenu"
	].forEach((type) => {
		video.addEventListener(type, blockEvent, { capture: true, passive: false });
	});

	video.addEventListener("timeupdate", () => {
		safeTime = video.currentTime;
	});

	video.addEventListener("pause", forcePlay);

	video.addEventListener("seeking", () => {
		if (Math.abs(video.currentTime - safeTime) > 0.25) {
			video.currentTime = safeTime;
		}
	});

	forcePlay();
});

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
		c: { t: "yeu", next: 19 }
	},
	200: {
		t: "Insérer scénario 2",
		action: () => { end2 = true },
		c: { t: "yeu", next: 19 }
	},
};

function afficherScenario() {
	const scenario = jeu[scenarioActuel];
	const storyDiv = document.getElementById("story");
	const buttonsDiv = document.querySelector(".buttons");

	if (scenario.action) {
		scenario.action();
	}

	storyDiv.textContent = scenario.t;
	buttonsDiv.innerHTML = "";

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
