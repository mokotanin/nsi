def modifier(L, e, i):
    if i > L[0]:
        print("Il n'y a pas d'élément à cet indice")
        return False
    else:
        L[i] = e
        return True
