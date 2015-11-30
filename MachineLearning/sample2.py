# Fuente: https://dlegorreta.wordpress.com/category/sobre-machine-learning/machine-learning-en-python/
# http://relopezbriega.github.io/blog/2015/06/27/probabilidad-y-estadistica-con-python/
#

# Ejemplos de estadistica descriptiva con python

import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt # importando matplotlib

np.random.seed(2131982) # para poder replicar el random

datos = np.random.randn(3, 2) # datos normalmente distribuidos
print (datos)

# media aritmetica
x = datos.mean() # Calcula la media aritmetica de
print (x)

x = datos.mean(axis=1) # media aritmetica de cada fila
print (x)

x = datos.mean(axis=0) # media aritmetica de cada columna
print (x)

# mediana
np.median(datos)
np.median(datos, 0) # media aritmetica de cada columna
 # Desviacion tipica
np.std(datos)

np.std(datos, 0)

# varianza
np.var(datos)
np.var(datos, 0) # varianza de cada columna
# moda
stats.mode(datos) # Calcula la moda de cada columna

# correlacion
np.corrcoef(datos)
np.corrcoef(datos[0], datos[1])
# covarianza
np.cov(datos) # calcula matriz de covarianza
# covarianza de dos vectores
np.cov(datos[0], datos[1])

