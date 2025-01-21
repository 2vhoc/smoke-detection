path = '/home/vuvanhoc/Documents/YOLOv8-20250121T081121Z-001/YOLOv8/Datasets/runs/detect/train2/weights/best.pt'
import torch
import cv2
from ultralytics import YOLO

model = YOLO(path)
# #
# # metrics = model.val(data='/home/vuvanhoc/Documents/YOLOv8-20250121T081121Z-001/YOLOv8/Datasets/data.yaml')
path_img = '/home/vuvanhoc/Documents/YOLOv8-20250121T081121Z-001/YOLOv8/Datasets/test_reality/logo-chayrungnghean1-15934249163021906583196.webp'
results = model(path_img)
results[0].show()
