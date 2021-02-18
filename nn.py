import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.neuron = nn.Linear(4,1, False)
    
    
    def fordward(self, input):
        return self.neuron(input)
