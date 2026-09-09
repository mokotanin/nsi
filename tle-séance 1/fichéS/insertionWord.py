def inserer(L, e, i):
    if (L[0] == len(L)) or (i - 1 > L[0]):
        print(f"La liste {L} est pleine ou {i} n'est pas correct")
        return False
    else:
        for k in range(L[0] + 1, i + 1, -1):
            L[k] = L[k - 1]
        L[i] = e
        L[0] += 1
    return True
