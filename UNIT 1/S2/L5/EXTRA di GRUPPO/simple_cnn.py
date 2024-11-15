import torch.nn as nn
import torch

class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, 3, 1)
        self.fc1 = nn.Linear(16 * 30 * 30, 9)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = x.view(-1, 16 * 30 * 30)
        x = self.fc1(x)
        return x
