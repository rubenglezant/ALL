import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, datasets
from sklearn.externals import joblib
from numpy import *

print ('2.- Entrenamiento de la maquina super-lista')

#Se importan los datos
p = pd.read_csv('datos.csv')
X = p.values[:,0:2] 
y = p.values[:,2]

#Parametro de regularizacion
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, y)

# Entrenamos y guardamos
joblib.dump(clf, 'maquinaDTC.pkl')

print ('Algoritmo: tree.DecisionTreeClassifier')
print ('')


