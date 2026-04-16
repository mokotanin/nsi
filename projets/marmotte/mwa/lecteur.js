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

function get(id) {
    return document.getElementById(id)
  }

function afficherChoix() {
    const vidFile = document.getElementById("video-file")
    const video = new VideoFrame()
    video.src = vidFile.src
}
