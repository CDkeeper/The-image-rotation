import os

from PIL import Image
from torchvision import transforms
from torchvision.transforms import RandomVerticalFlip

image = Image.open('4.jpg')
new_im = transforms.RandomRotation((-45, 45))(image)  # 随机旋转45度
new_im.save(os.path.join('./4_new.jpg'))
