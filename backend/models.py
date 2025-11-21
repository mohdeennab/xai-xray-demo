import torch
from torchvision import models

class DenseNet121Model:
    def __init__(self):
        # Load DenseNet121 model pre-trained on ImageNet
        self.model = models.densenet121(pretrained=True)
        self.model.eval()  # Set the model to evaluation mode

    def predict(self, input_tensor):
        with torch.no_grad():  # Disable gradient calculation
            output = self.model(input_tensor)
        return output

# Example of usage:
# model = DenseNet121Model()
# prediction = model.predict(input_tensor)
