import tkinter as tk
import cv2
import numpy as np
from PIL import ImageTk, Image
from Detector import Detector


class Display():
    def __init__(self):
        self.initialize_variables()
        self.create_window()
        self.create_label()
        self.show_frames()
        self.root.mainloop()

    def initialize_variables(self):
        self.detector = Detector()
        self.height = 800;
        self.width = 1200;
        self.ai = True

    def create_window(self):
        self.root = tk.Tk()
        self.root.geometry(str(self.width) + "x" + str(self.height))
        self.root.title("Webcam")

    def create_label(self):
        self.label = tk.Label(self.root)
        self.label.grid(row=0, column=0)
        self.cap = cv2.VideoCapture(0)

    def show_frames(self):
        # Get the latest frame and convert into Image
        cv2image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)

        if(self.ai):
            img = Image.fromarray(self.detector.get_prediction(cv2image))
        else:
            img = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image=img)
        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

        self.label.after(1, self.show_frames)

    def enable_ai(self):
        self.ai = True

    def disable_ai(self):
        self.ai = False