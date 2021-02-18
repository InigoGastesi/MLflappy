import torch
import torch.nn as nn

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.neuron = nn.Linear(4,1, False)
        nn.init.normal_(self.neuron.weight, mean=0, std=1.0)
    
    
    def fordward(self, input):
        return self.neuron(input)
