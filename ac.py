#Exo 1
L=[4,7,12,3,9]
print(L[0],L[4])
L[1]=99
L[0], L[4] = L[4], L[0]

#Exo 2
print(L)
print([l for l in L if l % 2 == 0])
print([l for l in L if l>=10])

#Exo 3
notes = [12, 4, 18, 9, 13]
notes