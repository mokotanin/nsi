def enfiler(f, e):
    if f[2] == len(f) - 3:
        print(f"La file {f} est pleine")
        return False
    else:
        f[f[1]] = e
        if f[1] == len(f) - 1:
            f[1] = 3
        else:
            f[1] = f[1] + 1
        f[2] = f[2] + 1
        return True
