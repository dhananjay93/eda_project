# %load q03_regression_plot/build.py
# Default imports

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


dataframe = pd.read_csv('data/house_prices_multivariate.csv')
variable1 = 'GrLivArea'
variable2 = 'SalePrice'

# Write your code here
def regression_plot(variable1,variable2):
    sns.lmplot(variable1,variable2, data=dataframe, fit_reg=True)
    plt.show()
    






