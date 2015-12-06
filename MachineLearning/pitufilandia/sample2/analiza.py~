import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from numpy import *

#Se importan los datos
#iris = datasets.load_iris()
pd = pd.read_csv('datos.csv')
iris = pd.values
print (iris)

X = iris[:,0:2] 
y = iris[:,2]
#print (X)

#Se importan los datos
#iris = datasets.load_iris()
#X = iris.data[:, :2] 
#y = iris.target

print (pd)
print (X)
print (y)

h = .02

#Parametro de regularizacion
C = 1.0 

svc = svm.SVC(kernel='linear', C=C).fit(X, y)
rbf_svc = svm.SVC(kernel='rbf', gamma=0.7, C=C).fit(X, y)
poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(X, y)
lin_svc = svm.LinearSVC(C=C).fit(X, y)

#Probe pero no me gusto el resultado con sigmoid
#sigmoid_svc=svm.SVC(kernel='sigmoid').fit(X,y)

x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),np.arange(y_min, y_max, h))

#Titulos para las graficas
titles = ['SVC con kernel lineal',
 'Lineal SVC',
 'SVC con RBF kernel',
 'SVC con polinomio(grado 3) kernel']


for i, clf in enumerate((svc,lin_svc, rbf_svc, poly_svc)):
 # Se grafican las fronteras 
 plt.subplot(2, 2, i + 1)
 plt.subplots_adjust(wspace=0.4, hspace=0.4)

 Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

 #Color en las graficas
 Z = Z.reshape(xx.shape)
 plt.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.8)

 #Puntos de entrenamiento
 plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
 plt.xlabel('Longitud Sepal')
 plt.ylabel('Peso Sepal')
 plt.xlim(xx.min(), xx.max())
 plt.ylim(yy.min(), yy.max())
 plt.xticks(())
 plt.yticks(())
 plt.title(titles[i])

plt.show()


