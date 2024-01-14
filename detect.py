import os
import time
import json
from PIL import Image
from ultralytics import YOLO


resDir = "inference/"
if not os.path.exists(resDir):
    os.makedirs(resDir)



if __name__ == "__main__":


    # Load a pretrained YOLOv8n model
    model = YOLO("runs/detect/yolov8n/weights/best.pt")


    while True:
        inputImg = input("请输入本地图像路径[回车即可启动计算]:")
        print("Loading Image From: ", inputImg)
        start = time.time()
        results = model(inputImg)
        # plot a BGR numpy array of predictions
        im_array = results[0].plot()
        # RGB PIL image
        im = Image.fromarray(im_array[..., ::-1])
        # save image
        one_id = inputImg.split("/")[-1].split(".")[0].strip()
        one_save_path = resDir + one_id + ".jpg"
        im.save(one_save_path)
        print("检测识别结果图片存储完成!")
        end = time.time()
        delta = end - start
        print("TimeConsume: ", delta)
        print("\n")
        show = Image.open(one_save_path)
        show.show()

