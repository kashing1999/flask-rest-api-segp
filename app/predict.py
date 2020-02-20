import torch
import torchvision.transforms as transforms
import io
from PIL import Image

class Predict:
    def __init__(self, path):
        classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
        model = torch.load(path)


    def transform_image(self, image_bytes):
        img_transforms = transforms.Compose([transforms.Resize(255),
                                            transforms.CenterCrop(224),
                                            transforms.ToTensor(),
                                            transforms.Normalize(
                                                [0.485, 0.456, 0.406],
                                                [0.229, 0.224, 0.225])])
        image = Image.open(io.BytesIO(image_bytes))
        return my_transforms(image).unsqueeze(0)


    def get_prediction(self, image_bytes):
        tensor = transform_image(image_bytes=image_bytes)
        outputs = model.forward(tensor)
        _, y_hat = outputs.max(1)
        return classes[y_hat]