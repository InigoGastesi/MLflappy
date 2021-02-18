import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.input = nn.Linear(6,1)
        self.output = nn.Linear(1,1)
