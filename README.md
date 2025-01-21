# Smoke Detection System

## Overview
Dự án phát hiện khói tự động sử dụng Computer Vision và Deep Learning để phát hiện và cảnh báo sớm về khói trong các khu vực được giám sát. Hệ thống có thể được triển khai trong các tòa nhà, nhà máy hoặc khu vực ngoài trời để tăng cường an toàn phòng cháy chữa cháy.

## Tính năng chính
- Phát hiện khói từ ảnh giám sát


## Yêu cầu hệ thống
- Python 3.8+
- CUDA capable GPU (recommended)
- Các thư viện chính:
  - OpenCV
  - PyTorch

## Cài đặt
1. Clone repository:
```bash
git clone https://github.com/2vhoc/smoke-detection.git
cd smoke-detection
```

2. Tạo môi trường ảo:
```bash
python -m venv pt
source pt/bin/activate  # Linux/Mac
pt\Scripts\activate     # Windows
```

3. Cài đặt các dependencies:
```bash
pip install -r requirements.txt
```



## Cấu trúc project
```
smoke-detection/
├── Datasets/                    
├── script/                         
└── src/         

```
## Sử dụng

### Chạy hệ thống
```bash
python evaluation.py
```
### Convert mô hình từ dạng .pt sang các thiết bị nhúng như là TensorRT, Google Edge

```bash
python export_to_device.py --device "onnx" # mặc định là TensorRT của Nvidia
```





## Model Training

### Dataset
- Sử dụng bộ dataset smoke detection với ~500 ảnh


## Đánh giá hiệu năng
| PR Curve | P Curve | R Curve |
|----------|---------|---------|
| ![PR Curve](https://raw.githubusercontent.com/2vhoc/smoke-detection/main/script/runs/detect/val4/PR_curve.png) | ![P Curve](https://raw.githubusercontent.com/2vhoc/smoke-detection/main/script/runs/detect/val4/P_curve.png) | ![R Curve](https://raw.githubusercontent.com/2vhoc/smoke-detection/main/script/runs/detect/val4/R_curve.png) |

| Confusion Matrix | Confusion Matrix Normalized |
|------------------|-----------------------------|
| ![Confusion Matrix](https://raw.githubusercontent.com/2vhoc/smoke-detection/main/script/runs/detect/val4/confusion_matrix.png) | ![Confusion Matrix Normalized](https://raw.githubusercontent.com/2vhoc/smoke-detection/main/script/runs/detect/val4/confusion_matrix_normalized.png) |

| Validation Batch Labels | Validation Batch Predictions |
|--------------------------|------------------------------|
| ![Val Batch Labels](https://raw.githubusercontent.com/2vhoc/smoke-detection/main/script/runs/detect/val4/val_batch2_labels.jpg) | ![Val Batch Predictions](https://raw.githubusercontent.com/2vhoc/smoke-detection/main/script/runs/detect/val4/val_batch0_pred.jpg) |

*Hình ảnh: Đánh giá qua bộ test mà mô hình chưa gặp bao giờ*

## Đóng góp
Mọi đóng góp đều được chào đón. Vui lòng:
1. Fork repository
2. Tạo branch mới (`git checkout -b feature/amazing-feature`)
3. Commit thay đổi (`git commit -m 'Add amazing feature'`)
4. Push lên branch (`git push origin feature/amazing-feature`)
5. Tạo Pull Request


## Liên hệ
- Email: 2vhoc7@gmail.com
- Website: https://2vhocblog.vercel.app
- Issues: https://github.com/2vhoc/smoke-detection/issues

## Citation
Nếu bạn sử dụng project này trong nghiên cứu của mình, vui lòng trích dẫn:
```
@article{smoke-detection2024,
  title={Real-time Smoke Detection Using Deep Learning},
  author={Vũ Văn Học},
  year={2024}
}
```
