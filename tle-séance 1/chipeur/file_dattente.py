def file(n):
    f = [None] * (n + 3)
    f[0] = 3  # indice premier élément
    f[1] = 3  # indice dernier élément (3 car elle est vide donc y'en a pas)
    f[2] = 0  # correspond à la taille
    return f
