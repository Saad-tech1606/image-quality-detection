import torch
import torchvision.models as models
from torchvision.models import ResNet18_Weights

def load_resnet():
    model = models.resnet18(weights=ResNet18_Weights.DEFAULT)
    model.eval()
    return model