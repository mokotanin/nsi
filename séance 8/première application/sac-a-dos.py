# Créé par csieg, le 28/11/2025 en Python 3.7
# Créé par csieg, le 21/11/2025 en Python 3.7

Valeurs=[[4,6],[6,7],[8,13],[12,16]] #declaration des objets


rapport=[]            # calcul des différent coefficient valeur /poids
for element in Valeurs:
    rapport.append(element[1]/element[0])
print(rapport)
ordre=[n for n in rapport] # copy de la liste rapport dans la liste ordre
rapport.sort()           #on a trie du + petit au + grand

rapport.reverse()        #on a maintenant la liste rapport classée du + grand au plus petit
                         #le classement ma faire perdre l'ordre des objets
                         #exemple le premier coeff ne correspond plus au premier objet de la
                         #liste Valeurs mais au 3eme d'indice 2
# on cherche a savoir maintenant en créant un tableau indice l'indice de la valeur
#qui corrspond a chaque coefficient classe du tableau rapport
indices=[]
for i in range(0,len(rapport)):# on veut lire chaque element des coefficient rapport qui sont classés
     for j in range(0,len(ordre)):#on veut lire chaque element des element rapport non classé
        if rapport[i]==ordre[j]: #pour retouver la poisiton d'origine des elements de la liste
            indices.append(j)

# La liste indice contient respectivement l'indice des element les plus interressant au moins interessant
print("valeurs",Valeurs)
print("rapport",rapport)
print("indice",indices)
