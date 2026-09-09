def defiler(f):
    if f[2] == 0:
        print("La file est vide")
    else:
        e = f[f[0]]
        if f[0] == len(f) - 1:
            f[0] = 3
        else:
            f[0] = f[0] + 1
        f[2] = f[2] - 1
        return e

    print(defiler(f))
