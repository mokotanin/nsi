def indexer(L, i):
    if i > L[0]:  # élimine le cas du None
        return "Il n'y a pas d'élément à cet indice"
    else:
        return L[i]
