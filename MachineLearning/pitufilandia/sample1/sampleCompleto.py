__author__ = 'ruben'

from sklearn import datasets
boston = datasets.load_boston()
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

def plot_feature(feature):
    f = (boston.feature_names == feature)
    plt.scatter(boston.data[:,f], boston.target, c='b', alpha=0.3)
    plt.plot(boston.data[:,f], boston.data[:,f]*lr.coef_[f] + lr.intercept_, 'k')
    plt.legend(['Predicted value', 'Actual value'])
    plt.xlabel(feature)
    plt.ylabel("Median value in $1000's")
    plt.show();

lr = LinearRegression(normalize=True)
lr.fit(boston.data, boston.target)

plot_feature('AGE')

