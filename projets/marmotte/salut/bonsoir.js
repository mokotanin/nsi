document.addEventListener("DOMContentLoaded", () => {
  document.addEventListener("click", (event) => {
    const link = event.target.closest("span");
    if (!link) return;

    const isMarmotte = link.textContent.trim() === "marmotte/";

    if (!isMarmotte) return;

    document.getElementById("folder2").innerText = "ça fonctionne !";
    document.getElementById("folder2").style.setProperty("--folder", "var(--file)")
    document.getElementById("folder2").closest("tr").querySelectorAll("td.detailsColumn")[0].textContent = "très petit fichier"
    document.getElementById("folder2").closest("tr").querySelectorAll("td.detailsColumn")[1].textContent = "très vieille date !"
  });
});
