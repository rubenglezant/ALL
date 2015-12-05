#Importamos las librerias necesarias

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd

#Cargamos los datos y graficamos
datos=load_iris()
dat=datos.data
caract_names=datos.feature_names
tar=datos.target

pd = pd.read_csv('datos.csv')
iris = pd.values

#dat = iris[:,1:3] 
dat = iris[:,0:2] 

print (dat)

# Calculamos lo mismo mediante la libreria scikit-lean
KM=KMeans(init='random',n_clusters=2).fit(dat)

#Extraemos las medias
L=KM.cluster_centers_

#Extraemos los valores usados para los calculos
Lab=KM.labels_

#Generamos las grafica
plot3= plt.scatter(dat[:,0], dat[:,1], c=Lab, alpha=0.75)
#Agregamos las Medias a las graficas
plot4= plt.scatter(L[:,0], L[:,1],c=[1,2], s=128, marker='d')
#Mostramos la grafica con los dos calculos
plt.show() 


