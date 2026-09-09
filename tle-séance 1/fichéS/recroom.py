# fonction récursive
def fact(N):
    # arrêt -> if N==1: return 1
    return N * fact(N - 1)


# liste
L = [1, 2, 3]
L2 = L  # la même fonction : quand L modifiée, L2 modifiée (vice versa)
L3 = L[:]  # indépendante
