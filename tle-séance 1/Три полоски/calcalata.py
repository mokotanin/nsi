exp = " 26+1-"
pile = []
op1 = 0
op2 = 0

for c in exp:
    if c not in "+-*/":
        # chiffre
        pile.append(c)
    else:
        op1 = int(pile.pop())
        op2 = int(pile.pop())

        if c == "+":
            pile.append(op1 + op2)
        elif c == "*":
            pile.append(op1 * op2)
        elif c == "-":
            pile.append(op1 - op2)
        elif c == "/" and op2 != 0:
            pile.append(op1 / op2)
print(pile, "est la réponse")
