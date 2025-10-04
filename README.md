# space-station-safety-detection-hackaura
An AI-powered object detection system designed to ensure astronaut safety inside a space station. The model is trained on the Falcon dataset using YOLOv8, capable of detecting key safety equipment such as fire extinguishers, first aid boxes, nitrogen tanks, space tanks, emergency phones, fire alarms, and safety switch panels.
# Space Station Safety Detection (HackAura)


Detects critical safety objects inside a space station using YOLOv8.


## Object classes
- space_tank
- nitrogen_tank
- first_aid_box
- fire_alarm
- safety_switch_panel
- emergency_phone
- fire_extinguisher


## Project structure
space_station_safety/ ├── dataset/ │ ├── images/ │ └── labels/ ├── models/ ├── train.py ├── detect.py ├── main.py ├── dataset.yaml ├── requirements.txt └── README.md

## Quick start
1. Create a Python venv (recommended) and activate it.
2. Install requirements: `pip install -r requirements.txt`
3. Put the Falcon dataset into `./dataset` so that `images/train`, `images/val` and `labels/*` exist, or edit `dataset.yaml` to match paths.
4. Train: `python main.py train --epochs 50 --imgsz 640 --model yolov8n.pt`
5. Run inference: `python main.py detect --source path_or_camera --weights runs/train/exp/weights/best.pt --conf 0.25`


## Notes
- This project uses Ultralytics YOLO (v8) Python API.
- If your Falcon dataset uses COCO/YOLO/PASCAL VOC, convert or update `dataset.yaml` accordingly.
