import os
import time
import json
from ultralytics import YOLO


if __name__ == "__main__":



    model = YOLO("runs/detect/yolov8n/weights/best.pt")

    # Validate the model
    metrics = model.val(
        data="data/self.yaml",
        imgsz=640,
        batch=16,
        save_json=False,
        save_hybrid=False,
        conf=0.001,
        iou=0.50,
        max_det=300,
        half=False,
        device="cpu",
        dnn=False,
        plots=True,
        rect=False,
        split="val",
    )
    print("metrics: ", metrics)


