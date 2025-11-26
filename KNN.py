import pandas
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
iris=pandas.read_csv("iris.csv")
x=iris.loc[:,"petal_length"]  
y=iris.loc[:,"petal_width"]  
lab=iris.loc[:,"species"]  
plt.scatter(x[lab == 0], y[lab == 0], color='g', label='setosa')  
plt.scatter(x[lab == 1], y[lab == 1], color='r', label='virginica')  
plt.scatter(x[lab == 2], y[lab == 2], color='b', label='versicolor')  
plt.scatter(2.5, 0.75, color='k')
plt.legend()  
d=list(zip(x,y))
k=2
model=KNeighborsClassifier(n_neighbors=k)
model.fit(d,lab)

longueur=2.5
largeur=0.75
prediction=model.predict([[longueur,largeur]])
#Affichage résultats 
txt="Résultat : " 
if prediction[0]==0: 
  txt=txt+"setosa" 
if prediction[0]==1: 
  txt=txt+"virginica" 
if prediction[0]==2: 
  txt=txt+"versicolor" 
plt.text(3,0.5,"largeur : {0} cm, longueur : {1} cm.".format(largeur,longueur),fontsize=12) 
plt.text(3,0.3, "k : {0}".format(k), fontsize=12) 
plt.text(3,0.1, txt, fontsize=12) 
#fin affichage résultats
plt.show()