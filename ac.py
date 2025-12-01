objet=[[4,6],[6,7],[8,13],[12,16]]

rapport=[]
for i in range (len(objet)):
    rapport.append(objet[i][1]/objet[i][0])
    # input("") pour tester l'évolution de la liste
    # print(rapport)
print(rapport)
rapport.sort()
rapport.reverse()
print(rapport)

for i in range(0,len(rapport)): 
        for j in range(0,len(rapport)): 
            if rapport[i]==ordre[j]: 
                indices.append(j)