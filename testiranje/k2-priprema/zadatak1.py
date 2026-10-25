import pandas as pd 
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import f1_score # Import koji ćemo koristiti za izračunavanje krajnje metrike

# za reproducibilnost
seed=42
torch.manual_seed(seed)

df = pd.read_csv("data/train.csv")

# prikaži f1 meru
# f1 = f1_score(y_pred=predicted, y_true=y_test, average='micro')
# print(f'F1: {f1}')