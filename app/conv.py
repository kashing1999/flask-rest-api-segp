import torch.nn as nn
from torchvision import models
import torch.nn.functional as F

class convNet(nn.Module):
    def __init__(self, num_classes):
        super(convNet, self).__init__()

        self.conv = models.resnet152(pretrained=True)
        for child in self.conv.children():
            for param in child.parameters():
                param.requires_grad = False

        num_ftrs = self.conv.fc.in_features
        self.conv.fc = nn.Linear(num_ftrs, num_classes)

        # self.fc1 = nn.Linear(64, num_classes)
        # self.fc2 = nn.Linear(16, num_classes)

    def forward(self, x):
        # x = F.relu(self.conv(x))
        x = self.conv(x)
        # x = F.dropout(x, p=0.5)
        # x = F.relu(self.fc1(x))
        # x = F.dropout(x, p=0.5)
        # x = F.relu(self.fc2(x))
        return x