import os

import cv2
import requests

from tensorflow.keras.applications import imagenet_utils
from keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelBinarizer
from tensorflow.keras.models import load_model
from imageai.Detection import ObjectDetection

import keras
import tensorflow as tf

class Detector():
    model_yolo_v3 = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'
    model_tiny_yolo_v3 = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5'
    tiny_yolo_path = '../model/tiny_yolo.h5'

    def __init__(self):
        self.get_model()
        self.n = 0

    def get_model(self):
        if not os.path.exists(self.tiny_yolo_path):
            r = requests.get(self.model_tiny_yolo_v3, timeout=0.5)
            with open(self.tiny_yolo_path, 'wb') as outfile:
                outfile.write(r.content)
        self.detector = ObjectDetection()
        self.detector.setModelTypeAsTinyYOLOv3()
        self.detector.setModelPath(self.tiny_yolo_path)
        self.detector.loadModel(self.tiny_yolo_path)

    def get_prediction(self, image):
        #TODO -> which can be a filepath, image numpy array or image file stream
        detectedImage, detections = self.detector.detectObjectsFromImage(output_type="array",
                                                                    input_image=image,
                                                                    input_type="array",
                                                                    thread_safe=True,
                                                                    minimum_percentage_probability=30)
        convertedImage = cv2.cvtColor(detectedImage, cv2.COLOR_RGB2BGR)
        self.n += 1
        print("Images converted: ", self.n)
        return convertedImage

        # for eachObject in detections:
        #     print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
        #     print("--------------------------------")