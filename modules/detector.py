from ultralytics import YOLO
import torch
from config import MODEL_PATH, CONFIDENCE, IMG_SIZE


class Detector:

    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print("Using device:", self.device)

        self.model = YOLO(MODEL_PATH)

        # Force GPU if available
        if self.device == "cuda":
            self.model.to("cuda")

    def detect(self, frame):

        return self.model.track(
            frame,
            persist=True,
            conf=CONFIDENCE,
            imgsz=IMG_SIZE,
            device=self.device
        )
