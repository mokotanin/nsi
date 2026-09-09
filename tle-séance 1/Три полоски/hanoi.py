def hanoi(n, depart, arrivee, intermediaire):
    global compteur

    if n != 0:
        hanoi(n - 1, depart, intermediaire, arrivee)

        disque = depart.pop()
        arrivee.append(disque)

        compteur += 1
        print(p1, p2, p3)

        hanoi(n - 1, intermediaire, arrivee, depart)


p1 = []
p2 = []
p3 = []

n = int(input("Donner le nombre de disques : "))

for i in range(n, 0, -1):
    p1.append(i)

compteur = 0

print(p1, p2, p3)

hanoi(n, p1, p3, p2)

print(compteur)
