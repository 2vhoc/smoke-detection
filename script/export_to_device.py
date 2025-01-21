from evaluation import model
import argparse
"""
    onnx,
    tensorrt
    "mlmodel", "mlpackage", "mlprogram", "apple", "ios", "coreml", etc
"""
def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_path', type=str, default='./model')
    parser.add_argument('--device', type=str, default='onnx')
    return parser.parse_args()
device = args().device
path = model.export(format=f"{device}")