import os

import cv2
import requests

from imageai.Detection import ObjectDetection
from LoggingManager import LoggingManager

class Detector():
    model_yolo_v3 = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5'
    model_tiny_yolo_v3 = 'https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo-tiny.h5'
    path = os.getcwd()
    tiny_yolo_path = path + '/model/tiny_yolo.h5'
    model_yolo_path = path + '../model/yolo.h5'


    def __init__(self, using_model=tiny_yolo_path):
        self.using_model = using_model
        self.get_model()
        self.log = LoggingManager()

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
        detectedImage, detections = self.detector.detectObjectsFromImage(output_type="array",
                                                                    input_image=image,
                                                                    input_type="array",
                                                                    thread_safe=True,
                                                                    minimum_percentage_probability=30)
        convertedImage = cv2.cvtColor(detectedImage, cv2.COLOR_RGB2BGR)

        objects = ""
        for eachObject in detections:
            objects += eachObject["name"] + " : " +\
                       str(eachObject["percentage_probability"]) + " : " + str(eachObject["box_points"]) + "\n"
        objects += "---"*5
        self.log.log_records(objects)
        return convertedImage