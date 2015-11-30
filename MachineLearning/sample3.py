# importanto la api de statsmodels
import statsmodels.formula.api as smf
import statsmodels.api as sm
import pandas as pd

# Creando un DataFrame de pandas.
df = pd.read_csv('http://vincentarelbundock.github.io/Rdatasets/csv/datasets/longley.csv', index_col=0)
df.head() # longley dataset

# utilizando la api de formula de statsmodels
est = smf.ols(formula='Employed ~ GNP', data=df).fit()
print (est.summary()) # Employed se estima en base a GNP.
