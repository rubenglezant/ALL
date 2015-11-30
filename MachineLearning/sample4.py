#Graficamos

#Importamos las librerias necesarias

from matplotlib import pyplot as plt
from sklearn.datasets import load_iris

#Cargamos los datos y graficamos

datos=load_iris()
caract=datos.data
caract_names=datos.feature_names
tar=datos.target

# Graficamos los datos con colores distintos y tipo de marcas distintos

for t, marca,c in zip(xrange(3),">ox","rgb"):
 plt.scatter(caract[tar==t,0],caract[tar==t,1],marker=marca,c=c)

plt.show()

