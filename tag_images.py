import os

import numpy as np
from PIL import Image
from sklearn.feature_extraction import image

BASE_PATH = 'Kendall_Square_datasets/Kendall_Square_'
IMG_SIZE = (210, 137)


def create_metadata():
    data = []
    for label in ['sunny', 'cloudy']:
        file_path = './{}{}/'.format(BASE_PATH, label)
        files = os.listdir(file_path)

        for img in files:
            img_path = file_path + img
            raw_img = read_image(img_path)
            data.append((raw_img, label))
    return data


def read_image(path):
    img = Image.open(path)
    img = img.resize(IMG_SIZE)
    rgb_values = np.array(img.getdata())
    patches = image.extract_patches_2d(rgb_values, (2,2))

    import ipdb; ipdb.set_trace()


if __name__ == '__main__':
    data = create_metadata()
    for i in data:
        print(i)