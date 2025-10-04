# main.py — CLI entrypoint to train, validate, detect, export
import argparse
import subprocess
from train import train
from detect import detect


if __name__ == '__main__':
parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest='cmd')


parser_train = sub.add_parser('train')
parser_train.add_argument('--data', default='dataset.yaml')
parser_train.add_argument('--model', default='yolov8n.pt')
parser_train.add_argument('--epochs', type=int, default=50)
parser_train.add_argument('--imgsz', type=int, default=640)
parser_train.add_argument('--batch', type=int, default=16)


parser_detect = sub.add_parser('detect')
parser_detect.add_argument('--weights', default='runs/train/exp/weights/best.pt')
parser_detect.add_argument('--source', default=0)
parser_detect.add_argument('--conf', type=float, default=0.25)
parser_detect.add_argument('--save', action='store_true')
parser_detect.add_argument('--show', action='store_true')


parser_export = sub.add_parser('export')
parser_export.add_argument('--weights', default='runs/train/exp/weights/best.pt')
parser_export.add_argument('--format', default='onnx')


args = parser.parse_args()


if args.cmd == 'train':
train(data=args.data, model=args.model, epochs=args.epochs, imgsz=args.imgsz, batch=args.batch)
elif args.cmd == 'detect':
detect(weights=args.weights, source=args.source, conf=args.conf, save=args.save, show=args.show)
elif args.cmd == 'export':
# Use Ultralytics export via CLI for convenience
subprocess.run(['yolo', 'export', 'model='+args.weights, 'format='+args.format])
else:
parser.print_help()
