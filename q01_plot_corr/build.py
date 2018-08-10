# %load q01_plot_corr/build.py
# Default imports
import pandas as pd
from matplotlib.pyplot import yticks, xticks, subplots, set_cmap

data = pd.read_csv('data/house_prices_multivariate.csv')


# Write your solution here:
def plot_corr(data, size=11):
    corr = data.corr()
    fig, ax = subplots(figsize=(size, size))
    set_cmap('YlOrRd')
    ax.plot(corr)
    xticks( corr.columns, rotation=90)

    return ax

