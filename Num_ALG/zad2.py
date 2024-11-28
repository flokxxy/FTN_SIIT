import pandas as pd
from sklearn.model_selection import train_test_split
from utils_nans1 import *
###### №1

df_train = pd.read_csv('data/train.csv',sep = ',')
df_test = pd.read_csv('data/test.csv',sep = ',')
#df_train.head()

rand_state = 42
train_part = 0.8
alpha = 0.05 #из уровня доверия или 0.95 или 0.05 <--


#create model
df_train = df_train.dropna() #очистка

x_train = df_train.drop(columns=['plata'])
y_train = df_train['plata']


model = get_fitted_model(x_train,y_train)
print(model.summary())


min, max = get_conf_interval(model,'zvanje',alpha)
print(f"Max: {max:.2f}")
print(f"Min: {min:.2f}")

# Проверка предположений модели

print("\nПроверка предположений модели:")

# 1. Проверка на независимость остатков
autocorrelation, _ = independence_of_errors_assumption(model, sm.add_constant(x_train), y_train, plot=False)
if autocorrelation is None:
    print('Ошибки независимы (значения действительны).')
else:
    print('Ошибки автокоррелированы (значения недействительны).')

# 2. Проверка на нормальность остатков
if normality_of_errors_assumption(model, sm.add_constant(x_train),y_train,plot = False)[0] == 'non-normal':
    print('Ошибки нормально распределены (значения действительны).')
else:
    print('Ошибки не нормально распределены (значения недействительны).')
