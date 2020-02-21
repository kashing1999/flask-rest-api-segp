import io
import torch
import torchvision.transforms as transforms
from PIL import Image
from app.conv import convNet


class Inference:
    def __init__(self, path):
        self.classes = ['cardboard', 'glass', 'metal', 'paper', 'plastic']
        self.model=convNet(len(self.classes))
        self.model.load_state_dict(torch.load(path, map_location="cpu"))
        self.model.eval()


    def transform_image(self, image_bytes):
        img_transforms = transforms.Compose([
            transforms.Resize([224, 224]),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        image = Image.open(io.BytesIO(image_bytes))
        return img_transforms(image).unsqueeze(0)


    def make_inference(self, image_bytes):
        tensor = self.transform_image(image_bytes=image_bytes)
        outputs = self.model.forward(tensor)
        _, y_hat = outputs.max(1)
        return self.classes[y_hat]
