import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import svm, datasets
from sklearn.externals import joblib
from numpy import *

#Se importan los datos
p = pd.read_csv('test.csv')
X_test = p.values[:,0:2] 
y_test = p.values[:,2]

#Cargamos la maquina
svc = joblib.load('maquinaSVM.pkl')

# Verificamos el acierto con el grupo de test
P = svc.predict(X_test)
print ('Porcentaje de Acierto:')
a = sum(P == y_test)
b = y_test.shape[0]
print (a)
print (b)
print (a*100/b)

