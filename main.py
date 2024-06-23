import cv2
import pandas as pd
from ultralytics import YOLO
import numpy as np
from paddleocr import PaddleOCR, draw_ocr

#laod model
model = YOLO('yolov8_custom.pt')

ocr = PaddleOCR(use_angle_cls=True, lang='fr', use_gpu=False)

def process_image(image_path):

    my_file = open("classes.txt", "r")
    data = my_file.read()
    class_list = data.split("\n")

    area = [(27, 417), (16, 456), (1015, 451), (992, 417)]

    frame = cv2.imread(image_path)
    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)
    a = results[0].boxes.data
    a = a.cpu()
    px = pd.DataFrame(a).astype("float")

    count = 0
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])

        d = int(row[5])
        c = class_list[d]
        cx = int(x1 + x2) // 2
        cy = int(y1 + y2) // 2
        result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
        if result >= 0:
            crop = frame[y1:y2, x1:x2]
            result = ocr.ocr(crop, cls=True)
            texts = [item[1][0] for line in result for item in line]
            with open("PisteMRZ.txt", "a") as file:
                file.write(f"{texts}\n")
            cv2.imwrite(f"cropped mrz/crop_{count}_{index}.jpg", crop)

        count += 1

process_image("5.jpg")