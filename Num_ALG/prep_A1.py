import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *

df_train = pd.read_csv('data_A1/train.csv',sep=',')
df_test = pd.read_csv('data_A1/train.csv',sep=',')

alpha = 0.05


#zad 1
df_train = df_train.dropna()
df_test = df_test.dropna()
print(df_train.head()) #вывод первых 5 строк для проверки нетпустоты

x_train = df_train.drop(columns = ['Test Score'])
y_train = df_train['Test Score']
model = get_fitted_model(x_train,y_train)
print(model.summary())

x_test = df_test.drop(columns = ['Test Score'])
y_test = df_test['Test Score']

test_r = get_rsquared_adj(model,x_test,y_test)
print(test_r)
#print(f'Mera prilagodjeni r2: {test_r:.2f}')

### zad 2

x = df_train['Test Score']
y = df_train['Sleep Hours']
model = get_fitted_model(x,y)
min,max = get_pred_interval(model,8,alpha)
print("min:",min)

###zad 3

df = pd.read_csv('data_A1/train.csv',sep = ',')
#print(df.isnull().sum())

df['Previous Scores'] = df['Previous Scores'].interpolate(method = 'spline',order =1,limit_direction='both')
df['Sleep Hours '] = df['Sleep Hours'].interpolate(method = 'spline',order = 3,limit_direction='both')


df = df.drop(columns=['Has Cat', 'Questions Practiced','Questions Skipped'])

df.replace([np.inf, -np.inf], np.nan, inplace=True)
df.dropna(inplace=True)

x = df.drop(columns = ['Test Score'])
y = df['Test Score']

x_train,x_val,y_train,y_val = train_test_split(x,y,train_size=0.7,shuffle=True,random_state=123)

modelnn = get_fitted_model(x_train,y_train)
print(modelnn.summary())


df_test = pd.read_csv('data_A1/train.csv',sep = ',')

df_test['Previous Scores'] = df_test['Previous Scores'].interpolate(method='spline',order=1, limit_direction='both')
df_test['Sleep Hours'] = df_test['Sleep Hours'].interpolate(method='spline', order=3, limit_direction='both')

df_test.replace([np.inf, -np.inf], np.nan, inplace=True)
df_test.dropna(inplace=True)

x_test = df_test.drop(columns=['Has Cat', 'Questions Practiced','Questions Skipped'])
y_test = df_test['Test Score']

test_r_2 = get_rsquared_adj(modelnn,x_test,y_test)
print(test_r_2)
#print(f'Test prilagodjeni r2: {test_r_2:.2f}')






### zad 4

