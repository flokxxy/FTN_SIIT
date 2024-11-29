import pandas as pd
from scipy.stats import median_test
from sklearn.model_selection import train_test_split
from statsmodels.tools import add_constant
from utils_nans1 import *


###1
df_train = pd.read_csv('data_C2/train.csv',sep =',')
df_test = pd.read_csv('data_C2/test.csv',sep = ',')

alpha = 0.05

df_train = df_train.dropna()
x_train = df_train.drop(columns = ['AirPollution'])
y_train = df_train['AirPollution']

print(df_train.head())

model = get_fitted_model(x_train,y_train)
print(model.summary())

x_test = df_test.drop(columns=['AirPollution'])
y_test = df_test['AirPollution']
test_r = get_rsquared_adj(model,x_test,y_test)
print("metriks = ",test_r)

### 2
min, max = get_conf_interval(model,'TrafficDensity',alpha)
print(f"Max: {max:.2f}")
print(f"Min: {min:.2f}")
autocorrelation,_ = independence_of_errors_assumption(model,add_constant(x_train),y_train,plot = False)

if autocorrelation is None:
    print ('ошибки независимы (знач действ)')
else:
    print('ошибки зависимы (значения не действ)')

if normality_of_errors_assumption(model,add_constant(x_train),y_train,plot = False)[0] == 'non-normal':
    print('ошибка норм распределения (значения действ)')
else:
    print('ошибки не норм распред (знач недейств)')


##### 3
df_train = pd.read_csv('data_C2/train.csv',sep =',')


print(df_train.isnull().sum())
df_train['TrafficDensity']=df_train['TrafficDensity'].interpolate(method='spline',order =2,limit_direction='both')
df_train['GreenSpace']=df_train['GreenSpace'].interpolate(method='spline',order =2,limit_direction='both')

df_train=df_train.drop(columns=['WindSpeed','Temperature','GreenSpace','Wind'])


x_train = df_train.drop(columns = ['AirPollution'])
y_train = df_train['AirPollution']

x_train,x_val,y_train,y_val = train_test_split(x_train,y_train,train_size=0.9,random_state=42,shuffle=True)

model = get_fitted_model(x_train,y_train)
print(model.summary())

df_test = pd.read_csv('data_C2/test.csv',sep = ',')
df_test['TrafficDensity']=df_test['TrafficDensity'].interpolate(method='spline',order =2,limit_direction='both')
df_test['GreenSpace']=df_test['GreenSpace'].interpolate(method='spline',order =2,limit_direction='both')

df_test=df_test.drop(columns=['WindSpeed','Temperature','GreenSpace','Wind'])
x_test = df_test.drop(columns = ['AirPollution'])
y_test = df_test['AirPollution']

test_r2 = get_rsquared_adj(model,x_test,y_test)
print(test_r2)



#### 4
#для чего используется т-тест?
#т-тест проверяет существует ли линейная связь между Х и У

#### 5
#
