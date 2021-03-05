import torch
import torch.nn as nn
import numpy as np

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.neuron = nn.Linear(4,1, False)
        nn.init.normal_(self.neuron.weight, mean=0, std=1.0)
        self.neuron.weight.requires_grad=False
    
    def fordward(self, input):
        return self.neuron(input)

    def getWeights(self):
        return self.neuron.weight.numpy()

    def setWeights(self, means=0, sd=1.0):
        weights = []
        for i in range(0,4):
            s = np.random.normal(means[0][i], sd[0][i])
            weights.append(s)
        weights = torch.tensor(weights)
        print(weights)
        old = (self.neuron.state_dict())
        old['weight'].copy_(weights)
