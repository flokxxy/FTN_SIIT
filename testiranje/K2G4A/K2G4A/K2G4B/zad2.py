import os
import torchvision
import torch.nn as nn
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from torchvision.datasets import ImageFolder
from sklearn.model_selection import train_test_split

from zad1 import MyAct

# Pošto su slike raznolikih dimenzija, potrebno ih je skalirati na određene dimenzije
# U ovom slučaju 128x128
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor(),
])

dataset_path = "cats_dataset"
custom_dataset = ImageFolder(dataset_path, transform=transform)

train_set, test_set = train_test_split(custom_dataset, test_size=0.2, random_state=42)

# nastavi zadatak...