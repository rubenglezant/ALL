import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, datasets
from sklearn.externals import joblib
from numpy import *
from sklearn.metrics import classification_report

print ('3.- Resultados del vector de prueba')
print ('-----------------------------------')

#Se importan los datos
p = pd.read_csv('test.csv')
X_test = p.values[:,0:2] 
y_test = p.values[:,2]

#Cargamos la maquina
tree = joblib.load('maquinaDTC.pkl')

# Verificamos el acierto con el grupo de test
P = tree.predict(X_test)
print(classification_report(y_test, P))
print ('')

