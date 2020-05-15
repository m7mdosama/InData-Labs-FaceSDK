import yaml
import os

import cv2
import numpy as np


def read_yaml(path: str):
    with open(path, "r") as fp:
        res = yaml.load(fp, Loader=yaml.FullLoader)
    return res


def read_image(path: str):

    """Reads an image in RGB format."""

    assert os.path.exists(path)
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    assert image is not None
    return image


def save_image(image: np.ndarray, path: str):

    """Saves an image in RGB format"""

    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    cv2.imwrite(path, image)
