🦅 Falcon Safety Equipment Detection
📌 Project Overview

This project focuses on automatic detection of workplace safety equipment using the YOLOv8 object detection model.
The solution is built using the Falcon dataset, which contains annotated images of multiple safety-related objects.

Our objective is to ensure real-time detection of essential safety tools, which can be applied in industries, factories, or workplaces to minimize human error and enhance safety compliance.

👥 Team
Anshu Porwal
Meenakshi Paraye
Naman Singh Kushwaha

Team: SolutionMakers

🚀 Features

Detects 7 classes of safety equipment:

Oxygen Tank

Nitrogen Tank

First Aid Box

Fire Alarm

Safety Switch Panel

Emergency Phone

Fire Extinguisher

Training performed using YOLOv8n (lightweight, fast, and accurate).

Includes training pipeline, evaluation, and prediction scripts (train.py, predict.py).

Results include metrics such as Precision, Recall, mAP@50, mAP@50-95, Confusion Matrix.

📂 Project Structure
Final_Submission/
│── train.py          # Training script
│── predict.py        # Prediction script
│── falcon.yaml       # Dataset configuration
│── runs/             # Training outputs (weights, metrics, logs)
│── Final_Submission.zip

⚙️ Installation & Requirements

Run in Google Colab (preferred) or a local Python environment with GPU.

Install dependencies:
pip install ultralytics opencv-python matplotlib seaborn albumentations gdown

📊 Training

To train the model:

python train.py


This will:

Train YOLOv8n for 50 epochs.

Save weights in runs/exp_falcon/weights/best.pt.

🔎 Prediction

To run inference on test images:

python predict.py


Outputs are saved in:

runs/exp_falcon_preds/images/

📈 Results & Performance

Precision: ~81%

Recall: ~76%

mAP@50: ~78%

mAP@50-95: ~62%

Confusion matrix confirms strong detection across most classes.

🎯 Future Work

Expand dataset with more real-world images.

Try larger YOLOv8 variants (YOLOv8m, YOLOv8l).

Deploy model into real-time surveillance systems.

🙏 Acknowledgment

Ultralytics YOLOv8 for state-of-the-art object detection.

Falcon Dataset for safety equipment images.
