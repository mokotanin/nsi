def supprimer(L, i):
    if (L[0] != 0) and (i <= L[0]):
        for k in range(i, L[0] - 1, -1):
            L[k] = L[k + 1]
        L[i] = None
        L[0] = L[0] - 1
        return True
    else:
        print(f"La liste {L} est vide ou l'index {i} n'est pas correct")
    return False
