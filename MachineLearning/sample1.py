# Ejemplo de ML
# 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier

iris = pd.read_csv('iris.csv')          # Importamos el dataset.
X = iris[['PetalLength', 'PetalWidth']]
y = iris['Species'].astype('category')
y.cat.categories = [0, 1, 2]

n_neighbors = 15
h = .02          # step size de la malla
# Creamos los colormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

for weights in ['uniform', 'distance']:
    # Creamos una instancia de Neighbors Classifier y hacemos un fit a partir de los
    # datos.
    clf = KNeighborsClassifier(n_neighbors, weights=weights)
    clf.fit(X, y)


    x_min, x_max = X.iloc[:, 0].min() - 1, X.iloc[:, 0].max() + 1
    y_min, y_max = X.iloc[:, 1].min() - 1, X.iloc[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    plt.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap=cmap_bold)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.title("3-Class classification (k = %i, weights = '%s')"
              % (n_neighbors, weights))
    plt.xlabel('Petal Width')
    plt.ylabel('Petal Length')
    plt.savefig('iris-knn-{}'.format(weights))
