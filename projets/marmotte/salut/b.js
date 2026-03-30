function returnsTrueFromB() {
  return typeof window.returnsTrueFromA === "function" && window.returnsTrueFromA()
}

window.returnsTrueFromB = returnsTrueFromB
