from ultralytics import YOLO
import argparse


def train(data='dataset.yaml', model='yolov8n.pt', epochs=50, imgsz=640, batch=16):
# Create a YOLO object and call .train()
yolo = YOLO(model)
yolo.train(data=data, epochs=epochs, imgsz=imgsz, batch=batch)


if __name__ == '__main__':
parser = argparse.ArgumentParser()
parser.add_argument('--data', default='dataset.yaml')
parser.add_argument('--model', default='yolov8n.pt')
parser.add_argument('--epochs', type=int, default=50)
parser.add_argument('--imgsz', type=int, default=640)
parser.add_argument('--batch', type=int, default=16)
args = parser.parse_args()
train(data=args.data, model=args.model, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch)
