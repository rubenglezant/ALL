# Ejemplos de estadistica descriptiva con python

import numpy as np
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt # importando matplotlib

np.random.seed(2131982) # para poder replicar el random

datos = np.random.randn(100, 2) # datos normalmente distribuidos
print (datos)

for i in range(100):
	datos[i,0] = i
	datos[i,1] = i*2

print (datos)

# correlacion
a = np.corrcoef(datos[0], datos[1])
print (a)

a = np.cov(datos[0], datos[1])
print (a)


	
	

