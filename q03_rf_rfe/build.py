# %load q03_rf_rfe/build.py
# Default imports
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier


# Your solution code here

def rf_rfe(df):
    X=df.drop('SalePrice',axis=1)
    y=df.SalePrice
    model=RandomForestClassifier()
    rfe=RFE(model)
    rfe=rfe.fit(X,y)
    
    a=pd.DataFrame()
    a['rank']=rfe.ranking_
    a['columns']=data.drop('SalePrice',axis=1).columns
    result=(a.sort_values('rank')['columns'].head(int(a.shape[0]/2)))
    result.sort_index(inplace=True)
    
    return result.tolist()


