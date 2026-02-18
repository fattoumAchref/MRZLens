# 🛂 Passport MRZ Extractor with Computer Vision and PaddleOCR

## 🧠 Overview

This project is a **Computer Vision-based pipeline** using **PaddleOCR** to automatically detect, crop, and extract the MRZ (Machine Readable Zone) from scanned or photographed passport images. MRZ zones are crucial for document verification and identity extraction in automated systems such as border control, eKYC, or identity validation.

---

## 🚀 Features

- ✅ **Automatic MRZ Detection** on passport images
- ✂️ **Smart Cropping**: Extracts only the MRZ zone from the image
- 🔤 **Text Recognition** using PaddleOCR
- 🖼️ Supports multiple image formats: `.jpg`, `.png`, `.jpeg`, `.webp`
- ⚙️ Easy to integrate with backend verification systems

---

## 🛠️ Tech Stack

| Component       | Technology      |
|----------------|------------------|
| Programming    | Python           |
| OCR Engine     | [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) |
| Computer Vision| YOLOV8          |
| Image Handling | PIL / NumPy      |
| Model Inference| Pretrained PaddleOCR detection/recognition models |

---

## 🖼️ MRZ Detection Pipeline

1. 📸 **Input Image** (passport image)
2. 🎯 **Text Detection** with PaddleOCR
3. 🔍 **MRZ Zone Identification** based on line structure & regex
4. ✂️ **Cropping** the detected MRZ region
5. 🧠 **Text Recognition** using PaddleOCR
6. 📤 **Export/Return** the MRZ text and cropped image
