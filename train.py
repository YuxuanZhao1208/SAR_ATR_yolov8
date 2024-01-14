# import os
# import time
# import json
# from ultralytics import YOLO
#
#
# if __name__ == "__main__":
#
#
#     model = YOLO("weights/yolov8s.pt")
#     print("Loading preTrain ModelWeight............")
#     results = model.train(
#         task='detect',
#         data="/Users/zhaoyuxuan/Desktop/20240102-mstar-yolov8/data/sar_parameter.yaml",
#         hyp="data/hyps/hyp.scratch-low.yaml",
#         epochs=100,
#         device=0,
#         batch=64,
#         imgsz=640,
#         name="yolov8s_100ep"
#     )
#     print("results: ", results)

from ultralytics import YOLO
import yaml
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--task', type=str, default='detect', help='detect,classify,segment')
parser.add_argument('--data', type=str, default='data/sar_parameter.yaml', help='dataset.yaml path')
parser.add_argument('--epochs', type=int, default=100, help='number of epochs')
parser.add_argument('--hyp', type=str, default='data/hyps/hyp.scratch-low.yaml', help='size of each image batch')
parser.add_argument('--model', type=str, default='weights/yolov8s.pt', help='pretrained weights or model.config path')
parser.add_argument('--batch-size', type=int, default=-1, help='size of each image batch')
parser.add_argument('--img-size', type=int, default=640, help='size of each image dimension')
parser.add_argument('--device', type=str, default='0', help='cuda device, i.e. 0 or 0,1,2,3 or cpu')
parser.add_argument('--project', type=str, default='yolo-sar', help='project name')
parser.add_argument('--name', type=str, default='yolov8s-100ep', help='exp name')
parser.add_argument('--resume', nargs='?', const=True, default=False, help='resume most recent training')

args = parser.parse_args()

assert args.data, 'argument --data path is required'
assert args.model, 'argument --model path is required'

if __name__ == '__main__':
    # Initialize
    model = YOLO(args.model)
    hyperparams = yaml.safe_load(open(args.hyp))
    hyperparams['epochs'] = args.epochs
    hyperparams['batch'] = args.batch_size
    hyperparams['imgsz'] = args.img_size
    hyperparams['device'] = args.device
    hyperparams['project'] = args.project
    hyperparams['name'] = args.name
    hyperparams['resume'] = args.resume

    model.train(data= args.data, **hyperparams)

