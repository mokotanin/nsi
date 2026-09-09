def vide(n):
    L = [None] * (n + 1)
    L[0] = 0
    return L


L = vide(6)
print(L)


def inserer(L, e, i):
    if L[0] == len(L):
        print(f"La liste {L} est pleine ou {i} n'est pas correct")
        return False
    else:
        for k in range(L[0] + 1, i + 1, -1):
            L[k] = L[k - 1]
            L[i] = e
            L[0] += 1
    return True


inserer(L, 3, 1)
inserer(L, 7, 2)
inserer(L, 1, 3)
inserer(L, 8, 4)

print(L)
