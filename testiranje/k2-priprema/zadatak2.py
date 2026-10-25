import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import torch

# za reproducibilnost
seed=42
torch.manual_seed(seed)

# Učitavanje podataka i enkodovanje labela (Cartman - 1, Stan - 2 ...)
df = pd.read_csv('./data/south_park_train.csv')

# prikaži meru tačnosti
# from sklearn.metrics import accuracy_score
# print(f'Accuracy: {accuracy_score(y_pred, y_test)}')