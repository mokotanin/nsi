def rechercher(L, e):
    indice = -1
    for k in range(1, L[0] + 1, 1):
        if L[k] == e:
            indice = k
    return indice
