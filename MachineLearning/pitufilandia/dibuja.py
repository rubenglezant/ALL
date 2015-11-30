import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.neighbors import KNeighborsClassifier

matplotlib.style.use('ggplot')

pd = pd.read_csv('datos.csv')
pdA = pd[(pd['COLOR']==0)]
pdR = pd[(pd['COLOR']==1)]

plt.scatter(pdA['X'],pdA['Y'],marker="o",c="b")
plt.scatter(pdR['X'],pdR['Y'],marker="o",c="r")



plt.show()




