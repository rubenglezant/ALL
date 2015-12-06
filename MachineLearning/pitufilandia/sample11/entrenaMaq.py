import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, datasets, svm
from sklearn.externals import joblib
from numpy import *
from sklearn.cluster import KMeans

print ('2.- Entrenamiento de la maquina super-lista')
print ('-------------------------------------------')

#Se importan los datos
p = pd.read_csv('datos.csv')
X = p.values[:,0:2] 
y = p.values[:,2]

#Parametro de regularizacion


start_time = time.clock()
C = 1.0 
#clf = svm.SVC(kernel='linear', C=C)
#clf = svm.SVC(kernel='poly', C=C)
#clf = tree.DecisionTreeClassifier()
clf = KMeans(n_clusters=2, random_state=0)
clf = clf.fit(X, y)
print ('Tiempo entrenamiento: '+str(time.clock()-start_time)+' seg')

# Entrenamos y guardamos
joblib.dump(clf, 'maquinaDTC.pkl')

print ('Algoritmo: '+str(clf))
print ('')


