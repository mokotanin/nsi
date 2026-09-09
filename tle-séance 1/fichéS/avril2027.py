urne1 = ["Balludur", "Giscard", "Macron"]
urne2 = ["Attal", "Bardella", "Macron"]
urne3 = ["Bardella", "LePen", "Zémour", "Attal"]


def scrutin(urne):
    global d
    d = {}
    for candidat in urne:
        if candidat in d:
            d[candidat] += 1
        else:
            d[candidat] = 1


scrutin(urne1)
scrutin(urne2)
scrutin(urne3)

print(d)
# ou pour un meilleur rendu
for nom, valeur in d.items():
    print(f"{nom}: {valeur}")
