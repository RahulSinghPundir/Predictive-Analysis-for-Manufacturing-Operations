import pandas as pd

from sklearn.tree import DecisionTreeRegressor

import pickle as pkl

model=DecisionTreeRegressor()

df=pd.read_csv('data.csv')
if('Unnamed: 0' in df.columns):
    df.drop("Unnamed: 0", axis=1, inplace=True)
df.dropna(inplace=True)
df['Downtime']=df['Downtime'].replace('Machine_Failure',1).replace('No_Machine_Failure',0)
y=df['Downtime']
x=df.drop('Downtime',axis=1)
model.fit(x,y)

with open('model.pkl','wb') as file:
    pkl.dump(model,file)