import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *

df_train = pd.read_csv('data/train.csv',sep = ',')
df_test = pd.read_csv('data/test.csv',sep = ',')
#df_train.head()

rand_state = 42
train_part = 0.8

###### №1
df_train = df_train.dropna()

x_train = df_train.drop(columns=['plata'])
y_train = df_train['plata']

model = get_fitted_model(x_train,y_train)
print(model.summary())



#print(df_train.isna().sum())
#print(df_test.isna().sum())






