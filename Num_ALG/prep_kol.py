import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *
###### №1

df_train = pd.read_csv('data/train.csv',sep = ',')
df_test = pd.read_csv('data/test.csv',sep = ',')
#df_train.head()
alpha = 0.05 #из уровня доверия или 0.95 или 0.05 <--

df_train = df_train.dropna()
x_train = df_train.drop(columns=['plata'])
y_train = df_train['plata']

model = get_fitted_model(x_train,y_train)
print(model.summary())

x_test = df_test.drop(columns=['plata'])
y_test = df_test['plata']

test_rmse = get_rmse(model,x_test,y_test)
print(test_rmse)


##### 2
max, min = get_conf_interval(model,'zvanje',alpha)
print('min: ',min)
print('max: ',max)

print("надежность значений, когда нет автокореляции и остатки нормально распределены")
autokor,_ = independence_of_errors_assumption(model,sm.add_constant(x_train),y_train,plot = False)
if autokor is None:
    print ('ошибки независ (нет автокореляции)-> знач действ')
else:
    print('ошибки завис -> знач недейств')

if normality_of_errors_assumption(model,sm.add_constant(x_train),y_train,plot = False)[0]=='non-normal':
    print('остатки норм распред -> знач действ')
else:
    print('остатки не норм распред -> знач недейств')

#### 3
df_train = pd.read_csv('data/train.csv',sep = ',')
df_test = pd.read_csv('data/test.csv',sep = ',')

print(df_train.isnull().sum())

df_train['zvanje'] = df_train['zvanje'].interpolate(method='spline',order = 2,limit_direction='both')
df_train['godina_doktor'] = df_train['godina_doktor'].interpolate(method='spline',order = 2,limit_direction='both')

df_train = df_train.drop(columns=['pol Zenski','pol Muski'])

x = df_train.drop(columns=['plata'])
y = df_train['plata']
x_train,x_val,y_train,y_val = train_test_split(x,y,train_size=0.8,random_state=42,shuffle=True)


model2 = get_fitted_model(x_train,y_train)
print(model2.summary())

df_test['zvanje'] = df_test['zvanje'].interpolate(method='spline',order = 2,limit_direction='both')
df_test['godina_doktor'] = df_test['godina_doktor'].interpolate(method='spline',order = 2,limit_direction='both')

df_test = df_test.drop(columns=['pol Zenski','pol Muski'])
x_test = df_test.drop(columns=['plata'])
y_test = df_test['plata']

test_rmse_2 = get_rmse(model2,x_test,y_test)
print(test_rmse_2)
