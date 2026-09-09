def empiler(p, e):
    if p[0] == len(p):
        print(f"La pile {p} est pleine")
        return False

    else:
        p[p[0]] = e
        p[0] = p[0] + 1
        return True
