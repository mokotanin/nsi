expression = input("creez votre formule")


def verification(expresion):
    global pile
    pile = []
    for car in expression:
        if car == "(":
            pile.append(car)
        elif car == ")":
            if len(pile) == 0:
                return False
            else:
                pile.pop()
    return len(pile) == 0
