def depiler(p):
    if p[0] != 1:
        p[0] = p[0] - 1
        return p[p[0]]
    else:
        print("La pile est vide")

    print(depiler(p))
