import cv2 as cv
from tensorflow.keras.models import load_model, model_from_json
import numpy as np
from efficientnet.tfkeras import EfficientNetB4
from keras.initializers import glorot_uniform



global model, category
model = load_model("my_model.h5")
category = ["cancerous", "not_cancerous"]


def prepare(x): # x = path of image
    img = cv.imread(x, cv.IMREAD_COLOR)
    new_img = cv.resize(img, (256,256))
    new_img = new_img.reshape(-1,256,256,3)
    return new_img

