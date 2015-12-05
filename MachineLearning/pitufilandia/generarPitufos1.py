import random
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def creaDatos(archi, num):
    archi.write('X,Y,COLOR\n')
    for x in range(num):
        X = random.randrange(100)
        Y = random.randrange(100)
        archi.write(str(X))
        archi.write(',')
        archi.write(str(Y))
        archi.write(',')
        if (X > 50):
			if (Y > 50):
				archi.write('0\n')
			else:
				archi.write('20\n')
        else:
			if (Y <= 50):
				archi.write('10\n')
			else:
				archi.write('30\n')

archi=open('datos.csv','w')
creaDatos(archi, 100)
archi.close()

archi=open('test.csv','w')
creaDatos(archi, 10)
archi.close()

#Se importan los datos
pd = pd.read_csv('datos.csv')
X = pd.values[:,0:2] 
y = pd.values[:,2]

# Se presentan en una grafica
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.xlabel('X')
plt.ylabel('Y')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.title('Representacion de Pitufos')

plt.show()


