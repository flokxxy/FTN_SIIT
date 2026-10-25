import torch
import torch.nn as nn

class MyAct(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        raise NotImplementedError()


# ovde možeš dodati kod da proveriš implementiranu aktivacionu funkciju