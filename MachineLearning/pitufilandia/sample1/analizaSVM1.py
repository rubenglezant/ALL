import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from numpy import *

#Se importan los datos
pd = pd.read_csv('datos.csv')
iris = pd.values
print (iris)

X = iris[:,0:2] 
y = iris[:,2]

print (pd)
print (X)
print (y)

#Parametro de regularizacion
C = 1.0 
h = .02

svc = svm.SVC(kernel='linear', C=C).fit(X, y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))

Z = svc.predict(np.c_[xx.ravel(), yy.ravel()])

#Color en las graficas
Z = Z.reshape(xx.shape)
plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

#Puntos de entrenamiento
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())
plt.xticks(())
plt.yticks(())
plt.title('SVC con kernel Lineal')

plt.show()


