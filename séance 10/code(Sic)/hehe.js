document.addEventListener("DOMContentLoaded", () => {
	const btn = document.getElementById("show-photo");
	const container = document.getElementById("photo-container");

	if (!btn || !container) {
		return;
	}

	btn.addEventListener("click", () => {
		const isVisible = container.classList.toggle("visible");
		container.setAttribute("aria-hidden", String(!isVisible));
		btn.textContent = isVisible ? "Masquer la photo" : "Sa photo";
	});
});
