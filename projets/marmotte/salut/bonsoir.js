function get(id) {
  return document.getElementById(id)
}

function taille(id, taille) {
  return (document
    .getElementById(id)
    .closest("tr")
    .querySelectorAll("td.detailsColumn")[0].textContent = taille)
}

function date(id, date) {
  return (document
    .getElementById(id)
    .closest("tr")
    .querySelectorAll("td.detailsColumn")[1].textContent = date)
}

function hide(dv) {
  const fileRow = document.querySelector(`td[data-value="${dv}"]`)?.closest("tr")

  if (fileRow) fileRow.classList.add("is-hidden")
}

function show(dv) {
  const fileRow = document.querySelector(`td[data-value="${dv}"]`)?.closest("tr")

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

function parent() {
  const link = target.closest("span")
  if (!link) return
  const isParentLinkClick =
    isSpan(link, "parentDirLink") ||
    isSpan(link, "parentDirText") ||
    !!link.closest("#parentDirLink")

  if (isParentLinkClick) {
    show("folder1")
    show("folder2")
    show("folder3")
    show("file1")
    show("blockedFolder")
    hide("folder4")
    hide("folder5")
    hide("folder6")
    hide("folder7")
    hide("folder8")
    return
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
  if (!(target instanceof Element)) return

  parent

  const link = target.closest("span")
  if (!link) return

  if (!isSpan(link, "span1")) return
  get("span2").innerText = "ça fonctionne !"
  get("span2").style.setProperty("--folder", "var(--file)")
  taille("span2", "80 Mb")
  date("span2", "très vieille date !")
  hide("folder1")
  icon("span3", "file")
})
