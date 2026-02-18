# MRZLens – Passport MRZ Extractor

![MRZLens Banner]

**MRZLens** is a **Computer Vision pipeline** that automatically detects, crops, and extracts the **Machine Readable Zone (MRZ)** from passport images — whether scanned documents or real-world smartphone photos.

Built with **YOLOv8** for robust MRZ detection and **PaddleOCR** for high-accuracy text recognition, this tool is ideal for:
- eKYC / identity verification systems
- Border control & immigration automation
- Fintech document processing
- Automated passport / visa reading

## Features
- Automatic detection of MRZ zones (TD1, TD2, TD3 formats)
- Intelligent cropping — extracts only the MRZ region
- Precise OCR using PaddleOCR (better than Tesseract on real photos)
- Supports common formats: JPG, PNG, JPEG, WEBP
- Ready for backend/API integration
- Custom-trained YOLOv8 model for improved accuracy on passport images

## Tech Stack

| Component          | Technology                          |
|--------------------|-------------------------------------|
| Language           | Python                              |
| Object Detection   | YOLOv8 (Ultralytics)                |
| OCR Engine         | PaddleOCR                           |
| Image Processing   | PIL (Pillow), NumPy                 |
| Models             | yolov8_custom.pt (fine-tuned)       |

## Pipeline Overview
1. Load input passport image  
2. Detect text regions using PaddleOCR  
3. Identify MRZ zone (based on structure, line count, regex patterns)  
4. Crop the MRZ region precisely  
5. Perform final OCR on the cropped zone  
6. Output: extracted MRZ text + cropped image  

## Installation

```bash
# Clone the repository
git clone https://github.com/fattoumAchref/MRZLens.git
cd MRZLens

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install paddleocr ultralytics pillow numpy opencv-python
# Optional: for better performance / GPU support → follow PaddleOCR docs