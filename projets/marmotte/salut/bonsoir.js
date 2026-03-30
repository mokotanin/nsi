//const isTrueFromB = typeof window.returnsTrueFromB === "function" && window.returnsTrueFromB()
//console.log("Boolean received in bonsoir.js:", isTrueFromB)

//const isTrueFromA = typeof window.returnsTrueFromA === "function" && window.returnsTrueFromA()
//console.log("Boolean received in bonsoir.js:", isTrueFromA)
 
function get(id) {
  return document.getElementById(id)
}

function taille(id, taille) {
  return (document.getElementById(id).closest("tr").querySelectorAll("td.detailsColumn")[0].textContent = taille)
}

function date(id, date) {
  return (document.getElementById(id).closest("tr").querySelectorAll("td.detailsColumn")[1].textContent = date)
}

function hide(dv) {
  const fileCell = document.querySelector(`td[data-value="${dv}"]`)
  const fileRow = fileCell?.closest("tr")

  if (fileCell) fileCell.classList.add("hidden-row")
  if (fileRow) fileRow.classList.add("is-hidden")
}

function show(dv) {
  const fileCell = document.querySelector(`td[data-value="${dv}"]`)
  const fileRow = fileCell?.closest("tr")

  if (fileCell) fileCell.classList.remove("is-hidden", "hidden-row")
  if (fileRow) fileRow.classList.remove("is-hidden")
}

function icon(id, type) {
  const allowed = ["dir", "file", "block", "unblock"]
  if (!allowed.includes(type)) return

  const span = document.getElementById(id)
  if (!span) return

  span.classList.remove(...allowed)
  span.classList.add(type)
}

function isSpan(link, id) {
  return !!link && link.id === id
}

function onParentClick() {
  const box = get("listingParsingErrorBox")
  const header = get("header")
  const table = document.querySelector("table")
  const tableBox = table?.closest("div")
  const parentText = get("parentDirText")

  if (header) header.style.display = ""
  if (tableBox) tableBox.style.display = ""
  if (box) box.style.display = "none"
  if (parentText) parentText.innerText = "[répertoire parent]"
  ;["folder1", "folder2", "folder3", "file1", "blockedFolder"].forEach(show)
  ;["folder4", "folder5", "folder6", "folder7", "folder8"].forEach(hide)

  icon("span1", "dir")
  icon("span2", "dir")
  icon("span3", "dir")
  icon("spanF", "file")
  icon("spanB", "block")

  const span2 = get("span2")
  if (span2) {
    span2.innerText = "morpion/"
    span2.style.removeProperty("--folder")
  }

  date("span2", "12/01/2026 19:04:15")
}

function text(title, content) {
  const box = get("listingParsingErrorBox")
  const header = get("header")
  const table = document.querySelector("table")
  const tableBox = table?.closest("div")
  const parentText = get("parentDirText")

  if (header) header.style.display = "none"
  if (tableBox) tableBox.style.display = "none"
  if (parentText) parentText.innerText = "[retour à l'index]"

  if (box) {
    box.style.display = "block"
    box.innerHTML = `
      <h2>${title}</h2>
      ${content}
    `
  }
}

document.addEventListener("DOMContentLoaded", () => {
  //? gèle la position des tables
  const table = document.querySelector("table")
  const headers = document.querySelectorAll("thead th")

  if (table && headers.length > 0) {
    const tableWidth = table.getBoundingClientRect().width
    const columnWidths = Array.from(headers, (th) => th.getBoundingClientRect().width)

    table.style.tableLayout = "fixed"
    table.style.width = `${tableWidth}px`

    document.querySelectorAll("tr").forEach((row) => {
      Array.from(row.children).forEach((cell, index) => {
        if (columnWidths[index]) {
          cell.style.width = `${columnWidths[index]}px`
        }
      })
    })
  }
})

document.addEventListener("click", (event) => {
  const target = event.target
  if (!(target instanceof Element)) return //sécurité

  const parentLink = target.closest("#parentDirLink")
  if (parentLink) {
    onParentClick()
    return
  }

  const link = target.closest("span")
  if (!link) return

  if (isSpan(link, "spanF")) {
    text(
      "Salut",
      `
      <p>Yop tt le monde jsuis papa (faux)</p>
      <p>Deuxieme ligne</p>
    `,
    )
    return
  }

  if (!isSpan(link, "span1")) return
  get("span2").innerText = "ça fonctionne !"
  get("span2").style.setProperty("--folder", "var(--file)")
  date("span2", "très vieille date !")
  hide("folder1")
  icon("span3", "block")
  show("folder6")
  show("folder7")
  show("folder8")
})
