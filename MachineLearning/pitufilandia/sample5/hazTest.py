import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree, datasets
from sklearn.externals import joblib
from numpy import *

print ('3.- Resultados del vector de prueba')

#Se importan los datos
p = pd.read_csv('test.csv')
X_test = p.values[:,0:2] 
y_test = p.values[:,2]

#Cargamos la maquina
tree = joblib.load('maquinaDTC.pkl')

# Verificamos el acierto con el grupo de test
P = tree.predict(X_test)
a = sum(P == y_test)
b = y_test.shape[0]

print ('Porcentaje de Acierto :'+str(a)+' / ' +str(b)+ ' => ' + str(float(a)/float(b)))

# PROBAR INET
#test_score = tree.score(X_test)
#print (test_score)

print ('')

